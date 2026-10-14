(() => {
'use strict';
const DATA={"a":[0,0,0,0,-2,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,2,0,0,0,-2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,-2,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,-2,0,0,-2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,2,0,0,0,-2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,-2,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,-2,0,0,0,0,-2,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,-2,0,0,0,-2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,-2,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,-2,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,-2,0,0,0,0,0,0,2,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"b":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,-1,1,0,0,1,1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,-1,0,0,1,-1,0,0,0,0,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,1,1,0,0,-1,-1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,-1,0,0,-1,1,0,0,0,0,-1,-1,0,0],"d":4};
const $=id=>document.getElementById(id);
const FACES=['R','L','U','D','F','B'];
const NORMALS=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]];
const HOMES=[[1,1,1],[-1,1,-1],[-1,-1,1],[1,-1,-1]];
const HOME_LABELS=['RUF','LUB','LDF','RDB'];
const PAIRS=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
const AXES={R:[0,1],L:[0,-1],U:[1,1],D:[1,-1],F:[2,1],B:[2,-1]};
const KEYS={r:{face:'R',q:1},R:{face:'R',q:3},l:{face:'L',q:1},L:{face:'L',q:3},u:{face:'U',q:1},U:{face:'U',q:3},d:{face:'D',q:1},D:{face:'D',q:3},f:{face:'F',q:1},F:{face:'F',q:3},b:{face:'B',q:1},B:{face:'B',q:3}};
const FACE_COLOURS={R:'#dc443d',L:'#f4a13b',U:'#f4f2e9',D:'#f4d643',F:'#269267',B:'#397cce'};
const BASES={R:[[0,0,-1],[0,1,0]],L:[[0,0,1],[0,1,0]],U:[[1,0,0],[0,0,-1]],D:[[1,0,0],[0,0,1]],F:[[1,0,0],[0,1,0]],B:[[-1,0,0],[0,1,0]]};
const I3=()=>[[1,0,0],[0,1,0],[0,0,1]],clone=x=>JSON.parse(JSON.stringify(x));
const eq=(a,b)=>a.length===b.length&&a.every((x,i)=>x===b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),add=(a,b)=>a.map((x,i)=>x+b[i]),scale=(a,s)=>a.map(x=>x*s);
const mv=(a,v)=>a.map(row=>dot(row,v));
const mm=(a,b)=>a.map(row=>b[0].map((_,j)=>row.reduce((s,x,k)=>s+x*b[k][j],0)));

