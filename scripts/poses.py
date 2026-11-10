"""The eleven Fištrónek poses in the brand style C, each with one moving part."""
from skeleton import *
import skeleton as gen
V="C"
LEG="#3a415a"; LINE="#c9cedb"; PEND="#8a90a6"; TAPE="#f2c94c"; STEAM="#a9b1cc"
BROOM="#8a6a45"; STRAW="#c9a15b"; STRAW_LINE="#a8823f"

def S(dark): return style_for(V,dark)
def oc(dark): return INK if not dark else "#c3cae0"   # outline colour
def ow(dark,w=3): return f' stroke="{oc(dark)}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'

def wingpath(d,dark,cls=None,origin="104px 110px",extra=""):
    s=S(dark); body=sh(d,s["wing"],s)
    if cls: return f'<g class="{cls}" style="transform-origin:{origin}">{body}{extra}</g>'
    return body+extra

def shadow(w=46,dark=False): return f'<ellipse cx="96" cy="172" rx="{w}" ry="5" fill="{IND if not dark else "#000"}" opacity="0.12"/>'

def cb(x,y,s,dark,anim="pop"):
    k=s/20
    return (f'<g class="{anim}" style="transform-origin:{x+s/2}px {y+s/2}px"><rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{4.5*k}" fill="{LEAF}"{ow(dark,2.5)}/>'
            f'<path d="M{x+4.5*k} {y+10*k} L{x+8.5*k} {y+14*k} L{x+15.5*k} {y+6*k}" stroke="#fff" stroke-width="{2.8*k}" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g>')

def scrap(x,y,r,s=1):
    return f'<g transform="translate({x} {y}) rotate({r}) scale({s})"><rect x="-6" y="-4" width="12" height="8" rx="2" fill="{LINE}"/><path d="M-3 -2 L3 2 M3 -2 L-3 2" stroke="{PEND}" stroke-width="1.5"/></g>'

