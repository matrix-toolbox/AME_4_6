const TABLE_I = [
  {
    "k": 0,
    "m": 0,
    "tau": "251340",
    "sigma": [
      "253104"
    ],
    "denominator": 4
  },
  {
    "k": 0,
    "m": 1,
    "tau": "341205",
    "sigma": [
      "243150"
    ],
    "denominator": 4
  },
  {
    "k": 0,
    "m": 2,
    "tau": "430215",
    "sigma": [
      "423150"
    ],
    "denominator": 4
  },
  {
    "k": 0,
    "m": 3,
    "tau": "520341",
    "sigma": [
      "523104"
    ],
    "denominator": 4
  },
  {
    "k": 1,
    "m": 0,
    "tau": "253014",
    "sigma": [
      "350241"
    ],
    "denominator": 4
  },
  {
    "k": 1,
    "m": 1,
    "tau": "342051",
    "sigma": [
      "340215"
    ],
    "denominator": 4
  },
  {
    "k": 1,
    "m": 2,
    "tau": "432150",
    "sigma": [
      "430215"
    ],
    "denominator": 4
  },
  {
    "k": 1,
    "m": 3,
    "tau": "523104",
    "sigma": [
      "530241"
    ],
    "denominator": 4
  },
  {
    "k": 2,
    "m": 0,
    "tau": "035142",
    "sigma": [
      "314025"
    ],
    "denominator": 4
  },
  {
    "k": 2,
    "m": 1,
    "tau": "124035",
    "sigma": [
      "315042"
    ],
    "denominator": 4
  },
  {
    "k": 2,
    "m": 2,
    "tau": "215043",
    "sigma": [
      "134025"
    ],
    "denominator": 4
  },
  {
    "k": 2,
    "m": 3,
    "tau": "304125",
    "sigma": [
      "135042"
    ],
    "denominator": 4
  },
  {
    "k": 3,
    "m": 0,
    "tau": "031452",
    "sigma": [
      "201534"
    ],
    "denominator": 4
  },
  {
    "k": 3,
    "m": 1,
    "tau": "120534",
    "sigma": [
      "201453"
    ],
    "denominator": 4
  },
  {
    "k": 3,
    "m": 2,
    "tau": "210453",
    "sigma": [
      "021534"
    ],
    "denominator": 4
  },
  {
    "k": 3,
    "m": 3,
    "tau": "301524",
    "sigma": [
      "021453"
    ],
    "denominator": 4
  },
  {
    "k": 4,
    "m": 0,
    "tau": "142530",
    "sigma": [
      "415320",
      "504321"
    ],
    "denominator": 16
  },
  {
    "k": 4,
    "m": 1,
    "tau": "145203",
    "sigma": [
      "412503",
      "502413"
    ],
    "denominator": 16
  },
  {
    "k": 4,
    "m": 2,
    "tau": "152403",
    "sigma": [
      "415302",
      "504312"
    ],
    "denominator": 16
  },
  {
    "k": 4,
    "m": 3,
    "tau": "154320",
    "sigma": [
      "402531",
      "512430"
    ],
    "denominator": 16
  },
  {
    "k": 4,
    "m": 4,
    "tau": "403512",
    "sigma": [
      "054312",
      "145302"
    ],
    "denominator": 16
  },
  {
    "k": 4,
    "m": 5,
    "tau": "405231",
    "sigma": [
      "042531",
      "152430"
    ],
    "denominator": 16
  },
  {
    "k": 4,
    "m": 6,
    "tau": "503421",
    "sigma": [
      "054321",
      "145320"
    ],
    "denominator": 16
  },
  {
    "k": 4,
    "m": 7,
    "tau": "504312",
    "sigma": [
      "052413",
      "142503"
    ],
    "denominator": 16
  },
  {
    "k": 5,
    "m": 0,
    "tau": "042513",
    "sigma": [
      "415302",
      "504312"
    ],
    "denominator": 16
  },
  {
    "k": 5,
    "m": 1,
    "tau": "045231",
    "sigma": [
      "412530",
      "502431"
    ],
    "denominator": 16
  },
  {
    "k": 5,
    "m": 2,
    "tau": "052431",
    "sigma": [
      "415320",
      "504321"
    ],
    "denominator": 16
  },
  {
    "k": 5,
    "m": 3,
    "tau": "054312",
    "sigma": [
      "402513",
      "512403"
    ],
    "denominator": 16
  },
  {
    "k": 5,
    "m": 4,
    "tau": "413520",
    "sigma": [
      "054321",
      "145320"
    ],
    "denominator": 16
  },
  {
    "k": 5,
    "m": 5,
    "tau": "415203",
    "sigma": [
      "042513",
      "152403"
    ],
    "denominator": 16
  },
  {
    "k": 5,
    "m": 6,
    "tau": "513402",
    "sigma": [
      "054312",
      "145302"
    ],
    "denominator": 16
  },
  {
    "k": 5,
    "m": 7,
    "tau": "514320",
    "sigma": [
      "052431",
      "142530"
    ],
    "denominator": 16
  }
];
const MATCHING_WORDS = ["23310102", "21303021", "32113020", "11302230", "7632321056014475", "6013617402535724"];
const COLORS = ["#FF6666", "#65D8E8", "#DC6EEB", "#69D879", "#F0DE5C", "#6867EF"];
const DISPLAY_ROWS = [0,2,4,5,3,1];
const DISPLAY_COLS = [2,4,0,1,5,3];
// signs computed from Eq. (5), independently of Table I and Eq. (B1)
const COEFFICIENT_SIGNS = {"0,0,2,3":1,"0,0,3,2":1,"0,0,5,4":-1,"0,0,5,5":-1,"0,1,2,3":1,"0,1,3,2":-1,"0,1,4,4":1,"0,1,4,5":-1,"0,2,0,2":1,"0,2,1,3":1,"0,2,2,1":1,"0,2,3,0":1,"0,3,0,2":-1,"0,3,1,3":1,"0,3,2,1":-1,"0,3,3,0":1,"0,4,0,4":-1,"0,4,1,4":-1,"0,4,4,0":1,"0,4,4,1":1,"0,4,5,0":1,"0,4,5,1":-1,"0,5,0,5":1,"0,5,1,5":-1,"0,5,4,0":-1,"0,5,4,1":1,"0,5,5,0":1,"0,5,5,1":1,"1,0,2,3":-1,"1,0,3,2":1,"1,0,4,4":1,"1,0,4,5":-1,"1,1,2,3":-1,"1,1,3,2":-1,"1,1,5,4":-1,"1,1,5,5":-1,"1,2,0,2":-1,"1,2,1,3":1,"1,2,2,1":1,"1,2,3,0":-1,"1,3,0,2":1,"1,3,1,3":1,"1,3,2,1":-1,"1,3,3,0":-1,"1,4,0,4":-1,"1,4,1,4":1,"1,4,4,0":1,"1,4,4,1":-1,"1,4,5,0":1,"1,4,5,1":1,"1,5,0,5":1,"1,5,1,5":1,"1,5,4,0":-1,"1,5,4,1":-1,"1,5,5,0":1,"1,5,5,1":-1,"2,0,0,3":1,"2,0,3,1":1,"2,1,0,3":-1,"2,1,3,1":1,"2,2,1,0":1,"2,2,4,4":1,"2,2,4,5":1,"2,2,5,4":-1,"2,2,5,5":1,"2,3,1,0":-1,"2,3,4,4":1,"2,3,4,5":1,"2,3,5,4":-1,"2,3,5,5":1,"2,4,2,5":1,"2,4,4,2":-1,"2,4,5,2":1,"2,5,2,4":1,"2,5,4,2":1,"2,5,5,2":1,"3,0,1,2":1,"3,0,2,0":1,"3,1,1,2":1,"3,1,2,0":-1,"3,2,0,1":1,"3,2,4,4":1,"3,2,4,5":1,"3,2,5,4":1,"3,2,5,5":-1,"3,3,0,1":1,"3,3,4,4":-1,"3,3,4,5":-1,"3,3,5,4":-1,"3,3,5,5":1,"3,4,3,5":-1,"3,4,4,3":1,"3,4,5,3":1,"3,5,3,4":1,"3,5,4,3":1,"3,5,5,3":-1,"4,0,0,5":1,"4,0,1,4":1,"4,0,4,0":1,"4,0,4,1":1,"4,0,5,0":-1,"4,0,5,1":-1,"4,1,0,5":1,"4,1,1,4":-1,"4,1,4,0":1,"4,1,4,1":-1,"4,1,5,0":-1,"4,1,5,1":1,"4,2,2,4":1,"4,2,3,5":1,"4,2,4,2":-1,"4,2,4,3":1,"4,2,5,2":-1,"4,2,5,3":1,"4,3,2,4":1,"4,3,3,5":-1,"4,3,4,2":-1,"4,3,4,3":-1,"4,3,5,2":-1,"4,3,5,3":-1,"4,4,0,0":1,"4,4,2,2":1,"4,5,1,1":1,"4,5,3,3":-1,"5,0,0,4":1,"5,0,1,5":-1,"5,0,4,0":1,"5,0,4,1":-1,"5,0,5,0":1,"5,0,5,1":-1,"5,1,0,4":1,"5,1,1,5":1,"5,1,4,0":1,"5,1,4,1":1,"5,1,5,0":1,"5,1,5,1":1,"5,2,2,5":1,"5,2,3,4":-1,"5,2,4,2":1,"5,2,4,3":1,"5,2,5,2":-1,"5,2,5,3":-1,"5,3,2,5":1,"5,3,3,4":1,"5,3,4,2":1,"5,3,4,3":-1,"5,3,5,2":-1,"5,3,5,3":1,"5,4,1,1":1,"5,4,3,3":1,"5,5,0,0":1,"5,5,2,2":-1};

