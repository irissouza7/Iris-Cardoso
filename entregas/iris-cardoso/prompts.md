# Diário de prompts

**Link compartilhado da conversa (opcional):** sessão no Claude Code (não compartilhada publicamente).

---

## Prompt 1

```
me ajude a fazer essa atividade - A escala de dashboard deve ser azul e lilaz: Storytelling de Dados · Atividade 1
[colei o enunciado completo da atividade: objetivo, base de dados, os 4 arquivos, passo a passo e critérios de avaliação]
```

**O que funcionou / o que mudei:** o Claude baixou o repositório da disciplina, leu o dicionário e os modelos e conferiu a verificação automática do PR (nome da pasta, 4 arquivos, seção obrigatória do `claude.md`, cabeçalho da `skill.md`). Mas ele não tinha como saber meu tema e pediu essa informação. Aprendi que o tema e o briefing precisam vir logo no primeiro prompt.

---

## Prompt 2

```
[anexei o PDF com o tema] esse é o meu tema
(Tema 5 – Quem governa os municípios. Pergunta norteadora: Quem são, afinal, as pessoas que
governam os municípios brasileiros a partir de 2025? Briefing: portal de transparência voltado
ao cidadão; usuário comum que decide em poucos segundos se continua; linguagem acessível sem
perder a precisão; cabe a mim escolher as características do retrato e o ângulo memorável.)
```

**O que funcionou / o que mudei:** com o briefing, o Claude calculou em Python o perfil dos prefeitos (gênero, raça/cor, escolaridade, estado civil, idade, ocupação, reeleição), por região e por UF, e comparou com os vices. A partir dos números, escolheu o ângulo "se o Brasil tivesse só 100 prefeitos" e uma virada: cada traço é maioria, mas só 24% reúnem todos. Mantive a decisão de usar só prefeitos no retrato principal e deixar os vices numa seção própria, como manda o dicionário (contar uma pessoa por município).

---

## Etapa 3: revisão feita pelo Claude dentro do Prompt 2 (sem prompt novo)

```
(Sem prompt novo: o próprio Claude testou o HTML em 1280 px e 380 px e validou a paleta
azul e lilás, que era a exigência do Prompt 1.)
```

**O que funcionou / o que mudei:** no teste com 380 px de largura, a página tinha 17 px de rolagem horizontal, porque os rótulos das barras mais longas (o funil e a ocupação "prefeito") vazavam da tela. A correção foi colocar o rótulo dentro da barra, em branco, quando ela passa de ~78% da largura. Essa regra entrou na `skill.md`. O par azul `#2f5db8` + lilás `#9b7bd4` passou no validador de daltonismo. Já o par mais claro que testei para o modo escuro falhou (ΔE 2,9), então mantive só o tema claro, com fundo lavanda.

---

## Etapa 4: ajustes finais feitos pelo Claude (sem prompt novo)

```
(Sem prompt novo: ajustes de texto feitos na revisão final, para atender às regras do enunciado.)
```

**O que funcionou / o que mudei:** a faixa do topo dizia "Portal da Transparência", o que podia parecer um órgão real. Ela passou a dizer "Retrato do poder municipal · Eleições de 2024". Na `skill.md`, tirei qualquer menção a eleições e prefeitos: os exemplos agora são genéricos ("A maioria dos clientes volta em menos de 30 dias"), e tudo o que é específico deste trabalho ficou no `claude.md`.

---

## Prompts 3 a 7: entrega no GitHub

```
vc criou essa pasta no meu github?
quero sim - faça o fork
onde eu clico em fork no repositório https://github.com/prof-danny-idp/storytelling-dados-atividade1?
pronto
a fusão do pull request não finalizou ainda [...] - me ajude
valida a entrega - foi rejeitada pois foi como rascunho
manda um commit
```

**O que funcionou / o que mudei:** o Claude não tinha permissão para fazer o fork do repositório do professor. Então eu fiz o fork, e ele enviou a pasta `entregas/iris-cardoso/` para o meu fork. Abri o PR, mas ele ficou como rascunho (draft) e foi rejeitado. Marquei como "Ready for review" e pedi um commit novo, este registro, para a verificação automática rodar de novo. Lição: o merge é do professor e não acontece sozinho, e o PR precisa ser aberto como "Create pull request", não como "Create draft pull request".
