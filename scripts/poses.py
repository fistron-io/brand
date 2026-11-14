"""The thirty-four Fištrónek poses in the brand style C. A pose moves one part or
tells a short story (several parts one after another); the loop stays calm and
the pose still reads when nothing moves (2026-11-14)."""
from skeleton import *
import skeleton as gen
V="C"
LEG="#3a415a"; LINE="#c9cedb"; PEND="#8a90a6"; TAPE="#f2c94c"; STEAM="#a9b1cc"
BROOM="#8a6a45"; STRAW="#c9a15b"; STRAW_LINE="#a8823f"; BULB="#ffe27a"; LAMP="#f2c94c"; CLOUD="#eef0f7"

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
    if name in NEW: return N(name,dark)   # the poses of 2026-11-14
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

    if name=="working":
        # in development: he hammers a checkbox that is not finished yet (dashed, half a tick)
        ham=(f'<g class="hammer" style="transform-origin:100px 112px">'+sh("M94 112 Q118 96 140 88 L146 98 Q122 110 100 126 Z",s["wing"],s)+
             f'<path d="M140 92 L162 124" stroke="{BROOM}" stroke-width="6" stroke-linecap="round"/>'
             f'<path d="M149 128.5 L156 138.5 L180 121.5 L173 111.5 Z" fill="{LEG}"{ow(dark,2.5)}/></g>')
        box=(f'<rect x="142" y="138" width="30" height="30" rx="6.75" fill="none" stroke="{PEND}" stroke-width="3" stroke-dasharray="6 5"/>'
             f'<path d="M148.75 153 L154.75 159" stroke="{LEAF}" stroke-width="4.2" stroke-linecap="round"/>')
        return shadow(60,dark)+f'<g transform="translate(-14 0)">{crow(V,dark,dict(px=4,py=4,brow="M112 54 Q124 50 136 58"),wing=ham)}</g>'+box
    if name=="lightbulb":
        # fištrón: wit; the idea lights up above his head
        glow=(f'<g class="glow"><path d="M160 6 V0 M182 16 L188 11 M138 16 L132 11 M190 36 H197 M130 36 H123" stroke="{LAMP}" stroke-width="3" stroke-linecap="round"/>'
              f'<circle cx="160" cy="34" r="14" fill="{BULB}"/></g>')
        bulb=(f'<circle cx="160" cy="34" r="14" fill="#fff" fill-opacity="0.35"{ow(dark,2.5)}/>{glow}'
              f'<path d="M155 36 L158 40 L160 36 L162 40 L165 36" stroke="{LEG}" stroke-width="1.6" fill="none" stroke-linejoin="round"/>'
              f'<rect x="153.5" y="47" width="13" height="9" rx="2" fill="{LEG}"{ow(dark,2)}/>')
        w=wingpath("M92 112 Q118 100 138 96 L142 106 Q118 116 98 128 Z",dark)
        return shadow(46,dark)+crow(V,dark,dict(big=True,px=1,py=-3,brow="M112 50 Q124 42 136 50"),wing=w,item=bulb)
    if name=="cloud":
        # on a platform's cloud, inside their service, with the checkbox to offer
        cl=(f'<path d="M22 182 Q10 160 36 158 Q42 142 64 148 Q76 132 100 142 Q120 130 136 146 Q160 140 166 160 Q190 160 182 182 Z" fill="{CLOUD}"{ow(dark)}/>')
        w=wingpath("M92 112 Q122 98 148 92 L152 102 Q124 114 98 128 Z",dark)
        body=crow(V,dark,dict(px=3,py=0,brow="M112 56 Q124 50 136 57"),wing=w,item=cb(150,78,22,dark,""))
        return f'<g class="float">{body}{cl}</g>'
    if name=="abacus":
        # the price per active committer: he counts them on an abacus
        rods="".join(f'<path d="M140 {y} H196" stroke="{LEG}" stroke-width="2.5"/>' for y in (116,134,152))
        beads=("".join(f'<circle cx="{x}" cy="116" r="5.5" fill="{IND}"{ow(dark,1.5)}/>' for x in (148,159))
               +"".join(f'<circle cx="{x}" cy="134" r="5.5" fill="{IND}"{ow(dark,1.5)}/>' for x in (148,159,170))
               +f'<circle cx="148" cy="152" r="5.5" fill="{IND}"{ow(dark,1.5)}/>'
               +f'<g class="slide"><circle cx="188" cy="116" r="5.5" fill="{LEAF}"{ow(dark,1.5)}/></g>')
        frame=(f'<rect x="134" y="102" width="68" height="64" rx="5" fill="none" stroke="{BROOM}" stroke-width="5"/>'
               f'<path d="M140 166 V176 M196 166 V176" stroke="{BROOM}" stroke-width="5" stroke-linecap="round"/>')
        w=wingpath("M92 112 Q116 104 132 110 L134 120 Q116 120 98 128 Z",dark)
        body=crow(V,dark,dict(px=5,py=4,brow="M112 54 Q124 48 136 56"),wing=w)
        return shadow(66,dark)+f'<g transform="translate(-20 0)">{body}</g>'+rods+beads+frame
    if name=="journey":
        # the roadmap: on the road with his bundle, the road passing under him
        bundle=(f'<path d="M128 96 L60 50" stroke="{BROOM}" stroke-width="4" stroke-linecap="round"/>'
                f'<path d="M62 50 Q44 32 56 28 Q68 24 74 40 Q84 46 68 58 Q56 62 62 50 Z" fill="{LEAF}"{ow(dark,2.5)}/>')
        stick=sh("M96 108 Q114 96 126 92 L132 100 Q118 110 102 124 Z",s["wing"],s)
        road=(f'<path d="M0 176 H200" stroke="{LINE}" stroke-width="6" stroke-linecap="round"/>'
              f'<path class="road" d="M-20 176 H220" stroke="#fff" stroke-width="2" stroke-dasharray="10 10"/>')
        post=(f'<path d="M184 176 V120" stroke="{BROOM}" stroke-width="4" stroke-linecap="round"/>'
              f'<path d="M168 114 H196 L200 122 L196 130 H168 Z" fill="#fff"{ow(dark,2)}/>{cb(172,116,12,dark,"")}')
        return road+post+crow(V,dark,dict(px=4,py=-1,brow="M112 54 Q124 48 136 54"),wing=stick,back=bundle)
    if name=="clipboard":
        # what each plan includes: he checks the list, the last item gets its tick
        board=(f'<g transform="rotate(8 166 118)"><rect x="140" y="80" width="52" height="70" rx="5" fill="{BROOM}"{ow(dark,2)}/>'
               f'<rect x="145" y="88" width="42" height="57" rx="2" fill="#fff"/><rect x="156" y="76" width="20" height="9" rx="3" fill="{LEG}"{ow(dark,1.5)}/>'
               f'<rect x="150" y="94" width="8" height="8" rx="1.8" fill="{LEAF}"/><path d="M162 98 H182" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
               f'<rect x="150" y="108" width="8" height="8" rx="1.8" fill="{LEAF}"/><path d="M162 112 H178" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
               f'<rect x="150.5" y="122.5" width="7" height="7" rx="1.6" fill="none" stroke="{PEND}" stroke-width="1.2"/><rect class="tick" x="150" y="122" width="8" height="8" rx="1.8" fill="{LEAF}"/>'
               f'<path d="M162 126 H184" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/></g>')
        w=wingpath("M92 112 Q118 106 142 112 L142 122 Q118 122 98 128 Z",dark)
        return shadow(56,dark)+f'<g transform="translate(-14 0)">{crow(V,dark,dict(big=True,px=5,py=4,brow="M112 52 Q124 46 136 54"),wing=w)}</g>'+board

