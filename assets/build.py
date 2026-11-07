"""Generates the animated SVGs used by the profile README.

GitHub READMEs cannot run JavaScript or page-level CSS, but an SVG loaded as an
<img> can run its own CSS keyframe animations. Every effect here is therefore
self-running (no mouse interaction) and degrades to a static, fully visible
image when the viewer has "reduce motion" enabled.

Run:  python assets/build.py
"""
import math
import random
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
random.seed(42)  # deterministic output, clean diffs

SANS = "'Segoe UI','Helvetica Neue',Ubuntu,Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"

BLUE, TEAL, INK, MUTED = "#58A6FF", "#5EEAD4", "#E6EDF3", "#8B949E"


def svg(w, h, body, style, label):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'role="img" aria-label="{escape(label)}">\n<style>\n{style}\n{REDUCED}\n</style>\n{body}\n</svg>\n'
    )


def wave_path(width, period, amp, base, height, phase=0.0, step=10):
    """Closed sine-wave area from y=base(+wave) down to y=height."""
    pts = []
    for x in range(0, width + step, step):
        y = base + amp * math.sin(2 * math.pi * x / period + phase)
        pts.append(f"{x},{y:.1f}")
    return f"M0,{height} L" + " L".join(pts) + f" L{width},{height} Z"


def particles(n, w, h, colors, rmin=0.8, rmax=2.4, rise=40):
    """Self-drifting, twinkling particles (the cursor-free take on a particle field)."""
    out = []
    for _ in range(n):
        x, y = random.uniform(0, w), random.uniform(0, h)
        r = random.uniform(rmin, rmax)
        dur = random.uniform(6, 14)
        delay = -random.uniform(0, dur)  # negative delay: already mid-flight at load
        dx = random.uniform(-25, 25)
        c = random.choice(colors)
        out.append(
            f'<circle class="p" cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="{c}" '
            f'style="--dx:{dx:.0f}px;--dy:-{rise}px;animation-duration:{dur:.1f}s;animation-delay:{delay:.1f}s"/>'
        )
    return "\n".join(out)


PARTICLE_CSS = """
.p{animation:drift linear infinite;opacity:.0}
@keyframes drift{0%{transform:translate(0,0);opacity:0}15%{opacity:.85}85%{opacity:.6}100%{transform:translate(var(--dx),var(--dy));opacity:0}}
"""

# --------------------------------------------------------------------------- hero


