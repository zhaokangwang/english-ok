// Release configuration is embedded by prepare_pwa.mjs; never serve this template directly.
const RELEASE=__RELEASE_CONFIG__;
const base=self.registration.scope;
const prefix=`english-ok:${encodeURIComponent(base)}:`;
const cacheName=prefix+RELEASE.version;
const resources=new Map(RELEASE.assets.map(asset=>[new URL(asset.path,base).href,asset]));
const marker=new URL('__offline_complete__',base).href;
async function verifiedResource(url,asset){
    const response=await fetch(url,{cache:'no-store',credentials:'same-origin'});
    if(!response.ok||response.redirected)throw Error(`资源下载失败：${asset.path}`);
    const bytes=await response.clone().arrayBuffer();
    const hash=[...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(x=>x.toString(16).padStart(2,'0')).join('');
    if(hash!==asset.sha256)throw Error(`资源版本不一致：${asset.path}`);
    return response;
}
async function verifiedResources(){
  return Promise.all([...resources].map(async([url,asset])=>[url,await verifiedResource(url,asset)]));
}
async function prepare(){
  // Validate the whole release before replacing any cached response.
  const responses=await verifiedResources();
  const cache=await caches.open(cacheName);
  await cache.delete(marker);
  await Promise.all(responses.map(([url,response])=>cache.put(url,response)));
  await cache.put(marker,new Response(RELEASE.version));
}
async function complete(){
  const cache=await caches.open(cacheName);
  if((await (await cache.match(marker))?.text())!==RELEASE.version)return false;
  const results=await Promise.all([...resources.keys()].map(url=>cache.match(url)));
  return results.every(Boolean);
}
self.addEventListener('install',event=>{
  event.waitUntil(prepare());
  // No skipWaiting: an update cannot take over an ongoing learning session.
});
self.addEventListener('activate',event=>{
  event.waitUntil((async()=>{
    if(!await complete())throw Error('离线缓存不完整');
    await Promise.all((await caches.keys()).filter(name=>name.startsWith(prefix)&&name!==cacheName).map(name=>caches.delete(name)));
    await self.clients.claim();
  })());
});
self.addEventListener('fetch',event=>{
  if(event.request.method!=='GET')return;
  const url=new URL(event.request.url);
  if(url.origin!==new URL(base).origin||!url.href.startsWith(base))return;
  url.search='';url.hash='';
  let key=url.href;
  if(key===base)key=new URL('index.html',base).href;
  if(!resources.has(key))return;
  event.respondWith((async()=>{
    const cache=await caches.open(cacheName);
    const response=await cache.match(key);
    if(response)return response;
    // Recover an evicted resource only when its bytes still match this exact release.
    // In particular, a changed network response must never replace an old JS or database.
    try{
      const repaired=await verifiedResource(key,resources.get(key));
      await cache.put(key,repaired.clone());return repaired;
    }catch{
      return new Response('离线资源缺失且暂时无法修复。请联网后关闭所有同网址窗口，稍等片刻再打开。请勿清除学习记录。',{status:503,headers:{'Content-Type':'text/plain; charset=utf-8'}});
    }
  })());
});
let repairing;
self.addEventListener('message',event=>{
  if(!event.ports[0]||!['STATUS','REPAIR'].includes(event.data?.type))return;
  event.waitUntil((async()=>{
    try{
      if(event.data.type==='REPAIR'){
        repairing??=prepare().finally(()=>{repairing=undefined;});
        await repairing;
      }
      event.ports[0].postMessage({version:RELEASE.version,contentVersion:RELEASE.contentVersion,complete:await complete()});
    }catch(error){event.ports[0].postMessage({error:error.message});}
  })());
});