# ---------------------------------------------------------------- 2026-11-14: Available now, the GUI's features and states
ARM = "M92 112 Q118 100 138 96 L142 106 Q118 116 98 128 Z"      # wing reaching forward
LOW = "M94 112 Q114 112 130 128 L124 136 Q106 126 92 126 Z"      # wing reaching down

def N(name, dark=False):
    s = S(dark); o = oc(dark)
    def line(d, col=None, w=3, extra=""): return f'<path d="{d}" stroke="{col or o}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" fill="none"{extra}/>'

    # ------------------------------------------------ Available now
    if name == "coffee":
        # done: he leans on the finished checkbox, the hammer put away, and sips
        mug = (f'<rect x="141" y="80" width="17" height="17" rx="3.5" fill="#fff"{ow(dark,2.5)}/>'
               + line("M141 85 Q133 85 133 89.5 Q133 94 141 93", w=2.5))
        w = wingpath("M92 112 Q116 104 136 98 L141 107 Q118 116 98 128 Z", dark, "sip", "100px 118px", mug)
        ham = (line("M196 170 L186 136", BROOM, 5) + f'<path d="M176 128 L196 124 L198 134 L178 138 Z" fill="{LEG}"{ow(dark,2.5)}/>')
        return (shadow(64, dark) + cb(140, 138, 30, dark, "") + ham
                + f'<g transform="translate(-18 0)">{crow(V, dark, dict(px=2, py=3, brow="M112 60 Q124 57 136 61"), wing=w)}</g>')

    # ------------------------------------------------ Review, Become a developer
    if name == "redpen":
        paper = (f'<g transform="translate(142 130) rotate(-6)"><rect x="-6" y="-22" width="52" height="64" rx="4" fill="#fff"{ow(dark,2)}/>'
                 f'<path d="M2 -12 H34" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
                 f'<rect x="0" y="-6" width="40" height="8" rx="2" fill="{RED}" opacity="0.22"/><path d="M3 -2 H7 M12 -2 H34" stroke="{RED}" stroke-width="2.6" stroke-linecap="round"/>'
                 f'<rect x="0" y="5" width="40" height="8" rx="2" fill="{LEAF}" opacity="0.25"/><path d="M3 9 H7 M5 7 V11 M12 9 H30" stroke="{LEAF}" stroke-width="2.6" stroke-linecap="round"/>'
                 f'<path d="M2 20 H30 M2 29 H36" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/></g>')
        pen = (f'<path d="M150 92 L158 112" stroke="{RED}" stroke-width="5.5" stroke-linecap="round"/><path d="M158 112 L160 118" stroke="{o}" stroke-width="3" stroke-linecap="round"/>')
        arm = f'<g class="scribble">' + sh("M94 108 Q130 98 156 104 L154 114 Q126 122 100 126 Z", s["wing"], s) + pen + '</g>'
        glasses = (f'<circle cx="126" cy="72" r="13" fill="none" stroke="{o}" stroke-width="2.6"/>' + line("M113 72 L98 68", w=2.6))
        return shadow(56, dark) + paper + f'<g transform="translate(-16 0)">{crow(V, dark, dict(px=3, py=4, brow="M112 52 Q124 46 137 53"), wing=arm, item=glasses)}</g>'
    if name == "teacher":
        board = (f'<rect x="146" y="46" width="52" height="50" rx="4" fill="{NIGHT}" stroke="{BROOM}" stroke-width="5"/>'
                 + line("M157 56 L152 62 L157 68 M165 56 L170 62 L165 68", "#fff", 2.2)
                 + f'<rect x="177" y="55" width="14" height="14" rx="3.2" fill="none" stroke="#fff" stroke-width="2.2"/>' + line("M180 62 L183 65 L188 58.5", LEAF, 2.6)
                 + line("M154 80 H186 M154 87 H174", "#fff", 2.2, ' opacity="0.6"')
                 + line("M154 96 L150 168 M190 96 L195 168", BROOM, 4))
        ptr = line("M136 100 L176 72", BROOM, 3.5)
        w = wingpath(ARM, dark, "arm", "96px 116px", ptr)
        cap = (f'<path d="M92 44 L120 32 L148 44 L120 56 Z" fill="{INK}"{ow(dark,2.5)}/>' + line("M146 44 V60", LAMP, 2.5) + f'<circle cx="146" cy="62" r="3.2" fill="{LAMP}"/>')
        return shadow(60, dark) + board + f'<g transform="translate(-10 20) scale(0.88)">{crow(V, dark, dict(px=3, py=-2, brow="M112 58 Q124 54 136 58"), wing=w, item=cap)}</g>'

    # ------------------------------------------------ States
    if name == "empty":
        box = (f'<path d="M142 130 L132 114 M190 130 L199 113" stroke="{o}" stroke-width="3" stroke-linecap="round"/>'
               f'<path d="M142 130 L132 114 L150 112 L156 130 Z M190 130 L199 113 L182 112 L176 130 Z" fill="{STRAW}"{ow(dark,2.5)}/>'
               f'<rect x="142" y="130" width="48" height="38" rx="2" fill="{STRAW}"{ow(dark)}/>' + line("M158 146 H174", STRAW_LINE, 3))
        moth = (f'<g class="flutter" style="transform-origin:166px 96px"><path d="M166 96 L156 86 L155 98 Z M166 96 L176 86 L177 98 Z" fill="#fff"{ow(dark,1.8)}/>'
                f'<path d="M166 92 V101" stroke="{o}" stroke-width="2.4" stroke-linecap="round"/></g>')
        w = wingpath("M92 112 Q112 108 126 114 L126 124 Q112 122 98 128 Z", dark)
        return shadow(62, dark) + f'<g transform="translate(-20 0)">{crow(V, dark, dict(big=True, px=4, py=5, brow="M112 50 Q124 42 136 52"), wing=w)}</g>' + box + moth
    if name == "hourglass":
        hg = (f'<path d="M150 104 H186 M150 168 H186" stroke="{BROOM}" stroke-width="5" stroke-linecap="round"/>'
              f'<path d="M154 107 H182 L170 136 L182 165 H154 L166 136 Z" fill="#fff" fill-opacity="0.7"{ow(dark,2.5)}/>'
              f'<path class="drain" style="transform-origin:168px 134px" d="M159 116 H177 L168.6 134 H167.4 Z" fill="{LAMP}"/>'
              f'<path class="pile" style="transform-origin:168px 163px" d="M157 163 H179 L168 142 Z" fill="{LAMP}"/>')
        w = wingpath("M104 104 Q82 96 54 130 Q86 138 106 122 Z", dark)
        return shadow(62, dark) + f'<g transform="translate(-18 0)">{crow(V, dark, dict(px=4, py=4, brow="M112 58 Q124 56 136 62"), wing=w)}</g>' + hg
    if name == "lost":
        mp = (f'<g transform="rotate(10 164 116)"><rect x="140" y="94" width="50" height="40" rx="3" fill="#fff"{ow(dark,2)}/>'
              + line("M157 94 V134 M173 94 V134", LINE, 2) + line("M146 104 Q156 112 164 104 Q172 98 180 110", PEND, 2, ' stroke-dasharray="3 4"')
              + line("M178 119 L184 125 M184 119 L178 125", RED, 2.6) + '</g>')
        q = (f'<g class="float">' + line("M150 30 Q150 16 162 16 Q174 16 174 28 Q174 37 162 41 V48", IND if not dark else "#c9d0f2", 5.5)
             + f'<circle cx="162" cy="59" r="3.6" fill="{IND if not dark else "#c9d0f2"}"/></g>')
        w = wingpath("M92 112 Q118 104 142 106 L142 116 Q118 120 98 128 Z", dark)
        return shadow(54, dark) + f'<g transform="translate(-16 0)">{crow(V, dark, dict(big=True, px=-3, py=-3, brow="M112 48 Q122 44 136 54"), wing=w)}</g>' + mp + q
    if name == "megaphone":
        horn = (f'<path d="M140 92 L166 76 L166 122 L140 108 Z" fill="#fff"{ow(dark,2.5)}/><rect x="132" y="92" width="10" height="16" rx="3" fill="{LEG}"{ow(dark,2)}/>'
                f'<rect x="164" y="72" width="6" height="54" rx="3" fill="{RED}"{ow(dark,2)}/>')
        w = wingpath("M92 112 Q116 102 134 98 L138 108 Q118 116 98 128 Z", dark, extra=horn)
        waves = (f'<g class="wave">' + line("M158 86 Q166 99 158 112", w=3.5) + '</g>'
                 f'<g class="wave late">' + line("M170 78 Q182 99 170 120", w=3.5) + '</g>')
        return shadow(54, dark) + f'<g transform="translate(-20 0)">{crow(V, dark, dict(big=True, px=4, py=0, brow="M112 52 Q124 44 136 50"), wing=w)}</g>' + f'<g transform="translate(4 0)">{waves}</g>'
    if name == "juggle":
        w = wingpath("M92 112 Q122 102 150 88 L156 97 Q124 112 98 128 Z", dark)
        boxes = (f'<g class="hop">{cb(134, 38, 17, dark, "")}</g><g class="hop late">{cb(158, 20, 17, dark, "")}</g><g class="hop late2">{cb(180, 44, 17, dark, "")}</g>')
        return shadow(50, dark) + f'<g transform="translate(-14 0)">{crow(V, dark, dict(big=True, px=3, py=-4, brow="M112 50 Q124 42 136 50"), wing=w)}</g>' + boxes

    # ------------------------------------------------ Memory, models, agents
    if name == "memory":
        cab = (f'<rect x="146" y="92" width="50" height="76" rx="4" fill="{LEG}"{ow(dark)}/>'
               f'<rect x="151" y="134" width="40" height="28" rx="2" fill="{IND}"{ow(dark,2)}/><path d="M165 146 H177" stroke="{LINE}" stroke-width="3.5" stroke-linecap="round"/>'
               f'<g class="drawer"><path d="M158 100 V88 H166 V100 M170 100 V84 H178 V100 M181 100 V90 H188 V100" fill="#fff"{ow(dark,1.8)}/>'
               f'<rect x="151" y="98" width="40" height="28" rx="2" fill="{IND}"{ow(dark,2)}/><path d="M165 110 H177" stroke="{LINE}" stroke-width="3.5" stroke-linecap="round"/></g>')
        card = f'<rect x="134" y="84" width="16" height="20" rx="2" fill="#fff"{ow(dark,2)}/><rect x="138" y="89" width="7" height="7" rx="1.6" fill="{LEAF}"/>'
        w = wingpath(ARM, dark, extra=card)
        return shadow(62, dark) + cab + f'<g transform="translate(-18 0)">{crow(V, dark, dict(px=3, py=1, brow="M112 54 Q124 48 136 54"), wing=w)}</g>'
    if name == "scales":
        beam = (f'<g class="tilt" style="transform-origin:166px 96px"><path d="M138 96 H194" stroke="{o}" stroke-width="4" stroke-linecap="round"/>'
                + line("M142 96 L134 124 M142 96 L150 124 M190 96 L182 124 M190 96 L198 124", w=1.8)
                + f'<path d="M131 124 H153 M179 124 H199" stroke="{o}" stroke-width="4" stroke-linecap="round"/>'
                f'<rect x="135" y="108" width="14" height="14" rx="3" fill="{IND}"{ow(dark,2)}/><circle cx="189" cy="115" r="7" fill="{BULB}"{ow(dark,2)}/></g>')
        post = (f'<path d="M166 96 V166" stroke="{BROOM}" stroke-width="5" stroke-linecap="round"/><path d="M152 168 H180" stroke="{BROOM}" stroke-width="6" stroke-linecap="round"/>'
                f'<circle cx="166" cy="96" r="4.5" fill="{LEG}"{ow(dark,2)}/>')
        w = wingpath("M104 104 Q82 96 54 130 Q86 138 106 122 Z", dark)
        return shadow(62, dark) + f'<g transform="translate(-10 20) scale(0.88)">{crow(V, dark, dict(big=True, px=4, py=2, brow="M112 52 Q124 44 137 55"), wing=w)}</g>' + post + beam
    if name == "remote":
        bot = (f'<g class="patrol">' + line("M172 136 V124", w=2.5) + f'<rect x="167.500" y="114" width="9" height="9" rx="2" fill="{LEAF}"{ow(dark,1.6)}/>'
               f'<rect x="154" y="136" width="36" height="24" rx="6" fill="{CLOUD}"{ow(dark,2.5)}/><circle cx="165" cy="147" r="4.5" fill="#fff"{ow(dark,1.6)}/><circle cx="166" cy="147" r="2" fill="{INK}"/>'
               f'<path d="M175 150 H184" stroke="{o}" stroke-width="2.4" stroke-linecap="round"/>'
               f'<circle cx="162" cy="164" r="5" fill="{LEG}"{ow(dark,2)}/><circle cx="182" cy="164" r="5" fill="{LEG}"{ow(dark,2)}/></g>')
        rc = (f'<rect x="132" y="92" width="18" height="13" rx="3" fill="{LEG}"{ow(dark,2)}/>' + line("M146 92 L152 76", w=2.5) + f'<circle cx="138" cy="98.500" r="2.4" fill="{RED}"/>')
        w = wingpath("M92 112 Q116 104 134 100 L138 110 Q118 116 98 128 Z", dark, extra=rc)
        return shadow(70, dark) + f'<g transform="translate(-18 0)">{crow(V, dark, dict(px=5, py=4, brow="M112 54 Q124 48 136 56"), wing=w)}</g>' + bot
    if name == "alarm":
        clock = (f'<g class="shake" style="transform-origin:166px 142px">' + line("M152 160 L147 168 M180 160 L185 168", w=4)
                 + f'<circle cx="152" cy="118" r="7" fill="{LAMP}"{ow(dark,2)}/><circle cx="180" cy="118" r="7" fill="{LAMP}"{ow(dark,2)}/>'
                 + line("M166 112 V120", w=3) + f'<circle cx="166" cy="142" r="22" fill="#fff"{ow(dark)}/>'
                 + line("M166 142 V128 M166 142 L176 148", w=3) + f'<circle cx="166" cy="142" r="2.5" fill="{o}"/></g>')
        cap = (f'<path d="M98 56 Q112 30 138 46 Q150 30 160 40 Q148 44 142 58 Z" fill="#fff"{ow(dark,2.5)}/><circle cx="162" cy="40" r="5" fill="#fff"{ow(dark,2)}/>')
        w = wingpath("M104 104 Q82 96 54 130 Q86 138 106 122 Z", dark)
        return shadow(62, dark) + f'<g transform="translate(-18 0)">{crow(V, dark, dict(px=4, py=4, brow="M112 62 Q124 62 137 66"), wing=w, item=cap)}</g>' + clock
    if name == "piggy":
        pig = (line("M150 160 V170 M182 160 V170", w=5) + f'<ellipse cx="166" cy="146" rx="28" ry="20" fill="{CLOUD}"{ow(dark)}/>'
               f'<path d="M150 130 L154 119 L162 128 Z" fill="{CLOUD}"{ow(dark,2.5)}/><ellipse cx="193" cy="146" rx="6" ry="8" fill="{CLOUD}"{ow(dark,2.5)}/>'
               f'<circle cx="180" cy="139" r="2.4" fill="{INK}"/>' + line("M160 128 H174", w=3.5) + line("M138 146 Q131 142 134 136", w=2.5))
        coin = f'<g class="drop"><circle cx="167" cy="112" r="7.5" fill="{BULB}"{ow(dark,2)}/><path d="M167 108 V116" stroke="{LAMP}" stroke-width="2.4" stroke-linecap="round"/></g>'
        w = wingpath("M92 112 Q120 98 146 96 L148 106 Q122 112 98 128 Z", dark)
        return shadow(66, dark) + f'<g transform="translate(-7 0)">{coin}{pig}</g>' + f'<g transform="translate(-18 0)">{crow(V, dark, dict(px=5, py=3, brow="M112 53 Q124 47 136 54"), wing=w)}</g>'

    # ------------------------------------------------ Migration, DCV, daily CI, growth
    if name == "suitcase":
        case = (line("M134 132 Q134 122 142 122 Q150 122 150 132", w=3)
                + f'<rect x="120" y="132" width="46" height="34" rx="5" fill="{STRAW}"{ow(dark)}/>' + line("M120 144 H166", STRAW_LINE, 2.5)
                + f'<rect x="147" y="149" width="12" height="12" rx="2.7" fill="{LEAF}"{ow(dark,1.6)}/><path d="M149.700 155 L152.100 157.400 L156.300 152.600" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
                + f'<circle cx="131" cy="155" r="4.5" fill="{RED}"{ow(dark,1.6)}/>')
        w = wingpath(LOW, dark, "sweep2", "112px 104px", case)
        hat = (f'<ellipse cx="118" cy="52" rx="30" ry="6" fill="{STRAW}"{ow(dark,2.5)}/><path d="M102 50 Q104 30 118 30 Q132 30 134 50 Z" fill="{STRAW}"{ow(dark,2.5)}/>' + line("M103 46 H133", RED, 3))
        return shadow(52, dark) + crow(V, dark, dict(px=4, py=0, brow="M112 60 Q124 58 136 60"), wing=w, item=hat)
    if name == "plane":
        pl = (f'<g class="glide"><path d="M146 66 L196 44 L178 84 L170 70 Z" fill="#fff"{ow(dark,2.5)}/>' + line("M196 44 L170 70 L166 84 L178 84", w=2.5)
              + f'<rect x="150" y="80" width="12" height="12" rx="2.7" fill="{LEAF}"{ow(dark,1.6)}/><path d="M152.700 86 L155.100 88.400 L159.300 83.600" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
              + line("M156 80 L166 72", w=1.6) + '</g>')
        trail = line("M112 70 Q128 62 140 66", PEND, 2.5, ' stroke-dasharray="3 6"')
        w = wingpath("M92 112 Q112 92 124 72 L134 78 Q120 102 98 128 Z", dark)
        return shadow(46, dark) + f'<g transform="translate(-18 0)">{crow(V, dark, dict(big=True, px=4, py=-3, brow="M112 50 Q124 42 136 50"), wing=w)}</g>' + f'<g transform="translate(20 -6)">{trail}</g>' + pl
    if name == "newspaper":
        sun = (f'<g transform="translate(-8 0)"><g class="rise"><circle cx="176" cy="60" r="15" fill="{BULB}"{ow(dark,2.5)}/>'
               + line("M176 34 V28 M196 42 L201 37 M156 42 L151 37", LAMP, 3) + '</g></g>')
        horizon = f'<rect x="140" y="62" width="64" height="30" fill="var(--surface-page, #fff)"/>'
        paper = (f'<g transform="rotate(6 166 126)"><rect x="136" y="92" width="62" height="64" rx="3" fill="#fff"{ow(dark,2.5)}/>'
                 f'<rect x="142" y="98" width="50" height="9" rx="2" fill="{INK}"/>'
                 f'<rect x="142" y="113" width="9" height="9" rx="2" fill="{LEAF}"/><path d="M155 117.500 H190" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
                 f'<rect x="142" y="127" width="9" height="9" rx="2" fill="{RED}"/><path d="M155 131.500 H184" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
                 f'<rect x="142" y="141" width="9" height="9" rx="2" fill="{LEAF}"/><path d="M155 145.500 H188" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>'
                 + line("M167 92 V156", LINE, 1.2) + '</g>')
        w = wingpath("M92 112 Q116 106 136 110 L136 120 Q116 120 98 128 Z", dark)
        return shadow(60, dark) + sun + f'<g transform="translate(-20 0)">{crow(V, dark, dict(px=4, py=4, brow="M112 53 Q124 47 136 55"), wing=w)}</g>' + paper
    if name == "grow":
        plant = (f'<g class="sprout" style="transform-origin:170px 146px">' + line("M170 146 V104", "#2f7d50", 4)
                 + f'<path d="M170 132 Q156 130 154 118 Q168 118 170 132 Z M170 124 Q184 122 186 110 Q172 110 170 124 Z" fill="{LEAF}"{ow(dark,2)}/>'
                 + f'<rect x="160" y="84" width="20" height="20" rx="4.5" fill="{LEAF}"{ow(dark,2)}/><path d="M164.500 94 L168.500 98 L175.500 90" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g>')
        pot = f'<path d="M154 146 H186 L182 168 H158 Z" fill="{STRAW}"{ow(dark,2.5)}/><rect x="151" y="142" width="38" height="8" rx="3" fill="{STRAW}"{ow(dark,2.5)}/>'
        can = (f'<rect x="124" y="92" width="24" height="20" rx="4" fill="{LEG}"{ow(dark,2.5)}/>' + line("M148 106 L164 94", w=4.5) + line("M124 96 Q114 102 124 108", w=3)
               + line("M166 100 L168 108 M170 97 L174 105", STEAM, 2.2))
        w = wingpath("M92 112 Q112 104 126 102 L130 112 Q114 116 98 128 Z", dark, extra=can)
        return shadow(64, dark) + plant + pot + f'<g transform="translate(-18 0)">{crow(V, dark, dict(px=4, py=3, brow="M112 54 Q124 48 136 54"), wing=w)}</g>'
    raise KeyError(name)