def hero():
    W, H = 1200, 380
    name = "Prince Verma"
    subtitle = "AI/ML Engineer | Computer Vision | OCR | GenAI"

    letters = "".join(
        f'<tspan class="ltr" style="animation-delay:{0.25 + i * 0.07:.2f}s">{escape(ch) if ch != " " else "&#160;"}</tspan>'
        for i, ch in enumerate(name)
    )

    # audio waveform (speech AI motif, left)
    bars = []
    for i in range(14):
        hgt = 14 + 46 * abs(math.sin(i * 0.9))
        bars.append(
            f'<rect class="bar" x="{70 + i * 11}" y="{170 - hgt / 2:.0f}" width="6" height="{hgt:.0f}" rx="3" '
            f'fill="url(#gBar)" style="animation-delay:-{i * 0.13:.2f}s"/>'
        )

    waves = [
        (wave_path(2400, 600, 10, 330, H, 0.0), "0.10", "w1"),
        (wave_path(2400, 400, 8, 345, H, 1.3), "0.14", "w2"),
    ]
    wave_svg = "\n".join(f'<path class="{c}" d="{d}" fill="{BLUE}" opacity="{o}"/>' for d, o, c in waves)

    style = f"""
text{{font-family:{SANS}}}
.grid{{animation:pan 10s linear infinite}}
@keyframes pan{{to{{transform:translate(-40px,-40px)}}}}
.blob{{animation:float 16s ease-in-out infinite alternate}}
.blob2{{animation:float 22s ease-in-out infinite alternate-reverse}}
@keyframes float{{0%{{transform:translate(-30px,10px)}}100%{{transform:translate(40px,-15px)}}}}
.spot{{animation:sweep 9s ease-in-out infinite alternate;mix-blend-mode:screen}}
@keyframes sweep{{0%{{transform:translateX(-420px)}}100%{{transform:translateX(420px)}}}}
.ltr{{animation:rise .7s cubic-bezier(.2,.7,.2,1) backwards}}
@keyframes rise{{0%{{opacity:0;fill:{BLUE}}}100%{{opacity:1}}}}
.glow{{animation:pulse 4s ease-in-out 1.4s infinite alternate backwards}}
@keyframes pulse{{0%{{opacity:.15}}100%{{opacity:.55}}}}
.sub{{animation:fade 1s ease-out 1.15s backwards}}
@keyframes fade{{0%{{opacity:0;transform:translateY(8px)}}100%{{opacity:1;transform:none}}}}
.rule{{stroke-dasharray:320;animation:draw 1.2s ease-out 1.5s backwards}}
@keyframes draw{{0%{{stroke-dashoffset:320}}100%{{stroke-dashoffset:0}}}}
.bar{{transform-box:fill-box;transform-origin:center;animation:eq 1.3s ease-in-out infinite alternate}}
@keyframes eq{{0%{{transform:scaleY(.25)}}100%{{transform:scaleY(1)}}}}
.w1{{animation:slide 18s linear infinite}}
.w2{{animation:slide 11s linear infinite}}
@keyframes slide{{to{{transform:translateX(-1200px)}}}}
.pupils{{animation:look 9s ease-in-out infinite}}
@keyframes look{{0%,12%{{transform:translate(0,0)}}18%,32%{{transform:translate(-7px,1px)}}38%,50%{{transform:translate(6px,-3px)}}56%,70%{{transform:translate(-4px,4px)}}76%,100%{{transform:translate(0,0)}}}}
.lid{{transform-box:fill-box;transform-origin:center;animation:blink 5.5s ease-in-out infinite}}
@keyframes blink{{0%,90%,100%{{transform:scaleY(1)}}94%{{transform:scaleY(.08)}}}}
.box{{animation:boxpulse 2.4s ease-in-out infinite alternate}}
@keyframes boxpulse{{0%{{opacity:.55}}100%{{opacity:1}}}}
{PARTICLE_CSS}
"""

    def eye(cx):
        return (
            f'<g class="lid"><ellipse cx="{cx}" cy="150" rx="24" ry="17" fill="{INK}"/>'
            f'<clipPath id="c{cx}"><ellipse cx="{cx}" cy="150" rx="24" ry="17"/></clipPath>'
            f'<g clip-path="url(#c{cx})"><g class="pupils"><circle cx="{cx}" cy="151" r="9.5" fill="#0B1220"/>'
            f'<circle cx="{cx + 3}" cy="147" r="2.6" fill="#fff"/></g></g></g>'
        )

    body = f"""
<defs>
  <linearGradient id="gBg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0F2027"/><stop offset=".5" stop-color="#203A43"/><stop offset="1" stop-color="#2C5364"/>
  </linearGradient>
  <radialGradient id="gSpot"><stop offset="0" stop-color="{BLUE}" stop-opacity=".45"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
  <radialGradient id="gBlob"><stop offset="0" stop-color="{TEAL}" stop-opacity=".22"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></radialGradient>
  <linearGradient id="gBar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
  <linearGradient id="gRule" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset=".5" stop-color="{TEAL}"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></linearGradient>
  <pattern id="pGrid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{BLUE}" stroke-opacity=".08"/></pattern>
  <filter id="fGlow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="9"/></filter>
  <clipPath id="cCard"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#cCard)">
  <rect width="{W}" height="{H}" fill="url(#gBg)"/>
  <!-- parallax layer 1: slow grid -->
  <rect class="grid" width="{W + 80}" height="{H + 80}" fill="url(#pGrid)"/>
  <!-- parallax layer 2: drifting light blobs -->
  <circle class="blob" cx="260" cy="90" r="220" fill="url(#gBlob)"/>
  <circle class="blob2" cx="980" cy="300" r="260" fill="url(#gBlob)"/>
  <!-- spotlight sweep -->
  <ellipse class="spot" cx="600" cy="170" rx="360" ry="200" fill="url(#gSpot)"/>
  <!-- parallax layer 3: particles -->
  {particles(70, W, H, [BLUE, TEAL, "#ffffff"])}
  <!-- parallax layer 4: waves -->
  {wave_svg}

  <!-- speech motif -->
  <g opacity=".9">{''.join(bars)}</g>
  <text x="70" y="232" font-family="{MONO}" font-size="12" fill="{TEAL}" opacity=".8" style="font-family:{MONO}">speech.ai</text>

  <!-- vision motif: eyes inside a detection box -->
  <g>
    {eye(1040)}{eye(1100)}
    <g class="box" fill="none" stroke="{TEAL}" stroke-width="2">
      <rect x="996" y="118" width="148" height="66" rx="6" stroke-dasharray="6 5"/>
    </g>
    <rect x="996" y="96" width="88" height="20" rx="4" fill="{TEAL}"/>
    <text x="1004" y="111" font-size="12" font-weight="700" fill="#0B1220" style="font-family:{MONO}">eyes 0.99</text>
  </g>

  <!-- name -->
  <text x="600" y="178" text-anchor="middle" font-size="82" font-weight="800" fill="{BLUE}" class="glow" filter="url(#fGlow)">{escape(name)}</text>
  <text x="600" y="178" text-anchor="middle" font-size="82" font-weight="800" fill="{INK}" letter-spacing="1">{letters}</text>
  <text class="sub" x="600" y="232" text-anchor="middle" font-size="23" fill="#A5D6FF" letter-spacing=".5">{escape(subtitle)}</text>
  <line class="rule" x1="440" y1="262" x2="760" y2="262" stroke="url(#gRule)" stroke-width="3" stroke-linecap="round"/>
</g>
"""
    return svg(W, H, body, style, f"{name}: {subtitle}")


