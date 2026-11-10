"""Build every Fistron brand file from the sources in this folder.

    npm install            # IBM Plex Sans for the wordmark outlines
    pip install -r scripts/requirements.txt
    python3 scripts/build.py

Writes tokens/, logo/, mascot/ and status/. PNG icons need rsvg-convert (librsvg).
"""
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import skeleton  # noqa: E402
from poses import ALL, EXTRA_CSS, P  # noqa: E402
from status import ICONS, STATUS_CSS  # noqa: E402
from wordmark import wordmark_svg  # noqa: E402

INDIGO = "#24305e"
LEAF = "#3fa66b"
WHITE = "#ffffff"


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(text if text.endswith("\n") else text + "\n")


# ---------------------------------------------------------------- logo

def mark_inner(head, box, tick, uid="m"):
    """The head mark on a 48 grid. The eye and the gap around the checkbox are holes (mask)."""
    return (
        f'<defs><mask id="{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48">'
        f'<rect width="48" height="48" fill="#fff"/><circle cx="22" cy="19.5" r="4.8" fill="#000"/>'
        f'<rect x="26.5" y="27.5" width="19" height="19" rx="4.5" fill="#000" stroke="#000" stroke-width="2.6"/></mask></defs>'
        f'<g mask="url(#{uid})" fill="{head}"><path d="M11.5 13 L13 5.5 L18.5 10 Z" stroke="{head}" stroke-width="1.8" stroke-linejoin="round"/>'
        f'<circle cx="19" cy="22" r="13"/><path d="M28 15.5 L44 22 L28 28.5 Z" stroke="{head}" stroke-width="1.8" stroke-linejoin="round"/></g>'
        f'<circle cx="23.6" cy="20.2" r="2.4" fill="{head}"/>'
        f'<rect x="26.5" y="27.5" width="19" height="19" rx="4.5" fill="{box}"/>'
        f'<path d="M30.8 37 L34.5 40.7 L41.2 33.3" stroke="{tick}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    )


def mark_svg(head=INDIGO):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">{mark_inner(head, LEAF, WHITE)}</svg>'


def mark_one_colour_svg(ink=INDIGO):
    inner = mark_inner(ink, ink, "#000")
    box = f'<rect x="26.5" y="27.5" width="19" height="19" rx="4.5" fill="{ink}"/>'
    tick = '<path d="M30.8 37 L34.5 40.7 L41.2 33.3" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    cut = (
        '<mask id="t" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48"><rect width="48" height="48" fill="#fff"/>'
        f'{tick}</mask><rect x="26.5" y="27.5" width="19" height="19" rx="4.5" fill="{ink}" mask="url(#t)"/>'
    )
    inner = inner.replace(box + tick, cut)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">{inner}</svg>'


def favicon_svg():
    """Indigo head in light mode, white head in dark mode."""
    style = "<style>svg{color:#24305e}@media (prefers-color-scheme: dark){svg{color:#ffffff}}</style>"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">{style}{mark_inner("currentColor", LEAF, WHITE)}</svg>'


