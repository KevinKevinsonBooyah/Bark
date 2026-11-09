import {mkdir,readFile,writeFile,copyFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const files=['index.html','style.css','app.js','model.js','engine.js','catalog.js','runtime-extra.js','block-shapes.js','costume-tools.js'];
const sources=await Promise.all(files.map(f=>readFile(f,'utf8')));
const version=createHash('sha256').update(sources.join('\n')).digest('hex').slice(0,12);
await mkdir('dist',{recursive:true});
for(let i=0;i<files.length;i++){let s=sources[i];if(files[i].endsWith('.js'))s=s.replace(/from (['"])(\.\/[^'"?]+\.js)\1/g,(_,q,url)=>`from ${q}${url}?v=${version}${q}`);if(files[i]==='index.html')s=s.replace(/(href="style\.css|src="app\.js)(?:\?[^" ]*)?"/g,`$1?v=${version}"`);await writeFile('dist/'+files[i],s);}
await copyFile('icon.svg','dist/icon.svg');await copyFile('dist/index.html','dist/editor.html');
console.log('Built Bark '+version+'. No external dependencies.');
