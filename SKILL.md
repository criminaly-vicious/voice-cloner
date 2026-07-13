---
name: voice-cloner
description: Extrai o idioleto de uma pessoa ou o tom de voz de uma marca a partir de amostras reais de texto, fala transcrita ou material de marca, e gera uma skill de voz reutilizável (SKILL.md) que faz qualquer IA escrever naquela voz. Use quando alguém pedir para clonar a voz, capturar o estilo de escrita, extrair tom de voz, criar uma brand voice, montar um guia de estilo a partir de exemplos, treinar a IA para escrever como fulano, ou transformar amostras de texto em prompt de estilo. Também use ao auditar ou corrigir uma skill de voz existente que está gerando texto genérico.
---

# Voice Cloner

Esta skill transforma amostras reais em uma skill de voz utilizável. O produto final é um arquivo `SKILL.md` no formato `<nome>-voice`, que funciona como skill do Claude Code, custom instruction do ChatGPT ou system prompt de qualquer API sem adaptação.

O erro clássico nesse tipo de trabalho é a IA receber duas amostras, pular direto para a geração e inventar o resto. Esta skill existe para impedir isso. O processo tem três fases obrigatórias e nenhuma delas pode ser pulada.

## Antes de tudo: consentimento e escopo

Voz é ativo de identidade. Antes de começar, confirme que a pessoa tem direito de usar aquele material, seja porque a voz é dela, seja porque é cliente ou empregadora dela. Se o pedido for imitar alguém sem relação com o solicitante para se passar por essa pessoa (fraude, falsa autoria, deepfake textual), recuse e explique o motivo em uma frase, sem sermão.

Esta skill trabalha apenas com voz escrita, ou seja, idioleto e tom de voz textual. Ela não faz clonagem de áudio.

## Fase 1: Coleta

Nunca analise antes de coletar o suficiente. Peça as amostras explicando por que cada tipo importa.

Para pessoa física, o mínimo viável é:

- Cinco amostras de texto escrito com calma no teclado, como e-mails longos, posts, documentos ou mensagens extensas, cada uma rotulada com contexto (para quem era, com qual objetivo, qual o grau de formalidade).
- Três amostras de fala, que podem ser transcrições de áudio, mensagens ditadas ou trechos de reunião, marcadas explicitamente como fala, porque fala e escrita são dois sistemas diferentes e vão ser tratados separadamente.
- Aviso explícito sobre qualquer amostra que tenha sido editada por terceiros ou escrita com ajuda de IA, porque essas contaminam o sinal e devem entrar com peso menor ou ficar de fora.

Para marca, o mínimo viável é:

- Textos publicados em pelo menos três canais diferentes, como site, e-mail, redes sociais, documentação ou proposta comercial, porque marca costuma ter registros distintos por canal.
- Qualquer guia de marca, manifesto, missão ou glossário interno já existente, mesmo que desatualizado, porque revela a intenção declarada e permite comparar com a prática real.
- Exemplos do que a marca considera fora do tom, quando existirem, já que o contraexemplo é a evidência mais barata que existe.

Se todas as amostras vierem do mesmo contexto, aponte a limitação e pergunte se há material de outros registros antes de seguir. Se a pessoa insistir em prosseguir com pouca amostra, prossiga, mas registre no documento final quais seções são hipótese e não evidência.

O formulário completo de coleta está em [templates/formulario-de-coleta.md](templates/formulario-de-coleta.md).

## Fase 2: Análise e relatório de voz

Analise as amostras nas dimensões descritas em [references/protocolo-de-extracao.md](references/protocolo-de-extracao.md), que cobre léxico, sintaxe, ritmo, pontuação, estrutura de argumento, marcadores pessoais, tom por contexto e diferenças entre fala e escrita.

O passo mais importante da análise é isolar os invariantes, ou seja, os traços que aparecem em todos os registros e em todos os canais. Invariante é o núcleo da voz e tem prioridade máxima na skill final. Traço que aparece em uma amostra só é ruído até prova em contrário.

Ao final da fase, entregue um relatório de voz com três partes:

- As descobertas, cada afirmação sustentada por um trecho real citado da amostra, porque afirmação sem evidência é invenção.
- O que você não conseguiu determinar com confiança, dito abertamente em vez de preenchido com achismo.
- De três a cinco perguntas de calibração no formato "você diria X ou Y nesta situação", usando pares de frases concretas construídas a partir das lacunas encontradas.

Só passe para a Fase 3 depois que a pessoa validar o relatório.

## Fase 3: Geração da skill de voz

Gere o documento final seguindo [templates/TEMPLATE-voice-skill.md](templates/TEMPLATE-voice-skill.md), no idioma das amostras, nunca traduzido.

As regras de qualidade do documento final são inegociáveis:

- Os exemplos calibrados valem mais que as regras, porque IA aprende voz por imitação de exemplo, não por descrição abstrata. Cada par errado versus certo deve tratar do mesmo assunto, e o lado errado deve ser um texto de IA genérico plausível, não um espantalho ridículo.
- Toda instrução deve ser operacional e positiva sempre que possível, como "abra com o contexto em uma frase", em vez de proibição vaga do tipo "não seja genérico".
- Cada regra precisa ser específica o suficiente para que duas IAs diferentes seguindo a skill produzam textos parecidos. Se a regra admite dez interpretações, ela não é uma regra.
- Nenhum traço pode entrar sem estar nas amostras ou ter sido confirmado nas perguntas de calibração. Na dúvida, deixe de fora, porque falso positivo em voz produz paródia.

Depois de gerar, rode a validação:

```bash
python3 scripts/validar_skill.py caminho/para/<nome>-voice/SKILL.md
```

O script confere frontmatter, tamanho da description, presença das seções obrigatórias e antipadrões comuns. Ele não julga se a voz ficou boa, ele só impede que o arquivo saia quebrado.

## Teste de aceitação

Uma skill de voz só está pronta quando passa neste teste. Peça um texto novo, sobre assunto que não estava nas amostras, gerado com a skill aplicada. Mostre para a pessoa dona da voz junto com um texto real dela, sem dizer qual é qual. Se ela hesitar para identificar, a skill funciona. Se ela apontar o texto gerado de primeira, volte para a Fase 2 e descubra qual traço ficou de fora.

## Casos especiais

Marca não é pessoa e o protocolo muda em pontos importantes, principalmente porque marca tem múltiplos autores, precisa de regras mais rígidas e costuma ter um tom declarado que não bate com o praticado. As diferenças estão em [references/marca-vs-pessoa.md](references/marca-vs-pessoa.md).

Os modos de falha mais comuns, como cair na média genérica de IA, confundir assinatura de estilo com muleta verbal ou copiar tema em vez de voz, estão catalogados em [references/antipadroes.md](references/antipadroes.md). Leia antes de gerar, não depois.

## Uso sem Claude Code

Quem não usa Claude Code pode colar [prompt-standalone.md](prompt-standalone.md) em qualquer IA e seguir o mesmo processo em três fases dentro do chat.
