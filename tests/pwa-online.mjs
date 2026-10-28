// Optional verification against an already deployed HTTPS site, using an isolated profile.
// node tests/pwa-online.mjs https://<actual-pages-url>/
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {mkdir,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const target=new URL(process.argv[2]);
assert.equal(target.protocol,'https:','线上验收必须使用实际 HTTPS 地址');
assert(target.pathname.endsWith('/'),'网址需要以 / 结尾');
const output=resolve('tmp/pwa-verification');await mkdir(output,{recursive:true});
const releaseResponse=await fetch(new URL('release.json',target));assert.equal(releaseResponse.status,200);
const release=await releaseResponse.json();
for(const asset of release.assets){
  const url=new URL(asset.path,target);assert.equal(url.origin,target.origin);
  assert(url.pathname.startsWith(target.pathname));
  const response=await fetch(url);assert.equal(response.status,200,asset.path);
  const bytes=Buffer.from(await response.arrayBuffer());
  assert.equal(createHash('sha256').update(bytes).digest('hex'),asset.sha256,asset.path);
}
console.log(`PASS HTTPS release ${release.version}: ${release.assets.length} resource hashes match`);
const {chromium}=await import(process.env.PLAYWRIGHT_MODULE?pathToFileURL(process.env.PLAYWRIGHT_MODULE).href:'playwright');
const browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})});
try{
  const context=await browser.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true});
  let page=await context.newPage();
  await page.goto(target.href,{waitUntil:'load',timeout:60000});
  await page.waitForFunction(()=>document.querySelector('#pwa-status')?.dataset.state==='ready',null,{timeout:60000});
  await page.waitForFunction(()=>!document.querySelector('#reveal').disabled);
  assert.equal(await page.locator('meta[name="pwa-release"]').getAttribute('content'),release.version);
  await page.locator('#reveal').click();await page.locator('[data-rating="good"]').click();
  await page.waitForFunction(()=>document.querySelector('#progress').textContent==='已记录 1 次学习');
  await page.locator('[data-page="settings"]').click();
  await page.screenshot({path:resolve(output,'online-settings.png'),fullPage:true});
  console.log('PASS online launch, worker control, vocabulary load, and feedback save');
  await context.setOffline(true);await page.close();page=await context.newPage();
  await page.goto(target.href,{waitUntil:'load'});
  await page.waitForFunction(()=>document.querySelector('#pwa-status')?.dataset.state==='ready',null,{timeout:30000});
  await page.waitForFunction(()=>!document.querySelector('#reveal').disabled);
  assert.equal(await page.locator('#progress').textContent(),'已记录 1 次学习');
  await page.locator('#reveal').click();await page.locator('[data-rating="good"]').click();
  await page.waitForFunction(()=>document.querySelector('#progress').textContent==='已记录 2 次学习');
  console.log('PASS network-disabled reopen and subsequent learning save with preserved progress');
  await writeFile(resolve(output,'online-results.json'),JSON.stringify({url:target.href,release:release.version,contentVersion:release.contentVersion,assets:release.assets.length,https:true,resourceHashes:true,controlled:true,offlineReopen:true,offlineSave:true,engine:'Chrome',iphoneTested:false},null,2)+'\n');
}finally{await browser.close();}