# ------------------------------------------------------------------------ divider


def divider():
    W, H = 1200, 28
    style = """
.beam{animation:beam 4.5s cubic-bezier(.5,0,.5,1) infinite}
@keyframes beam{0%{transform:translateX(-300px)}100%{transform:translateX(1200px)}}
.dot{transform-box:fill-box;transform-origin:center;animation:dot 2.2s ease-in-out infinite alternate}
@keyframes dot{0%{transform:rotate(45deg) scale(.7);opacity:.6}100%{transform:rotate(45deg) scale(1.15);opacity:1}}
"""
    body = f"""
<defs>
  <linearGradient id="gLine" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset=".5" stop-color="{BLUE}" stop-opacity=".45"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></linearGradient>
  <linearGradient id="gBeam" x1="0" x2="1"><stop offset="0" stop-color="{TEAL}" stop-opacity="0"/><stop offset=".5" stop-color="{TEAL}"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></linearGradient>
  <filter id="fG" x="-10%" y="-200%" width="120%" height="500%"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<rect x="0" y="13" width="{W}" height="2" fill="url(#gLine)"/>
<g class="beam"><rect width="300" height="6" y="11" rx="3" fill="url(#gBeam)" filter="url(#fG)"/><rect width="300" height="2" y="13" fill="url(#gBeam)"/></g>
<rect class="dot" x="594" y="8" width="12" height="12" rx="2" fill="{TEAL}"/>
"""
    return svg(W, H, body, style, "")


# -------------------------------------------------------------------------- cards


