# TPC2: Conversor de MarkDown para HTML

## Autor
- **Nome:** Francisca Costa Cardoso
- **ID:** a112105
- **Foto:**
<img src="IMG_0331.jpeg" alt="Foto de Perfil" width="150"/>

## Resumo
O objetivo deste trabalho prático foi desenvolver em Python capaz de transformar anotações em MarkDown na sua representação equivalente em HTML, cobrindo os elementos básicos de sintaxe:
- **Cabeçalhos:** Conversão de títulos iniciados por `#`, `##`, `###` em `<h1>`, `<h2>`e `<h3>`, respetivamente.
- **Formatação de texto:** Conversão de texto a negrito (`**texto**` para `<b>texto</b>`) e em itálico (`*texto*` para `<i>texto</i>`).
- **Listas numeradas:** Identificação de sequências de itens numerados (`1. item`), agrupando-os dentro de blocos `<ol>`com elementos individuais `<li>`.
- **Hiperligações e Imagens:** Tratamento de links (`[texto](url)` para `<a href="url">texto</a>`) e de imagens (`![alt](url)` para `<img src="url" alt="alt"/>`).

## Lógica de implementação
A solução recorre ao módulo `re` do Python, aplicando substituições sequenciais por expressões regulares com regras de precedência fundamentais:
1. **Imagens antes de Links:** As imagens contêm uma sintaxe semelhante à dos links (precedida por `!`). Ao processar prioritariamente evita que sejam confundidas com links comuns.
2. **Negrito antes de Itálico:** Como ambos usam o asterisco (`*`), o negrito (`**`) é substituido em primeiro lugar para impedir que os pares de asteriscos sejam interpretados de forma errada como itálicos.
3. **Listas em duas etapas:** Primeiro, cada linha numerada é convertida na sua tag de item (`<li>...</li>`); de seguida, blocos contínuos de itens são envolvidos pela tag `<ol>...</ol>`.

## Ficheiro de Teste e Validação
Para validar o correto funcionamento do código, criei um ficheiro de teste (`exemplo.md`) que contém instâncias de todos os casos enunciados. O programa lê este ficheiro de entrada e gera automaticamente o ficheiro `resultado.html` com o código estruturado final. 

## Lista de Resultados
* [Conversor de MarkDown para HTML (conversor.py)](conversor.py)
* [Ficheiro de Teste (exemplo.md)](exemplo.md)
* [Ficheiro HTML gerado (resultado.html)](resultado.html)