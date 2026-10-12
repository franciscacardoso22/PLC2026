import sys 
import re

def tokenize(texto):
    reconhecidos = []
    linha = 1

    padrao = r'(?P<COMENTARIO>#.*)|(?P<LIMIT>\bLIMIT\b)|(?P<RESERVADA>\b(?:select|where)\b)|(?P<VARIAVEL>\?\w+)|(?P<LINGUA>@[a-zA-Z]{2})|(?P<STRING>"[^"]*")|(?P<NUMERO>\d+)|(?P<DELIMITADOR>[{}.])|(?P<CONCEITO>[a-zA-Z0-9]+:[a-zA-Z0-9]+|[a-zA-Z0-9]+)|(?P<SKIP>[ \t]+)|(?P<NEWLINE>\n)|(?P<ERRO>.)'

    mo = re.finditer(padrao, texto)

    for m in mo:
        dic = m.groupdict()

        if dic['COMENTARIO']:
            t = ("COMENTARIO", dic['COMENTARIO'], linha, m.span())
        
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())

        elif dic['RESERVADA']:
            t = ("RESERVADA", dic['RESERVADA'], linha, m.span())

        elif dic['VARIAVEL']:
            t = ("VARIAVEL", dic['VARIAVEL'], linha, m.span())

        elif dic['LINGUA']:
            t = ("LINGUA", dic['LINGUA'], linha, m.span())

        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())

        elif dic['NUMERO']:
            t = ("NUMERO", dic['NUMERO'], linha, m.span())

        elif dic['DELIMITADOR']:
            t = ("DELIMITADOR", dic['DELIMITADOR'], linha, m.span())

        elif dic['CONCEITO']:
            t = ("CONCEITO", dic['CONCEITO'], linha, m.span())

        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())

        elif dic['NEWLINE']:
            linha += 1
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())

        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())

        else:
            t = ("UNKNOWN", m.group(), linha, m.span())

        if not dic['SKIP'] and not dic['NEWLINE'] and not dic['COMENTARIO'] and t[0] != 'UNKNOWN':
            reconhecidos.append(t)
    
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)