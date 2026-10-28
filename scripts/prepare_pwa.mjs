import {createHash} from 'node:crypto';
import {readFile,writeFile,mkdir,readdir,lstat} from 'node:fs/promises';
import {resolve,dirname,relative,sep} from 'node:path';
import {fileURLToPath} from 'node:url';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
export const publicFiles=[
  'index.html','style.css','app.mjs','core.mjs','storage.mjs','pwa.mjs','manifest.webmanifest',
  'icons/icon-192.png','icons/icon-512.png','icons/apple-touch-icon.png',
  'vendor/sql-wasm.js','vendor/sql-wasm.wasm','vendor/SQL-JS-LICENSE',
  'data/vocabulary.sqlite','data/learning.sql','data/catalog.json',
];
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
export async function buildPwa(output=resolve(root,'dist/pwa')){
  const files=new Map(await Promise.all(publicFiles.map(async path=>[path,await readFile(resolve(root,'web',path))])));
  const template=await readFile(resolve(root,'scripts/service-worker.js'),'utf8');
  const version='pwa-'+digest(Buffer.concat([...files].flatMap(([path,bytes])=>[Buffer.from(path+'\0'),bytes]).concat(Buffer.from(template)))).slice(0,16);
  const contentVersion=JSON.parse(files.get('data/catalog.json')).content_version;
  files.set('index.html',Buffer.from(files.get('index.html').toString().replace('content="development"',`content="${version}"`)));
  const release={version,contentVersion,assets:[...files].map(([path,bytes])=>({path,sha256:digest(bytes),bytes:bytes.length}))};
  files.set('sw.js',Buffer.from(template.replace('__RELEASE_CONFIG__',JSON.stringify(release))));
  files.set('release.json',Buffer.from(JSON.stringify(release,null,2)+'\n'));
  files.set('.nojekyll',Buffer.alloc(0));
  await mkdir(output,{recursive:true});
  // Refuse unexpected files rather than accidentally publish leftovers or delete user files.
  async function audit(directory){
    for(const name of await readdir(directory)){
      const path=resolve(directory,name),info=await lstat(path);
      if(info.isSymbolicLink())throw Error(`发布目录不能包含链接：${path}`);
      if(info.isDirectory())await audit(path);
      else if(!files.has(relative(output,path).split(sep).join('/')))throw Error(`发布目录包含非白名单文件：${path}`);
    }
  }
  await audit(output);
  for(const [path,bytes] of files){
    const target=resolve(output,path);await mkdir(dirname(target),{recursive:true});await writeFile(target,bytes);
  }
  return {...release,output,totalBytes:[...files.values()].reduce((sum,bytes)=>sum+bytes.length,0),files:[...files.keys()]};
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
  const result=await buildPwa();
  console.log(`PWA ${result.version} / ${result.contentVersion}\n${result.files.length} files, ${result.totalBytes} bytes\nOutput: ${result.output}`);
}
