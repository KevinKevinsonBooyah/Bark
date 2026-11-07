from pathlib import Path
import json, hashlib, zipfile, copy, wave, math, io, struct
out=Path('static/samples');out.mkdir(parents=True,exist_ok=True)
dog='''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="96" viewBox="0 0 100 96"><g stroke="#472e28" stroke-width="3" stroke-linejoin="round"><path d="M28 50 Q8 67 20 87 L31 86 L35 74 L63 74 L69 88 L80 87 Q92 65 72 49" fill="#d39251"/><path d="M26 27 Q5 11 6 37 Q5 57 24 52 M73 27 Q98 10 95 38 Q96 57 76 52" fill="#704737"/><path d="M21 33 Q20 9 49 10 Q79 10 80 35 L77 56 Q74 71 50 71 Q25 71 22 55Z" fill="#eeb778"/><ellipse cx="50" cy="52" rx="21" ry="15" fill="#ffe1ad"/><path d="M43 46 Q50 42 58 46 Q57 55 50 55 Q44 54 43 46" fill="#392a28"/><path d="M50 55 V60 M50 60 Q42 65 39 60 M50 60 Q58 65 62 60" fill="none"/><ellipse cx="34" cy="35" rx="3" ry="5" fill="#302529"/><ellipse cx="66" cy="35" rx="3" ry="5" fill="#302529"/><path d="M79 66 Q97 61 92 49" fill="none" stroke-width="7"/></g></svg>'''
backdrop='<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360"><rect width="480" height="360" fill="#ffffff"/></svg>'
assets={}
def costume(svg,name,cx,cy):
 data=svg.encode();h=hashlib.md5(data).hexdigest();assets[h+'.svg']=data
 return dict(assetId=h,md5ext=h+'.svg',dataFormat='svg',name=name,bitmapResolution=1,rotationCenterX=cx,rotationCenterY=cy)
c=costume(dog,'Bark',50,48);bg=costume(backdrop,'White',240,180)
def base():
 stage=dict(isStage=True,name='Stage',variables={'score':['score',0]},lists={},broadcasts={'party':'party'},blocks={},comments={},currentCostume=0,costumes=[bg],sounds=[],volume=100,layerOrder=0,tempo=60,videoTransparency=50,videoState='off',textToSpeechLanguage=None)
 sprite=dict(isStage=False,name='Bark',variables={},lists={},broadcasts={},blocks={},comments={},currentCostume=0,costumes=[c],sounds=[],volume=100,layerOrder=1,visible=True,x=0,y=0,size=80,direction=90,draggable=False,rotationStyle='left-right')
 return dict(targets=[stage,sprite],monitors=[],extensions=[],meta=dict(semver='3.0.0',vm='0.2.0',agent='Bark'))
def block(op,next=None,parent=None,inputs=None,fields=None,top=False,x=50,y=50):
 d=dict(opcode=op,next=next,parent=parent,inputs=inputs or {},fields=fields or {},shadow=False,topLevel=top)
 if top:d.update(x=x,y=y)
 return d
def num(v):return [1,[4,str(v)]]
def text(v):return [1,[10,str(v)]]
def save(name,p):
 with zipfile.ZipFile(out/(name+'.sb3'),'w',zipfile.ZIP_DEFLATED) as z:
  z.writestr('project.json',json.dumps(p))
  for k,v in assets.items():z.writestr(k,v)
p=base();p['targets'][1]['blocks']={
 'flag':block('event_whenflagclicked','loop',top=True),
 'loop':block('control_forever',parent='flag',inputs={'SUBSTACK':[2,'move']}),
 'move':block('motion_movesteps','bounce','loop',{'STEPS':num(10)}),
 'bounce':block('motion_ifonedgebounce',parent='move')}
