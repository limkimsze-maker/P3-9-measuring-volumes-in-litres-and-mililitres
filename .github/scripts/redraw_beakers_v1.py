from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

new_fn=r'''function beakerSVG(cap,amount){const dims=cap===1000?{w:176,h:176}:cap===500?{w:160,h:154}:{w:140,h:134};const vw=dims.w,vh=dims.h,top=22,bottom=vh-22,right=vw-34,fillH=(amount/cap)*(bottom-top),fillY=bottom-fillH,major=cap===100?10:100,minor=major/2;let ticks="",labels="";for(let m=minor;m<=cap;m+=minor){const y=bottom-(m/cap)*(bottom-top),isMajor=m%major===0,len=isMajor?21:11;ticks+=`<line x1="${right-len}" y1="${y}" x2="${right}" y2="${y}" stroke="${isMajor?'#173b5e':'#7890a5'}" stroke-width="${isMajor?2.4:1.2}"/>`;if(isMajor)labels+=`<text x="${right+4}" y="${y+4}" font-size="${cap===100?11:12}" font-weight="900" fill="#173b5e">${m}</text>`}return `<svg viewBox="0 0 ${vw} ${vh}" style="width:${vw}px;height:${vh}px;max-width:100%" aria-label="original ${cap} ml Sports Lab measuring cup"><defs><linearGradient id="sailCup${cap}${amount}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#8edff0"/><stop offset="1" stop-color="#4bb1d2"/></linearGradient></defs><path d="M23 17 H${vw-28} L${vw-36} ${bottom} Q${vw-38} ${vh-9} ${vw-55} ${vh-9} H42 Q25 ${vh-9} 23 ${bottom} Z" fill="#f8fdff" stroke="#176ca5" stroke-width="4" stroke-linejoin="round"/><path d="M19 17 H${vw-24}" stroke="#176ca5" stroke-width="8" stroke-linecap="round"/><path d="M29 ${fillY} H${vw-40} L${vw-46} ${bottom-3} Q${vw-47} ${vh-15} ${vw-58} ${vh-15} H45 Q34 ${vh-15} 33 ${bottom-3} Z" fill="url(#sailCup${cap}${amount})" opacity=".9"/><line x1="30" y1="${fillY}" x2="${vw-40}" y2="${fillY}" stroke="#1689bd" stroke-width="3"/>${ticks}${labels}<rect x="32" y="28" width="${Math.max(50,vw-100)}" height="20" rx="10" fill="#176ca5"/><text x="${32+Math.max(50,vw-100)/2}" y="42" text-anchor="middle" font-size="9" font-weight="900" fill="#fff">SPORTS LAB</text><text x="${vw-18}" y="${vh-6}" text-anchor="end" font-size="12" font-weight="900" fill="#0c5c92">ml</text></svg>`}'''

s,n=re.subn(r'function beakerSVG\(cap,amount\)\{.*?\}\s*function bottleSVG',new_fn+'\nfunction bottleSVG',s,count=1,flags=re.S)
if n!=1:
    raise SystemExit('Could not replace Sailing beakerSVG')
p.write_text(s,encoding='utf-8')