// Cube rotations, the permutation of the four body diagonals and D(R) on their six oriented pairs.
function rot(face,q=1){const [ax,side]=AXES[face],p=[[1,2],[2,0],[0,1]][ax],count=((-side*q)%4+4)%4,R=I3();for(let n=0;n<count;n++){const a=R[p[0]].slice(),b=R[p[1]].slice();R[p[0]]=b.map(x=>-x);R[p[1]]=a;}return R;}
function rotContinuous(axis,angle){const R=I3(),[a,b]=[[1,2],[2,0],[0,1]][axis],c=Math.cos(angle),s=Math.sin(angle);R[a][a]=c;R[a][b]=-s;R[b][a]=s;R[b][b]=c;return R;}
function diagonalPermutation(R){return HOMES.map(v=>{const w=mv(R,v);return HOMES.findIndex(x=>eq(w,x)||eq(w,scale(x,-1)));});}
function wedge(R){const sig=diagonalPermutation(R),D=Array.from({length:6},()=>Array(6).fill(0));PAIRS.forEach(([i,j],col)=>{const a=sig[i],b=sig[j],r=PAIRS.findIndex(x=>x[0]===Math.min(a,b)&&x[1]===Math.max(a,b));D[r][col]=a<b?1:-1;});return D;}
function parse(word){const ts=word.replaceAll('’',"'").replaceAll('′',"'").trim().split(/\s+/).filter(Boolean);if(ts.some(t=>!/^[RLUDFB](2|')?$/.test(t)))throw Error("use R L U D F B moves separated by spaces, with optional 2 or '");return ts.map(t=>({face:t[0],q:t.endsWith('2')?2:t.endsWith("'")?3:1}));}
function token(m){return m.face+(m.q===2?'2':m.q===3?"'":'');}
function invert(m){return {face:m.face,q:4-m.q};}
function frameStep(fs,face,q=1){const [ax,side]=AXES[face],Q=rot(face,q);return fs.map((R,p)=>mv(R,HOMES[p])[ax]===side?mm(Q,R):clone(R));}

// Exact state: O(R) = W D(R) W^T acts on one party; W = H + I4 in the mixed basis, W = I6 in the pair basis.
function reduce(t){while(t.d%2===0&&t.a.every(x=>x%2===0)&&t.b.every(x=>x%2===0)){t.d/=2;t.a=t.a.map(x=>x/2);t.b=t.b.map(x=>x/2);}return t;}
function hblock(t,axis){const stride=6**(3-axis),a=t.a.map(x=>2*x),b=t.b.map(x=>2*x);for(let i=0;i<1296;i++){if(Math.floor(i/stride)%6!==0)continue;const j=i+stride;a[i]=2*(t.b[i]+t.b[j]);a[j]=2*(t.b[i]-t.b[j]);b[i]=t.a[i]+t.a[j];b[j]=t.a[i]-t.a[j];}return reduce({a,b,d:t.d*2});}
function local(t,D,axis){const a=Array(1296).fill(0),b=Array(1296).fill(0),stride=6**(3-axis);for(let i=0;i<1296;i++){const old=Math.floor(i/stride)%6;for(let r=0;r<6;r++)if(D[r][old]){const j=i+(r-old)*stride;a[j]=D[r][old]*t.a[i];b[j]=D[r][old]*t.b[i];}}return {a,b,d:t.d};}
function decode(fs,which){let t={a:DATA.a.slice(),b:DATA.b.slice(),d:DATA.d};fs.forEach((R,p)=>{if(which==='mixed')t=hblock(t,p);t=local(t,wedge(R),p);if(which==='mixed')t=hblock(t,p);});return t;}
const reference={a:DATA.a.slice(),b:DATA.b.slice(),d:DATA.d};
function index(q){return ((q[0]*6+q[1])*6+q[2])*6+q[3];}
function digits(i){return [Math.floor(i/216),Math.floor(i/36)%6,Math.floor(i/6)%6,i%6];}
function flattenIndex(r,c,pair){const rest=[0,1,2,3].filter(x=>!pair.includes(x)),q=[0,0,0,0];q[pair[0]]=Math.floor(r/6);q[pair[1]]=r%6;q[rest[0]]=Math.floor(c/6);q[rest[1]]=c%6;return index(q);}
// a a^T + 2 b b^T = d^2 I and a b^T + b a^T = 0 for all six two-party flattenings.
function isAME(t){const M=Math.max(...t.a.map(Math.abs),...t.b.map(Math.abs));if(!Number.isSafeInteger(t.d)||108*M*M+t.d*t.d>=Number.MAX_SAFE_INTEGER)throw Error('exact integer range exceeded');
 for(let p=0;p<4;p++)for(let q=p+1;q<4;q++){const A=[],B=[];for(let r=0;r<36;r++){A.push([]);B.push([]);for(let c=0;c<36;c++){const j=flattenIndex(r,c,[p,q]);A[r].push(t.a[j]);B[r].push(t.b[j]);}}
  for(let r=0;r<36;r++)for(let s=r;s<36;s++){let x=r===s?-t.d*t.d:0,y=0;for(let c=0;c<36;c++){x+=A[r][c]*A[s][c]+2*B[r][c]*B[s][c];y+=A[r][c]*B[s][c]+B[r][c]*A[s][c];}if(x||y)return false;}}
 return true;}
function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b){const t=b;b=a%b;a=t;}return a||1;}
function simplified(a,b,d){const g=gcd(gcd(a,b),d);return {a:a/g,b:b/g,d:d/g};}
function fraction(a,d){const g=gcd(a,d),n=Math.abs(a/g);return (a<0?'−':'')+(d/g===1?String(n):`${n}/${d/g}`);}
function exact(a,b,d){if(!b)return fraction(a,d);const term=v=>{const f=fraction(Math.abs(v),d);return (f==='1'?'':f+'·')+'√2';};if(!a)return (b<0?'−':'')+term(b);return fraction(a,d)+(b<0?' − ':' + ')+term(b);}
function scalarProduct(t,u){const M=Math.max(...t.a.map(Math.abs),...t.b.map(Math.abs)),N=Math.max(...u.a.map(Math.abs),...u.b.map(Math.abs));if(3888*M*N>=Number.MAX_SAFE_INTEGER)throw Error('exact overlap bound exceeded');let a=0,b=0;for(let i=0;i<1296;i++){a+=t.a[i]*u.a[i]+2*t.b[i]*u.b[i];b+=t.a[i]*u.b[i]+t.b[i]*u.a[i];}return simplified(a,b,36*t.d*u.d);}
function square(s){if(3*Math.max(Math.abs(s.a),Math.abs(s.b))**2>=Number.MAX_SAFE_INTEGER||s.d*s.d>=Number.MAX_SAFE_INTEGER)throw Error('exact probability bound exceeded');return simplified(s.a*s.a+2*s.b*s.b,2*s.a*s.b,s.d*s.d);}
function approx(s){return (s.a+Math.SQRT2*s.b)/s.d;}
function shortDecimal(s){if(!s.a&&!s.b)return '0';if(!s.b&&s.a===s.d)return '1';return Math.max(0,approx(s)).toPrecision(4);}
function frameMatrix(R,which){const D=wedge(R);if(which==='pairs')return {a:D.flat(),b:Array(36).fill(0),d:1};const A=Array.from({length:6},()=>Array(6).fill(0)),B=Array.from({length:6},()=>Array(6).fill(0));for(let i=2;i<6;i++)A[i][i]=2;B[0][0]=B[0][1]=B[1][0]=1;B[1][1]=-1;const aa=mm(mm(A,D),A),bb=mm(mm(B,D),B),ab=mm(mm(A,D),B),ba=mm(mm(B,D),A);return reduce({a:aa.flat().map((v,i)=>v+2*bb.flat()[i]),b:ab.flat().map((v,i)=>v+ba.flat()[i]),d:4});}
function matrixEntryShort(a,b,d){if(!a&&!b)return '·';if(!b)return fraction(a,d);if(!a){const z=simplified(a,b,d);if(Math.abs(z.b)===1&&z.d===2)return (z.b<0?'−':'')+'1/√2';return exact(a,b,d);}return approx({a,b,d}).toFixed(2);}
function positionLabel(v){return v.map((s,ax)=>FACES[2*ax+(s<0?1:0)]).join('');}

// Cube state, move queue and controls.
function solvedCubies(){const out=[];for(let x=-1;x<=1;x++)for(let y=-1;y<=1;y++)for(let z=-1;z<=1;z++){if(!x&&!y&&!z)continue;const home=[x,y,z];out.push({home,position:home.slice(),R:I3(),party:HOMES.findIndex(h=>eq(h,home))});}return out;}
let cubies=solvedCubies(),frames=HOMES.map(I3),previousFrames=null,current=null,lastMove=null,wordHistory=[],queue=[],active=null,mode='mixed',selectedIndex=0,heatLookup=[];
let view={yaw:-.62,pitch:.43,zoom:1},pointer=null,rafID=0,renderDirty=true;
function error(message){$('error').textContent=message||'';}
function knownSolved(){return cubies.every(c=>eq(c.position,c.home)&&FACES.every((f,i)=>{const [ax,s]=AXES[f];return c.home[ax]!==s||eq(mv(c.R,NORMALS[i]),NORMALS[i]);}));}
function busy(){return !!active||queue.length>0;}
function syncControlState(){const b=busy();$('undo').disabled=b||!wordHistory.length;$('solve').disabled=b||!wordHistory.length;$('stop').disabled=!b;
 $('moveCount').textContent=`${wordHistory.length} move${wordHistory.length===1?'':'s'}`+(queue.length?' (press escape to stop)':'');
 $('cubeStatus').textContent=queue.length?`${queue.length} move${queue.length===1?'':'s'} queued`:active?'turning':knownSolved()?'solved':'scrambled';}
function commit(move,operation){
 const before=clone(frames),[axis,side]=AXES[move.face],Q=rot(move.face,move.q),affected=[];
 frames.forEach((R,p)=>{if(mv(R,HOMES[p])[axis]===side)affected.push(p);});
 cubies.forEach(c=>{if(c.position[axis]===side){c.position=mv(Q,c.position);c.R=mm(Q,c.R);}});
 frames=frameStep(frames,move.face,move.q);
 previousFrames=before;lastMove={...move,affected};
 if(operation==='undo')wordHistory.pop();else wordHistory.push({...move});
 refresh();renderDirty=true;
}
function enqueue(moves,operation='normal'){if(moves.length+queue.length>1000){error('the queue is limited to 1000 moves');return;}error(null);queue.push(...moves.map(m=>({move:m,operation})));syncControlState();requestDraw();}
function beginNext(time){if(active||!queue.length)return;const item=queue.shift();if(!$('animate').checked){commit(item.move,item.operation);syncControlState();return;}
 const [axis,side]=AXES[item.move.face],q=item.move.q,angle=-side*(q===3?-1:q)*Math.PI/2;
 active={...item,axis,side,angle,started:time,duration:q===2?350:235,progress:0};syncControlState();}
function stopQueue(){queue=[];syncControlState();requestDraw();}
function resetCube(){queue=[];active=null;cubies=solvedCubies();frames=HOMES.map(I3);previousFrames=null;lastMove=null;wordHistory=[];error(null);refresh();renderDirty=true;requestDraw();}
function applyWord(word){try{enqueue(parse(word));}catch(e){error(e.message);}}
function scramble(){const moves=[];let lastAxis=-1;for(let i=0;i<20;i++){let f;do{f=FACES[Math.floor(Math.random()*6)];}while(AXES[f][0]===lastAxis);lastAxis=AXES[f][0];moves.push({face:f,q:1+Math.floor(Math.random()*3)});}enqueue(moves);}
function retrace(){if(!busy())enqueue(wordHistory.slice().reverse().map(invert),'undo');}
function undo(){if(!busy()&&wordHistory.length)enqueue([invert(wordHistory[wordHistory.length-1])],'undo');}

// Software 3D renderer of the 26 cubies and the unfolded net.
function camera(p){const sy=Math.sin(view.yaw),cy=Math.cos(view.yaw),sp=Math.sin(view.pitch),cp=Math.cos(view.pitch),x=cy*p[0]+sy*p[2],z=-sy*p[0]+cy*p[2];return [x,cp*p[1]-sp*z,sp*p[1]+cp*z];}
function project(p,w,h){const v=camera(p),s=Math.min(w,h)*1.57*view.zoom/(9-v[2]);return [w/2+v[0]*s,h/2-v[1]*s,v[2]];}
function preparedCanvas(canvas){const r=canvas.getBoundingClientRect(),dpr=Math.min(window.devicePixelRatio||1,2),w=r.width,h=r.height;if(canvas.width!==Math.round(w*dpr)||canvas.height!==Math.round(h*dpr)){canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);}const ctx=canvas.getContext('2d');ctx.setTransform(dpr,0,0,dpr,0,0);return {ctx,w,h};}
function polygon(ctx,vertices,fill,stroke=null,line=1){ctx.beginPath();vertices.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.closePath();ctx.fillStyle=fill;ctx.fill();if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=line;ctx.stroke();}}
function shade(hex,f){const n=parseInt(hex.slice(1),16),ch=[n>>16,(n>>8)&255,n&255];return `rgb(${ch.map(x=>Math.round(Math.min(255,x*f))).join(',')})`;}
function renderCube(){const {ctx,w,h}=preparedCanvas($('cubeCanvas'));ctx.clearRect(0,0,w,h);
 const polys=[],turn=active?rotContinuous(active.axis,active.angle*(active.progress<.5?4*active.progress**3:1-(-2*active.progress+2)**3/2)):null;
 cubies.forEach(c=>{let R=c.R,pos=c.position;if(active&&pos[active.axis]===active.side){R=mm(turn,R);pos=mv(turn,pos);}FACES.forEach((f,fi)=>{const normal=mv(R,NORMALS[fi]),center=add(pos,scale(normal,.467)),cc=camera(center),nn=camera(normal);if(dot(nn,[-cc[0],-cc[1],9-cc[2]])<=0)return;
  const [u0,v0]=BASES[f],u=mv(R,u0),v=mv(R,v0),shape=(half,offset)=>[[-1,-1],[1,-1],[1,1],[-1,1]].map(([a,b])=>project(add(add(add(pos,scale(normal,offset)),scale(u,a*half)),scale(v,b*half)),w,h));
  const [ax,s]=AXES[f],hasSticker=c.home[ax]===s,level=Math.abs(c.home[0])+Math.abs(c.home[1])+Math.abs(c.home[2]),light=.71+.29*Math.max(0,dot(nn,[.18,.5,.82]));
  polys.push({depth:cc[2],body:shape(.471,.471),sticker:hasSticker?shape(.382,.474):null,colour:shade(FACE_COLOURS[f],light),center:project(add(pos,scale(normal,.476)),w,h),party:hasSticker?c.party:-1,label:hasSticker&&level===1?f:'',normal:nn});
 });});
 polys.sort((a,b)=>a.depth-b.depth);polys.forEach(p=>{polygon(ctx,p.body,shade('#1b242a',.78+.34*Math.abs(p.normal[2])),'#0a151c',.75);if(!p.sticker)return;polygon(ctx,p.sticker,p.colour,'#ffffff14',.6);
  const edge=Math.hypot(p.sticker[1][0]-p.sticker[0][0],p.sticker[1][1]-p.sticker[0][1]),edge2=Math.hypot(p.sticker[2][0]-p.sticker[1][0],p.sticker[2][1]-p.sticker[1][1]),radius=Math.min(edge,edge2)*.225;
  ctx.textAlign='center';ctx.textBaseline='middle';
  if(p.party>=0&&radius>2){ctx.fillStyle='#122631e8';ctx.beginPath();ctx.arc(p.center[0],p.center[1],Math.max(5,radius),0,2*Math.PI);ctx.fill();ctx.fillStyle='#fff';ctx.font=`700 ${Math.max(8,radius*1.32)}px sans-serif`;ctx.fillText('ABCD'[p.party],p.center[0],p.center[1]+.3);}
  else if(p.label){ctx.fillStyle='#132d3aca';ctx.font=`600 ${Math.max(10,radius*1.6)}px sans-serif`;ctx.fillText(p.label,p.center[0],p.center[1]);}
 });
}
function stickerRecords(){const out=[];cubies.forEach(c=>FACES.forEach((f,fi)=>{const [ax,s]=AXES[f];if(c.home[ax]===s)out.push({position:c.position.slice(),normal:mv(c.R,NORMALS[fi]),original:f,party:c.party});}));return out;}
function renderNet(){const {ctx,w,h}=preparedCanvas($('netCanvas'));ctx.clearRect(0,0,w,h);const box=Math.min((w-10)/4,(h-13)/3),cell=(box-5)/3,net={L:[0,0,[0,1,0],[0,0,-1]],U:[1,0,[1,0,0],[0,0,-1]],F:[1,1,[1,0,0],[0,1,0]],R:[2,1,[0,0,-1],[0,1,0]],D:[2,2,[0,0,-1],[1,0,0]],B:[3,2,[0,1,0],[1,0,0]]},offx=(w-4*box)/2,offy=(h-3*box)/2;
 const records=stickerRecords();FACES.forEach((f,fi)=>{const [gx,gy,u,v]=net[f],x=offx+gx*box,y=offy+gy*box;records.filter(s=>eq(s.normal,NORMALS[fi])).forEach(s=>{const col=1+dot(s.position,u),row=1-dot(s.position,v),xx=x+col*cell,yy=y+row*cell;ctx.fillStyle=FACE_COLOURS[s.original];ctx.fillRect(xx,yy,cell-1,cell-1);ctx.strokeStyle='#00000030';ctx.strokeRect(xx+.5,yy+.5,cell-2,cell-2);ctx.textBaseline='middle';ctx.textAlign='center';
  if(s.party>=0){ctx.fillStyle='#172f35';ctx.font=`700 ${Math.max(8,cell*.61)}px sans-serif`;ctx.fillText('ABCD'[s.party],xx+(cell-1)/2,yy+(cell-1)/2+.5);}
  else if(col===1&&row===1){ctx.fillStyle='#1b373e';ctx.font=`600 ${Math.max(8,cell*.62)}px sans-serif`;ctx.fillText(f,xx+(cell-1)/2,yy+(cell-1)/2+.5);}});});}