// exact accumulation in units of 1/16: each w is either 4/16 or 1/16
const AREA_UNITS = Object.create(null);
const CONTRIBUTIONS = Object.create(null);
for (const record of TABLE_I) {
  for (let q = 0; q < record.sigma.length; q++) {
    for (let i = 0; i < 6; i++) {
      const j = Number(record.tau[i]), l = Number(record.sigma[q][i]);
      const key = [i,j,record.k,l].join(',');
      AREA_UNITS[key] = (AREA_UNITS[key] || 0) + 16/record.denominator;
      (CONTRIBUTIONS[key] ||= []).push({m:record.m, q:q+1, denominator:record.denominator});
    }
  }
}

const byId = id => document.getElementById(id);
const gcd = (a,b) => b ? gcd(b,a%b) : a;
function fraction(n,d) { const g=gcd(n,d); return d/g === 1 ? String(n/g) : `${n/g}/${d/g}`; }
function chip(l) { return `<span class="color-chip${l===5?' color-dark':''}" style="--color:${COLORS[l]}">${l}</span>`; }
function amplitude(units,sign,normalized=false) {
  const value = normalized ? ({2:'1/(12\\sqrt{2})',4:'1/12',8:'1/(6\\sqrt{2})'})[units] : ({2:'1/(2\\sqrt{2})',4:'1/2',8:'1/\\sqrt{2}'})[units];
  return '$'+(sign<0?'-':'+')+(value || `\\sqrt{${fraction(units,16)}}${normalized?'/6':''}`)+'$';
}
function ordinal(n) { return n + ((n%100>=11 && n%100<=13)?'<sup>th</sup>':({1:'<sup>st</sup>',2:'<sup>nd</sup>',3:'<sup>rd</sup>'}[n%10]||'<sup>th</sup>')); }

