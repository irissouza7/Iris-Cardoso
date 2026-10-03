## Qual história meu dashboard conta?

Quem governa os municípios brasileiros desde 2025 tem, na maioria das vezes, o mesmo rosto: homem (87%), branco (66%), com cerca de 49 anos, curso superior (60%) e, em quase metade dos casos, já era prefeito. Esse retrato é muito diferente da população que ele governa. Mas há uma virada: só 1 em cada 4 prefeitos reúne todos esses traços ao mesmo tempo, e o retrato muda bastante do Sul para o Norte e da cadeira de prefeito para a de vice.

## Contexto do projeto

- **Tema recebido:** 5. Quem governa os municípios.
- **Pergunta norteadora:** quem são, afinal, as pessoas que governam os municípios brasileiros a partir de 2025?
- **Briefing:** um portal de transparência voltado ao cidadão quer um dashboard de abertura que apresente ao público o perfil de quem foi escolhido para comandar as prefeituras. Cabe a mim escolher as características do retrato e o ângulo que o torna memorável.
- **Base:** `dados/eleitos.csv` (11.106 linhas, 72 colunas: prefeito e vice de 5.553 municípios, extração de 01/10/2026), lida junto com `dados/dicionario.md`.
- **Cuidados do dicionário aplicados:**
  - Leitura com separador `;`, vírgula decimal e UTF-8 com BOM. Códigos foram lidos como texto.
  - O retrato principal usa **só `cargo = Prefeito`** (uma pessoa por município). Os vices aparecem numa seção própria, de comparação.
  - Raça/cor e gênero são **declarações publicadas pelo TSE**, sem inferência por nome ou imagem. Os 16 prefeitos sem raça/cor informada ficam como "sem informação". Células vazias não foram tratadas como zero.
  - Reeleição é a declaração `ST_REELEICAO`, não uma auditoria do mandato anterior.
  - Ocupação "PREFEITO" indica quem já estava no cargo e não informa a formação profissional. O painel avisa isso.
  - A base mostra quem foi **eleito em 2024**, e não quem está no cargo hoje: há chapas cassadas, e 16 municípios ficaram de fora. O painel diz isso na nota de dados.
- **Referência externa:** para o "espelho" com a população, uso o IBGE, Censo 2022: mulheres = 51,5%, pretos e pardos = 55,5%, superior completo = 18,4% das pessoas com 25 anos ou mais.
- **Agregação:** os números foram calculados do CSV com um script em Python (pandas). Só os agregados (Brasil, 5 regiões, 26 UFs, faixas de idade, ocupações, funil) estão embutidos no HTML.

## Público-alvo

O cidadão comum que chega ao portal por curiosidade. Ele não conhece estatística eleitoral, não sabe o que é "turno decisivo" e decide **em poucos segundos** se continua lendo. Por isso:

- a mensagem principal precisa estar no título e nos cinco números do topo;
- a linguagem é cotidiana ("1 em cada 4", "se o Brasil tivesse só 100 prefeitos"), mas cada número é exato e tem fonte;
- o fim da página devolve a pergunta ao leitor: o que ele faz com esse retrato é decidido no voto;
- um seletor "E no seu estado?" dá ao cidadão um motivo pessoal para explorar.

## Perguntas que os dados respondem

1. **Qual é o perfil típico de quem governa?** Gênero, raça/cor, escolaridade e reeleição, num retrato de 100 figuras.
2. **Esse perfil se parece com a população?** Prefeitos comparados com o Censo 2022 (mulheres, pretos e pardos, curso superior).
3. **Quantos prefeitos reúnem todos os traços do "típico"?** Um funil: homem, depois branco, depois superior, depois casado.
4. **O retrato muda pelo território?** Percentual de prefeitos pretos ou pardos e de mulheres por região.
5. **De onde vêm e quanta experiência têm?** Idade na posse e ocupação declarada.
6. **Quem está ao lado, na vice, é diferente?** Prefeitos comparados com vices.
7. **E no meu estado?** Ficha por UF, comparada com a média do Brasil.

## Decisões de design

- **Skill seguida:** `skill.md` (`dashboard-narrativo-azul-lilas`).
- **Ângulo memorável: "100 prefeitos".** Um gráfico de unidades (waffle) com 100 figuras transforma percentuais em pessoas e funciona para quem não lê gráficos. Os botões trocam a característica sem mudar o gráfico.
- **Virada narrativa com um funil.** Depois de mostrar que cada traço é maioria, o funil mostra que a combinação completa vale só para 24%. Isso evita o estereótipo e dá à história um "meio" com tensão.
- **Barras horizontais pareadas** para comparar prefeitos com a população e prefeitos com vices: os rótulos ficam legíveis no celular e a escala é sempre de 0 a 100%, sem cortar o eixo.
- **Colunas para a idade,** porque as faixas têm ordem natural. O pico (40–49 anos) aparece em lilás.
- **Paleta azul e lilás,** a pedido. O azul (`#2f5db8`) é a série principal (prefeitos). O lilás (`#9b7bd4`) é a comparação (população ou vices) ou o destaque. O par foi validado para daltonismo (ΔE 12,4 protan) e contraste ≥ 3:1. Cinza neutro para "sem informação".
- **Títulos que são frases com a conclusão** ("Quem governa não se parece com quem é governado"), não rótulos de tema.
- **Interação mínima e útil:** dica ao passar o mouse, botões do retrato e seletor de UF. A história se entende sem clicar.
- **Acessibilidade:** a identidade nunca depende só da cor (legendas e rótulos diretos), há uma tabela com os dados por região, foco visível por teclado e `aria-live` nas partes que mudam.
- **Sem bibliotecas externas:** HTML, CSS e JavaScript puros, com fontes do sistema. O arquivo abre sem internet.
- **Responsivo:** testado em 1280 px e 380 px de largura, sem rolagem horizontal e sem erros no console.
- **Ficou de fora:** partidos (tema 3), bens declarados (a mediana é sensível a declarações incompletas e desviaria para "riqueza") e mapa municipal (pesado e pouco legível com 5.553 polígonos).

## Instruções para o Claude

- Gerar um único arquivo `dashboard.html`, autocontido, com os dados agregados embutidos. Nunca ler o CSV no navegador.
- Seguir a skill descrita em `skill.md`.
- Usar apenas `cargo = Prefeito` no retrato principal. Vices só na seção de comparação, sempre identificados.
- Escrever para o cidadão comum: frases curtas, sem jargão eleitoral, números arredondados no texto e exatos na dica e na tabela.
- Toda comparação com a população deve citar o Censo 2022 do IBGE.
- Manter visíveis os cuidados de leitura: declaração do TSE, eleitos em 2024 e não ocupantes atuais, 16 municípios fora da base.
- Conferir cada número do texto com o script de agregação antes de entregar.