def card(slug, kicker, metrics, motif, motif_css, label):
    W, H = 1000, 190
    chips = []
    for i, (val, cap) in enumerate(metrics):
        x = 330 + i * 220
        d = 0.35 + i * 0.18
        chips.append(
            f'<g class="chip" style="animation-delay:{d:.2f}s">'
            f'<rect x="{x}" y="72" width="204" height="84" rx="10" fill="#ffffff" fill-opacity=".04" stroke="{BLUE}" stroke-opacity=".22"/>'
            f'<text x="{x + 16}" y="112" font-size="29" font-weight="700" fill="{INK}">{escape(val)}</text>'
            f'<text x="{x + 16}" y="139" font-size="12.5" fill="{MUTED}">{escape(cap)}</text></g>'
        )

    style = f"""
text{{font-family:{SANS}}}
.tilt{{transform-box:view-box;transform-origin:500px 95px;animation:tilt 9s ease-in-out infinite}}
@keyframes tilt{{
 0%,100%{{transform:skew(0deg,0deg) scale(1)}}
 25%{{transform:skew(-1.6deg,.5deg) scale(.985)}}
 50%{{transform:skew(0deg,-.6deg) scale(1)}}
 75%{{transform:skew(1.6deg,.5deg) scale(.985)}}}}
.shadow{{transform-box:view-box;transform-origin:500px 95px;animation:shadow 9s ease-in-out infinite}}
@keyframes shadow{{
 0%,100%{{transform:translate(0,6px)}}
 25%{{transform:translate(10px,8px)}}
 50%{{transform:translate(0,10px)}}
 75%{{transform:translate(-10px,8px)}}}}
.shine{{animation:shine 6s ease-in-out infinite}}
@keyframes shine{{0%,30%{{transform:translateX(-500px) skewX(-20deg)}}70%,100%{{transform:translateX(1300px) skewX(-20deg)}}}}
.chip{{animation:up .8s cubic-bezier(.2,.7,.2,1) backwards}}
.kick{{animation:up .8s cubic-bezier(.2,.7,.2,1) .15s backwards}}
@keyframes up{{0%{{opacity:0;transform:translateY(10px)}}100%{{opacity:1;transform:none}}}}
{motif_css}
"""
    body = f"""
<defs>
  <linearGradient id="gC{slug}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0D1B2A"/><stop offset="1" stop-color="#16324A"/></linearGradient>
  <linearGradient id="gE{slug}" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}" stop-opacity=".7"/><stop offset=".5" stop-color="{TEAL}" stop-opacity=".25"/><stop offset="1" stop-color="{BLUE}" stop-opacity=".7"/></linearGradient>
  <linearGradient id="gS{slug}" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".09"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <filter id="fS{slug}" x="-10%" y="-30%" width="120%" height="160%"><feGaussianBlur stdDeviation="8"/></filter>
  <clipPath id="cl{slug}"><rect x="16" y="14" width="968" height="158" rx="16"/></clipPath>
  <clipPath id="cm{slug}"><rect x="0" y="0" width="284" height="158"/></clipPath>
</defs>
<rect class="shadow" x="30" y="20" width="940" height="150" rx="16" fill="#000" opacity=".35" filter="url(#fS{slug})"/>
<g class="tilt">
  <rect x="16" y="14" width="968" height="158" rx="16" fill="url(#gC{slug})" stroke="url(#gE{slug})" stroke-width="1.5"/>
  <g clip-path="url(#cl{slug})">
    <g transform="translate(16,14)"><g clip-path="url(#cm{slug})">{motif}</g></g>
    <line x1="300" y1="34" x2="300" y2="152" stroke="{BLUE}" stroke-opacity=".18"/>
    <text class="kick" x="330" y="50" font-size="13" font-weight="700" letter-spacing="2.2" fill="{TEAL}" style="font-family:{MONO}">{escape(kicker)}</text>
    {''.join(chips)}
    <rect class="shine" x="0" y="0" width="160" height="200" fill="url(#gS{slug})"/>
  </g>
</g>
"""
    return svg(W, H, body, style, label)