def app_icon_svg():
    """Square app icon: indigo ground, white head, leaf checkbox (like the current app icons)."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" fill="{INDIGO}"/>'
            f'<g transform="translate(7.2 7.2) scale(0.7)">{mark_inner(WHITE, LEAF, WHITE)}</g></svg>')


def lockup_svg(text=INDIGO, head=INDIGO):
    wm = wordmark_svg(text)
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', wm).group(1).split()]
    inner = re.sub(r'^<svg[^>]*>|</svg>$', '', wm)
    h, gap = 48, 10
    k = h * 0.66 / 898          # font units -> mark units: cap height about 0.51 of the mark
    baseline = h * 0.8705       # text baseline near the bottom of the head
    wh, ww = vb[3] * k, vb[2] * k
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {h + gap + ww:.1f} {h}">{mark_inner(head, LEAF, WHITE, "lm")}'
            f'<svg x="{h + gap}" y="{baseline + vb[1] * k:.2f}" width="{ww:.2f}" height="{wh:.2f}" viewBox="{" ".join(str(v) for v in vb)}">{inner}</svg></svg>')


def png(svg_path, png_path, size):
    if not shutil.which("rsvg-convert"):
        print(f"skip {png_path}: rsvg-convert not found")
        return
    subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size), os.path.join(ROOT, svg_path),
                    "-o", os.path.join(ROOT, png_path)], check=True)


def build_logo():
    write("logo/fistron-mark.svg", mark_svg())
    write("logo/fistron-mark-on-dark.svg", mark_svg(WHITE))
    write("logo/fistron-mark-one-colour.svg", mark_one_colour_svg())
    write("logo/fistron-wordmark.svg", wordmark_svg(INDIGO))
    write("logo/fistron-wordmark-on-dark.svg", wordmark_svg(WHITE))
    write("logo/fistron-lockup.svg", lockup_svg())
    write("logo/fistron-lockup-on-dark.svg", lockup_svg(WHITE, WHITE))
    write("logo/favicon.svg", favicon_svg())
    write("logo/app-icon.svg", app_icon_svg())
    png("logo/fistron-mark.svg", "logo/favicon-32.png", 32)
    png("logo/app-icon.svg", "logo/apple-touch-icon.png", 180)
    png("logo/app-icon.svg", "logo/app-icon-512.png", 512)


# ---------------------------------------------------------------- mascot

def themable(svg):
    """Outlines, legs and a few details follow the page theme through CSS variables."""
    svg = re.sub(r'stroke="#1b2033" stroke-width="(?!3\.2")', 'stroke="var(--crow-outline, #1b2033)" stroke-width="', svg)
    svg = svg.replace('stroke="#3a415a"', 'stroke="var(--crow-leg, #3a415a)"')
    svg = svg.replace('class="float late" fill="#24305e"', 'class="float late" fill="var(--color-indigo, #24305e)"')
    svg = svg.replace('fill-opacity="0.55" stroke="#24305e"', 'fill-opacity="0.55" stroke="var(--color-indigo, #24305e)"')
    svg = svg.replace('class="speed" d="M8 70 H38 M4 92 H30 M12 114 H38" stroke="#24305e"',
                      'class="speed" d="M8 70 H38 M4 92 H30 M12 114 H38" stroke="var(--color-indigo, #24305e)"')
    return svg


def static(svg):
    return re.sub(r' (style|class)="[^"]*"', '', svg)


MASCOT_CSS = re.sub(r'</?style>', '', skeleton.CSS).strip() + EXTRA_CSS


def build_mascot():
    for pose in ALL:
        light, dark = P(pose, False), P(pose, True)
        write(f"mascot/fistronek-{pose}.svg",
              f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 185"><style>{MASCOT_CSS}</style>{themable(light)}</svg>')
        write(f"mascot/static/fistronek-{pose}.svg", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 185">{static(light)}</svg>')
        write(f"mascot/static/fistronek-{pose}-on-dark.svg", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 185">{static(dark)}</svg>')
    write("mascot/fistronek.css", MASCOT_CSS)


# ---------------------------------------------------------------- status

def build_status():
    for name, draw in ICONS.items():
        body = draw().replace('stroke="#24305e"', 'stroke="currentColor"')
        write(f"status/status-{name}.svg",
              f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" color="#24305e">{body}</svg>')
    write("status/status.css", STATUS_CSS.strip() + "\n@media (prefers-reduced-motion: reduce) {\n  .st-spin, .st-dot, .st-wobble, .st-flip, .st-stripe { animation: none !important; }\n}")


# ---------------------------------------------------------------- tokens

def build_tokens():
    with open(os.path.join(ROOT, "tokens", "tokens.json")) as f:
        tokens = json.load(f)
    names = {t["name"] for t in tokens["color"]["tokens"]}

    def css_name(name):
        """CSS names follow the fistron.io stylesheet: raw and text colours get a color- prefix."""
        if name.startswith(("surface-", "btn-", "crow-", "status-")):
            return name
        return "color-" + name

    def value(v, theme):
        v = v if isinstance(v, str) else v.get(theme, v["light"])
        m = re.fullmatch(r"\{(.+)\}", v)
        if m:
            assert m.group(1) in names, m.group(1)
            return f"var(--{css_name(m.group(1))})"
        return v

    light = [f"  --{css_name(t['name'])}: {value(t['value'], 'light')};" for t in tokens["color"]["tokens"]]
    dark = [f"  --{css_name(t['name'])}: {value(t['value'], 'dark')};" for t in tokens["color"]["tokens"] if isinstance(t["value"], dict)]
    other = [f"  --{t['name']}: {t['value']};" for fam in ("spacing", "radius") for t in tokens[fam]["tokens"]]
    other += [f"  --font-{k}: {v};" for k, v in tokens["type"]["families"].items()]
    css = ["/* Fistron brand tokens, generated from tokens.json by scripts/build.py. Do not edit. */",
           ":root {", *light, *other, "}", "", ':root[data-theme="dark"] {', *dark, "}", "",
           "@media (prefers-color-scheme: dark) {", '  :root:not([data-theme="light"]) {',
           *["  " + line for line in dark], "  }", "}"]
    write("tokens/tokens.css", "\n".join(css))


if __name__ == "__main__":
    build_tokens()
    build_logo()
    build_mascot()
    build_status()
    print("done")