function tick(time){rafID=0;if(!active)beginNext(time);if(active){active.progress=Math.min(1,(time-active.started)/active.duration);renderCube();if(active.progress>=1){const finished=active;active=null;try{commit(finished.move,finished.operation);}catch(e){error(e.message);queue=[];}syncControlState();renderDirty=true;}}else if(renderDirty){renderCube();renderDirty=false;}if(active||queue.length||renderDirty)requestDraw();}
function requestDraw(){if(!rafID)rafID=requestAnimationFrame(tick);}

// Readouts of the decoded state and of the local frames.
function refresh(){mode=$('mode').value;current=decode(frames,mode);const previous=previousFrames?decode(previousFrames,mode):null;
 if(!isAME(current))error('exact AME check failed');
 const norm=scalarProduct(current,current),ov=scalarProduct(reference,current),fidelity=square(ov),prev=previous?scalarProduct(previous,current):null;
 if(norm.a!==norm.d||norm.b)throw Error('state normalization check failed');
 $('fidelity').textContent=shortDecimal(fidelity);$('fidelity').title=exact(fidelity.a,fidelity.b,fidelity.d);$('overlap').textContent='⟨ψ₀|ψ⟩ = '+exact(ov.a,ov.b,ov.d);
 $('support').textContent=current.a.reduce((n,a,i)=>n+(a||current.b[i]?1:0),0);
 if(lastMove){const people=lastMove.affected.map(p=>'ABCD'[p]);$('action').innerHTML=`<code>${token(lastMove)}</code> moves ${people.length?'parties '+people.join(', '):'no marked corner'}, `+(!people.length?'the state did not change':prev&&!prev.a&&!prev.b?'the new state is orthogonal to the previous one':'the local frames changed but the state is still AME');}
 else $('action').textContent='reference state ψ₀, all four local frames are the identity';
 $('history').textContent=wordHistory.length?wordHistory.map(token).join(' '):'no moves';$('history').scrollTop=$('history').scrollHeight;
 renderNet();renderHeat();inspectCoefficient(selectedIndex);renderGates();syncControlState();
}
// Drawn in device pixels with whole-pixel cell edges, so all grid lines and the frame have the same width.
function renderHeat(){const canvas=$('heatCanvas'),dpr=Math.min(window.devicePixelRatio||1,2),W=Math.max(36,Math.round(canvas.getBoundingClientRect().width*dpr));if(canvas.width!==W||canvas.height!==W){canvas.width=W;canvas.height=W;}
 const ctx=canvas.getContext('2d'),pair=$('flatten').value.split('').map(Number),edge=n=>Math.round(n*W/36),lw=Math.max(1,Math.round(dpr));heatLookup=Array.from({length:36},(_,r)=>Array.from({length:36},(_,c)=>flattenIndex(r,c,pair)));ctx.clearRect(0,0,W,W);
 for(let r=0;r<36;r++)for(let c=0;c<36;c++){const j=heatLookup[r][c],a=(current.a[j]+Math.SQRT2*current.b[j])/(6*current.d),v=Math.min(1,Math.sqrt(Math.abs(a)*6)),white=[248,250,247],colour=a<0?[72,111,166]:[190,99,62];ctx.fillStyle=`rgb(${white.map((w,k)=>Math.round(w*(1-v)+colour[k]*v)).join(',')})`;ctx.fillRect(edge(c),edge(r),edge(c+1)-edge(c),edge(r+1)-edge(r));}
 ctx.fillStyle='#62746770';for(let j=0;j<=36;j+=6){const x=Math.min(edge(j),W-lw);ctx.fillRect(x,0,lw,W);ctx.fillRect(0,x,W,lw);}
 for(let r=0;r<36;r++)for(let c=0;c<36;c++)if(heatLookup[r][c]===selectedIndex){ctx.strokeStyle='#152c30';ctx.lineWidth=2*lw;ctx.strokeRect(edge(c)+lw,edge(r)+lw,edge(c+1)-edge(c)-2*lw,edge(r+1)-edge(r)-2*lw);}
}
function inspectCoefficient(j){selectedIndex=j;const a=current.a[j],b=current.b[j],d=6*current.d,p=square(simplified(a,b,d));$('ket').textContent='|'+digits(j).join('')+'⟩';$('amplitude').textContent=exact(a,b,d);$('probability').textContent=exact(p.a,p.b,p.d);}
function renderGates(){const step=$('gateView').value==='step';$('gateGrid').innerHTML=frames.map((R,p)=>{const affected=!!lastMove&&lastMove.affected.includes(p),Q=step?(affected?rot(lastMove.face,lastMove.q):I3()):R,M=frameMatrix(Q,mode);
 return `<div class="gate${affected?' affected':''}"><div><b>${'ABCD'[p]}</b> <code>${HOME_LABELS[p]}</code> → <code>${positionLabel(mv(R,HOMES[p]))}</code></div><div class="matrix">${M.a.map((a,i)=>{const b=M.b[i],val=(a+Math.SQRT2*b)/M.d;return `<span class="${val>0?'pos':val<0?'neg':''}" title="row ${Math.floor(i/6)}, column ${i%6}: ${exact(a,b,M.d)}">${matrixEntryShort(a,b,M.d)}</span>`;}).join('')}</div></div>`;}).join('');}

