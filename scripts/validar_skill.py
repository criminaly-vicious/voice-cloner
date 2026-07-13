#!/usr/bin/env python3
"""
Validador de skill de voz gerada pelo voice-cloner.

Este script nao julga se a voz ficou boa, porque isso so o dono da voz consegue
julgar. Ele confere se o arquivo esta estruturalmente valido e se os antipadroes
mais comuns de texto de IA vazaram para dentro do documento.

Uso:
    python3 scripts/validar_skill.py caminho/para/SKILL.md
"""

import re
import sys

SECOES_OBRIGATORIAS = [
    "Quando usar",
    "Regras absolutas",
    "Léxico",
    "Sintaxe e ritmo",
    "Tom por registro",
    "Modo fala e modo escrita",
    "Exemplos calibrados",
    "Checklist de auto-validação",
    "Limitações conhecidas",
]

# Frases que quase nunca pertencem a uma voz humana real e denunciam default de IA.
ANTIPADROES = [
    "espero ter ajudado",
    "estou à disposição",
    "qualquer dúvida estou aqui",
    "ótima pergunta",
    "excelente pergunta",
    "vamos mergulhar",
    "vamos explorar juntos",
    "no mundo atual",
    "nos dias de hoje",
    "não é apenas",
]

PLACEHOLDERS = ["NOME", "CONTEXTO", "Texto genérico aqui", "Texto na voz real aqui"]


def ler(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def validar_frontmatter(texto, erros, avisos):
    if not texto.startswith("---\n"):
        erros.append("O arquivo nao comeca com frontmatter YAML na linha 1.")
        return

    fim = texto.find("\n---", 4)
    if fim == -1:
        erros.append("O frontmatter nao foi fechado com --- em nenhuma linha.")
        return

    bloco = texto[4:fim]

    nome = re.search(r"^name:\s*(.+)$", bloco, re.MULTILINE)
    if not nome:
        erros.append("O campo name esta ausente no frontmatter.")
    else:
        valor = nome.group(1).strip()
        if not re.fullmatch(r"[a-z0-9-]{1,64}", valor):
            erros.append(
                f"O name '{valor}' e invalido. Use apenas minusculas, numeros e hifens, com no maximo 64 caracteres."
            )
        if not valor.endswith("-voice"):
            avisos.append(
                f"O name '{valor}' nao termina em -voice, o que quebra a convencao do voice-cloner."
            )

    desc = re.search(r"^description:\s*(.+)$", bloco, re.MULTILINE | re.DOTALL)
    if not desc:
        erros.append("O campo description esta ausente no frontmatter.")
    else:
        valor = desc.group(1).strip()
        if len(valor) > 1024:
            erros.append(
                f"A description tem {len(valor)} caracteres e o limite e 1024."
            )
        if len(valor) < 80:
            avisos.append(
                "A description tem menos de 80 caracteres e provavelmente nao tem gatilhos suficientes para a skill ser encontrada."
            )


def validar_secoes(texto, erros):
    for secao in SECOES_OBRIGATORIAS:
        if not re.search(rf"^##\s+.*{re.escape(secao)}", texto, re.MULTILINE | re.IGNORECASE):
            erros.append(f"A secao obrigatoria '{secao}' esta faltando.")


def validar_exemplos(texto, erros, avisos):
    pares = len(re.findall(r"^###\s+Exemplo", texto, re.MULTILINE))
    if pares < 3:
        erros.append(
            f"Foram encontrados {pares} exemplos calibrados e o minimo exigido e 3, porque exemplo ensina voz melhor que regra."
        )
    elif pares < 5:
        avisos.append(
            f"Foram encontrados {pares} exemplos calibrados. Cinco e o ideal para cobrir registros diferentes."
        )


def _linha_e_prescritiva(linha):
    """Linha que ensina a evitar o antipadrao, ou blockquote de exemplo errado,
    nao conta como ocorrencia. Sem isso o validador acusaria a propria regra."""
    baixo = linha.strip().lower()
    if baixo.startswith(">"):
        return True
    gatilhos = ["evite", "evitar", "nunca use", "não use", "nao use", "proibid", "antipadr"]
    return any(g in baixo for g in gatilhos)


def validar_antipadroes(texto, avisos):
    for numero, linha in enumerate(texto.splitlines(), start=1):
        if _linha_e_prescritiva(linha):
            continue
        baixo = linha.lower()
        for frase in ANTIPADROES:
            if frase in baixo:
                avisos.append(
                    f"Linha {numero}: o antipadrao '{frase}' aparece no documento. Se as amostras nao provam que a voz usa isso, remova."
                )


def validar_placeholders(texto, erros):
    for marca in PLACEHOLDERS:
        if marca in texto:
            erros.append(
                f"O placeholder '{marca}' do template ficou no arquivo final e precisa ser substituido."
            )


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 scripts/validar_skill.py caminho/para/SKILL.md")
        sys.exit(2)

    caminho = sys.argv[1]
    try:
        texto = ler(caminho)
    except OSError as exc:
        print(f"Nao foi possivel ler o arquivo: {exc}")
        sys.exit(2)

    erros, avisos = [], []

    validar_frontmatter(texto, erros, avisos)
    validar_secoes(texto, erros)
    validar_exemplos(texto, erros, avisos)
    validar_antipadroes(texto, avisos)
    validar_placeholders(texto, erros)

    print(f"Validando {caminho}\n")

    if erros:
        print(f"ERROS ({len(erros)}), o arquivo nao esta pronto para uso:")
        for e in erros:
            print(f"  [x] {e}")
        print()

    if avisos:
        print(f"AVISOS ({len(avisos)}), vale revisar antes de publicar:")
        for a in avisos:
            print(f"  [!] {a}")
        print()

    if not erros and not avisos:
        print("Nenhum erro e nenhum aviso. A estrutura esta valida.")
        print("Lembre que estrutura valida nao significa voz capturada.")
        print("O teste que importa e o teste cego com o dono da voz.")
    elif not erros:
        print("Nenhum erro estrutural. Resolva os avisos se fizerem sentido.")

    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
