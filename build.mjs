import {mkdir,copyFile} from 'node:fs/promises';
await mkdir('dist',{recursive:true});
for(const f of ['index.html','style.css','app.js','model.js','engine.js','icon.svg'])await copyFile(f,'dist/'+f);
await copyFile('index.html','dist/editor.html');
console.log('Built Bark. No external dependencies.');