def P(name,dark=False):
    s=S(dark)
    if name in ("main","investigating","chase"): return pose(V,name,dark)
    if name=="skeptical":
        w=wingpath("M92 114 Q124 102 156 110 L174 116 L154 120 Q124 126 98 128 Z",dark)
        body=crow(V,dark,dict(px=4,py=3,brow="M114 52 Q124 44 136 58"),wing=w)
        return (shadow(40,dark)+f'<g transform="translate(-16 0)">{body}</g>'
                f'<g transform="translate(178 148) scale(0.6)"><g class="hop">{flaky(V,dark)}</g></g>')
    if name=="telescope":
        tel=(f'<g class="arm" style="transform-origin:96px 110px">'+sh("M90 114 Q116 98 138 80 L146 88 Q120 112 98 128 Z",s["wing"],s)+
             f'<path d="M132 70 L166 48 L174 60 L138 82 Z" fill="{LEG}"{ow(dark)}/><path d="M162 42 L182 30 L190 46 L172 58 Z" fill="{IND}"{ow(dark)}/></g>')
        return shadow(46,dark)+crow(V,dark,dict(px=2,py=-2,brow="M112 56 Q124 50 136 54"),wing=tel)
    if name=="broom":
        br=(f'<g class="sweep2" style="transform-origin:112px 104px">'+sh("M94 112 Q114 112 130 128 L124 136 Q106 126 92 126 Z",s["wing"],s)+
            f'<path d="M114 102 L160 158" stroke="{BROOM}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M150 152 L176 148 L184 174 L150 176 Z" fill="{STRAW}"{ow(dark,2.5)}/><path d="M156 158 L160 174 M164 156 L168 175 M172 154 L176 174" stroke="{STRAW_LINE}" stroke-width="2"/></g>')
        return shadow(52,dark)+crow(V,dark,dict(px=3,py=4,brow="M112 54 Q124 48 136 56"),wing=br)+scrap(188,168,-20)+scrap(194,152,15,0.85)
    if name=="stamp":
        paper=(f'<g transform="translate(142 130) rotate(-6)"><rect x="-6" y="-22" width="52" height="64" rx="4" fill="#fff"{ow(dark,2)}/>'
               f'<path d="M2 -10 H36 M2 -2 H30 M2 6 H34" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>{cb(10,16,18,dark,"pop late")}</g>')
        arm=(f'<g class="press">'+sh("M94 108 Q130 98 156 108 L154 118 Q126 122 100 126 Z",s["wing"],s)+
             f'<rect x="152" y="86" width="10" height="18" rx="3" fill="{LEG}"{ow(dark,2)}/><rect x="146" y="102" width="22" height="8" rx="2" fill="{IND}"{ow(dark,2)}/></g>')
        return shadow(56,dark)+paper+f'<g transform="translate(-16 0)">{crow(V,dark,dict(px=3,py=3,brow="M112 54 Q124 48 136 56"),wing=arm)}</g>'
    if name=="conductor":
        back=(f'<g class="baton" style="transform-origin:104px 104px">'+sh("M88 106 Q94 48 132 24 Q118 56 112 104 Z",s["wing"],s)+
              f'<path d="M130 26 L164 8" stroke="{INK if not dark else "#c3cae0"}" stroke-width="3" stroke-linecap="round"/><circle cx="165" cy="8" r="2.5" fill="#fff"{ow(dark,1.5)}/></g>')
        notes=(f'<g class="float"><g fill="{LEAF}"><circle cx="168" cy="122" r="5"/><rect x="172" y="98" width="2.6" height="25"/></g>'
               f'<path d="M174 98 Q184 102 182 112" stroke="{LEAF}" stroke-width="2.6" fill="none"/></g>'
               f'<g class="float late" fill="{IND if not dark else "#c9d0f2"}" opacity="0.7"><circle cx="188" cy="80" r="4.2"/><rect x="191.2" y="60" width="2.2" height="21"/></g>')
        return shadow(46,dark)+crow(V,dark,dict(px=2,py=-1,brow="M112 54 Q124 46 136 54"),back=back)+notes
    if name=="chef":
        toque=(f'<g transform="translate(6 3)"><path d="M100 50 Q92 30 106 28 Q110 14 122 20 Q134 14 138 30 Q150 34 134 52 Z" fill="#fff"{ow(dark,2)}/>'
               f'<path d="M101 50 L134 52 L133 58 L102 56 Z" fill="#fff"{ow(dark,2)}/></g>')
        stir=(f'<g class="stir" style="transform-origin:150px 118px">'+sh("M94 112 Q122 100 146 98 L148 108 Q124 116 100 126 Z",s["wing"],s)+
              f'<path d="M146 102 L156 118" stroke="{LEG}" stroke-width="4" stroke-linecap="round"/></g>')
        pot=(f'<path class="steam" d="M160 108 q-6 -8 0 -14 q6 -6 0 -14 M174 108 q-6 -8 0 -14 q6 -6 0 -14" stroke="{STEAM}" stroke-width="2.5" stroke-linecap="round" fill="none"/>'
             f'<rect x="138" y="122" width="58" height="46" rx="8" fill="{LEG}"{ow(dark)}/><rect x="134" y="116" width="66" height="9" rx="4" fill="{INK}"{ow(dark,2)}/>'
             f'<path d="M138 134 h-7 M196 134 h7" stroke="{INK if not dark else "#c3cae0"}" stroke-width="5" stroke-linecap="round"/>{cb(158,136,18,dark,"")}')
        return shadow(60,dark)+crow(V,dark,dict(px=2,py=2,brow="M112 58 Q124 54 136 60"),wing=stir,item=toque+pot)
    if name=="desk":
        scr=(f'<rect x="142" y="56" width="58" height="46" rx="5" fill="{INK}"{ow(dark,2)}/><rect x="146" y="60" width="50" height="38" rx="2" fill="#fff"/>'
             f'<rect x="150" y="65" width="7" height="7" rx="1.6" fill="{LEAF}"/><path d="M160 68.5 H188" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
             f'<rect x="150" y="76" width="7" height="7" rx="1.6" fill="{LEAF}"/><path d="M160 79.5 H182" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
             f'<rect x="150.5" y="87.5" width="6" height="6" rx="1.4" fill="none" stroke="{PEND}" stroke-width="1.2"/><rect class="tick" x="150" y="87" width="7" height="7" rx="1.6" fill="{LEAF}"/>'
             f'<path d="M160 90.5 H186" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
             f'<path d="M171 102 V116" stroke="{INK if not dark else "#c3cae0"}" stroke-width="4"/><path d="M134 116 H200 M140 116 V168 M194 116 V168" stroke="{LEG if not dark else "#8a93b8"}" stroke-width="5" stroke-linecap="round"/>')
        w=wingpath("M92 112 Q118 104 140 102 L142 112 Q118 118 98 128 Z",dark,"type","100px 116px")
        return shadow(64,dark)+crow(V,dark,dict(big=True,px=4,py=-1,brow="M112 52 Q124 44 136 52"),wing=w,item=scr)
    if name=="quarantine":
        def tape(y,a): return (f'<g transform="rotate({a} 150 {y})"><rect x="98" y="{y-5}" width="104" height="10" fill="{TAPE}"{ow(dark,1.5)}/>'
                   + ''.join(f'<path d="M{104+i*12} {y-5} l6 10" stroke="{INK}" stroke-width="3.2"/>' for i in range(8)) + '</g>')
        w=sh("M104 104 Q82 96 54 130 Q86 138 106 122 Z",s["wing"],s)
        return (shadow(70,dark)+f'<g transform="translate(-26 6) scale(0.86)">{crow(V,dark,dict(px=5,py=2,brow="M114 54 Q126 48 138 56"),wing=w)}</g>'
                f'<g transform="translate(154 126) scale(0.76)"><g class="shake">{flaky(V,dark)}</g></g>'+tape(143,-8)+tape(154,7)+
                f'<g class="pulse" style="transform-origin:188px 90px"><circle cx="188" cy="90" r="7" fill="{LEAF}"{ow(dark,2)}/><path d="M185.5 86.5 L191 90 L185.5 93.5 Z" fill="#fff"/></g>')

