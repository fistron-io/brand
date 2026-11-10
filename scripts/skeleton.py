"""Fištrónek skeleton: the shared crow geometry (body, head, tuft, beak, eye, wing, tail, legs),
Flaky, three basic poses and the animation CSS.

Three styles were explored: A (line), B (geometric) and C (fills with outline).
The brand uses C; A and B stay here for reference.
"""
IND="#24305e"; NIGHT="#1a2347"; INK="#1b2033"; LEAF="#3fa66b"; RED="#d64545"; WHITE="#ffffff"; PAPER="#f5f6f9"

def cbox(x,y,s,anim=True):
    k=s/20
    return (f'<g class="{ "pop" if anim else ""}" style="transform-origin:{x+s/2}px {y+s/2}px">'
            f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{4.5*k}" fill="{LEAF}"/>'
            f'<path d="M{x+4.5*k} {y+10*k} L{x+8.5*k} {y+14*k} L{x+15.5*k} {y+6*k}" stroke="#fff" stroke-width="{2.8*k}" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g>')

# ---------- shared geometry (variant A line, B geometric) ----------
TAIL="M62 116 L20 130 L28 108 Z"
BODY=(92,118,36)
HEAD=(120,76,27)
BEAK="M143 66 L174 79 L143 90 Z"
TUFT="M108 53 L114 38 L122 51 Z"
WING="M104 104 Q82 96 54 130 Q86 138 106 122 Z"
LEGS="M86 151 L84 168 M102 151 L104 168 M76 168 H92 M98 168 H112"

def style_for(v, dark=False):
    line = WHITE if dark else IND
    if v=="A":
        return dict(fill="#fff" if not dark else "#0e1430", wing="none", stroke=line, sw=5, beak="#fff" if not dark else "#0e1430", eyefill="#fff", pupil=line, outline=True)
    if v=="B":
        return dict(fill=IND if not dark else "#3a4a8c", wing=NIGHT if not dark else "#24305e", stroke="none", sw=0, beak=NIGHT if not dark else "#8a93b8", eyefill="#fff", pupil=INK, outline=False)
    if v=="C":
        return dict(fill=IND, wing=NIGHT, stroke=INK if not dark else "#c3cae0", sw=3, beak="#4a5170", eyefill="#fff", pupil=INK, outline=True)

def sh(d,fill,s,extra=""):
    st = f' stroke="{s["stroke"]}" stroke-width="{s["sw"]}" stroke-linejoin="round" stroke-linecap="round"' if s["outline"] else ""
    return f'<path d="{d}" fill="{fill}"{st}{extra}/>'

def circ(c,fill,s):
    st = f' stroke="{s["stroke"]}" stroke-width="{s["sw"]}"' if s["outline"] else ""
    return f'<circle cx="{c[0]}" cy="{c[1]}" r="{c[2]}" fill="{fill}"{st}/>'

def eye(s, v, big=False, px=0, py=0, brow=None):
    r=9 if not big else 10.5
    out=f'<g class="blink" style="transform-origin:126px 72px">'
    if v=="A":
        out+=f'<circle cx="{127+px}" cy="{72+py}" r="{5 if big else 4.2}" fill="{s["pupil"]}"/>'
    else:
        out+=f'<circle cx="126" cy="72" r="{r}" fill="#fff"/><circle cx="{129+px}" cy="{73+py}" r="{5 if big else 4.5}" fill="{INK}"/>'
    out+='</g>'
    if brow:
        out+=f'<path d="{brow}" stroke="{s["stroke"] if v!="B" else NIGHT}" stroke-width="{4.5 if v!="A" else 5}" stroke-linecap="round" fill="none"/>'
    return out

def legs(s,v,dark):
    col = (WHITE if dark else IND) if v=="A" else ("#3a415a" if not dark else "#8a93b8")
    return f'<path d="{LEGS}" stroke="{col}" stroke-width="5" stroke-linecap="round" fill="none"/>'

def crow(v, dark=False, eyeargs=None, wing=None, item="", fly=False, back=""):
    s=style_for(v,dark)
    eyeargs = eyeargs or {}
    o = sh(TAIL, s["wing"] if v!="A" else s["fill"], s)
    if fly:
        o += f'<g class="flap" style="transform-origin:92px 104px">{sh("M86 104 Q74 50 36 44 Q56 76 70 112 Z", s["wing"] if v!="A" else s["fill"], s)}</g>'
    else:
        o += legs(s,v,dark)
    o += circ(BODY, s["fill"], s)
    o += back
    o += sh(TUFT, s["fill"], s)
    o += circ(HEAD, s["fill"], s)
    o += sh(BEAK, s["beak"], s)
    if v=="A":
        o += f'<path d="M144 79 L155 79" stroke="{s["stroke"]}" stroke-width="3" stroke-linecap="round"/>'
    o += eye(s, v, **eyeargs)
    o += wing if wing is not None else f'<g class="wing" style="transform-origin:104px 110px">{sh(WING, s["wing"] if v!="A" else s["fill"], s)}</g>'
    o += item
    return o

