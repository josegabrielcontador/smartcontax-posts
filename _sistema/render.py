import os, re
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
M = 90
NAVY = "#0D1733"; INST = "#1B2F6E"; MID = "#2B4BAA"; ORANGE = "#D4600A"
GOLD = "#C8930A"; GREY = "#6B6E70"; WHITE = "#FFFFFF"; DARK = "#1A1F36"
LIGHT = "#F4F5F9"; TINT = "#FCEFE5"; LINE = "#E3E6EF"; SOFT = "#C3CBE3"

FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
_fc = {}
def F(w, s):
    k = (w, s)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(os.path.join(FD, f"Lato-{w}.ttf"), s)
    return _fc[k]

class Overflow(Exception):
    pass

_MD = ImageDraw.Draw(Image.new('RGB', (10, 10)))
def tw(d, t, f):
    return _MD.textlength(t, font=f)

def tokens(text, base, hl):
    """Words as lists of (segment, color); *x* marks highlight."""
    words = []; cur = []; buf = ""; on = False
    def flush_seg():
        nonlocal buf
        if buf:
            cur.append((buf, hl if on else base)); buf = ""
    for ch in text:
        if ch == "*":
            flush_seg(); on = not on
        elif ch == " ":
            flush_seg()
            if cur: words.append(cur)
            cur = []
        else:
            buf += ch
    flush_seg()
    if cur: words.append(cur)
    return words

def wlen(d, w, f):
    return sum(tw(d, s, f) for s, _ in w)

def wrap(d, text, f, maxw, base=DARK, hl=ORANGE):
    lines = []
    sp = tw(d, " ", f)
    for para in text.split("\n"):
        cur = []; curw = 0
        for w in tokens(para, base, hl):
            ww = wlen(d, w, f)
            if cur and curw + sp + ww > maxw:
                lines.append(cur); cur = [w]; curw = ww
            else:
                curw = curw + (sp if cur else 0) + ww
                cur.append(w)
        lines.append(cur)
    return lines

def draw_lines(d, lines, f, x, y, lh, align="left", maxw=None):
    sp = tw(d, " ", f)
    for ln in lines:
        cx = x
        for w in ln:
            for s, c in w:
                if d is not None:
                    d.text((cx, y), s, font=f, fill=c)
                cx += tw(d, s, f)
            cx += sp
        y += lh
    return y

def text_block_h(lines, lh):
    return len(lines) * lh

def spaced(d, xy, text, f, fill, track=3):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += tw(d, ch, f) + track
    return x

def spaced_w(d, text, f, track=3):
    return sum(tw(d, ch, f) + track for ch in text) - track

_LOGO = {}
def _logo(kind):
    if kind not in _LOGO:
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brand", f"logo_h_{kind}.png")
        im = Image.open(p).convert("RGBA")
        bb = im.getbbox(); _LOGO[kind] = im.crop(bb)
    return _LOGO[kind]

def wordmark(d, x, y, dark_bg=True, scale=1.0, on_orange=False):
    lg = _logo("white" if dark_bg else "color")
    h = int(74 * scale)
    w = int(lg.width * h / lg.height)
    lg = lg.resize((w, h), Image.LANCZOS)
    d._image.paste(lg, (x, y - 6), lg)

def arrow(d, cx, cy, r=34, bg=ORANGE, fg=WHITE):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg)
    d.line([cx - 13, cy, cx + 11, cy], fill=fg, width=5)
    d.line([cx + 1, cy - 11, cx + 13, cy], fill=fg, width=5)
    d.line([cx + 1, cy + 11, cx + 13, cy], fill=fg, width=5)

def fit_title(d, text, maxw, maxh, sizes, weight="Black", base=WHITE, hl=ORANGE, lhk=1.12):
    for s in sizes:
        f = F(weight, s)
        ln = wrap(d, text, f, maxw, base, hl)
        lh = int(s * lhk)
        if len(ln) * lh <= maxh:
            return f, ln, lh
    raise Overflow("title: " + text)

# ---------------- slides ----------------