def motif_ocr():
    # meter nameplate being scanned; detection box locks on the serial
    css = f"""
.scan{{animation:scan 3.2s ease-in-out infinite alternate}}
@keyframes scan{{0%{{transform:translateY(0)}}100%{{transform:translateY(96px)}}}}
.lock{{animation:lock 3.2s ease-in-out infinite}}
@keyframes lock{{0%,40%{{opacity:0;transform:scale(1.15)}}55%,90%{{opacity:1;transform:scale(1)}}100%{{opacity:0}}}}
.lock{{transform-box:fill-box;transform-origin:center}}
"""
    m = f"""
<rect x="40" y="26" width="200" height="110" rx="10" fill="#0B1220" stroke="{MUTED}" stroke-opacity=".5"/>
<circle cx="140" cy="62" r="20" fill="none" stroke="{MUTED}" stroke-opacity=".5" stroke-width="2"/>
<path d="M140 62 L152 52" stroke="{TEAL}" stroke-width="2"/>
<text x="140" y="112" text-anchor="middle" font-size="15" fill="{INK}" letter-spacing="2" style="font-family:{MONO}">SN 7A20481</text>
<g class="lock"><rect x="66" y="96" width="148" height="24" rx="4" fill="none" stroke="{TEAL}" stroke-width="2"/></g>
<rect class="scan" x="44" y="30" width="192" height="3" fill="{TEAL}" opacity=".7"/>
"""
    return m, css


def motif_civic():
    css = f"""
.road{{animation:road 1.6s linear infinite}}
@keyframes road{{to{{transform:translateX(-60px)}}}}
.det{{stroke-dasharray:240;animation:det 3s ease-in-out infinite}}
@keyframes det{{0%{{stroke-dashoffset:240;opacity:1}}45%,85%{{stroke-dashoffset:0;opacity:1}}100%{{opacity:0}}}}
.tag{{animation:tag 3s ease-in-out infinite}}
@keyframes tag{{0%,40%{{opacity:0}}50%,85%{{opacity:1}}100%{{opacity:0}}}}
"""
    dashes = "".join(f'<rect x="{x}" y="110" width="30" height="4" fill="{MUTED}" opacity=".6"/>' for x in range(20, 400, 60))
    m = f"""
<path d="M0 140 L300 140 L300 80 L0 80 Z" fill="#0B1220"/>
<g class="road">{dashes}</g>
<ellipse cx="150" cy="96" rx="34" ry="9" fill="#1F2937" stroke="{MUTED}" stroke-opacity=".4"/>
<rect class="det" x="104" y="80" width="92" height="34" rx="3" fill="none" stroke="{TEAL}" stroke-width="2"/>
<g class="tag"><rect x="104" y="60" width="64" height="18" rx="3" fill="{TEAL}"/>
<text x="111" y="73" font-size="11" font-weight="700" fill="#0B1220" style="font-family:{MONO}">pothole</text></g>
<rect x="40" y="30" width="16" height="50" fill="{MUTED}" opacity=".35"/><circle cx="48" cy="26" r="9" fill="{BLUE}" opacity=".35"/>
<rect x="240" y="40" width="30" height="40" fill="{MUTED}" opacity=".25"/>
"""
    return m, css


def motif_rag():
    css = f"""
.vb{{transform-box:fill-box;transform-origin:center;animation:eq 1s ease-in-out infinite alternate}}
@keyframes eq{{0%{{transform:scaleY(.3)}}100%{{transform:scaleY(1)}}}}
.flow{{stroke-dasharray:4 6;animation:flow 1s linear infinite}}
@keyframes flow{{to{{stroke-dashoffset:-20}}}}
.hl{{animation:hl 3s ease-in-out infinite}}
@keyframes hl{{0%,100%{{transform:translateY(0)}}33%{{transform:translateY(16px)}}66%{{transform:translateY(32px)}}}}
"""
    bars = "".join(
        f'<rect class="vb" x="{36 + i * 9}" y="{80 - h / 2:.0f}" width="5" height="{h:.0f}" rx="2.5" fill="{TEAL}" style="animation-delay:-{i * .15:.2f}s"/>'
        for i, h in enumerate([18, 34, 50, 30, 56, 40, 22, 44])
    )
    lines = "".join(f'<rect x="196" y="{54 + i * 16}" width="{60 - (i % 2) * 16}" height="5" rx="2" fill="{MUTED}" opacity=".6"/>' for i in range(4))
    m = f"""
{bars}
<path class="flow" d="M118 80 H178" stroke="{BLUE}" stroke-width="2.5" fill="none"/>
<path d="M174 74 L182 80 L174 86" stroke="{BLUE}" stroke-width="2.5" fill="none"/>
<rect x="186" y="38" width="80" height="92" rx="8" fill="#0B1220" stroke="{MUTED}" stroke-opacity=".5"/>
<rect class="hl" x="190" y="50" width="72" height="13" rx="3" fill="{BLUE}" opacity=".3"/>
{lines}
"""
    return m, css


