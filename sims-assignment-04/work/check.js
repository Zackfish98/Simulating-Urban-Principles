const fs=require('fs');const h=fs.readFileSync('index.html','utf8');
const data=h.match(/<script id="data"[^>]*>([\s\S]*?)<\/script>/)[1];
let code=h.match(/<script>([\s\S]*?)<\/script>/)[1];
const els={};function mk(){return {style:{},children:[],setAttribute(){},appendChild(c){this.children.push(c);return c},removeChild(){},get firstChild(){return null},addEventListener(){},querySelector(){return mk()},set innerHTML(v){},value:'0',textContent:''}}
global.document={getElementById:id=>id==='data'?{textContent:data}:(els[id]=els[id]||(id==='clock'?Object.assign(mk(),{value:'0'}):id==='edgeDist'?Object.assign(mk(),{value:'10'}):mk())),createElementNS:()=>mk(),createElement:()=>mk(),querySelectorAll:()=>[],querySelector:()=>mk()};
global.window={};eval(code);
const s=window.__sandbox;
for(const k of ['shortest','edge','shade']){const r=s.routes[k];console.log(k,r?('pts '+r.length):'NO ROUTE', 'score',r?s.score(k).toFixed(1):'');}
console.log('speed',s.SPEED.toFixed(2));