ALL=["main","investigating","skeptical","chase","telescope","broom","stamp","conductor","chef","desk","quarantine"]
EXTRA_CSS="""
.sweep2{animation:sweep2 1.4s ease-in-out infinite alternate}
@keyframes sweep2{from{transform:rotate(-6deg)}to{transform:rotate(8deg)}}
.press{animation:press 2.4s ease-in-out infinite}
@keyframes press{0%,40%,100%{transform:translateY(0)}55%,65%{transform:translateY(16px)}}
.late{animation-delay:.25s}
.baton{animation:baton .9s ease-in-out infinite alternate}
@keyframes baton{from{transform:rotate(-6deg)}to{transform:rotate(10deg)}}
.float{animation:float 2s ease-in-out infinite alternate}
@keyframes float{from{transform:translateY(0)}to{transform:translateY(-8px)}}
.stir{animation:stir 1.2s ease-in-out infinite alternate}
@keyframes stir{from{transform:rotate(-8deg)}to{transform:rotate(8deg)}}
.steam{animation:steam 1.6s ease-in-out infinite}
@keyframes steam{0%{opacity:0;transform:translateY(6px)}50%{opacity:1}100%{opacity:0;transform:translateY(-8px)}}
.type{animation:type .35s ease-in-out infinite alternate}
@keyframes type{from{transform:rotate(0)}to{transform:rotate(-5deg)}}
.tick{animation:tick 3s infinite}
@keyframes tick{0%,45%{opacity:0}55%,100%{opacity:1}}
.shake{animation:shake .5s ease-in-out infinite alternate}
@keyframes shake{from{transform:rotate(-6deg)}to{transform:rotate(6deg)}}
.pulse{animation:pulse 1.6s ease-in-out infinite}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
"""