def motif_xvector():
    css = f"""
.vb{{transform-box:fill-box;transform-origin:center;animation:eq 1.1s ease-in-out infinite alternate}}
@keyframes eq{{0%{{transform:scaleY(.3)}}100%{{transform:scaleY(1)}}}}
.pt{{animation:conv 3.5s ease-in-out infinite}}
@keyframes conv{{0%{{transform:translate(0,0);opacity:0}}20%{{opacity:1}}70%,100%{{transform:translate(var(--tx),var(--ty));opacity:.9}}}}
.core{{transform-box:fill-box;transform-origin:center;animation:core 3.5s ease-in-out infinite}}
@keyframes core{{0%,60%{{transform:scale(.6);opacity:.4}}80%{{transform:scale(1.2);opacity:1}}100%{{transform:scale(1);opacity:.8}}}}
"""
    bars = "".join(
        f'<rect class="vb" x="{30 + i * 9}" y="{80 - h / 2:.0f}" width="5" height="{h:.0f}" rx="2.5" fill="{BLUE}" style="animation-delay:-{i * .12:.2f}s"/>'
        for i, h in enumerate([20, 44, 30, 58, 36, 50, 24])
    )
    pts = []
    for i in range(10):
        sx, sy = 110 + random.uniform(0, 20), random.uniform(40, 120)
        pts.append(
            f'<circle class="pt" cx="{sx:.0f}" cy="{sy:.0f}" r="3" fill="{TEAL}" '
            f'style="--tx:{215 - sx:.0f}px;--ty:{80 - sy:.0f}px;animation-delay:{i * .12:.2f}s"/>'
        )
    m = f"""
{bars}
{''.join(pts)}
<circle class="core" cx="215" cy="80" r="18" fill="none" stroke="{TEAL}" stroke-width="2"/>
<circle cx="215" cy="80" r="5" fill="{TEAL}"/>
<text x="215" y="124" text-anchor="middle" font-size="11" fill="{MUTED}" style="font-family:{MONO}">x-vector</text>
"""
    return m, css


def motif_slim():
    css = f"""
.vb{{transform-box:fill-box;transform-origin:center;animation:eq 1s ease-in-out infinite alternate}}
@keyframes eq{{0%{{transform:scaleY(.35)}}100%{{transform:scaleY(1)}}}}
.att{{animation:att 2.4s ease-in-out infinite}}
@keyframes att{{0%,100%{{opacity:.08}}50%{{opacity:.85}}}}
"""
    top = "".join(
        f'<rect class="vb" x="{40 + i * 14}" y="{48 - h / 2:.0f}" width="7" height="{h:.0f}" rx="3" fill="{BLUE}" style="animation-delay:-{i * .1:.2f}s"/>'
        for i, h in enumerate([14, 26, 18, 32, 22, 30, 16, 28, 20, 24, 14, 26, 18, 30])
    )
    bot = "".join(
        f'<rect class="vb" x="{40 + i * 14}" y="{118 - h / 2:.0f}" width="7" height="{h:.0f}" rx="3" fill="{TEAL}" style="animation-delay:-{i * .17:.2f}s"/>'
        for i, h in enumerate([22, 16, 30, 20, 26, 14, 32, 18, 24, 28, 16, 22, 30, 20])
    )
    att = []
    for i in range(12):
        a, b = random.randrange(14), random.randrange(14)
        att.append(
            f'<path class="att" d="M{43 + a * 14} 66 L{43 + b * 14} 100" stroke="#fff" stroke-width="1.2" '
            f'style="animation-delay:{i * .2:.1f}s"/>'
        )
    m = f"""
<text x="40" y="24" font-size="10" fill="{MUTED}" style="font-family:{MONO}">style</text>
{top}
{''.join(att)}
{bot}
<text x="40" y="148" font-size="10" fill="{MUTED}" style="font-family:{MONO}">linguistic</text>
"""
    return m, css


