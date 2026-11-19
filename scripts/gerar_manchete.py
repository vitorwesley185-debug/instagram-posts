"""Gera post de FOTO ÚNICA estilo 'manchete' (1080x1350 PNG) para @wesleyvitor.ecom.

Uso: python3 scripts/gerar_manchete.py post.json saida.png

post.json = {"fundo": "assets/fundos/arquivo.jpg",   # imagem 1080x1350 (caminho relativo à raiz do repo)
             "tag": "E-COMMERCE",                    # etiqueta curta em maiúsculas
             "manchete": "texto com <b>destaque</b>", # 2 a 4 linhas
             "fonte": "Fonte do dado"}               # opcional
"""
import asyncio, base64, json, sys
from pathlib import Path
from playwright.async_api import async_playwright

RAIZ = Path(__file__).resolve().parent.parent
NOME, HANDLE = "Wesley Vitor", "@wesleyvitor.ecom"
FOTO = base64.b64encode((RAIZ / "assets" / "foto.png").read_bytes()).decode()
ACENTO = "#ffcc33"

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:'Inter',sans-serif;color:#fff;position:relative;overflow:hidden;background:#000}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.gr{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.95) 0%,rgba(0,0,0,.88) 30%,rgba(0,0,0,.45) 55%,rgba(0,0,0,0) 75%)}
.box{position:absolute;left:80px;right:80px;bottom:70px}
.tag{display:flex;align-items:center;gap:18px;font-weight:700;font-size:30px;letter-spacing:3px;margin-bottom:30px}
.tag i{display:block;width:8px;height:38px;background:@AC@}
h1{font-weight:800;font-size:78px;line-height:1.07;letter-spacing:-2px;margin-bottom:46px}
h1 b{color:@AC@;font-weight:800}
.row{display:flex;align-items:center;gap:22px}
.av{width:84px;height:84px;border-radius:50%;overflow:hidden;flex-shrink:0}
.av img{width:100%;height:100%;object-fit:cover;transform:scale(1.06)}
.nm{font-weight:800;font-size:34px}
.hn{font-size:28px;color:#c4cbd2;margin-top:2px}
.fonte{margin-top:26px;font-size:23px;color:#9aa4ad}
""".replace("@AC@", ACENTO)

def html(p):
    bg = base64.b64encode((RAIZ / p["fundo"]).read_bytes()).decode()
    fonte = f'<div class="fonte">Fonte: {p["fonte"]}</div>' if p.get("fonte") else ""
    return f"""<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>
<div class="bg" style="background-image:url(data:image/jpeg;base64,{bg})"></div><div class="gr"></div>
<div class="box"><div class="tag"><i></i>{p["tag"]}</div><h1>{p["manchete"]}</h1>
<div class="row"><div class="av"><img src="data:image/png;base64,{FOTO}"></div>
<div><div class="nm">{NOME}</div><div class="hn">{HANDLE}</div></div></div>{fonte}</div></body></html>"""

async def main(p, out):
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        await pg.set_content(html(p)); await pg.wait_for_timeout(200)
        await pg.screenshot(path=str(out)); await b.close()
    print("ok", out)

if __name__ == "__main__":
    asyncio.run(main(json.loads(Path(sys.argv[1]).read_text()), Path(sys.argv[2])))
