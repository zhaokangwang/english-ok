const status=document.querySelector('#pwa-status');
const version=document.querySelector('#pwa-version');
const button=document.querySelector('#pwa-check');
const pageRelease=document.querySelector('meta[name="pwa-release"]').content;
const base=new URL('./',import.meta.url);
let registration;
const show=(text,state='preparing')=>{status.textContent=text;status.dataset.state=state;};
function message(worker,type){
  return new Promise((resolve,reject)=>{
    const channel=new MessageChannel();
    const timer=setTimeout(()=>{channel.port1.close();reject(Error('检查超时，请联网后重试'));},45000);
    channel.port1.onmessage=event=>{
      clearTimeout(timer);channel.port1.close();
      if(event.data.error)reject(Error(event.data.error));else resolve(event.data);
    };
    worker.postMessage({type},[channel.port2]);
  });
}
async function inspect(repair=false){
  const worker=navigator.serviceWorker.controller;
  if(!worker){show('资源准备后，请关闭此应用及同网址的 Safari 页面，再重新打开。');return;}
  let result=await message(worker,'STATUS');
  if(result.version!==pageRelease){
    show('页面与离线版本不同。请结束学习，关闭此应用及同网址的 Safari 页面后重新打开。','update');return;
  }
  if(!result.complete&&repair){
    show('正在重新下载并校验离线资源，请保持联网…');
    result=await message(worker,'REPAIR');
  }
  version.textContent=`应用 ${result.version} · 词库 ${result.contentVersion}`;
  if(!result.complete){
    if(registration?.waiting)show('旧版离线资源不完整，新版本已准备好。请结束学习并关闭所有同网址窗口，稍等片刻后重新打开。','update');
    else show('离线资源不完整。请联网后点击下方按钮重试；学习记录仍保存在本机。','error');
    return;
  }
  show('离线资源已准备好，可断网重新打开。','ready');
  if(registration?.waiting)show('离线资源已准备好；新版本也已就绪。结束学习后，关闭此应用及同网址的 Safari 页面，再重新打开以更新。','update');
}
function observe(worker){
  if(!worker)return;
  worker.addEventListener('statechange',()=>{
    if(worker.state==='installed'||worker.state==='activated')inspect().catch(fail);
    if(worker.state==='redundant')show('新资源准备失败，可能是网络中断或网站正在更新。请联网后重试；已有版本与学习记录保留。','error');
  });
}
function fail(error){show(`离线准备未完成：${error.message}。请保持联网后重试。`,'error');}
async function check(){
  button.disabled=true;
  try{
    show('正在检查离线资源与更新…');
    if(!registration||(!registration.active&&!registration.installing&&!registration.waiting)){
      registration=await navigator.serviceWorker.register(new URL('sw.js',base),{scope:base.href,updateViaCache:'none'});
      registration.addEventListener('updatefound',()=>observe(registration.installing));
      observe(registration.installing);
    }
    // Failure to reach the update server must not invalidate an intact offline cache.
    try{await registration.update();}catch{if(!navigator.serviceWorker.controller)throw Error('无法连接更新服务');}
    await inspect(!registration.waiting);
  }catch(error){fail(error);}finally{button.disabled=false;}
}
if(!isSecureContext||!('serviceWorker' in navigator)){
  show('当前地址无法准备离线资源。iPhone 请使用 HTTPS 网址；电脑可使用 localhost 预览。','error');button.hidden=true;
}else if(pageRelease==='development'){
  show('当前为开发预览。请使用 PWA 预览或已发布的 HTTPS 网址准备离线资源。');button.hidden=true;
}else{
  navigator.serviceWorker.addEventListener('controllerchange',()=>inspect().catch(fail));
  button.addEventListener('click',check);
  check();
}
