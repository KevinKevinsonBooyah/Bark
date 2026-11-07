/* Materialize the complete, pinned GPL editor source and apply the Bark changes. */
const {execFileSync}=require('node:child_process');
const fs=require('node:fs'), path=require('node:path');
const root=path.resolve(__dirname,'..'), engine=path.join(root,'engine');
const upstream=JSON.parse(fs.readFileSync(path.join(root,'upstream.json')));
function run(cmd,args,cwd=engine){execFileSync(cmd,args,{cwd,stdio:'inherit'});}
if(fs.existsSync(engine))throw new Error('engine/ already exists. Reuse it for development or remove the generated directory before a clean bootstrap.');
fs.mkdirSync(engine);
run('git',['init','--quiet']);
run('git',['remote','add','origin',upstream.repository]);
run('git',['fetch','--quiet','--depth','1','origin',upstream.commit]);
run('git',['checkout','--quiet','--detach','FETCH_HEAD']);
run('git',['apply',path.join(root,'bark.patch')]);
fs.copyFileSync(path.join(root,'engine-package.json'),path.join(engine,'package.json'));
fs.copyFileSync(path.join(root,'engine-package-lock.json'),path.join(engine,'package-lock.json'));
fs.mkdirSync(path.join(engine,'scripts'),{recursive:true});
for(const file of ['create-samples.py','runtime-tests.cjs'])fs.copyFileSync(path.join(root,'scripts',file),path.join(engine,'scripts',file));
run('python3',['scripts/create-samples.py']);
fs.copyFileSync(path.join(root,'README.md'),path.join(engine,'BARK-README.md'));
fs.copyFileSync(path.join(root,'THIRD_PARTY.md'),path.join(engine,'BARK-THIRD-PARTY.md'));
console.log('Bark source is ready in engine/. Run npm ci --ignore-scripts --legacy-peer-deps there.');