save('bounce',p)
p=base();b=p['targets'][1]['blocks'];b.update({
 'flag':block('event_whenflagclicked','set',top=True),
 'set':block('data_setvariableto','loop','flag',{'VALUE':text(0)},{'VARIABLE':['score','score']}),
 'loop':block('control_forever',parent='set',inputs={'SUBSTACK':[2,'change']}),
 'change':block('data_changevariableby','check','loop',{'VALUE':num(1)},{'VARIABLE':['score','score']}),
 'check':block('control_if','wait','change',{'CONDITION':[2,'greater'],'SUBSTACK':[2,'send']}),
 'greater':block('operator_gt',parent='check',inputs={'OPERAND1':[3,'read',[10,'']],'OPERAND2':text(3)}),
 'read':block('data_variable',parent='greater',fields={'VARIABLE':['score','score']}),
 'send':block('event_broadcast',parent='check',inputs={'BROADCAST_INPUT':[1,[11,'party','party']]}),
 'wait':block('control_wait',parent='check',inputs={'DURATION':num(.3)})})
second=copy.deepcopy(p['targets'][1]);second.update(name='Buddy',x=120,size=60,layerOrder=2);p['targets'][1]['x']=-110
second['blocks']={'receive':block('event_whenbroadcastreceived','turn',fields={'BROADCAST_OPTION':['party','party']},top=True),'turn':block('motion_turnright','say','receive',{'DEGREES':num(30)}),'say':block('looks_say',parent='turn',inputs={'MESSAGE':text('Party!')})};second['rotationStyle']='all around';p['targets'].append(second)
p['monitors']=[dict(id='score',mode='default',opcode='data_variable',params={'VARIABLE':'score'},spriteName=None,value=0,width=0,height=0,x=10,y=10,visible=True,sliderMin=0,sliderMax=100,isDiscrete=True)];save('broadcast',p)
p=base();p['targets'][1]['blocks']={
 'flag':block('event_whenflagclicked','loop',top=True),'loop':block('control_forever',parent='flag',inputs={'SUBSTACK':[2,'if']}),
 'if':block('control_if_else',parent='loop',inputs={'CONDITION':[2,'finger'],'SUBSTACK':[2,'goto'],'SUBSTACK2':[2,'mouse']}),
 'finger':block('sensing_fingerdown',parent='if',inputs={'FINGER_OPTION':num(1)}),
 'goto':block('motion_gotoxy',parent='if',inputs={'X':[3,'fx',[4,'0']],'Y':[3,'fy',[4,'0']]}),
 'fx':block('sensing_fingerx',parent='goto',inputs={'FINGER_OPTION':num(1)}),'fy':block('sensing_fingery',parent='goto',inputs={'FINGER_OPTION':num(1)}),
 'mouse':block('motion_gotoxy',parent='if',inputs={'X':[3,'mx',[4,'0']],'Y':[3,'my',[4,'0']]}),'mx':block('sensing_mousex',parent='mouse'),'my':block('sensing_mousey',parent='mouse')};save('touch',p)
# Blank new project with original Bark dog and a short generated bark-like sound.
p=base();p['targets'][0]['variables']={};p['targets'][0]['broadcasts']={}
with io.BytesIO() as stream:
 with wave.open(stream,'wb') as w:
  w.setnchannels(1);w.setsampwidth(2);w.setframerate(22050)
  w.writeframes(b''.join(struct.pack('<h',int(9000*math.exp(-18*i/22050)*math.sin(2*math.pi*(190*i/22050-80*(i/22050)**2)))) for i in range(6600)))
 data=stream.getvalue()
h=hashlib.md5(data).hexdigest();assets[h+'.wav']=data
p['targets'][1]['sounds']=[dict(assetId=h,name='Bark',dataFormat='wav',format='',rate=22050,sampleCount=6600,md5ext=h+'.wav')]
save('blank',p)
Path('src/lib/default-project/default-project.sb3').write_bytes((out/'blank.sb3').read_bytes())
print('Created three examples and Bark default project')
