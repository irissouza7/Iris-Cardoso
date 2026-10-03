---
name: dashboard-narrativo-azul-lilas
description: Regras visuais e narrativas para dashboards em HTML que contam uma história com dados para o público leigo, numa paleta azul e lilás. Use sempre que for criar um painel, gráfico, indicador ou relatório visual em HTML, com qualquer base de dados.
---

# Dashboard narrativo azul e lilás

## Quando usar

- Sempre que o pedido for um dashboard, painel, relatório visual ou gráfico em HTML.
- Principalmente quando o público não é especialista e decide em poucos segundos se continua lendo.
- Não use para tabelas técnicas de consulta, em que o usuário já sabe o que procura. Nesse caso, priorize filtro e tabela.

## Estrutura narrativa

Organize a página como uma história de começo, meio e fim:

1. **Título-manchete com a conclusão.** O `<h1>` é uma frase com a descoberta principal, não o nome do tema. Ex.: "A maioria dos clientes volta em menos de 30 dias", e não "Análise de retorno de clientes".
2. **Subtítulo de 1 ou 2 frases** com o contexto mínimo: o que foi medido, onde e quando.
3. **De 3 a 5 indicadores no topo (KPIs)** que resumem a história na ordem das seções. Cada um tem um número grande e uma legenda curta em linguagem cotidiana.
4. **Seções numeradas** ("1 · O retrato", "2 · O espelho"...), cada uma respondendo a uma pergunta. Cada seção tem:
   - um título que é a conclusão daquela seção;
   - um parágrafo de 2 ou 3 frases que diz o que olhar no gráfico;
   - um único gráfico principal (no máximo dois, lado a lado, se forem complementares).
5. **Uma virada no meio.** Depois de estabelecer o padrão, mostre um dado que o complica ou o relativiza (exceção, contraste, combinação rara). É isso que torna a história memorável.
6. **Uma seção pessoal** ("E no seu caso?"): um seletor que permite ao leitor encontrar o próprio recorte (local, grupo, período), sempre comparado com o total.
7. **Fechamento** num bloco de destaque: responda à pergunta norteadora em 2 ou 3 frases e devolva uma reflexão ao leitor.
8. **Nota de dados recolhível** (`<details>`): fonte, data de extração, recorte, definições, limitações e uma tabela com os números principais.

## Linguagem

- Escreva para alguém sem formação técnica. Troque jargão por palavras do dia a dia e, se o termo for inevitável, explique-o na primeira vez.
- No texto, prefira frações e números redondos ("1 em cada 4", "87 em cada 100"). Na dica de hover e na tabela, mostre o valor exato.
- Use números no formato brasileiro (`toLocaleString("pt-BR")`): vírgula decimal e ponto de milhar.
- Nunca afirme no texto algo que o gráfico ao lado não mostre.
- Diga explicitamente o que o dado **não** permite concluir (autodeclaração, recorte temporal, valores ausentes).

## Escolha de gráficos

| Pergunta | Use | Evite |
| --- | --- | --- |
| Quanto de um todo? (uma proporção) | Gráfico de unidades (waffle 10×10) ou um número grande | Pizza com muitas fatias |
| Comparar categorias | Barras horizontais ordenadas do maior para o menor | Barras 3D, ordem alfabética sem motivo |
| Comparar dois grupos nas mesmas categorias | Barras pareadas (duas barras finas por categoria) | Eixo duplo |
| Distribuição em faixas ordenadas | Colunas na ordem natural das faixas | Reordenar faixas por tamanho |
| Filtros sucessivos / combinação de critérios | Funil de barras horizontais na mesma escala | Diagramas de Venn com mais de 3 conjuntos |
| Evolução no tempo | Linha (2 px) com marcadores nos pontos citados | Colunas para séries longas |
| Um número que resume tudo | Cartão de KPI | Um gráfico para um único valor |

Regras gerais:

