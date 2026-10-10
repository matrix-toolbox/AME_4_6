/* Exact interactive geometry for AME46_FRACTAL.html.
   All combinatorial input is in ame46_data.js, exported from seed46.py.
   Coordinates are integer cell addresses, with y counted upwards.
   Canvas is a display only. Coverage and coefficient counts use these integers. */
(function () {
  'use strict';
  const D = window.AME46_DATA;
  if (!D) return;
  const $ = id => document.getElementById(id);
  const NS = 6;
  const palette = ['#3973a5', '#db7f32', '#47927e', '#c25f62', '#ccaa38', '#886aa5'];
  const light = ['#d5e3ef', '#f3dfcd', '#d5e8e0', '#f0dadd', '#f1e8c4', '#e3dbef'];
  const fmt = x => x.toLocaleString('en-US');
  const signText = s => s < 0 ? '−' : '+';
  const wordText = w => '(' + w.join(',') + ')';
  const entryMap = new Map(D.entries.map(e => [[e.i,e.j,e.k,e.l].join(','),e]));
  const pieces = new Map(D.pieces.map(p => [p.i+','+p.j,p]));
  const gcd = (a,b) => b ? gcd(b,a%b) : a;
  function fraction(a,b) { const g=gcd(a,b); return b/g===1 ? String(a/g) : (a/g)+'/'+(b/g); }
  function fillSelect(id, values, selected) {
    const el=$(id); el.replaceChildren();
    values.forEach(v => { const o=document.createElement('option'); o.value=Array.isArray(v)?v[0]:v; o.textContent=Array.isArray(v)?v[1]:v; el.append(o); });
    if (selected !== undefined) el.value=selected;
  }
  function digits(n,depth) { const a=Array(depth).fill(0); for(let r=depth-1;r>=0;r--){a[r]=n%6;n=Math.floor(n/6);}return a; }
  function orderedWords(order,n) { let out=[[]]; for(let r=0;r<n;r++)out=out.flatMap(w=>order.map(x=>[...w,x]));return out; }
  function nested(word) {
    let cells=[{x:0,y:0,ks:[],ls:[],ids:[],baseSign:1,extra:1}], W=1,H=1;
    for(let r=word.length-1;r>=0;r--){
      const p=pieces.get(word[r].join(',')), next=[];
      const childRow = r+1<word.length ? word[r+1][0] : null;
      for(const placement of p.placements){
        const a=D.atoms[placement.atomId];
        const factor = a.k===0 && childRow===2 ? -1 : 1;
        for(const c of cells)next.push({
          x:a.a*H+c.y, y:(a.b+1)*W-1-c.x,
          ks:[a.k,...c.ks], ls:[placement.l,...c.ls], ids:[a.id,...c.ids],
          baseSign:placement.sign*c.baseSign, extra:factor*c.extra
        });
      }
      cells=next; [W,H]=[24*H,4*W];
    }
    return {cells,W,H,word};
  }
  function lineWords(depth,kind,index) {
    const rows=orderedWords(D.display.rows,depth),cols=orderedWords(D.display.columns,depth);
    if(kind==='row')return cols.map(J=>digits(index,depth).map((i,r)=>[i,J[r]]));
    if(kind==='column')return rows.map(I=>I.map((i,r)=>[i,digits(index,depth)[r]]));
    const diag=D.display.diagonals[kind==='diagonal'?0:1];
    return rows.map(I=>I.map(i=>[i,diag[i]]));
  }
  function coverage(wordList) {
    const first=nested(wordList[0]); const counts=new Uint8Array(first.W*first.H);
    let duplicates=0;
    wordList.forEach(word=>nested(word).cells.forEach(c=>{const t=c.y*first.W+c.x;if(counts[t]++)duplicates++;}));
    let covered=0; counts.forEach(c=>{if(c)covered++;});
    return {covered,duplicates,total:counts.length,W:first.W,H:first.H};
  }
  function typeset(el) {
    if(window.MathJax && MathJax.Hub) MathJax.Hub.Queue(['Typeset',MathJax.Hub,el]);
    else if(window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([el]).catch(()=>{});
  }
  function setupCanvas(canvas,aspect= Math.sqrt(6),width=1200) {
    const height=Math.round(width/aspect);
    if(canvas.width!==width || canvas.height!==height){canvas.width=width;canvas.height=height;}
    const ctx=canvas.getContext('2d');ctx.clearRect(0,0,width,height);ctx.fillStyle='#fafafa';ctx.fillRect(0,0,width,height);
    return ctx;
  }
  function drawCells(canvas,model,colour,options={}) {
    const bounds=options.bounds || {x:0,y:0,w:model.W,h:model.H};
    const shape=options.shape||'rectangle';
    const fullRatio=shape==='square'?1:Math.sqrt(6);
    const ratio=fullRatio*(bounds.w/model.W)/(bounds.h/model.H);
    const ctx=setupCanvas(canvas,ratio,options.width||1200);
    const sx=canvas.width/bounds.w, sy=canvas.height/bounds.h;
    for(const c of model.cells){
      if(c.x<bounds.x || c.x>=bounds.x+bounds.w || c.y<bounds.y || c.y>=bounds.y+bounds.h)continue;
      const x=(c.x-bounds.x)*sx, y=(bounds.y+bounds.h-c.y-1)*sy;
      ctx.fillStyle=colour(c);ctx.fillRect(x,y,sx,sy);
      if(options.labels && sx>=20 && sy>=16){ctx.fillStyle='#111';ctx.font=Math.max(12,Math.min(sx*.42,sy*.38,28))+'px sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(options.labels(c),x+sx/2,y+sy/2);}
      if(options.markSign && options.markSign(c)<0 && sx>=6 && sy>=6){ctx.strokeStyle='#111';ctx.lineWidth=Math.max(1,Math.min(sx,sy)*.1);ctx.beginPath();ctx.moveTo(x+sx*.2,y+sy*.25);ctx.lineTo(x+sx*.8,y+sy*.25);ctx.stroke();}
    }
    if(options.grid && bounds.w<=96 && bounds.h<=96){
      ctx.strokeStyle='#777';ctx.globalAlpha=.35;ctx.lineWidth=1;
      for(let x=0;x<=bounds.w;x++){ctx.beginPath();ctx.moveTo(x*sx,0);ctx.lineTo(x*sx,canvas.height);ctx.stroke();}
      for(let y=0;y<=bounds.h;y++){ctx.beginPath();ctx.moveTo(0,y*sy);ctx.lineTo(canvas.width,y*sy);ctx.stroke();}ctx.globalAlpha=1;
    }
    return {bounds,ctx};
  }
  function legend(id,labels,colours) {
    $(id).replaceChildren();labels.forEach((label,n)=>{
      const s=document.createElement('span'),sw=document.createElement('i');sw.className='swatch';sw.style.background=colours[n];s.append(sw,document.createTextNode(label));$(id).append(s);
    });
  }
  function matrixTex(entry) {
    if(!entry)return '0';const prefix=entry.sign<0?'-':'';
    return prefix+({2:'1/\\sqrt{2}',4:'1/2',8:'1/(2\\sqrt{2})'}[entry.square.den]);
  }
  function stateTex(entry) {
    if(!entry)return '0';const prefix=entry.sign<0?'-':'';
    return prefix+({2:'1/(6\\sqrt{2})',4:'1/12',8:'1/(12\\sqrt{2})'}[entry.square.den]);
  }

  // The pure functions are also used by the included browser verification script.
  window.AME46={data:D,nested,lineWords,coverage,digits,orderedWords};
  document.body.classList.add('js-ready');
  const six=[0,1,2,3,4,5];
  ['atom-sector','decode-i','decode-j','decode-k','decode-l','explorer-i','explorer-j'].forEach(id=>fillSelect(id,six));
  fillSelect('atom-position',Array.from({length:16},(_,i)=>i));

  function renderAtom() {
    const id=Number($('atom-sector').value)*16+Number($('atom-position').value),a=D.atoms[id];
    const model={W:24,H:4,cells:D.atoms.map(x=>({x:x.a,y:x.b,...x}))};
    const {ctx}=drawCells($('atom-canvas'),model,c=>c.id===id?palette[c.k]:light[c.k],{grid:true,labels:c=>String(c.matching)});
    const sx=$('atom-canvas').width/24,sy=$('atom-canvas').height/4;
    ctx.strokeStyle='#000';ctx.lineWidth=5;ctx.strokeRect(a.a*sx+2,(3-a.b)*sy+2,sx-4,sy-4);
    $('atom-readout').textContent='Atom '+id+' at (a,b)=('+a.a+','+a.b+'). Sector k='+a.k+', matching '+a.matching+'. τ='+a.tau.join('')+', σ='+a.sigma.join('')+'. Grid numbers are matching identifiers, not quantum colours.';
    $('atom-placements').replaceChildren();a.placements.forEach(p=>{
      const tr=document.createElement('tr');[p.i,p.j,p.l,signText(p.sign)].forEach(x=>{const td=document.createElement('td');td.textContent=x;tr.append(td);});$('atom-placements').append(tr);
    });
  }
  ['atom-sector','atom-position'].forEach(id=>$(id).addEventListener('change',renderAtom));
  $('atom-canvas').addEventListener('click',ev=>{
    const box=ev.currentTarget.getBoundingClientRect(),a=Math.min(23,Math.floor((ev.clientX-box.left)*24/box.width)),b=3-Math.min(3,Math.floor((ev.clientY-box.top)*4/box.height));
    $('atom-sector').value=Math.floor(a/4);$('atom-position').value=b*4+a%4;renderAtom();
  });renderAtom();

  let assembly=[],assemblyModel=null,activePiece=null,assemblyTimer=null;
  function stopAssembly(){if(assemblyTimer)clearInterval(assemblyTimer);assemblyTimer=null;$('assembly-play').textContent='Assemble step by step';}
  function updateAssemblyOptions(resetCount=true) {
    stopAssembly();const n=Number($('assembly-depth').value),kind=$('assembly-kind').value,d=6**n;
    const old=Number($('assembly-line').value)||0;
    fillSelect('assembly-line',Array.from({length:d},(_,i)=>[i,wordText(digits(i,n))]),Math.min(old,d-1));
    $('assembly-line-label').firstChild.textContent=kind==='column'?'Column label ':'Row label ';
    $('assembly-line-label').hidden=kind==='diagonal'||kind==='antidiagonal';
    $('assembly-count').max=d;if(resetCount)$('assembly-count').value=d;
    assembly=lineWords(n,kind,Number($('assembly-line').value)).map(word=>nested(word));
    assemblyModel={W:assembly[0].W,H:assembly[0].H,cells:[]};activePiece=null;
    $('assembly-key').replaceChildren();assembly.forEach((m,p)=>{
      const b=document.createElement('button');b.type='button';b.textContent='I='+wordText(m.word.map(x=>x[0]))+', J='+wordText(m.word.map(x=>x[1]));b.title='Highlight piece I='+wordText(m.word.map(x=>x[0]))+', J='+wordText(m.word.map(x=>x[1]));b.setAttribute('aria-pressed','false');
      b.addEventListener('click',()=>{activePiece=activePiece===p?null:p;renderAssembly();});$('assembly-key').append(b);
    });renderAssembly();
  }
  function contributorColour(p,total) {return total<=6?palette[p]:'hsl('+((p*137.508)%360).toFixed(1)+' 48% '+(p%2?43:61)+'%)';}
  function renderAssembly() {
    const count=Number($('assembly-count').value),d=assembly.length,shape=$('assembly-shape').value;
    $('assembly-wrap').classList.toggle('square-view',shape==='square');
    const cells=[];for(let p=0;p<count;p++)assembly[p].cells.forEach(c=>cells.push({...c,contributor:p}));
    const model={...assemblyModel,cells};const counts=new Uint8Array(model.W*model.H);let covered=0,overlap=0;
    cells.forEach(c=>{const index=c.y*model.W+c.x;if(counts[index]++)overlap++;else covered++;});
    drawCells($('assembly-canvas'),model,c=>activePiece!==null&&c.contributor!==activePiece?'#e2e2e2':contributorColour(c.contributor,d),{shape,grid:d===6});
    $('assembly-count-label').textContent=count+' / '+d;
    $('assembly-readout').textContent=fmt(covered)+' / '+fmt(counts.length)+' cells covered, '+fmt(counts.length-covered)+' uncovered and '+overlap+' overlapping interiors. '+(count===d?'The complete line fills the whole target exactly once.':'Add the remaining pieces to complete the target.');
    [...$('assembly-key').children].forEach((b,p)=>{b.setAttribute('aria-pressed',activePiece===p?'true':'false');b.style.borderBottom='5px solid '+contributorColour(p,d);b.style.opacity=p<count?'1':'.4';});
    $('assembly-canvas').setAttribute('aria-label',count+' of '+d+' pieces of the selected line. '+covered+' of '+counts.length+' target cells covered. '+overlap+' overlaps.');
  }
  ['assembly-depth','assembly-kind','assembly-line'].forEach(id=>$(id).addEventListener('change',()=>updateAssemblyOptions()));
  $('assembly-shape').addEventListener('change',renderAssembly);$('assembly-count').addEventListener('input',()=>{stopAssembly();renderAssembly();});
  $('assembly-play').addEventListener('click',()=>{
    if(assemblyTimer){stopAssembly();return;}$('assembly-count').value=0;renderAssembly();$('assembly-play').textContent='Pause';
    assemblyTimer=setInterval(()=>{const n=Number($('assembly-count').value)+1;$('assembly-count').value=n;renderAssembly();if(n>=assembly.length)stopAssembly();},assembly.length===6?650:170);
  });updateAssemblyOptions();

  $('decode-i').value=0;$('decode-j').value=4;$('decode-k').value=0;$('decode-l').value=4;
  function renderDecoder() {
    const address=['i','j','k','l'].map(q=>Number($('decode-'+q).value)),[i,j,k,l]=address;
    const entry=entryMap.get(address.join(','));const model=nested([[i,j]]);
    const match=c=>c.ks[0]===k&&c.ls[0]===l;
    drawCells($('decode-canvas'),model,c=>match(c)?palette[l]:'#e4e6e8',{grid:true,labels:c=>(c.baseSign<0?'−':'')+c.ls[0]});
    const el=$('decode-result');const m=entry?entry.fragmentCount:0;
    el.innerHTML='<p><strong>'+m+' equal atoms'+(entry?', sign '+signText(entry.sign):'')+'.</strong> '+(entry?'Add their areas before taking the square root.':'There is no region with this complete label, so the coefficient is zero.')+'</p><div class="equation">$$\\mu=\\frac{'+m+'}{96}='+fraction(m,96)+',\\qquad U^{\\rm g}_{'+(6*i+j)+','+(6*k+l)+'}='+matrixTex(entry)+',\\qquad\\psi_{'+address.join('')+'}='+stateTex(entry)+'.$$</div>';
    typeset(el);
  }
  ['decode-i','decode-j','decode-k','decode-l'].forEach(id=>$(id).addEventListener('change',renderDecoder));
  $('decode-example').addEventListener('click',()=>{['i','j','k','l'].forEach((q,r)=>$('decode-'+q).value=[0,4,0,4][r]);renderDecoder();});renderDecoder();

  let explorer=null,explorerBounds=null,explorerWordKey='',explorerLookup=null;
  $('explorer-i').value=2;$('explorer-j').value=0;
  function currentWord() {
    if($('explorer-address').value==='controlled')return [[0,2],[2,0]];
    return Array.from({length:Number($('explorer-depth').value)},()=>[Number($('explorer-i').value),Number($('explorer-j').value)]);
  }
  function explorerColour(c) {
    switch($('explorer-colour').value){
      case 'sector':return palette[c.ks[0]];
      case 'quantum':return palette[c.ls[0]];
      case 'product-sign':return c.baseSign<0?'#b5515a':'#3973a5';
      case 'controlled-sign':return c.baseSign*c.extra<0?'#b5515a':'#3973a5';
      case 'extra-sign':return c.extra<0?'#c79e30':'#3973a5';
      default:return '#246b75';
    }
  }
  function renderExplorer() {
    const custom=$('explorer-address').value==='controlled';
    ['explorer-i','explorer-j','explorer-depth'].forEach(id=>$(id).disabled=custom);
    if(custom)$('explorer-depth').value=2;
    const word=currentWord(),key=JSON.stringify(word),n=word.length;
    if(key!==explorerWordKey){
      explorer=nested(word);explorerWordKey=key;explorerLookup=new Map(explorer.cells.map(c=>[c.y*explorer.W+c.x,c]));
      const old=$('explorer-cell').value;
      fillSelect('explorer-cell',pieces.get(word[0].join(',')).atomIds.map(id=>{const a=D.atoms[id];return [id,'('+a.a+','+a.b+'), sector '+a.k];}),old);
      if(!$('explorer-cell').value)$('explorer-cell').selectedIndex=0;
      $('explorer-atom').textContent='';
    }
    const shape=$('explorer-shape').value,zoom=$('explorer-zoom').value==='cell';
    $('explorer-cell').disabled=!zoom;
    const a=D.atoms[Number($('explorer-cell').value)];
    explorerBounds=zoom?{x:a.a*explorer.W/24,y:a.b*explorer.H/4,w:explorer.W/24,h:explorer.H/4}:{x:0,y:0,w:explorer.W,h:explorer.H};
    $('explorer-wrap').classList.toggle('square-view',shape==='square'&&!zoom);
    const viewRatio=(shape==='square'?1:Math.sqrt(6))*(explorerBounds.w/explorer.W)/(explorerBounds.h/explorer.H);
    $('explorer-wrap').style.maxWidth=zoom?Math.round(620*viewRatio)+'px':'';
    const mode=$('explorer-colour').value;
    const markSign=mode==='product-sign'?c=>c.baseSign:mode==='controlled-sign'?c=>c.baseSign*c.extra:mode==='extra-sign'?c=>c.extra:null;
    drawCells($('explorer-canvas'),explorer,explorerColour,{shape,bounds:explorerBounds,width:zoom?Math.max(200,Math.round(1200*viewRatio)):1100,markSign});
    if(mode==='sector')legend('explorer-legend',six.map(x=>'first k = '+x),palette);
    else if(mode==='quantum')legend('explorer-legend',six.map(x=>'first l = '+x),palette);
    else if(mode==='product-sign'||mode==='controlled-sign')legend('explorer-legend',['positive','negative'],['#3973a5','#b5515a']);
    else if(mode==='extra-sign')legend('explorer-legend',['no extra minus','extra minus (toggle)'],['#3973a5','#c79e30']);
    else legend('explorer-legend',['occupied region'],['#246b75']);
    const visible=zoom?16**(n-1):16**n;
    const minusProduct=explorer.cells.filter(c=>c.baseSign<0).length,minusControl=explorer.cells.filter(c=>c.baseSign*c.extra<0).length;
    $('explorer-readout').textContent='I='+wordText(word.map(p=>p[0]))+', J='+wordText(word.map(p=>p[1]))+'. '+fmt(16**n)+' atoms. Target grid '+fmt(explorer.W)+' × '+fmt(explorer.H)+'. Area fraction 1/'+fmt(6**n)+'. '+(zoom?'The magnified outer cell contains '+fmt(visible)+' descendants. ':'')+'Negative atoms: '+fmt(minusProduct)+' with product signs, '+fmt(minusControl)+' with controlled signs. '+(mode==='quantum'?'Only the first colour digit is drawn. Complete words are available by clicking.':'');
    $('explorer-canvas').setAttribute('aria-label','Piece I='+wordText(word.map(p=>p[0]))+', J='+wordText(word.map(p=>p[1]))+', depth '+n+', '+fmt(visible)+' atoms in view. '+(zoom?'Magnified outer cell.':'Whole target.'));
  }
  ['explorer-address','explorer-i','explorer-j','explorer-depth','explorer-shape','explorer-colour','explorer-zoom','explorer-cell'].forEach(id=>$(id).addEventListener('change',renderExplorer));
  $('explorer-canvas').addEventListener('click',ev=>{
    const box=ev.currentTarget.getBoundingClientRect();const x=Math.min(explorer.W-1,Math.floor(explorerBounds.x+(ev.clientX-box.left)/box.width*explorerBounds.w));
    const y=Math.min(explorer.H-1,Math.ceil(explorerBounds.y+explorerBounds.h-(ev.clientY-box.top)/box.height*explorerBounds.h)-1);
    const c=explorerLookup.get(y*explorer.W+x);
    if(!c){$('explorer-atom').textContent='This cell is outside the selected piece.';return;}
    const count=explorer.cells.filter(z=>z.ks.join(',')===c.ks.join(',')&&z.ls.join(',')===c.ls.join(',')).length,n=explorer.word.length;
    $('explorer-atom').textContent='Cell ('+x+','+y+'). K='+wordText(c.ks)+', L='+wordText(c.ls)+'. Product sign '+signText(c.baseSign)+', extra factor '+signText(c.extra)+' and controlled sign '+signText(c.baseSign*c.extra)+'. This complete coefficient label occupies '+fmt(count)+' fragments: μ='+fraction(count,96**n)+'. Its state amplitude is '+signText(c.baseSign)+'√'+count+'/'+fmt(24**n)+' (product), '+signText(c.baseSign*c.extra)+'√'+count+'/'+fmt(24**n)+' (controlled).';
  });
  $('explorer-download').addEventListener('click',()=>{
    const a=document.createElement('a');a.download='AME46_piece_'+explorer.word.map(p=>p.join('-')).join('_')+'_'+$('explorer-colour').value+'.png';a.href=$('explorer-canvas').toDataURL('image/png');a.click();
  });
  $('show-control-example').addEventListener('click',()=>{
    $('explorer-address').value='controlled';$('explorer-shape').value='square';$('explorer-colour').value='controlled-sign';$('explorer-zoom').value='full';renderExplorer();
    $('explorer-address').closest('fieldset').scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'start'});
  });renderExplorer();

  fillSelect('invariant-depth',Array.from({length:12},(_,i)=>i+1),2);
  function renderInvariant(){
    const n=Number($('invariant-depth').value);let a=48n,b=6n,c=12n;
    for(let r=1;r<n;r++)[a,b,c]=[48n*a+68n*b+60n*c,6n*a-6n*b-12n*c,12n*a+16n*b+12n*c];
    const j=a+2n*b+c,p=72n**BigInt(n);
    $('invariant-readout').textContent='n='+n+': controlled numerator Jₙ='+j+' and seed-power numerator 72ⁿ='+p+'. Common denominator 6^'+(8*n)+'. '+(j===p?'They coincide at the seed level.':'The invariant values differ.');
  }$('invariant-depth').addEventListener('change',renderInvariant);renderInvariant();

  function dimension(t){return Math.log(16*t*t)/Math.log(t*Math.sqrt(96));}
  function renderDimension(){
    const t=Number($('refinement').value),canvas=$('dimension-canvas'),ctx=setupCanvas(canvas,2.75,1100);
    $('refinement-label').textContent=t;$('refinement-readout').textContent=fmt(16*t*t)+' retained cells out of '+fmt(96*t*t)+'. Scale ratio 1/('+t+'√96). Hausdorff dimension '+dimension(t).toFixed(12)+'. Base area fraction remains 1/6.';
    const L=82,R=30,T=25,B=60,w=canvas.width-L-R,h=canvas.height-T-B;
    const X=x=>L+(x-1)/15*w,Y=y=>T+(2-y)*h;
    ctx.font='20px serif';ctx.textAlign='right';ctx.textBaseline='middle';
    [1,1.25,1.5,1.75,2].forEach(y=>{ctx.strokeStyle='#d0d0d0';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(L,Y(y));ctx.lineTo(L+w,Y(y));ctx.stroke();ctx.fillStyle='#111';ctx.fillText(y.toFixed(2),L-12,Y(y));});
    ctx.textAlign='center';[1,2,4,8,12,16].forEach(x=>{ctx.fillStyle='#111';ctx.fillText(x,X(x),canvas.height-B+24);});
    for(let x=1;x<=16;x++){ctx.fillStyle=x===t?'#c79e30':'#246b75';ctx.beginPath();ctx.arc(X(x),Y(dimension(x)),x===t?9:5,0,Math.PI*2);ctx.fill();}
    ctx.fillStyle='#111';ctx.fillText('integer subdivision t',L+w/2,canvas.height-12);
    ctx.save();ctx.translate(20,T+h/2);ctx.rotate(-Math.PI/2);ctx.fillText('Hausdorff dimension',0,0);ctx.restore();
    canvas.setAttribute('aria-label','Dimension for subdivision t='+t+' is '+dimension(t).toFixed(12)+'. Values increase toward 2.');
  }$('refinement').addEventListener('input',renderDimension);renderDimension();

  function renderAutomaton(){
    const value=$('automaton-example').value;
    const entries=value==='controlled'?[[0,2,0,2],[2,0,0,3]]:value==='chain'?[[0,2,0,2],[2,0,0,3],[2,0,0,3]]:[[0,4,0,4]];
    let q=0,eps=1,toggles=0;$('automaton-rows').replaceChildren();
    entries.forEach((address,r)=>{
      const e=entryMap.get(address.join(',')),factor=q&&address[0]===2?-1:1,nextQ=address[2]===0?1:0;
      eps*=e.sign*factor;if(factor<0)toggles++;
      const tr=document.createElement('tr');[r+1,wordText(address),q,signText(e.sign),signText(factor),nextQ,signText(eps)].forEach(v=>{const td=document.createElement('td');td.textContent=v;tr.append(td);});$('automaton-rows').append(tr);q=nextQ;
    });
    $('automaton-readout').textContent=toggles+' extra sign toggle'+(toggles===1?'':'s')+' and final controlled sign '+signText(eps)+'. '+(toggles===2?'The two extra factors cancel, although the intermediate sign changes.':'The base sign and each extra factor are multiplied in sequence.');
  }$('automaton-example').addEventListener('change',renderAutomaton);renderAutomaton();

  document.addEventListener('visibilitychange',()=>{if(document.hidden)stopAssembly();});
  window.AME46.ready=true;
})();
