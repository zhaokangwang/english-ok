import http from 'node:http';
import {createReadStream} from 'node:fs';
import {stat} from 'node:fs/promises';
import {resolve,extname,sep} from 'node:path';
import {networkInterfaces} from 'node:os';
const root=resolve('web'),host=process.argv.includes('--lan')?'0.0.0.0':'127.0.0.1',port=5173;
const types={'.html':'text/html; charset=utf-8','.mjs':'text/javascript; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.wasm':'application/wasm','.sql':'text/plain; charset=utf-8','.sqlite':'application/vnd.sqlite3'};
http.createServer(async(req,res)=>{
  try{
    const url=new URL(req.url,'http://localhost');
    const file=resolve(root,'.'+decodeURIComponent(url.pathname==='/'?'/index.html':url.pathname));
    if(!file.startsWith(root+sep)){res.writeHead(403);res.end();return;}
    if(!['GET','HEAD'].includes(req.method)){res.writeHead(405);res.end();return;}
    const info=await stat(file);if(!info.isFile())throw Error('Not file');
    res.writeHead(200,{'Content-Type':types[extname(file)]??'application/octet-stream','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});
    if(req.method==='HEAD')res.end();else createReadStream(file).pipe(res);
  }catch{res.writeHead(404);res.end('Not found');}
}).listen(port,host,()=>{
  console.log(`Local: http://127.0.0.1:${port}`);
  if(host==='0.0.0.0')for(const net of Object.values(networkInterfaces()).flat())if(net?.family==='IPv4'&&!net.internal)console.log(`Phone (same Wi-Fi): http://${net.address}:${port}`);
});