function boot(){
 $('turnButtons').innerHTML=FACES.map(f=>{const style=`background:${FACE_COLOURS[f]};color:${'ULD'.includes(f)?'#000':'#fff'}`;return `<div><button data-face="${f}" title="key ${f.toLowerCase()}" style="${style}"><code>${f}</code></button><button data-inverse="${f}" title="key ${f}" style="${style}"><code>${f}<span class="prime">'</span></code></button></div>`;}).join('');
 document.querySelectorAll('[data-face]').forEach(b=>b.addEventListener('click',()=>enqueue([{face:b.dataset.face,q:1}])));
 document.querySelectorAll('[data-inverse]').forEach(b=>b.addEventListener('click',()=>enqueue([{face:b.dataset.inverse,q:3}])));
 $('scramble').onclick=scramble;$('undo').onclick=undo;$('solve').onclick=retrace;$('stop').onclick=stopQueue;$('reset').onclick=resetCube;
 $('applyWord').onclick=()=>applyWord($('word').value);$('word').addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();applyWord(e.target.value);}});
 $('mode').onchange=refresh;$('flatten').onchange=renderHeat;$('gateView').onchange=renderGates;
 $('homeView').onclick=()=>{view={yaw:-.62,pitch:.43,zoom:1};renderDirty=true;requestDraw();};
 window.addEventListener('keydown',e=>{if(e.ctrlKey||e.metaKey||e.altKey||e.isComposing)return;const t=e.target;if(t instanceof Element&&(t.closest('input,textarea,select')||t.isContentEditable||t.closest('.MathJax_Menu')))return;if(Object.hasOwn(KEYS,e.key)){e.preventDefault();enqueue([{...KEYS[e.key]}]);}else if(e.key==='Escape'){e.preventDefault();stopQueue();}});
 const cv=$('cubeCanvas');cv.addEventListener('pointerdown',e=>{pointer={id:e.pointerId,x:e.clientX,y:e.clientY};cv.setPointerCapture(e.pointerId);cv.focus({preventScroll:true});});
 cv.addEventListener('pointermove',e=>{if(!pointer||pointer.id!==e.pointerId)return;view.yaw+=(e.clientX-pointer.x)*.009;view.pitch=Math.max(-1.35,Math.min(1.35,view.pitch+(e.clientY-pointer.y)*.009));pointer.x=e.clientX;pointer.y=e.clientY;renderDirty=true;requestDraw();});
 const up=()=>{pointer=null;};cv.addEventListener('pointerup',up);cv.addEventListener('pointercancel',up);
 cv.addEventListener('wheel',e=>{e.preventDefault();view.zoom=Math.max(.7,Math.min(1.45,view.zoom*Math.exp(-e.deltaY*.0006)));renderDirty=true;requestDraw();},{passive:false});
 const inspect=e=>{const r=$('heatCanvas').getBoundingClientRect(),col=Math.min(35,Math.max(0,Math.floor((e.clientX-r.left)/r.width*36))),row=Math.min(35,Math.max(0,Math.floor((e.clientY-r.top)/r.height*36)));inspectCoefficient(heatLookup[row][col]);renderHeat();};
 $('heatCanvas').addEventListener('pointermove',inspect);$('heatCanvas').addEventListener('click',inspect);
 const ro=new ResizeObserver(()=>{renderDirty=true;renderNet();if(current)renderHeat();requestDraw();});ro.observe(cv);ro.observe($('heatCanvas'));
 if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)$('animate').checked=false;
 refresh();requestDraw();
}
try{boot();}catch(e){error(e.message);console.error(e);}
})();
