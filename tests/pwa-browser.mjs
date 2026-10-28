// Real Chromium verification. PLAYWRIGHT_MODULE points to an installed playwright entry file.
// Uses isolated browser contexts and an ephemeral local server, never existing user profiles.
import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {buildPwa} from '../scripts/prepare_pwa.mjs';
const {chromium}=await import(process.env.PLAYWRIGHT_MODULE?pathToFileURL(process.env.PLAYWRIGHT_MODULE).href:'playwright');
const release=await buildPwa();
const filesA=new Map(await Promise.all(release.files.map(async name=>[name,await readFile(resolve(release.output,name))])));
const filesB=new Map(filesA),versionB=release.version+'-test-update';
filesB.set('index.html',Buffer.from(filesB.get('index.html').toString().replace(release.version,versionB)));
filesB.set('style.css',Buffer.from(filesB.get('style.css').toString()+'\n/* browser update fixture */\n'));
const releaseB={...release,version:versionB,assets:release.assets.map(asset=>({...asset,sha256:createHash('sha256').update(filesB.get(asset.path)).digest('hex')}))};
const template=await readFile('scripts/service-worker.js','utf8');
filesB.set('sw.js',Buffer.from(template.replace('__RELEASE_CONFIG__',JSON.stringify(releaseB))));
let current=filesA,fault=false;
const types={html:'text/html; charset=utf-8',css:'text/css',mjs:'text/javascript',js:'text/javascript',wasm:'application/wasm',webmanifest:'application/manifest+json',png:'image/png',json:'application/json'};
const server=createServer((req,res)=>{
  const pathname=new URL(req.url,'http://localhost').pathname;
  const name=pathname.startsWith('/english-ok/')?pathname.slice('/english-ok/'.length):pathname.slice(1);
  const key=name||'index.html';
  if(fault&&key==='style.css'){res.writeHead(200,{'Content-Type':'text/css'});res.end('/* mismatched release */');return;}
  const data=current.get(key);
  if(!data){res.writeHead(404);res.end('not found');return;}
  res.writeHead(200,{'Content-Type':types[key.split('.').at(-1)]??'application/octet-stream','Cache-Control':'no-store'});res.end(data);
});
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
const url=`http://127.0.0.1:${server.address().port}/english-ok/`;
const browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})});
const results=[];
const pass=text=>{results.push(text);console.log('PASS '+text);};
const artifacts=resolve('tmp/pwa-verification');await mkdir(artifacts,{recursive:true});
async function ready(page){await page.waitForFunction(()=>document.querySelector('#pwa-status')?.dataset.state==='ready',{},{timeout:30000});}
async function appReady(page){await page.locator('#reveal').waitFor({state:'visible'});await page.waitForFunction(()=>!document.querySelector('#reveal').disabled);}
async function savedBytes(page){return page.evaluate(async()=>{
  const db=await new Promise((resolve,reject)=>{const r=indexedDB.open('english-ok-sqlite',1);r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);});
  const result=await new Promise((resolve,reject)=>{const tx=db.transaction('databases','readonly');const r=tx.objectStore('databases').get('learning');tx.oncomplete=()=>resolve(r.result);tx.onerror=()=>reject(tx.error);});db.close();return Array.from(result.bytes);
});}
try{
  const context=await browser.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:1});
  let page=await context.newPage();const errors=[];page.on('pageerror',error=>errors.push(error.message));
  await page.goto(url);await appReady(page);await ready(page);
  pass('first install controls page and validates all cached resources under /english-ok/');
  await page.evaluate(async()=>{
    for(const key of await caches.keys()){
      const cache=await caches.open(key);
      for(const path of ['app.mjs','pwa.mjs','vendor/sql-wasm.wasm'])await cache.delete(new URL(path,location.href).href);
    }
  });
  await page.reload();await appReady(page);await ready(page);
  pass('evicted startup modules and WASM recover online only from matching release bytes');
  await page.locator('[data-page="settings"]').click();
  await page.screenshot({path:resolve(artifacts,'settings-390.png'),fullPage:true});
  await page.locator('[data-page="study"]').click();
  await page.locator('#reveal').click();await page.locator('[data-rating="good"]').click();
  await page.waitForFunction(()=>document.querySelector('#progress').textContent==='已记录 1 次学习');
  const before=await savedBytes(page);
  await context.setOffline(true);await page.close();page=await context.newPage();
  await page.goto(url);await appReady(page);await ready(page);
  assert.equal(await page.locator('#progress').textContent(),'已记录 1 次学习');
  await page.locator('#reveal').click();await page.locator('[data-rating="good"]').click();
  await page.waitForFunction(()=>document.querySelector('#progress').textContent==='已记录 2 次学习');
  pass('offline cold page open, WASM load, learning save, and IndexedDB recovery');
  await page.locator('[data-page="settings"]').click();
  const downloadPromise=page.waitForEvent('download');await page.locator('#export').click();
  const download=await downloadPromise;const backupPath=resolve(artifacts,'backup.json');await download.saveAs(backupPath);
  const backup=JSON.parse(await readFile(backupPath,'utf8'));assert(backup);
  const recordBeforeBad=await savedBytes(page);
  await page.locator('#file').setInputFiles({name:'invalid.json',mimeType:'application/json',buffer:Buffer.from('{broken')});
  await page.waitForFunction(()=>document.querySelector('#status').textContent.includes('导入失败'));
  assert.deepEqual(await savedBytes(page),recordBeforeBad);
  pass('JSON export works offline and malformed JSON leaves saved bytes unchanged');
  page.on('dialog',dialog=>dialog.accept());
  await page.locator('#file').setInputFiles(backupPath);
  await page.waitForFunction(()=>document.querySelector('#status').textContent==='');
  assert.equal(await page.locator('#progress').textContent(),'已记录 2 次学习');
  pass('exported JSON restores successfully');
  await page.locator('[data-page="study"]').click();
  for(const size of [{width:320,height:568},{width:390,height:844},{width:844,height:390}]){
    await page.setViewportSize(size);await page.locator('#reveal').scrollIntoViewIfNeeded();
    assert(await page.locator('#reveal').isVisible());
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    if(size.width>size.height)assert(await page.evaluate(()=>document.querySelector('.study-scroll').getBoundingClientRect().bottom<=document.querySelector('.study-dock').getBoundingClientRect().top+1));
    await page.screenshot({path:resolve(artifacts,`study-${size.width}.png`),fullPage:true});
  }
  pass('320px, 390px, and landscape layouts have no horizontal overflow; study button reachable');
  await context.setOffline(false);current=filesB;
  await page.locator('[data-page="settings"]').click();
  await page.locator('#pwa-check').click();
  await page.waitForFunction(async()=>!!(await navigator.serviceWorker.getRegistration()).waiting,{},{timeout:30000});
  assert.equal(await page.locator('meta[name="pwa-release"]').getAttribute('content'),release.version);
  assert.equal(await page.locator('#progress').textContent(),'已记录 2 次学习');
  pass('new release waits without refreshing or replacing the current learning page');
  await page.close();
  // An observer outside this worker's scope does not keep the old version alive.
  const observer=await context.newPage();await observer.goto(new URL('/update-check',url).href);
  await observer.waitForFunction(async scope=>{
    const reg=await navigator.serviceWorker.getRegistration(scope);
    return reg?.active?.state==='activated'&&!reg.waiting;
  },url);
  await observer.close();
  await context.setOffline(true);page=await context.newPage();await page.goto(url);await appReady(page);await ready(page);
  assert.equal(await page.locator('meta[name="pwa-release"]').getAttribute('content'),versionB);
  assert.equal(await page.locator('#progress').textContent(),'已记录 2 次学习');
  pass('after closing old clients, prepared update opens offline and retains learning records');
  await context.close();
  current=filesA;fault=true;
  const failure=await browser.newContext();const failedPage=await failure.newPage();
  await failedPage.goto(url);await failedPage.waitForFunction(()=>document.querySelector('#pwa-status')?.dataset.state==='error',{},{timeout:30000});
  assert(!await failedPage.evaluate(()=>!!navigator.serviceWorker.controller));
  fault=false;await failedPage.locator('[data-page="settings"]').click();await failedPage.locator('#pwa-check').click();await ready(failedPage);
  pass('mixed-version install never claims readiness; retry recovers without deleting user data');
  await failure.close();
  const rootContext=await browser.newContext();const rootPage=await rootContext.newPage();await rootPage.goto(url.replace('/english-ok/','/'));await ready(rootPage);await appReady(rootPage);
  pass('root-directory installation also works');await rootContext.close();
  assert.deepEqual(errors,[]);assert(before.length>0);
  await writeFile(resolve(artifacts,'results.json'),JSON.stringify({release:release.version,engine:'Chromium',results,limitations:['Not an iPhone Safari or Home Screen installation test.']},null,2));
}finally{
  await browser.close();await new Promise(resolve=>server.close(resolve));
}
