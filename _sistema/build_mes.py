# Uso: python3 _sistema/build_mes.py <modulo_posts> <pasta_mes>
# Ex.:  python3 _sistema/build_mes.py posts_2027_02 4_Fevereiro_2027
# Rode a partir da raiz do repositório. O módulo fica em _sistema/meses/<modulo>.py
# e define POSTS (lista de car()/img() de helpers.py), com "date" e "time" (HH:MM) em cada post.
import os, sys, json, shutil, datetime, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "meses"))
from render import render_post

DOW = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
MES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

mod, pasta = sys.argv[1], sys.argv[2]
posts = sorted(importlib.import_module(mod).POSTS, key=lambda p: p["date"])
assert len(posts) <= 20, f"{len(posts)} posts: limite gratuito do Metricool é 20/mês"
assert len({p["date"] for p in posts}) == len(posts), "datas repetidas"
for p in posts:
    for ch in ("—", "–"):
        txt = json.dumps(p, ensure_ascii=False)
        assert ch not in txt, f"travessão em {p['tema']}"

shutil.rmtree(pasta, ignore_errors=True)
plan = []
for n, p in enumerate(posts, 1):
    d = datetime.date.fromisoformat(p["date"])
    fold = os.path.join(pasta, f"{n:02d}_{d.day:02d}{MES[d.month-1]}_{DOW[d.weekday()]}_{p['tema']}")
    files = render_post(p, fold)
    open(os.path.join(fold, "legenda.txt"), "w", encoding="utf-8").write(p["caption"] + "\n")
    plan.append(dict(date=p["date"], time=p.get("time", "11:45"), tema=p["tema"], fmt=p["fmt"],
                     files=[f.replace(os.sep, "/") for f in files], text=p["caption"]))
json.dump(plan, open(os.path.join(pasta, "plano.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(plan)} posts renderizados em {pasta}")
for x in plan:
    print(x["date"], x["time"], x["fmt"], len(x["files"]), x["tema"])
