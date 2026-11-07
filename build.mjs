import {mkdir,copyFile} from 'node:fs/promises';
await mkdir('dist',{recursive:true});
for(const f of ['index.html','style.css','app.js','model.js','engine.js','catalog.js','runtime-extra.js','block-shapes.js','costume-tools.js','icon.svg'])await copyFile(f,'dist/'+f);
await copyFile('index.html','dist/editor.html');
console.log('Built Bark. No external dependencies.');