function renderEdge(record,i) {
  const word=MATCHING_WORDS[record.k], count=word.length;
  const x0=35, y0=65, width=660, height=54, slotWidth=width/count;
  let occurrence=0;
  const parts=[];
  for (let t=0;t<count;t++) {
    const selected=Number(word[t])===record.m;
    let fill='#f3f3f3', textFill='#111', l=null, negative=false;
    if(selected) {
      const q=record.sigma.length===1?0:occurrence;
      l=Number(record.sigma[q][i]);
      negative=COEFFICIENT_SIGNS[[i,Number(record.tau[i]),record.k,l].join(',')]<0;
      fill=COLORS[l]; textFill=l===5?'#fff':'#111'; occurrence++;
    }
    const x=x0+t*slotWidth;
    parts.push(`<rect x="${x}" y="${y0}" width="${slotWidth}" height="${height}" fill="${fill}" stroke="#777"/>`);
    if(negative) parts.push(`<rect x="${x}" y="${y0}" width="${slotWidth}" height="${height}" fill="url(#edge-hatch-live)"/>`);
    parts.push(`<text x="${x+slotWidth/2}" y="${y0+35}" font-size="23" text-anchor="middle" fill="${textFill}" style="paint-order:stroke;stroke:${fill};stroke-width:3px;stroke-linejoin:round">${word[t]}</text>`);
    if(selected) parts.push(`<text x="${x+slotWidth/2}" y="${y0-13}" text-anchor="middle" font-size="16">l=${l}</text>`);
  }
  const occurrences=[...word].flatMap((m,t)=>Number(m)===record.m?[t+1]:[]);
  return `<svg viewBox="0 0 730 165" role="img" aria-labelledby="live-edge-title live-edge-desc"><title id="live-edge-title">Edge order for sector ${record.k}</title><desc id="live-edge-desc">Matching ${record.m} occupies intervals ${occurrences.join(' and ')} of ${count}. Colored intervals show its contribution to cell ${i},${record.tau[i]}. Hatching indicates a negative coefficient.</desc><defs><pattern id="edge-hatch-live" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M-2 2L2-2M0 8L8 0M6 10L10 6" stroke="#222" stroke-width=".6"/></pattern></defs><text x="35" y="25" font-size="17">matching labels along the edge</text>${parts.join('')}<text x="35" y="148" font-size="16">0</text><text x="695" y="148" text-anchor="end" font-size="16">1</text><text x="365" y="148" text-anchor="middle" font-size="16">each interval has width 1/${count}</text></svg>`;
}

