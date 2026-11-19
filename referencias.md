# Referências de conteúdo — @wesleyvitor.ecom

Perfis que o Wesley usa como referência de tema e estilo (pesquisar o que estão falando em fontes abertas: YouTube, blogs, X, LinkedIn, notícias).

- Thiago Nigro (Primo Rico) — finanças, negócios; referência do formato "tweet"
- Ecommerce Puro — e-commerce e marketplaces
- Gabriel Bollico — empresário de e-commerce (ShopB)
- Alfredo Soares — vendas, varejo, empreendedorismo
- Himmel Corp — @himmelcorp
- Dhiego Rosa — @dhiegorosa

## Temas
E-commerce, negócios, novidades, tecnologia, marketplaces (Mercado Livre, Shopee, Amazon, TikTok Shop).

## Regras do post
- Formato: estilo "tweet", 1080x1350, foto + Wesley Vitor + @wesleyvitor.ecom (carrossel de 6 a 8 slides, ou foto única na quarta)
- Máximo 5 hashtags (limite do Instagram)
- Calendário (definido pelo Wesley em 18/11): segunda, quinta e sexta = CARROSSEL; quarta = POST DE FOTO ÚNICA. Todos às 10h (America/Sao_Paulo), 4 por semana agendados. O Reel semanal o Wesley posta manualmente (não passa pelo Metricool e não conta no limite de 20/mês).
- Post de foto única (quarta): UM slide só, mesmo layout tweet (foto + nome + @), sobre o assunto mais quente/viralizado da semana em negócios, empreendedorismo e e-commerce (mesma regra de pauta do carrossel: pesquisar, número com fonte, nunca repetir o historico.md). Em vez de explicar a notícia, dá a opinião em 2 ou 3 frases. Alternar 3 formatos: (1) "Minha leitura": fato + minha leitura, tom empresário raiz; (2) "Número que chocou": dado em destaque + fonte + o que significa pro vendedor; (3) "Pergunta quente": assunto viral virando pergunta pra comentar. De vez em quando um gráfico simples ou ilustração leve (mesmas regras de visual). Legenda curta com 1 pergunta e até 5 hashtags. Gerar com scripts/gerar_tweet.py com 1 slide só e agendar com instagramData type POST e 1 mídia.
- Plano Free do Metricool: até 20 publicações/mês

## Imagens nos posts
- Padrão definido pelo Wesley (18/11): usar visual SEMPRE que possível, dosando (sem exagero): em cada carrossel, ~2 a 4 slides com visual e o resto só texto, evitando visuais em slides seguidos demais.
- Mistura de tipos de visual: (a) ilustração de objeto realista (Canva), (b) gráficos/barras/números desenhados em HTML (como no post de 17/11 de Black Friday), (c) elementos desenhados por código (ícones, comparativos, linhas do tempo). Variar os tipos dentro do mesmo carrossel.
- Pode: gráficos e números desenhados por código; ilustrações/ícones/telas genéricas feitas por código (SVG/HTML); imagens geradas por IA no Canva (generate-image).
- Não pode: fotos reais de pessoas famosas, fotos baixadas da internet, logos/marcas de terceiros, personagens.
- Posição: dentro do modelo tweet, abaixo do nome/@ e do texto, no 1º slide ou no slide onde fizer sentido.
- Se usar imagem gerada por IA, marcar instagramData.isAiGenerated = true no Metricool.

## Tom de voz
- Sincero, direto, "empresário raiz": fala de quem opera e põe a mão na massa, não de guru.
- Linguagem do dia a dia do vendedor (margem, frete, estoque, boleto, pedido atrasado), sem palavras difíceis nem frases de coach.
- Pode cutucar e discordar do senso comum; verdade incômoda > motivação vazia.
- Primeira pessoa ("eu faria", "na minha operação"), frases curtas.
- Sem palavrão pesado, sem prometer resultado fácil, sem inventar número: dado sempre com fonte.

## Estilo dos posts ilustrados (exemplos enviados pelo Wesley, posts do @thiago.nigro)
- Mesmo layout tweet: foto + nome + @ no topo, texto curto (1 a 3 frases) com 1 ou 2 palavras em negrito.
- Abaixo do texto, UM objeto/ilustração grande, centralizado, isolado em fundo branco puro (sem cenário, sem moldura).
- Estilo foto realista de produto (ex.: cofrinho quebrado com moedas, celular, cesta de pão francês, nota de dinheiro).
- O objeto ilustra literalmente a frase do slide (frase sobre pão -> pão; sobre dólar -> dinheiro).
- Imagem em vários slides do mesmo carrossel quando cada slide fala de um objeto diferente.
- No nosso: objetos genéricos SEM marca/logo visível; não usar cédula real nem capa de jogo/produto de marca.
- Texto um pouco maior quando o slide tem só 1 frase; imagem ocupando ~40% da altura do slide.

## Como gerar a ilustração em alta (pipeline testado em 17/11)
1. Canva `generate-image` com prompt: "<objeto>, estilo foto realista de produto, isolado em fundo branco puro, sem texto, sem logos".
2. O resultado vem em miniatura; para alta resolução: no design auxiliar do Canva DAHbHmz_oCw, `read-design` (open_transaction) → `edit-design-v2` com `add_page` (tamanho da imagem, fundo branco) → `add_image` com o media_id ocupando a página → commit → `export-design` PNG só dessa página → baixar o link (export-download.canva.com) com curl.
3. Depois de baixar, remover a página auxiliar (remove_page) pra não acumular.
4. Recortar o fundo branco excedente (PIL) e passar a imagem em base64 no campo "visual" do post.json (<img src='data:image/png;base64,...' style='width:100%;max-height:520px;object-fit:contain'>).
5. Marcar instagramData.isAiGenerated = true ao agendar.
