"""The wordmark outlined from IBM Plex Sans 500, with the checkbox above the s,
its bottom edge level with the bottom edge of the dot on the i."""
import io, os
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FONT=os.environ.get("PLEX_SANS_500", os.path.join(os.path.dirname(__file__), "..", "node_modules", "@fontsource", "ibm-plex-sans", "files", "ibm-plex-sans-latin-500-normal.woff2"))
tt=TTFont(FONT); buf=io.BytesIO(); tt.flavor=None; tt.save(buf); data=buf.getvalue()
upem=tt["head"].unitsPerEm
face=hb.Face(data); font=hb.Font(face)
def shape(text):
    b=hb.Buffer(); b.add_str(text); b.guess_segment_properties(); hb.shape(font,b,{"kern":True,"liga":False})
    return b.glyph_infos,b.glyph_positions
gs=tt.getGlyphSet(); order=tt.getGlyphOrder()
LS=-0.01*upem
def outline(text):
    infos,pos=shape(text); x=0; paths=[]; xs=[]
    for i,(inf,p) in enumerate(zip(infos,pos)):
        name=order[inf.codepoint]; pen=SVGPathPen(gs)
        tp=TransformPen(pen,(1,0,0,-1,x+p.x_offset,0)); gs[name].draw(tp)
        paths.append(pen.getCommands()); xs.append((x, x+p.x_advance))
        x+=p.x_advance+LS
    return paths,xs,x-LS
BOX='<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{r}" fill="#3fa66b"/><path d="M{a} {b} L{c} {d} L{e} {f}" fill="none" stroke="#ffffff" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def box(cx, top, size):
    k=size/12
    return BOX.format(x=cx-size/2+0.5*k,y=top+0.5*k,s=11*k,r=2.6*k,a=cx-size/2+3.2*k,b=top+6.2*k,c=cx-size/2+5.2*k,d=top+8.2*k,e=cx-size/2+8.9*k,f=top+4.1*k,w=1.9*k)
def wordmark_svg(color="#24305e"):
    paths,xs,width=outline("Fistron")
    # coordinates: baseline at y=0, ascender above (negative). em box top: with line-height 1 the box top sits at baseline - ascent-ish.
    # in CSS we placed checkbox top at 0.036em from line box top; line box top = baseline - (ascent+descent... ) -> use hhea metrics
    from fontTools.pens.recordingPen import DecomposingRecordingPen
    from fontTools.pens.boundsPen import BoundsPen
    rp=DecomposingRecordingPen(gs); gs["i"].draw(rp)
    contours=[];cur=[]
    for op,args in rp.value:
        cur.append((op,args))
        if op in("closePath","endPath"): contours.append(cur);cur=[]
    def bounds(c):
        bp=BoundsPen(gs)
        for op,args in c: getattr(bp,op)(*args)
        return bp.bounds
    dot=max((bounds(c) for c in contours), key=lambda b:b[3])   # highest contour
    size=0.32*upem; top=-dot[1]-size   # bottom edge of the box on the bottom edge of the dot
    s_x0,s_x1=xs[2]; cx=(s_x0+s_x1)/2
    minx=0; maxx=width; miny=top; maxy=0
    pad=0.03*upem
    vb=f"{minx-pad:.0f} {miny-pad:.0f} {maxx-minx+2*pad:.0f} {maxy-miny+2*pad:.0f}"
    g=''.join(f'<path d="{d}"/>' for d in paths)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><g fill="{color}">{g}</g>{box(cx,top,size)}</svg>'
