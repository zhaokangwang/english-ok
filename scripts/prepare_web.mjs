import { mkdir, copyFile } from 'node:fs/promises';
await mkdir('web/vendor', {recursive:true});
for (const file of ['sql-wasm.js','sql-wasm.wasm']) await copyFile(`node_modules/sql.js/dist/${file}`,`web/vendor/${file}`);
await copyFile('node_modules/sql.js/LICENSE','web/vendor/SQL-JS-LICENSE');
console.log('SQLite runtime copied locally; no CDN required.');