def cover(s, idx, total):
    im = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(im)
    # decoration
    d.ellipse([W - 360, -260, W + 260, 360], outline=INST, width=60)
    d.rectangle([0, H - 14, W, H], fill=ORANGE)
    wordmark(d, M, 80, True)
    y = 330
    d.rectangle([M, y, M + 110, y + 10], fill=ORANGE)
    y += 46
    spaced(d, (M, y), s["kicker"].upper(), F("Bold", 30), ORANGE, 4)
    y += 70
    f, ln, lh = fit_title(d, s["title"], W - 2 * M, 470, [96, 90, 84, 78, 72, 66, 60])
    y = draw_lines(d, ln, f, M, y, lh)
    if s.get("sub"):
        y += 30
        fs = F("Regular", 40)
        ln = wrap(d, s["sub"], fs, W - 2 * M, SOFT, ORANGE)
        y = draw_lines(d, ln, fs, M, y, 54)
    if s.get("note"):
        fn = F("Bold", 32)
        ln = wrap(d, s["note"], fn, W - 2 * M - 80, WHITE, ORANGE)
        bh = len(ln) * 44 + 56
        by = H - 150 - bh
        if by < y + 30:
            raise Overflow("cover note")
        d.rounded_rectangle([M, by, W - M, by + bh], radius=22, fill=INST)
        d.rectangle([M, by, M + 10, by + bh], fill=ORANGE)
        draw_lines(d, ln, fn, M + 44, by + 28, 44)
    spaced(d, (M, H - 104), "@SMARTCONTAX", F("Bold", 24), SOFT, 3)
    lab = "ARRASTE"
    fl = F("Bold", 24)
    lw = spaced_w(d, lab, fl, 3)
    spaced(d, (W - M - 80 - lw, H - 104), lab, fl, WHITE, 3)
    arrow(d, W - M - 30, H - 92)
    return im