function renderGrid(record,chosenI) {
  const x0=45,y0=40,size=44;
  const out=[];
  for(let a=0;a<6;a++) out.push(`<text x="27" y="${y0+a*size+28}" text-anchor="middle" font-size="17">${DISPLAY_ROWS[a]}</text>`);
  for(let b=0;b<6;b++) out.push(`<text x="${x0+b*size+22}" y="27" text-anchor="middle" font-size="17">${DISPLAY_COLS[b]}</text>`);
  for(let a=0;a<6;a++) for(let b=0;b<6;b++) {
    const i=DISPLAY_ROWS[a],j=DISPLAY_COLS[b],x=x0+b*size,y=y0+a*size;
    const selected=Number(record.tau[i])===j;
    out.push(`<rect x="${x}" y="${y}" width="${size}" height="${size}" fill="${a===b||a+b===5?'#f1f1f1':'#fff'}" stroke="#aaa"/>`);
    if(selected) {
      const qn=record.sigma.length;
      record.sigma.forEach((s,q)=>{
        const l=Number(s[i]), xx=x+q*size/qn, w=size/qn;
        out.push(`<rect x="${xx+1}" y="${y+1}" width="${w-2}" height="${size-2}" fill="${COLORS[l]}"/><text x="${xx+w/2}" y="${y+29}" text-anchor="middle" font-size="20" fill="${l===5?'#fff':'#111'}">${l}</text>`);
      });
      if(i===chosenI) out.push(`<rect x="${x+1.5}" y="${y+1.5}" width="${size-3}" height="${size-3}" fill="none" stroke="#111" stroke-width="3"/>`);
    }
  }
  return `<svg viewBox="0 0 350 322" role="img" aria-labelledby="live-grid-title live-grid-desc"><title id="live-grid-title">Cells selected by the matching</title><desc id="live-grid-desc">Rows and columns use the paper's printed ordering. Colors and their numbers mark six selected cells. The selected row's cell is outlined. A paired color record shows sigma one on the left and sigma two on the right.</desc><text x="10" y="27" font-size="17">i / j</text>${out.join('')}</svg><p class="small">Printed cell labels are shown outside the grid. ${record.sigma.length===2?'Each selected cell shows $\\sigma_1$ on the left and $\\sigma_2$ on the right. ':'The numbers inside are color labels. '}The outlined cell is the chosen row. This is a selection map, not the shape of the complete pieces.</p>`;
}

