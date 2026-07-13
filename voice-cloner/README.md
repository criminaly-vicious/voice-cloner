# voice-cloner

Skill para Claude Code que clona a voz escrita de qualquer pessoa ou marca a partir de amostras reais, e devolve uma skill de voz reutilizável no formato `<nome>-voice/SKILL.md`.

O arquivo gerado funciona em três lugares sem adaptação, sendo eles skill do Claude Code, custom instruction do ChatGPT e system prompt de qualquer API.

Esta skill trabalha com voz escrita, ou seja, idioleto e tom de voz textual. Ela não faz clonagem de áudio.

## O problema que ela resolve

Pedir para uma IA "escrever como fulano" com duas amostras produz paródia ou texto genérico. O modelo preenche a lacuna com o default dele, que é aquele português simpático, vazio e cheio de "espero ter ajudado".

O voice-cloner impõe um processo de três fases que não pode ser pulado. Primeiro coleta com amostras rotuladas e separação entre fala e escrita. Depois análise com evidência citada e perguntas de calibração. Por último geração, só após validação humana.

## Instalação

Skill pessoal, disponível em todos os projetos:

```bash
git clone https://github.com/SEU-USUARIO/voice-cloner.git ~/.claude/skills/voice-cloner
```

Skill de projeto, versionada junto com o repositório do time:

```bash
git clone https://github.com/SEU-USUARIO/voice-cloner.git .claude/skills/voice-cloner
```

Reinicie o Claude Code depois de instalar. A skill ativa sozinha quando você pede algo como "clona a voz do meu cliente", "extrai o tom de voz dessa marca" ou "cria um guia de estilo a partir desses textos".

## Uso

Basta pedir em linguagem natural e mandar o material:

```
Clona a voz da minha marca. Vou te mandar o site, três e-mails de campanha e o guia de tom que a agência entregou ano passado.
```

A skill vai pedir o que falta, entregar um relatório de voz com evidência citada, fazer as perguntas de calibração e só então gerar o `SKILL.md` final.

Depois de gerar, valide a estrutura:

```bash
python3 scripts/validar_skill.py caminho/para/nome-voice/SKILL.md
```

O validador não julga se a voz ficou boa, porque isso só o dono da voz consegue julgar. Ele impede que o arquivo saia quebrado, sem seção obrigatória, com placeholder esquecido ou com antipadrão de IA vazado para dentro do documento.

O teste que importa é o teste cego, descrito no `SKILL.md`, em que a pessoa dona da voz recebe um texto gerado e um texto real dela sem saber qual é qual. Se ela acerta de primeira, a skill não está pronta.

## Sem Claude Code

Copie o conteúdo de [prompt-standalone.md](prompt-standalone.md) e cole no Claude, ChatGPT ou Gemini. O processo em três fases roda inteiro dentro do chat.

## Estrutura

```
voice-cloner/
├── SKILL.md                          Instruções principais, as três fases
├── prompt-standalone.md              Versão portátil para qualquer IA
├── references/
│   ├── protocolo-de-extracao.md      As seis dimensões de análise
│   ├── marca-vs-pessoa.md            O que muda quando a voz é de uma marca
│   └── antipadroes.md                Modos de falha e sinais típicos de texto de IA
├── templates/
│   ├── TEMPLATE-voice-skill.md       Esqueleto do documento gerado
│   └── formulario-de-coleta.md       O que pedir antes de começar
├── examples/
│   └── trilha-voice.md               Exemplo completo, marca fictícia, passa no validador
└── scripts/
    └── validar_skill.py              Validador estrutural, sem dependências externas
```

## Requisitos

Python 3.8 ou superior para rodar o validador. Nenhuma biblioteca externa é necessária.

## Consentimento

Voz é ativo de identidade. Use apenas com material que você tem direito de usar, seja porque a voz é sua, seja porque é de cliente ou empregadora sua. A skill recusa pedidos cujo objetivo seja falsa autoria ou se passar por terceiro.

## Licença

MIT. Veja [LICENSE](LICENSE).
