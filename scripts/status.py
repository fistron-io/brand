"""Status icons on a 24 grid, drawn as the brand checkbox, and their animation CSS."""
LEAF="#3fa66b"; RED="#d64545"; IND="#24305e"; PEND="#8a90a6"; AMBER="#e0a020"; INK="#1b2033"
def box(fill, inner, stroke=None, dash=False):
    if fill=="none":
        st=f' stroke="{stroke}" stroke-width="1.8"' + (' stroke-dasharray="3 2.4"' if dash else '')
        return f'<rect x="2.9" y="2.9" width="18.2" height="18.2" rx="4.6" fill="none"{st}/>{inner}'
    return f'<rect x="2" y="2" width="20" height="20" rx="5" fill="{fill}"/>{inner}'
W='stroke="#ffffff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" fill="none"'
ICONS={
 "passed": lambda: box(LEAF, f'<path d="M7 12.3 L10.6 15.8 L17.2 8.6" {W}/>'),
 "failed": lambda: box(RED, f'<path d="M8 8 L16 16 M16 8 L8 16" {W}/>'),
 "flaky": lambda: ('<defs><clipPath id="fh"><rect class="st-flip" x="0" y="0" width="12" height="24"/></clipPath></defs><g class="st-wobble" style="transform-origin:12px 22px">'
     f'<path d="M5.5 9 L6.5 2.8 L9.5 6.4 L12 1.6 L14.5 6.4 L17.5 2.8 L18.5 9 Z" fill="{LEAF}"/><circle cx="12" cy="13.5" r="9" fill="{LEAF}"/>'
     f'<g clip-path="url(#fh)"><path d="M5.5 9 L6.5 2.8 L9.5 6.4 L12 1.6 L14.5 6.4 L17.5 2.8 L18.5 9 Z" fill="{RED}"/><circle cx="12" cy="13.5" r="9" fill="{RED}"/></g>'
     '<circle cx="9" cy="12" r="2.6" fill="#fff"/><circle cx="9.6" cy="12" r="1.2" fill="#1b2033"/><circle cx="15.2" cy="12.6" r="1.9" fill="#fff"/><circle cx="15.5" cy="12.6" r="0.9" fill="#1b2033"/>'
     '<path d="M8 17.2 L10 15.8 L12 17.4 L14 15.8 L16 17.2" stroke="#fff" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g>'),
 "quarantined": lambda: ('<clipPath id="qc"><rect x="2" y="2" width="20" height="20" rx="5"/></clipPath>'
     '<rect x="2" y="2" width="20" height="20" rx="5" fill="#f2c94c"/><g clip-path="url(#qc)">'
     '<path class="st-stripe" d="M-35 0 L-11 24 M-28 0 L-4 24 M-21 0 L3 24 M-14 0 L10 24 M-7 0 L17 24 M0 0 L24 24 M7 0 L31 24 M14 0 L38 24 M21 0 L45 24" stroke="#1b2033" stroke-width="2.4" opacity="0.85"/></g>'),
 "pending": lambda: box("none", f'<circle class="st-dot" cx="8" cy="12" r="1.5" fill="{PEND}"/><circle class="st-dot d2" cx="12" cy="12" r="1.5" fill="{PEND}"/><circle class="st-dot d3" cx="16" cy="12" r="1.5" fill="{PEND}"/>', PEND),
 "running": lambda: box("none", f'<path class="st-spin" style="transform-origin:12px 12px" d="M12 8.2 A3.8 3.8 0 1 1 8.2 12" stroke="{IND}" stroke-width="2.4" stroke-linecap="round" fill="none"/>', PEND),
 "skipped": lambda: box("#c9cedb", '<path d="M8 12 H16" stroke="#3a415a" stroke-width="2.8" stroke-linecap="round"/>'),
 "manual": lambda: box("none", f'<circle cx="12" cy="12" r="1.6" fill="{PEND}"/>', PEND, dash=True),
 "warning": lambda: box("#e8a33a", '<path d="M12 7 V13.2" stroke="#1b2033" stroke-width="2.8" stroke-linecap="round"/><circle cx="12" cy="17" r="1.6" fill="#1b2033"/>'),
}
LABEL={"passed":"passed · met","failed":"failed · not met","flaky":"flaky","quarantined":"quarantined","pending":"pending · not run",
       "running":"running","skipped":"skipped","manual":"manual · not observed","warning":"warning · needs input"}
def icon(name,size,uid=""):
    s=ICONS[name]().replace('id="fh"',f'id="fh{uid}"').replace('url(#fh)',f'url(#fh{uid})').replace('id="qc"',f'id="qc{uid}"').replace('url(#qc)',f'url(#qc{uid})')
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" role="img" aria-label="{name}" style="flex: none">{s}</svg>'

STATUS_CSS="""
.st-spin{animation:st-spin 1s linear infinite}
@keyframes st-spin{to{transform:rotate(360deg)}}
.st-dot{animation:st-dot 1.2s ease-in-out infinite}
.st-dot.d2{animation-delay:.2s}.st-dot.d3{animation-delay:.4s}
@keyframes st-dot{0%,60%,100%{opacity:.25}30%{opacity:1}}
.st-wobble{animation:st-wobble 1.4s ease-in-out infinite}
@keyframes st-wobble{0%,100%{transform:rotate(0)}20%{transform:rotate(-9deg)}40%{transform:rotate(7deg)}60%{transform:rotate(-4deg)}80%{transform:rotate(0)}}
.st-flip{animation:st-flip 2.8s steps(1) infinite}
.st-stripe{animation:st-stripe 3s linear infinite}
@keyframes st-stripe{from{transform:translateX(0)}to{transform:translateX(7px)}}
@keyframes st-flip{0%{transform:translateX(0)}50%{transform:translateX(12px)}}
"""