- Percentuais sempre na escala de 0 a 100%. Barras sempre começam do zero. Nunca corte o eixo de uma barra.
- No máximo 8 categorias por gráfico. O restante vai para "Outros".
- Rótulo direto ao lado da barra. Se a barra ocupar mais de ~80% da largura, coloque o rótulo dentro dela, em branco, para não vazar da tela.
- Grade e trilhos em tom muito claro. A tinta forte fica só nos dados.
- Destaque uma única barra ou coluna por gráfico (com a cor de destaque) quando ela for o ponto da frase.

## Paleta de cores

| Função | Cor | Uso |
| --- | --- | --- |
| Principal | `#2f5db8` (azul) | Série principal, barras padrão |
| Comparação / destaque | `#9b7bd4` (lilás) | Segunda série, valor de referência ou o ponto destacado |
| Terceira categoria | `#5b4a9e` (violeta escuro) | Só quando houver três categorias com valor |
| Títulos e números grandes | `#1f3f86` (azul escuro) | `h1`, `h2`, KPIs |
| Fundo da página | `#f7f6fc` | Lavanda quase branco |
| Cartões | `#ffffff` | Seções |
| Trilho / grade | `#ecebf5` | Fundo das barras |
| Fundos suaves | `#e3ebfa` (azul claro), `#e9e1f8` (lilás claro) | Selos, marcações de texto |
| Neutro | `#c9cbdc` | "Sem informação", "Outros" |
| Texto | `#1c1f3a` / secundário `#4d5275` / mudo `#6d7194` | Nunca use a cor da série para o texto |

- Defina as cores como variáveis CSS em `:root` e use só as variáveis.
- O par azul + lilás foi validado para daltonismo (protanopia ΔE ≈ 12) e contraste ≥ 3:1 sobre fundo claro. Se mudar os tons, valide de novo.
- A cor segue a entidade, nunca a posição: se o azul é "grupo A" num gráfico, é "grupo A" em todos.
- A cor nunca é o único código: sempre há legenda ou rótulo direto.
- Não use vermelho e verde. Eles soam como "bom/ruim" e não fazem parte da paleta.

## Tipografia e layout

- Fonte do sistema (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`). Nenhuma fonte externa obrigatória.
- Corpo com 17 px e altura de linha 1,55. `h1` entre 30 e 50 px (`clamp`). `h2` entre 21 e 27 px. Notas com 13 a 14 px.
- Números com `font-variant-numeric: tabular-nums`.
- Coluna central com até ~1040 px, margem lateral de 16 px e cartões com raio de 14 a 16 px e borda de 1 px.
- Abaixo de 720 px: tudo em uma coluna, rótulos acima das barras e nenhuma rolagem horizontal.

## Interação e acessibilidade

- Dica (tooltip) ao passar o mouse em cada barra, coluna ou unidade, com o valor exato.
- Botões de alternância com `aria-pressed`. Seletores com `<label>`. Foco visível (contorno lilás de 3 px).
- Regiões que mudam com `aria-live="polite"`. Gráficos de unidades com `role="img"` e `aria-label` descrevendo os valores.
- A história precisa funcionar **sem nenhum clique**. A interação é um bônus.
- Ofereça uma tabela com os números principais (dentro da nota de dados).
- Respeite `prefers-reduced-motion`.

## Técnica

- Um único arquivo `.html`, com CSS e JS embutidos. Bibliotecas, se houver, só por CDN. Prefira HTML/CSS puros para barras simples.
- Os dados entram **já agregados**, como objetos JS no próprio arquivo. Nunca leia arquivos locais (`fetch`, CSV).
- Gere os agregados com um script reprodutível e copie os números para o HTML. Não digite números à mão.

## Checklist final

- [ ] O `<h1>` é uma frase com a conclusão, e cada seção responde a uma pergunta.
- [ ] Há começo (padrão), meio (virada) e fim (resposta e reflexão).
- [ ] Todo número do texto confere com os dados embutidos.
- [ ] Todas as barras começam do zero, e os percentuais usam a escala de 0 a 100%.
- [ ] As cores vêm das variáveis da paleta, e nenhuma identidade depende só da cor.
- [ ] Fonte, data e limitações dos dados estão na nota de dados.
- [ ] O arquivo abre com dois cliques, sem internet, sem erros no console.
- [ ] Testado em ~1280 px e ~380 px de largura, sem rolagem horizontal.
