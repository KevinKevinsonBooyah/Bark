const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../engine/build');
for(const page of ['index.html','editor.html']){
 const html=fs.readFileSync(path.join(root,page),'utf8');
 assert(html.includes('Bark'),'Bark title must be present');
 for(const match of html.matchAll(/(?:src|href)="([^"?#]+)"/g)){
  const url=match[1];if(/^(https?:|data:|#)/.test(url))continue;
  const local=url.startsWith('/Bark/')?url.slice(6):url;
  assert(fs.existsSync(path.join(root,local)),`${page}: missing ${url}`);
 }
}
console.log('PASS Pages entrypoints and local script/style/image references');
