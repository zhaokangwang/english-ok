import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,readFile,writeFile,mkdir} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createHash,webcrypto} from 'node:crypto';
import {runInNewContext} from 'node:vm';
import {buildPwa} from '../scripts/prepare_pwa.mjs';

const output=await mkdtemp(join(tmpdir(),'english-ok-pwa-unit-'));
const release=await buildPwa(output);
const source=await readFile(join(output,'sw.js'),'utf8');
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');

test('release is repeatable, complete, and excludes user data and source files',async()=>{
  assert.equal((await buildPwa(output)).version,release.version);
  assert(!release.files.includes('data/learning.sqlite'));
  assert(!release.files.some(path=>path.includes('backup')||path.endsWith('.pdf')));
  const html=await readFile(join(output,'index.html'),'utf8');
  assert(html.includes(release.version));
  for(const asset of release.assets)assert.equal(sha(await readFile(join(output,asset.path))),asset.sha256);
  const manifest=JSON.parse(await readFile(join(output,'manifest.webmanifest'),'utf8'));
  for(const prefix of ['https://example.test/','https://example.test/english-ok/']){
    assert.equal(new URL(manifest.scope,prefix).href,prefix);
    assert.equal(new URL(manifest.start_url,prefix).href,prefix);
  }
  for(const [name,size] of [['icon-192.png',192],['icon-512.png',512],['apple-touch-icon.png',180]]){
    const png=await readFile(join(output,'icons',name));assert.equal(png.readUInt32BE(16),size);assert.equal(png.readUInt32BE(20),size);
  }
});

test('publishing refuses unexpected files rather than leaking them',async()=>{
  const directory=await mkdtemp(join(tmpdir(),'english-ok-pwa-audit-'));
  await mkdir(join(directory,'data'));
  await writeFile(join(directory,'data','personal-backup.json'),'{}');
  await assert.rejects(buildPwa(directory),/非白名单/);
});

function worker(scope='https://example.test/english-ok/'){
  const listeners=new Map(),stores=new Map();let tamper=false,claimed=false;
  const caches={
    async open(name){
      if(!stores.has(name))stores.set(name,new Map());const data=stores.get(name);
      return {async match(key){return data.get(String(key))?.clone();},async put(key,value){data.set(String(key),value.clone());},async delete(key){return data.delete(String(key));}};
    },
    async keys(){return [...stores.keys()];},async delete(name){return stores.delete(name);}
  };
  runInNewContext(source,{
    self:{registration:{scope},clients:{async claim(){claimed=true;}},addEventListener(type,listener){listeners.set(type,listener);}},
    caches,URL,Response,crypto:webcrypto,
    async fetch(url){
      const path=new URL(url).pathname.slice(new URL(scope).pathname.length);
      const bytes=await readFile(join(output,path));
      return new Response(tamper&&path==='data/vocabulary.sqlite'?'corrupted':bytes);
    }
  });
  return {
    caches,stores,setTamper(value){tamper=value;},get claimed(){return claimed;},
    async event(type,extra={}){let task;listeners.get(type)({...extra,waitUntil(value){task=value;}});await task;},
    async request(url,options={}){let response;listeners.get('fetch')({request:new Request(url,options),respondWith(value){response=value;}});return response?await response:undefined;},
    async status(){let value;await this.event('message',{data:{type:'STATUS'},ports:[{postMessage(result){value=result;}}]});return value;}
  };
}

test('worker rejects a mixed release before caching and never reports it ready',async()=>{
  const w=worker();w.setTamper(true);
  await assert.rejects(w.event('install'),/资源版本不一致/);
  assert.equal((await w.status()).complete,false);
  assert.equal([...w.stores.values()].reduce((n,store)=>n+store.size,0),0);
});

test('worker serves a consistent snapshot, scopes cleanup, and exposes missing cache',async()=>{
  const w=worker();
  await w.caches.open('unrelated-app');await w.caches.open('english-ok:'+encodeURIComponent('https://example.test/other/')+':old');
  await w.caches.open('english-ok:'+encodeURIComponent('https://example.test/english-ok/')+':old');
  await w.event('install');await w.event('activate');
  assert.equal(w.claimed,true);assert.equal((await w.status()).complete,true);
  assert((await w.caches.keys()).includes('unrelated-app'));
  assert((await w.caches.keys()).some(name=>name.includes(encodeURIComponent('https://example.test/other/'))));
  assert(!(await w.caches.keys()).some(name=>name.endsWith(':old')&&name.includes(encodeURIComponent('https://example.test/english-ok/'))));
  assert.equal((await w.request('https://example.test/english-ok/?source=home')).status,200);
  assert.equal(await w.request('https://example.test/english-ok/not-found'),undefined);
  assert.equal(await w.request('https://example.test/other/'),undefined);
  const cache=await w.caches.open('english-ok:'+encodeURIComponent('https://example.test/english-ok/')+':'+release.version);
  await cache.delete('https://example.test/english-ok/vendor/sql-wasm.wasm');
  assert.equal((await w.status()).complete,false);
  assert.equal((await w.request('https://example.test/english-ok/vendor/sql-wasm.wasm')).status,200);
  assert.equal((await w.status()).complete,true);
  await cache.delete('https://example.test/english-ok/data/vocabulary.sqlite');w.setTamper(true);
  assert.equal((await w.request('https://example.test/english-ok/data/vocabulary.sqlite')).status,503);
  assert.equal((await w.status()).complete,false);
});