NEW_CSS = """
.sip{animation:sip 3.2s ease-in-out infinite}
@keyframes sip{0%,55%,100%{transform:rotate(0)}68%,84%{transform:rotate(-13deg)}}
.scribble{animation:scribble .4s ease-in-out infinite alternate}
@keyframes scribble{from{transform:translate(-3px,0)}to{transform:translate(5px,1px)}}
.flutter{animation:flutter 2.2s ease-in-out infinite alternate}
@keyframes flutter{from{transform:translate(-4px,4px) rotate(-10deg)}to{transform:translate(6px,-14px) rotate(12deg)}}
.drain{animation:drain 3s linear infinite}
@keyframes drain{from{transform:scaleY(1)}to{transform:scaleY(0)}}
.pile{animation:pile 3s linear infinite}
@keyframes pile{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.wave{animation:wave 1.2s ease-out infinite}
@keyframes wave{0%{opacity:0;transform:translateX(-5px)}40%{opacity:1}100%{opacity:0;transform:translateX(5px)}}
.late2{animation-delay:.5s}
.drawer{animation:drawer 2.8s ease-in-out infinite}
@keyframes drawer{0%,25%,100%{transform:translateX(0)}45%,80%{transform:translateX(-10px)}}
.tilt{animation:tilt 2.6s ease-in-out infinite alternate}
@keyframes tilt{from{transform:rotate(-7deg)}to{transform:rotate(7deg)}}
.patrol{animation:patrol 1.8s ease-in-out infinite alternate}
@keyframes patrol{from{transform:translateX(-6px)}to{transform:translateX(8px)}}
.drop{animation:drop 2.2s ease-in infinite}
@keyframes drop{0%,20%{transform:translateY(-10px);opacity:1}55%{transform:translateY(16px);opacity:1}60%,100%{transform:translateY(18px);opacity:0}}
.glide{animation:glide 2.4s ease-in-out infinite alternate}
@keyframes glide{from{transform:translate(-6px,5px)}to{transform:translate(4px,-6px)}}
.rise{animation:rise 3s ease-in-out infinite alternate}
@keyframes rise{from{transform:translateY(16px)}to{transform:translateY(-4px)}}
.sprout{animation:sprout 3s ease-in-out infinite alternate}
@keyframes sprout{from{transform:scale(.62)}to{transform:scale(1)}}
"""
NEW = ["coffee","redpen","teacher","empty","hourglass","lost","megaphone","juggle","memory","scales","remote","alarm","piggy","suitcase","plane","newspaper","grow"]


ALL=["main","investigating","skeptical","chase","telescope","broom","stamp","conductor","chef","desk","quarantine",
     "working","lightbulb","cloud","abacus","journey","clipboard",*NEW]
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
.hammer{animation:hammer 1.2s ease-in infinite}
@keyframes hammer{0%,30%{transform:rotate(-26deg)}45%{transform:rotate(0)}52%{transform:rotate(-5deg)}60%,100%{transform:rotate(-26deg)}}
.glow{animation:glow 2.8s ease-in-out infinite}
@keyframes glow{0%,35%{opacity:0}45%{opacity:1}52%{opacity:.4}60%,92%{opacity:1}100%{opacity:0}}
.slide{animation:slide 2.4s ease-in-out infinite}
@keyframes slide{0%,25%{transform:translateX(0)}50%,85%{transform:translateX(-18px)}100%{transform:translateX(0)}}
.road{animation:road .8s linear infinite}
@keyframes road{from{transform:translateX(0)}to{transform:translateX(-20px)}}
"""+NEW_CSS