CARDS = [
    ("ocr", "01 · PRODUCTION OCR",
     [("14×", "faster on CPU · 253 → 18 ms"), ("98.2%", "precision · auto-accept gate"), ("84→21 MB", "INT8 quantized model")],
     motif_ocr, "Meter Serial OCR: 14x faster on CPU, 98.2% precision, 84 to 21 MB INT8 model"),
    ("civic", "02 · EDGE COMPUTER VISION",
     [("0.80", "mAP@50 · 10 classes"), ("17,000+", "real-world training images"), ("~26 MB", "INT8 TFLite · fully offline")],
     motif_civic, "Civic Monitor: 0.80 mAP@50, 17,000+ images, ~26 MB INT8 TFLite"),
    ("rag", "03 · VOICE RAG",
     [("ASR", "NVIDIA Canary voice queries"), ("FAISS", "retrieval · NVIDIA embeddings"), ("NIM", "grounded, source-linked answers")],
     motif_rag, "NVIDIA NIM RAG Voice Assistant: Canary ASR, FAISS retrieval, NIM answers"),
    ("xvector", "04 · SPEAKER IDENTIFICATION",
     [("93%", "accuracy · multi-speaker"), ("X-Vector", "embedding architecture"), ("ID + Verify", "identify & verify speakers")],
     motif_xvector, "Speaker Identification with X-Vectors: 93% accuracy"),
    ("slim", "05 · AUDIO DEEPFAKE DETECTION",
     [("99.98%", "fake-speech recall"), ("90%", "accuracy · ASVspoof 2019 LA"), ("4-head", "bidirectional cross-attention")],
     motif_slim, "SLIM-XA: 99.98% fake-speech recall, 90% accuracy on ASVspoof 2019 LA"),
]

# ------------------------------------------------------------------------- footer


def footer():
    W, H = 1200, 150
    layers = [
        (wave_path(2400, 600, 14, 60, H, 0.0), "#2C5364", ".55", 24),
        (wave_path(2400, 400, 12, 80, H, 1.1), "#203A43", ".8", 16),
        (wave_path(2400, 300, 10, 100, H, 2.2), "#0F2027", "1", 10),
    ]
    paths = "\n".join(
        f'<path d="{d}" fill="{c}" opacity="{o}" style="animation:slide {s}s linear infinite"/>' for d, c, o, s in layers
    )
    style = f"""
@keyframes slide{{to{{transform:translateX(-1200px)}}}}
{PARTICLE_CSS}
"""
    # particles drifting up off the wave crest
    body = f"""
{paths}
<g transform="translate(0,70)">{particles(28, W, 70, [BLUE, TEAL, "#ffffff"], rise=30)}</g>
"""
    return svg(W, H, body, style, "")


def main():
    files = {"hero.svg": hero(), "divider.svg": divider(), "footer.svg": footer()}
    for slug, kicker, metrics, motif_fn, label in CARDS:
        m, css = motif_fn()
        files[f"card-{slug}.svg"] = card(slug, kicker, metrics, m, css, label)
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
        print(f"{name:20s} {len(content.encode()) / 1024:6.1f} KB")


if __name__ == "__main__":
    main()
