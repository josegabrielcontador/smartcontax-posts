def C(kicker, title, sub=None, note=None):
    return {"k": "cover", "kicker": kicker, "title": title, "sub": sub, "note": note}

def S(n, title, blocks=None, box=None):
    return {"k": "c", "n": n, "title": title, "blocks": blocks or [], "box": box}

def A(title, text, share="Envie para quem precisa ver"):
    return {"k": "cta", "title": title, "text": text, "share": share}

def car(date, tema, slides, caption):
    return {"date": date, "fmt": "C", "tema": tema, "slides": slides, "caption": caption.strip()}

def img(date, tema, slide, caption):
    return {"date": date, "fmt": "I", "tema": tema, "slide": slide, "caption": caption.strip()}