function renderExplorer() {
  const k=Number(byId('sector-select').value),m=Number(byId('matching-select').value),i=Number(byId('row-select').value);
  const record=TABLE_I.find(r=>r.k===k&&r.m===m);
  const j=Number(record.tau[i]), qn=record.sigma.length;
  const word=MATCHING_WORDS[k],slots=[...word].flatMap((x,t)=>Number(x)===m?[t]:[]);
  byId('selected-record').innerHTML=`<span>$k=${k}$</span><span>$m=${m}$</span><span>\${\\tau=}$ <code>${record.tau}</code></span><span>\${\\sigma_1=}$ <code>${record.sigma[0]}</code></span><span>${qn===2?`\${\\sigma_2=}$ <code>${record.sigma[1]}</code>`:'$\\sigma_2=\\mbox{—}$'}</span><span>$w=1/${record.denominator}$</span>`;
  const rows=[];
  for(let ii=0;ii<6;ii++) rows.push(`<tr class="${ii===i?'chosen-row':''}"><th scope="row">${ii}</th><td>${record.tau[ii]}</td><td>${chip(Number(record.sigma[0][ii]))}</td>${qn===2?`<td>${chip(Number(record.sigma[1][ii]))}</td>`:''}</tr>`);
  byId('digit-table').innerHTML=`<table><caption>Read the digits at the chosen row label, highlighted below.</caption><thead><tr><th>row $i$</th><th>column $\\tau(i)$</th><th>color $\\sigma_1(i)$</th>${qn===2?'<th>color $\\sigma_2(i)$</th>':''}</tr></thead><tbody>${rows.join('')}</tbody></table>`;
  byId('edge-view').innerHTML=renderEdge(record,i);
  byId('selection-grid').innerHTML=renderGrid(record,i);
  const intervals=slots.map(t=>`[${fraction(t,word.length)}, ${fraction(t+1,word.length)}]`);
  byId('reading-result').innerHTML=`<h3>record details:</h3><p>At row <strong>$i=${i}$</strong>, the selected column is <strong>$j=${j}$</strong>. Work in <strong>sector $k=${k}$</strong> of <strong>cell (${i}, ${j})</strong>.</p><p>Matching ${m} owns the <strong>${ordinal(slots[0]+1)} and ${ordinal(slots[1]+1)} intervals</strong>. With equal widths, these are <strong>${intervals.join(' and ')}</strong>.</p><p>${qn===1?`Both intervals use color <strong>${record.sigma[0][i]}</strong>. This record contributes 1/${record.denominator} to that color's area.`:`The first interval uses color <strong>${record.sigma[0][i]}</strong> from $\\sigma_1$, the second uses color <strong>${record.sigma[1][i]}</strong> from $\\sigma_2$. Each color word contributes 1/${record.denominator}.`}</p>`;
  const colors=[...new Set(record.sigma.map(s=>Number(s[i])))];
  const results=[];
  for(const l of colors) {
    const key=[i,j,k,l].join(','),total=AREA_UNITS[key],sign=COEFFICIENT_SIGNS[key];
    const terms=CONTRIBUTIONS[key],own=terms.filter(t=>t.m===m).reduce((s,t)=>s+16/t.denominator,0);
    const termText=terms.map(t=>`1/${t.denominator} ($m=${t.m}$, $\\sigma_${t.q}$)`).join(' + ');
    results.push(`<p><strong>Color $l=${l}$:</strong> this record adds ${fraction(own,16)}. ${total===own?'It supplies the complete area for this coefficient.':`Other matching records also contribute. The complete area is ${fraction(total,16)}.`}</p><p class="small">All contributions: ${termText} = <strong>${fraction(total,16)}</strong>.</p><p>\${T^{\\rm g}_{${i}${j}${k}${l}}=}$ <strong>${amplitude(total,sign)}</strong>, normalized state amplitude = <strong>${amplitude(total,sign,true)}</strong>.</p>`);
  }
  byId('coefficient-result').innerHTML=`<h3>after adding all matching records:</h3>${results.join('')}<p class="small">The sign is taken from Eq. (5) and the selected edge intervals are hatched when it is negative.</p>`;
  byId('explorer').dataset.selection=[k,m,i].join(',');
  if (window.MathJax && MathJax.Hub) MathJax.Hub.Queue(['Typeset', MathJax.Hub, byId('explorer-result')]);
}

byId('sector-select').addEventListener('change',()=>{
  const k=Number(byId('sector-select').value);
  const current=Number(byId('matching-select').value);
  byId('matching-select').innerHTML=TABLE_I.filter(r=>r.k===k).map(r=>`<option value="${r.m}">${r.m}</option>`).join('');
  byId('matching-select').value=String(Math.min(current,k<4?3:7));
  renderExplorer();
});
byId('matching-select').addEventListener('change',renderExplorer);
byId('row-select').addEventListener('change',renderExplorer);
byId('paired-example').addEventListener('click',()=>{
  byId('sector-select').value='4';
  byId('sector-select').dispatchEvent(new Event('change'));
  byId('matching-select').value='0';
  byId('row-select').value='0';
  renderExplorer();
});