def content(s, idx, total):
    im = Image.new("RGB", (W, H), WHITE); d = ImageDraw.Draw(im)
    wordmark(d, M, 66, False, 0.8)
    pg = f"{idx:02d} / {total:02d}"
    fp = F("Bold", 24)
    spaced(d, (W - M - spaced_w(d, pg, fp, 2), 74), pg, fp, GREY, 2)
    d.line([M, 140, W - M, 140], fill=LINE, width=2)
    TOP = 186; footer_top = H - 150
    f, tln, lh = fit_title(d, s["title"], W - 2 * M, 300, [76, 70, 64, 58, 52], base=NAVY)
    head_h = (120 if s.get("n") else 0) + len(tln) * lh + 26
    for bs in [48, 46, 44, 42, 40, 38, 36, 34]:
        plan = []
        yy = head_h
        fb = F("Regular", bs); lhb = int(bs * 1.36)
        for bl in s.get("blocks", []):
            if isinstance(bl, (list, tuple)):
                lab, txt = bl
                plan.append(("lab", lab, yy)); yy += 50
                ln = wrap(d, txt, fb, W - 2 * M, DARK, ORANGE)
                plan.append(("txt", ln, yy, fb, lhb)); yy += len(ln) * lhb + 40
            else:
                ln = wrap(d, bl, fb, W - 2 * M, DARK, ORANGE)
                plan.append(("txt", ln, yy, fb, lhb)); yy += len(ln) * lhb + 32
        if s.get("box"):
            fx = F("Bold", bs - 2); lhx = int((bs - 2) * 1.34)
            ln = wrap(d, s["box"], fx, W - 2 * M - 90, NAVY, ORANGE)
            bh = len(ln) * lhx + 70
            yy += 14
            plan.append(("box", ln, yy, fx, lhx, bh)); yy += bh
        if TOP + yy <= footer_top - 20:
            break
    else:
        raise Overflow("content: " + s["title"])
    off = TOP + max(0, (footer_top - 20 - TOP - yy) // 2)
    y = off
    if s.get("n"):
        d.text((M, y - 18), s["n"], font=F("Black", 110), fill=ORANGE)
        y += 120
    draw_lines(d, tln, f, M, y, lh)
    for p in plan:
        if p[0] == "lab":
            spaced(d, (M, off + p[2]), p[1].upper(), F("Bold", 30), ORANGE, 3)
        elif p[0] == "txt":
            draw_lines(d, p[1], p[3], M, off + p[2], p[4])
        else:
            _, ln, by, fx, lhx, bh = p
            by += off
            d.rounded_rectangle([M, by, W - M, by + bh], radius=20, fill=TINT)
            d.rectangle([M, by, M + 10, by + bh], fill=ORANGE)
            draw_lines(d, ln, fx, M + 46, by + 35, lhx)
    d.line([M, H - 130, W - M, H - 130], fill=LINE, width=2)
    spaced(d, (M, H - 96), "@SMARTCONTAX", F("Bold", 24), GREY, 3)
    if idx < total:
        arrow(d, W - M - 30, H - 84)
    return im

def bookmark(d, x, y, c):
    d.polygon([(x, y), (x + 44, y), (x + 44, y + 58), (x + 22, y + 42), (x, y + 58)], fill=c)

def plane(d, x, y, c):
    d.polygon([(x, y + 24), (x + 58, y), (x + 40, y + 58), (x + 26, y + 34)], fill=c)

def cta(s, idx, total):
    im = Image.new("RGB", (W, H), ORANGE); d = ImageDraw.Draw(im)
    d.ellipse([-300, H - 420, 380, H + 260], outline="#E07A2E", width=60)
    wordmark(d, M, 80, True, on_orange=True)
    y = 300
    f, ln, lh = fit_title(d, s["title"], W - 2 * M, 420, [84, 78, 72, 66, 60], base=WHITE, hl=NAVY)
    y = draw_lines(d, ln, f, M, y, lh) + 30
    fb = F("Regular", 40)
    ln = wrap(d, s.get("text", ""), fb, W - 2 * M, WHITE, NAVY)
    y = draw_lines(d, ln, fb, M, y, 56) + 50
    if y > 960:
        raise Overflow("cta")
    by = max(y + 10, 760)
    bookmark(d, M, by, NAVY)
    d.text((M + 70, by + 8), "Salve para consultar depois", font=F("Bold", 36), fill=WHITE)
    plane(d, M - 4, by + 96, NAVY)
    d.text((M + 70, by + 104), s.get("share", "Envie para quem precisa ver"), font=F("Bold", 36), fill=WHITE)
    d.rectangle([0, H - 120, W, H], fill=NAVY)
    spaced(d, (M, H - 80), "@SMARTCONTAX", F("Bold", 28), WHITE, 3)
    t = "CONTABILIDADE CONSULTIVA"
    ft = F("Bold", 22)
    spaced(d, (W - M - spaced_w(d, t, ft, 3), H - 76), t, ft, SOFT, 3)
    return im

def single(s):
    theme = s.get("theme", "navy")
    bg = {"navy": NAVY, "light": LIGHT, "white": WHITE, "orange": ORANGE}[theme]
    dark = theme in ("navy", "orange")
    base = WHITE if dark else NAVY
    hl = NAVY if theme == "orange" else ORANGE
    acc = NAVY if theme == "orange" else ORANGE
    soft = SOFT if theme == "navy" else ("#FBE3D2" if theme == "orange" else GREY)
    body_c = soft if dark else DARK
    if theme == "orange": body_c = WHITE
    im = Image.new("RGB", (W, H), bg); real = ImageDraw.Draw(im)
    if theme == "navy":
        real.ellipse([W - 360, -260, W + 260, 360], outline=INST, width=60)
    elif theme == "light":
        real.rectangle([0, 0, 18, H], fill=ORANGE)
    wordmark(real, M, 80, dark, on_orange=(theme == "orange"))
    TOP, BOT = 230, H - 150
    def layout(d, y0, ts, bs):
        y = y0
        if s.get("chip"):
            fc = F("Black", 32)
            cw = spaced_w(real, s["chip"].upper(), fc, 4) + 60
            if d:
                d.rounded_rectangle([M, y, M + cw, y + 68], radius=34, fill=s.get("chipbg", acc))
                spaced(d, (M + 30, y + 15), s["chip"].upper(), fc, WHITE, 4)
            y += 112
        elif s.get("kicker"):
            if d:
                d.rectangle([M, y, M + 110, y + 10], fill=acc)
                spaced(d, (M, y + 46), s["kicker"].upper(), F("Bold", 32), acc, 4)
            y += 120
        if s.get("big"):
            bsz = s.get("bigsize", 230)
            if d:
                d.text((M - 8, y - int(bsz * 0.2)), s["big"], font=F("Black", bsz), fill=GOLD if theme == "navy" else acc)
            y += int(bsz * 0.95)
        ft = F("Black", ts); lht = int(ts * 1.13)
        ln = wrap(real, s["title"], ft, W - 2 * M, base, hl)
        y = draw_lines(d, ln, ft, M, y, lht) + 36
        if s.get("text"):
            fb = F("Regular", bs); lhb = int(bs * 1.4)
            for para in s["text"].split("\n"):
                ln = wrap(real, para, fb, W - 2 * M - (40 if para.startswith("• ") else 0), body_c, hl)
                if para.startswith("• "):
                    ln = wrap(real, para[2:], fb, W - 2 * M - 40, body_c, hl)
                    if d: d.ellipse([M, y + bs * 0.45, M + 14, y + bs * 0.45 + 14], fill=acc)
                    y = draw_lines(d, ln, fb, M + 40, y, lhb) + 12
                else:
                    y = draw_lines(d, ln, fb, M, y, lhb) + 12
            y += 22
        if s.get("box"):
            fx = F("Bold", bs - 2); lhx = int((bs - 2) * 1.36)
            ln = wrap(real, s["box"], fx, W - 2 * M - 90, NAVY if not theme == "navy" else WHITE, ORANGE if theme != "orange" else NAVY)
            bh = len(ln) * lhx + 70
            boxbg = {"navy": INST, "orange": "#FBE3D2"}.get(theme, TINT)
            if d:
                d.rounded_rectangle([M, y, W - M, y + bh], radius=22, fill=boxbg)
                d.rectangle([M, y, M + 10, y + bh], fill=acc)
                draw_lines(d, ln, fx, M + 46, y + 35, lhx)
            y += bh
        return y
    combo = None
    for bss in ([46, 44, 42], [40, 38, 36]):
        for ts in [100, 94, 88, 82, 76, 70, 64, 58]:
            for bs in bss:
                h = layout(None, 0, ts, bs)
                if h <= BOT - TOP:
                    combo = (ts, bs); break
            if combo: break
        if combo: break
    if not combo:
        raise Overflow("single: " + s["title"])
    ts, bs = combo
    h = layout(None, 0, ts, bs)
    y0 = TOP + max(0, (BOT - TOP - h) // 2)
    layout(real, y0, ts, bs)
    d = real
    d.rectangle([0, H - 14, W, H], fill=ORANGE if theme != "orange" else NAVY)
    spaced(d, (M, H - 96), "@SMARTCONTAX", F("Bold", 24), soft, 3)
    if s.get("foot"):
        ff = F("Bold", 22)
        spaced(d, (W - M - spaced_w(d, s["foot"].upper(), ff, 3), H - 94), s["foot"].upper(), ff, soft, 3)
    return im

def render_post(p, outdir):
    os.makedirs(outdir, exist_ok=True)
    files = []
    if p["fmt"] == "I":
        im = single(p["slide"])
        fn = os.path.join(outdir, "01.png"); im.save(fn, optimize=True); files.append(fn)
    else:
        sl = p["slides"]
        total = len(sl)
        for i, s in enumerate(sl, 1):
            k = s["k"]
            im = {"cover": cover, "c": content, "cta": cta}[k](s, i, total)
            fn = os.path.join(outdir, f"{i:02d}.png"); im.save(fn, optimize=True); files.append(fn)
    return files
