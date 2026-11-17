"""Gera carrossel estilo 'tweet' (1080x1350 PNG) para @wesleyvitor.ecom.

Uso: python3 scripts/gerar_tweet.py post.json pasta_saida

post.json = {"slides": [{"paras": ["texto com <b>negrito</b>", ...],
                         "visual": "<html opcional: gráfico, ilustração, <img src='data:...'>>",
                         "fonte": "texto opcional de fonte, rodapé"}]}
"""
import asyncio, base64, json, sys
from pathlib import Path
from playwright.async_api import async_playwright

RAIZ = Path(__file__).resolve().parent.parent
NOME, HANDLE = "Wesley Vitor", "@wesleyvitor.ecom"
FOTO = base64.b64encode((RAIZ / "assets" / "foto.png").read_bytes()).decode()

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#fff;font-family:'Inter',sans-serif;color:#0f1419}
.s{width:1080px;height:1350px;padding:0 110px;display:flex;flex-direction:column;justify-content:center;position:relative}
.hd{display:flex;align-items:center;gap:30px;margin-bottom:56px}
.av{width:150px;height:150px;border-radius:50%;overflow:hidden;flex-shrink:0}
.av img{width:100%;height:100%;object-fit:cover;transform:scale(1.06)}
.nm{font-weight:800;font-size:52px;letter-spacing:-.5px}
.hn{font-size:44px;color:#536471;margin-top:4px}
.t p{font-size:62px;line-height:1.28;letter-spacing:-.8px;margin-bottom:48px}
.t p:last-child{margin-bottom:0}
.t b{font-weight:800}
.v .t p{font-size:52px;margin-bottom:34px}
.vis{margin-top:48px}
.fonte{position:absolute;left:110px;right:110px;bottom:60px;font-size:24px;color:#8b98a5}
"""

def slide(s):
    ps = "".join(f"<p>{p}</p>" for p in s["paras"])
    vis = f'<div class="vis">{s["visual"]}</div>' if s.get("visual") else ""
    fonte = f'<div class="fonte">Fonte: {s["fonte"]}</div>' if s.get("fonte") else ""
    cls = "s v" if s.get("visual") else "s"
    return f"""<div class="{cls}"><div class="hd"><div class="av"><img src="data:image/png;base64,{FOTO}"></div>
<div><div class="nm">{NOME}</div><div class="hn">{HANDLE}</div></div></div><div class="t">{ps}</div>{vis}{fonte}</div>"""

async def main(post, out):
    out.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for k, s in enumerate(post["slides"], 1):
            await pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{slide(s)}</body></html>")
            await pg.wait_for_timeout(150)
            await pg.screenshot(path=str(out / f"slide_{k:02d}.png"))
        await b.close()
    print(len(post["slides"]), "slides em", out)

if __name__ == "__main__":
    asyncio.run(main(json.loads(Path(sys.argv[1]).read_text()), Path(sys.argv[2])))
