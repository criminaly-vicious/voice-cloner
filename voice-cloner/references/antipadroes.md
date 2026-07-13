# Antipadrões

Catálogo dos modos de falha que aparecem toda vez que alguém tenta clonar uma voz sem método. Leia antes de gerar, porque depois de gerado o texto parece bom para quem escreveu e ruim para quem é dono da voz.

## Falha 1: cair na média genérica

O sintoma é um texto que soa competente, simpático e absolutamente vazio, com abertura do tipo "no mundo atual, cada vez mais" e fechamento do tipo "espero que isso ajude". Acontece quando a análise foi rasa e o modelo caiu no default dele por falta de instrução específica.

A correção é aumentar a especificidade das regras e a qualidade dos exemplos calibrados. Regra genérica produz texto genérico, sempre.

## Falha 2: copiar tema em vez de voz

O sintoma é a skill só conseguir escrever bem sobre os assuntos que estavam nas amostras, e desmontar quando o tema muda. Acontece quando o vocabulário temático foi confundido com vocabulário de voz.

A correção é testar sempre com um assunto que não estava nas amostras. Se a voz não sobrevive à troca de tema, ela não foi capturada.

## Falha 3: paródia por excesso de traço

O sintoma é um texto que empilha todas as muletas verbais da pessoa em cada parágrafo, virando caricatura. Acontece quando o traço foi anotado sem frequência, ou seja, sem registrar de quantas em quantas frases ele realmente aparece.

A correção é quantificar. Se a pessoa usa "no fim das contas" uma vez a cada três textos, a skill precisa dizer isso, e não apenas listar a expressão como característica.

## Falha 4: limpar a fala

O sintoma é uma skill de voz falada que produz um texto impecável e morto. Acontece quando as hesitações, repetições e frases inacabadas foram tratadas como erro a corrigir em vez de dado a preservar.

A correção é manter os dois modos separados no documento final, com instrução explícita de quando cada um se aplica.

## Falha 5: confundir voz com formatação

O sintoma é uma skill que só fala de bullets, headers e negrito, e não diz nada sobre como a pessoa pensa e argumenta. Formatação faz parte da voz, mas é a camada mais superficial dela.

A correção é garantir que o documento final tenha regras sobre estrutura de argumento, tratamento de discordância e forma de nomear tensão, não só sobre marcação de texto.

## Falha 6: inventar o que faltou

O sintoma é uma skill cheia de afirmações confiantes sobre traços que não têm nenhuma evidência nas amostras. Acontece porque o modelo tem forte tendência a preencher lacuna em vez de admitir lacuna.

A correção é a regra dura do protocolo, que é não colocar no documento nada que não esteja citado nas amostras ou confirmado nas perguntas de calibração.

## Falha 7: validar com quem não é dono da voz

O sintoma é uma skill aprovada por todo mundo, menos pela pessoa que ela deveria imitar. Acontece quando o teste de aceitação foi feito com terceiros que não têm intimidade com a voz.

A correção é o teste cego com o próprio dono da voz, comparando texto gerado com texto real sem identificar qual é qual.

## Sinais típicos de texto de IA que quase nunca pertencem a uma voz real

Use esta lista como filtro final antes de entregar qualquer texto gerado pela skill, salvo se as amostras provarem que a pessoa realmente escreve assim.

- Abertura com concordância vazia do tipo "ótima pergunta" ou "excelente ponto", que existe para agradar e não para informar.
- Tricolon decorativo, isto é, a mania de listar três adjetivos onde um bastava, como "claro, conciso e eficaz".
- Estrutura de contraste automática do tipo "não é apenas X, é Y", que soa a slogan e aparece com frequência sobrenatural em texto de modelo.
- Fechamento do tipo "espero ter ajudado" ou "estou à disposição", que ninguém escreve espontaneamente em conversa real.
- Hedging empilhado, como "talvez seja possível considerar que", que dilui a afirmação até ela não dizer nada.
- Emoji usado como pontuação estrutural quando nenhuma amostra tinha emoji.
