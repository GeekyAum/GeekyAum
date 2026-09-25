#!/usr/bin/env python3
"""Generates every SVG used in the GeekyAum profile README.

Run:  python3 generate.py      -> writes assets/*-dark.svg and assets/*-light.svg
Edit the text in the CONTENT section and re-run; nothing else needs touching.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
CW = 0.6  # monospace advance width, in em

THEMES = {
    "dark": dict(panel="#161b22", border="#30363d", text="#e6edf3", muted="#8b949e",
                 faint="#21262d", green="#3fb950", amber="#d29922", red="#f85149",
                 blue="#58a6ff", body="#56d364", body2="#2ea043", line="#0d1117",
                 belly="#aff5b4", eye="#ffffff", pupil="#0d1117", cheek="#ff7b72", ant="#56d364"),
    "light": dict(panel="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#59636e",
                  faint="#eaeef2", green="#1a7f37", amber="#9a6700", red="#cf222e",
                  blue="#0969da", body="#4ac26b", body2="#1a7f37", line="#1f2328",
                  belly="#dafbe1", eye="#ffffff", pupil="#1f2328", cheek="#ff8182", ant="#1f2328"),
}

CSS = """
.eye{transform-box:fill-box;transform-origin:center;animation:blink 5s infinite}
@keyframes blink{0%,92%,100%{transform:scaleY(1)}95%{transform:scaleY(.1)}}
.antL{transform-box:fill-box;transform-origin:100% 100%;animation:wig 2.4s ease-in-out infinite alternate}
.antR{transform-box:fill-box;transform-origin:0% 100%;animation:wig 2.4s ease-in-out infinite alternate-reverse}
@keyframes wig{from{transform:rotate(-7deg)}to{transform:rotate(7deg)}}
.hop{animation:hop 3.2s ease-in-out infinite}
@keyframes hop{0%,70%,100%{transform:translateY(0)}78%{transform:translateY(-7px)}86%{transform:translateY(0)}}
.z{animation:zz 3s ease-in infinite;opacity:0}
.z2{animation-delay:1.5s}
@keyframes zz{0%{opacity:0;transform:translate(0,0)}25%{opacity:1}100%{opacity:0;transform:translate(10px,-22px)}}
.pulse{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:.25}50%{opacity:.9}}
.cur{animation:cur 1s steps(1) infinite}
@keyframes cur{50%{opacity:0}}
"""


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
            f'<title>{escape(title)}</title><style>{CSS}</style>{body}</svg>\n')


def text(x, y, s, size, fill, family=MONO, weight=400, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{escape(s)}</text>')


# ---------------------------------------------------------------- chip ---
def chip(x, y, s, expr, p):
    """Chip the cricket, drawn in a 120x124 box, placed at (x, y), scaled by s."""
    L, B = p["line"], p["body"]
    g = [f'<g transform="translate({x} {y}) scale({s})"><g class="hop">']
    # antennae
    g.append(f'<g class="antL"><path d="M50 34 C44 16 34 8 22 4" fill="none" stroke="{p["ant"]}" stroke-width="3" stroke-linecap="round"/>'
             f'<circle cx="22" cy="4" r="3.5" fill="{B}" stroke="{L}" stroke-width="2"/></g>')
    g.append(f'<g class="antR"><path d="M70 34 C76 16 86 8 98 4" fill="none" stroke="{p["ant"]}" stroke-width="3" stroke-linecap="round"/>'
             f'<circle cx="98" cy="4" r="3.5" fill="{B}" stroke="{L}" stroke-width="2"/></g>')
    # hind legs (the big jumpy ones)
    for d in ("M40 92 L16 70 L10 112", "M80 92 L104 70 L110 112"):
        g.append(f'<path d="{d}" fill="none" stroke="{L}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'
                 f'<path d="{d}" fill="none" stroke="{p["body2"]}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>')
    # body + little feet
    g.append(f'<path d="M50 112 L46 121 M70 112 L74 121" stroke="{L}" stroke-width="3" stroke-linecap="round"/>')
    g.append(f'<ellipse cx="60" cy="92" rx="27" ry="23" fill="{B}" stroke="{L}" stroke-width="2.5"/>')
    g.append(f'<ellipse cx="60" cy="97" rx="15" ry="13" fill="{p["belly"]}"/>')
    # head
    g.append(f'<circle cx="60" cy="54" r="28" fill="{B}" stroke="{L}" stroke-width="2.5"/>')
    g.append(f'<ellipse cx="44" cy="64" rx="5" ry="3" fill="{p["cheek"]}" opacity=".55"/>'
             f'<ellipse cx="76" cy="64" rx="5" ry="3" fill="{p["cheek"]}" opacity=".55"/>')

    def eye(cx, cy, r=8, pr=4):
        return (f'<g class="eye"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{p["eye"]}" stroke="{L}" stroke-width="2"/>'
                f'<circle cx="{cx+1}" cy="{cy+1}" r="{pr}" fill="{p["pupil"]}"/>'
                f'<circle cx="{cx+2.5}" cy="{cy-1.5}" r="1.3" fill="#fff"/></g>')

    def stroke(d, w=2.8):
        return f'<path d="{d}" fill="none" stroke="{L}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'

    if expr == "hi":
        g += [eye(49, 51), eye(71, 51), stroke("M53 66 Q60 72 67 66")]
    elif expr == "shock":  # o_O
        g += [eye(48, 52, 6, 3), eye(72, 50, 10, 4), f'<ellipse cx="60" cy="69" rx="3.5" ry="4" fill="{L}"/>']
    elif expr == "happy":  # ^o^
        g += [stroke("M42 54 Q49 44 56 54"), stroke("M64 54 Q71 44 78 54"),
              f'<path d="M53 64 Q60 76 67 64 Z" fill="{L}"/>']
    elif expr == "ow":  # >_<
        g += [stroke("M42 45 L54 51 L42 57"), stroke("M78 45 L66 51 L78 57"),
              stroke("M52 68 Q56 64 60 68 Q64 72 68 68")]
    elif expr == "meh":  # -_-
        g += [stroke("M42 52 L56 52"), stroke("M64 52 L78 52"), stroke("M54 67 L66 67")]
    elif expr == "sleep":  # -.-  zZ
        g += [stroke("M42 51 Q49 57 56 51"), stroke("M64 51 Q71 57 78 51"),
              f'<circle cx="60" cy="67" r="2.5" fill="{L}"/>']
    g.append("</g>")
    if expr == "sleep":
        g.append(f'<g class="z">{text(96, 30, "z", 16, p["muted"], weight=700)}</g>'
                 f'<g class="z z2">{text(104, 20, "Z", 20, p["muted"], weight=700)}</g>')
    g.append("</g>")
    return "".join(g)


def bubble(x, y, lines, p, size=14, tail="left"):
    """Speech bubble; returns (svg, width, height). Tail points left toward Chip."""
    cw = size * CW
    w = int(max(len(l) for l in lines) * cw + 32)
    lh = size * 1.5
    h = int(len(lines) * lh + 24)
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{p["panel"]}" stroke="{p["border"]}" stroke-width="1.5"/>']
    ty = y + h / 2
    if tail == "left":
        s.append(f'<path d="M{x+1} {ty-8} L{x-12} {ty+4} L{x+1} {ty+6}" fill="{p["panel"]}" stroke="{p["border"]}" stroke-width="1.5" stroke-linejoin="round"/>'
                 f'<rect x="{x}" y="{ty-7}" width="3" height="12" fill="{p["panel"]}"/>')
    else:  # tail at bottom-right, pointing down toward Chip
        tx = x + w - 40
        s.append(f'<path d="M{tx} {y+h-1} L{tx+14} {y+h+12} L{tx+16} {y+h-1}" fill="{p["panel"]}" stroke="{p["border"]}" stroke-width="1.5" stroke-linejoin="round"/>'
                 f'<rect x="{tx+1}" y="{y+h-3}" width="14" height="4" fill="{p["panel"]}"/>')
    for i, l in enumerate(lines):
        s.append(text(x + 16, y + 12 + lh * (i + 0.72), l, size, p["text"]))
    return "".join(s), w, h


def chip_says(name, expr, lines, title):
    for t, p in THEMES.items():
        s = 0.9
        cw, chh = 120 * s, 124 * s
        bx = int(cw + 26)
        b, bw, bh = bubble(bx, 0, lines, p)
        H = int(max(chh + 8, bh + 4))
        by = (H - bh) // 2
        b, bw, bh = bubble(bx, by, lines, p)
        body = chip(4, (H - chh) / 2, s, expr, p) + b
        (OUT / f"{name}-{t}.svg").write_text(svg(bx + bw + 4, H, body, title))


# ============================================================ CONTENT ===
def header():
    tag = "i build agents that are not allowed to make things up"
    W, H = 880, 222
    for t, p in THEMES.items():
        s = [f'<defs><pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse">'
             f'<circle cx="2" cy="2" r="1" fill="{p["border"]}"/></pattern>'
             f'<clipPath id="type"><rect x="36" y="112" height="30" width="0">'
             f'<animate attributeName="width" from="0" to="{int(len(tag)*16*CW)+4}" begin="0.4s" dur="2.6s" fill="freeze" '
             f'calcMode="discrete" values="{";".join(str(int(i*16*CW)) for i in range(len(tag)+1))}"/></rect></clipPath></defs>',
             f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="{p["panel"]}" stroke="{p["border"]}" stroke-width="1.5"/>',
             f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="url(#dots)" opacity=".6"/>',
             text(34, 92, "aum vyas", 58, p["text"], SANS, 800, extra='letter-spacing="-1.5"'),
             f'<g clip-path="url(#type)">{text(36, 132, tag, 16, p["green"])}</g>']
        # cursor that follows the typing
        xs = ";".join(str(36 + int(i * 16 * CW)) for i in range(len(tag) + 1))
        s.append(f'<rect class="cur" y="118" width="9" height="18" fill="{p["green"]}" x="36">'
                 f'<animate attributeName="x" values="{xs}" begin="0.4s" dur="2.6s" fill="freeze" calcMode="discrete"/></rect>')
        s.append(text(36, 174, "ai engineering · backend systems · iit bhubaneswar '27 · ex-google ai garage", 13, p["muted"]))
        b, bw, bh = bubble(548, 14, ["hi. i'm chip, the resident", "cricket. he builds the", "agents. i heckle them."], p, 13, tail="down")
        s.append(b)
        s.append(chip(742, 100, 0.95, "hi", p))
        (OUT / f"header-{t}.svg").write_text(svg(W, H, "".join(s), "aum vyas: i build agents that are not allowed to make things up"))


def pipeline():
    nodes = [  # (step, name, detail lines, metric, color key)
        ("01", "ingest", ["kafka + pathway", "5 feeds", "4 pipelines"], "streaming", "green"),
        ("02", "index", ["pathway", "vectorstore", "10k+ docs"], "< 50 ms", "green"),
        ("03", "route", ["heuristic", "classifier +", "drift tree"], "cheap first", "green"),
        ("04", "reason", ["leader +", "analyst agents", "one job only"], "200 ms overhead", "amber"),
        ("05", "gate", ["evidence check", "4 hard nos", "no proof, no op"], "fails closed", "red"),
    ]
    groups = [(0, 2, "green", "deterministic · tested · boring on purpose"),
              (3, 3, "amber", "the llm"),
              (4, 4, "red", "the wall")]
    W, H, nw, nh, gap, x0, y0 = 880, 262, 150, 138, 25, 15, 20
    for t, p in THEMES.items():
        s = []
        for i, (num, name, det, met, ck) in enumerate(nodes):
            x = x0 + i * (nw + gap)
            c = p[ck]
            if ck == "red":
                s.append(f'<rect class="pulse" x="{x-4}" y="{y0-4}" width="{nw+8}" height="{nh+8}" rx="14" fill="none" stroke="{c}" stroke-width="2"/>')
            s.append(f'<rect x="{x}" y="{y0}" width="{nw}" height="{nh}" rx="10" fill="{p["panel"]}" stroke="{p["border"]}" stroke-width="1.5"/>')
            s.append(f'<rect x="{x}" y="{y0}" width="{nw}" height="4" rx="2" fill="{c}"/>')
            s.append(text(x + 14, y0 + 30, num, 12, p["muted"]))
            s.append(text(x + 38, y0 + 30, name, 16, p["text"], weight=700))
            for j, d in enumerate(det):
                s.append(text(x + 14, y0 + 56 + j * 18, d, 12, p["muted"]))
            s.append(f'<line x1="{x+14}" y1="{y0+nh-32}" x2="{x+nw-14}" y2="{y0+nh-32}" stroke="{p["faint"]}" stroke-width="1.5"/>')
            s.append(text(x + 14, y0 + nh - 13, met, 12, c, weight=700))
            if i < len(nodes) - 1:
                ax1, ax2, ay = x + nw + 2, x + nw + gap - 3, y0 + nh / 2
                s.append(f'<line x1="{ax1}" y1="{ay}" x2="{ax2-5}" y2="{ay}" stroke="{p["border"]}" stroke-width="2"/>'
                         f'<path d="M{ax2-7} {ay-5} L{ax2} {ay} L{ax2-7} {ay+5} Z" fill="{p["border"]}"/>')
                pc = p["amber"] if i == 3 else p["green"]
                for k in range(2):
                    s.append(f'<circle r="3.5" cy="{ay}" fill="{pc}"><animate attributeName="cx" from="{ax1}" to="{ax2-4}" dur="1.6s" '
                             f'begin="{i*0.25 + k*0.8}s" repeatCount="indefinite"/>'
                             f'<animate attributeName="opacity" values="0;1;1;0" dur="1.6s" begin="{i*0.25 + k*0.8}s" repeatCount="indefinite"/></circle>')
        by = y0 + nh + 24
        for a, b, ck, label in groups:
            xa, xb = x0 + a * (nw + gap) + 4, x0 + b * (nw + gap) + nw - 4
            c = p[ck]
            s.append(f'<path d="M{xa} {by-8} L{xa} {by} L{xb} {by} L{xb} {by-8}" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"/>')
            s.append(text((xa + xb) / 2, by + 22, label, 12.5, c, weight=700, anchor="middle"))
        s.append(text(W / 2, H - 14, "the model gets exactly one box. everything around it is code that can be tested.", 13, p["muted"], anchor="middle", extra='font-style="italic"'))
        (OUT / f"pipeline-{t}.svg").write_text(svg(W, H, "".join(s),
            "pipeline: ingest, index, route (deterministic) → reason (the llm) → gate (fails closed)"))


def stack():
    rows = [
        ("ai", "green", ["agno", "langgraph", "langchain", "gemini", "gpt-4o", "pytorch", "hugging face"]),
        ("retrieval", "green", ["pathway vectorstore", "adaptive rag", "opik llm-judge evals"]),
        ("backend", "blue", ["python", "c++", "sql", "fastapi", "oauth 2.0", "google adk"]),
        ("data", "blue", ["kafka", "postgresql", "mongodb", "cloud spanner"]),
        ("ops", "amber", ["docker", "git", "prometheus", "grafana"]),
        ("silicon", "red", ["verilog", "rtl", "fsm design", "# not a job requirement. still fun."]),
    ]
    W, rh, fs = 880, 40, 12.5
    H = len(rows) * rh + 28
    for t, p in THEMES.items():
        s = [f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{p["panel"]}" stroke="{p["border"]}" stroke-width="1.5"/>']
        for i, (cat, ck, items) in enumerate(rows):
            y = 14 + i * rh
            c = p[ck]
            if i:
                s.append(f'<line x1="20" y1="{y}" x2="{W-20}" y2="{y}" stroke="{p["faint"]}" stroke-width="1"/>')
            s.append(f'<circle cx="30" cy="{y+rh/2}" r="4" fill="{c}"/>')
            s.append(text(44, y + rh / 2 + 4.5, cat + "/", 13, p["text"], weight=700))
            x = 150
            for it in items:
                if it.startswith("#"):
                    s.append(text(x + 4, y + rh / 2 + 4.5, it, fs, p["muted"], extra='font-style="italic"'))
                    continue
                w = len(it) * fs * CW + 20
                s.append(f'<rect x="{x}" y="{y+8}" width="{w}" height="{rh-16}" rx="{(rh-16)/2}" fill="{c}" fill-opacity=".12" stroke="{c}" stroke-opacity=".45"/>')
                s.append(text(x + 10, y + rh / 2 + 4.5, it, fs, p["text"]))
                x += w + 8
        (OUT / f"stack-{t}.svg").write_text(svg(W, H, "".join(s), "stack: " + "; ".join(f"{c}: {', '.join(i)}" for c, _, i in rows)))


if __name__ == "__main__":
    header()
    pipeline()
    stack()
    chip_says("chip-google", "shock", ["two state machines. in a calendar app.",
                                        "so nobody double-books a meeting room.",
                                        "i think about this more than a cricket",
                                        "reasonably should."], "chip: two state machines, in a calendar app")
    chip_says("chip-ow", "ow", ["OW."], "chip: OW.")
    chip_says("chip-fact", "meh", ["...fine. one fact, then leave me alone:",
                                   "'crickets' is what you hear when a repo",
                                   "has no commits. i am, structurally,",
                                   "a threat. behave."], "chip: crickets is what you hear when a repo has no commits")
    chip_says("chip-cricket", "happy", ["the third reason is the real one."], "chip: the third reason is the real one")
    chip_says("chip-sleep", "sleep", ["chip eats stars.", "current diet, below. ↓"], "chip is asleep. he eats stars.")
    print("wrote", len(list(OUT.glob("*.svg"))), "svgs to", OUT)
