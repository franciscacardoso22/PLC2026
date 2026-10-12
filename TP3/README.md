# TPC3: Analisador Léxico

## Autor
- **Nome:** Francisca Costa Cardoso
- **ID:** a112105
- **Foto:**
<img src="IMG_0331.jpeg" alt="Foto de Perfil" width="150"/>

## Resumo
O objetivo deste trabalho prático foi desenvolver um analisador léxico em Python para uma linguagem de *query* específica.
O analisador converte um texto de entrada numa sequência de *tokens* válidos, ignorando espaços em branco e comentários.

Para a implementação, seguiu-se a abordagem baseada em expressões regulares com grupos nomeados (*Named Groups*), utilizando a função `re.finditer()` do módulo `re`. A ordem das expressões regulares no padrão principal foi cuidadosamente definida para garantir a precedência correta (por exemplo, palavras reservadas como `LIMIT` são capturadas antes de identificadores genéricos de conceitos).

## Lista de Resultados
* [Analisador Léxico (analisador.py)](analisador.py)
* [Ficheiro de Teste (teste.txt)](teste.txt)