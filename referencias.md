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

### Assuntos virais fora do nicho (regra do Wesley, 19/11)
Não ficar 100% travado no nicho. Assuntos que estão em alta demais no Brasil (cultura pop, games, esporte, tecnologia, fatos da semana) podem virar post, carrossel, manchete ou vídeo, desde que o gancho conecte com negócios, vendas, consumo, marketing ou empreendedorismo. Exemplo enviado por ele: o Alfredo Soares postou sobre a Logitech dar folga remunerada para funcionários jogarem GTA VI (matéria da Forbes). Ou seja: pegar o assunto do momento (ex.: GTA VI) e tirar a lição ou o ângulo de negócio (ex.: cultura de empresa, marketing de lançamento, impacto em vendas de games e periféricos, produtividade).
- Na pesquisa, incluir também os assuntos mais comentados do momento (Brasil), não só e-commerce.
- Prioridade: o que está bombando e dá para ligar ao mundo do vendedor/empreendedor. Se o assunto não tem ligação nenhuma com negócios, não usar.
- Valem as mesmas regras: número com fonte confiável, sem inventar, sem repetir o historico.md. Em carrossel e manchete, citar a fonte (ex.: Forbes).
- Isso vale para o carrossel, a manchete, o Reel de terça e o vídeo de IA do domingo.

## Regras do post
- Formato: estilo "tweet", 1080x1350, foto + Wesley Vitor + @wesleyvitor.ecom (carrossel de 6 a 8 slides, ou foto única na quarta)
- Máximo 5 hashtags (limite do Instagram)
- Calendário (definido pelo Wesley em 18/11): segunda, quinta e sexta = CARROSSEL; quarta = POST DE FOTO ÚNICA. Todos às 10h (America/Sao_Paulo), 4 por semana agendados. O Reel semanal o Wesley posta manualmente (não passa pelo Metricool e não conta no limite de 20/mês).
- Post de foto única (quarta) = estilo MANCHETE (aprovado pelo Wesley em 19/11, inspirado em posts de notícia tipo Forbes BR): UMA imagem 1080x1350 com foto de fundo escura em tela cheia, etiqueta curta, manchete grande em branco com a palavra-chave/número em amarelo, e rodapé com foto + Wesley Vitor + @wesleyvitor.ecom e a fonte do dado. NÃO é o layout tweet. Assunto: o mais quente/viralizado da semana em negócios, empreendedorismo e e-commerce (mesma regra de pauta do carrossel: pesquisar, número com fonte, nunca repetir o historico.md).
- Manchete: o fato em 2 a 4 linhas (até ~12 palavras), direto, com número quando houver; destaque em <b> só 1 ou 2 trechos. Etiqueta: MARKETPLACES, E-COMMERCE, NEGÓCIOS, VAREJO, TECNOLOGIA etc. A opinião do Wesley (2 ou 3 frases, tom empresário raiz) vai na LEGENDA, que termina com uma pergunta e até 5 hashtags. Alternar o ângulo da legenda: "minha leitura", "número que chocou" ou "pergunta quente".
- Fundo da manchete: imagem gerada no Canva (generate-image, aspectRatio PORTRAIT_4_5) com prompt "<cena/objeto relacionado ao tema>, clima escuro e dramático, foto realista, sem pessoas, sem texto, sem logos". Nunca foto de notícia, de pessoa real, logo ou marca de terceiros; não copiar o layout/logo de nenhum veículo. Marcar isAiGenerated true no Metricool.
- Alta resolução do fundo: no design auxiliar do Canva DAHbHmz_oCw, REAPROVEITE as páginas auxiliares 2048x2048 que já existem (hoje as páginas 3 a 6, ids via read-design com open_transaction): em edit-design faça delete_element do elemento antigo e insert_fill com o media_id novo em left 205, top 0, width 1638, height 2048; commit; export-design PNG pages [N] export_quality pro; baixe o link com curl; recorte (205,0,1843,2048) e redimensione para 1080x1350 (PIL), salve como assets/fundos/AAAA-MM-DD-slug.jpg. Só adicione página nova se todas estiverem ocupadas (não há operação de remover página).
- Gerar: python3 scripts/gerar_manchete.py posts/<pasta>/manchete.json posts/<pasta>/slide_01.png, com manchete.json = {"fundo":"assets/fundos/AAAA-MM-DD-slug.jpg","tag":"E-COMMERCE","manchete":"texto com <b>destaque</b>","fonte":"..."}. Confira o PNG (Read): manchete legível, sem palavra órfã sozinha na última linha se der pra encurtar, sem texto cortado. Agendar com 1 mídia (slide_01.png), instagramData type POST e isAiGenerated true. Exemplos prontos em exemplos/.
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