def flaky(v, dark=False, run=False, back=False):
    spikes="M-22 -14 L-16 -34 L-6 -22 L0 -38 L6 -22 L16 -34 L22 -14 Z"
    if v=="A":
        col = WHITE if dark else IND
        bg = "#0e1430" if dark else "#fff"
        return (f'<path d="M-10 22 L-16 38 M10 22 L{18 if run else 12} {34 if run else 38}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
                f'<path d="{spikes}" fill="{bg}" stroke="{RED}" stroke-width="5" stroke-linejoin="round"/>'
                f'<circle r="25" fill="{bg}" stroke="{RED}" stroke-width="5"/>'
                f'<path d="M0 -25 A25 25 0 0 1 0 25" fill="none" stroke="{LEAF}" stroke-width="5"/>'
                f'<circle cx="{-10 if back else -6}" cy="-4" r="3.5" fill="{col}"/><circle cx="{6 if back else 10}" cy="-2" r="2.6" fill="{col}"/>'
                f'<path d="M-11 9 L-6 5 L-1 10 L4 5 L9 10" stroke="{col}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>')
    stroke = f' stroke="{INK if not dark else "#c3cae0"}" stroke-width="3" stroke-linejoin="round"' if v=="C" else ""
    leg = "#3a415a" if not dark else "#8a93b8"
    return (f'<defs><clipPath id="h{v}{int(dark)}{int(run)}"><rect x="-40" y="-60" width="40" height="120"/></clipPath></defs>'
            f'<path d="M-10 22 L-16 38 M10 22 L{18 if run else 12} {34 if run else 38}" stroke="{leg}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="{spikes}" fill="{LEAF}"/><circle r="25" fill="{LEAF}"/>'
            f'<g clip-path="url(#h{v}{int(dark)}{int(run)})"><path d="{spikes}" fill="{RED}"/><circle r="25" fill="{RED}"/></g>'
            f'<path d="{spikes}" fill="none"{stroke}/><circle r="25" fill="none"{stroke}/>'
            f'<circle cx="-8" cy="-4" r="7" fill="#fff"/><circle cx="{-11 if back else -6}" cy="-4" r="3.3" fill="{INK}"/>'
            f'<circle cx="10" cy="-2" r="4.5" fill="#fff"/><circle cx="{8 if back else 11}" cy="-2" r="2.1" fill="{INK}"/>'
            f'<path d="M-11 9 L-6 5 L-1 10 L4 5 L9 10" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>')

def pose(v, name, dark=False):
    s=style_for(v,dark)
    wfill = s["wing"] if v!="A" else s["fill"]
    shadow = f'<ellipse cx="96" cy="172" rx="46" ry="5" fill="{IND if not dark else "#000"}" opacity="0.12"/>'
    if name=="main":
        return shadow + crow(v,dark,dict(brow="M112 56 Q124 50 136 57"), item=cbox(166,70,22))
    if name=="investigating":
        arm = (f'<g class="arm" style="transform-origin:92px 108px">'
               + sh("M92 112 Q118 94 152 100 Q130 114 100 126 Z", wfill, s)
               + f'<path d="M151 104 L160 95" stroke="{("#3a415a" if v!="A" else s["stroke"])}" stroke-width="5" stroke-linecap="round"/>'
               + f'<circle cx="172" cy="82" r="16" fill="#ffffff" fill-opacity="{0.55 if v!="A" else 0}" stroke="{IND if not dark else WHITE}" stroke-width="5"/>'
               + f'<circle cx="176" cy="80" r="3.5" fill="{INK if not dark else WHITE}" opacity="0.6"/></g>')
        return shadow + crow(v,dark,dict(big=True,px=3,py=-1,brow="M112 50 Q124 42 136 50"), wing=arm)
    if name=="chase":
        body = crow(v,dark,dict(big=True,px=4,brow="M114 57 Q126 51 138 59"), fly=True)
        return (f'<ellipse cx="150" cy="174" rx="26" ry="4" fill="{IND}" opacity="0.12"/>'
                f'<g class="fly"><g transform="translate(-6 8) scale(0.8) rotate(-8 100 110)">{body}</g></g>'
                f'<path class="speed" d="M8 70 H38 M4 92 H30 M12 114 H38" stroke="{IND if not dark else WHITE}" stroke-opacity="0.3" stroke-width="3" stroke-linecap="round"/>'
                f'<g transform="translate(162 136) scale(0.7)"><g class="hop">{flaky(v,dark,run=True,back=True)}</g></g>')

CSS = """<style>
.pop{animation:pop 2.4s ease-in-out infinite}
@keyframes pop{0%,70%,100%{transform:scale(1)}78%{transform:scale(1.22)}86%{transform:scale(.95)}}
.blink{animation:blink 4s infinite}
@keyframes blink{0%,92%,100%{transform:scaleY(1)}95%{transform:scaleY(.1)}}
.arm{animation:sweep 2.6s ease-in-out infinite}
@keyframes sweep{0%,100%{transform:rotate(0)}50%{transform:rotate(-9deg)}}
.flap{animation:flap .45s ease-in-out infinite alternate}
@keyframes flap{from{transform:rotate(0)}to{transform:rotate(38deg)}}
.fly{animation:bob .9s ease-in-out infinite alternate}
@keyframes bob{from{transform:translateY(-3px)}to{transform:translateY(3px)}}
.hop{animation:hop .45s ease-in-out infinite alternate}
@keyframes hop{from{transform:translateY(0)}to{transform:translateY(-9px)}}
.speed{animation:speed .45s linear infinite}
@keyframes speed{from{transform:translateX(6px);opacity:.3}to{transform:translateX(-6px);opacity:1}}
@media (prefers-reduced-motion: reduce){*{animation:none!important}}
</style>"""

def svg(inner, vb="0 0 200 185", w=None, anim=True):
    ww = f' width="{w}"' if w else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{ww}>{CSS if anim else ""}{inner}</svg>'
