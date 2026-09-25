# TPC1: Expressão Regular para Cadeias Binárias sem "011"

## Autor
- **Nome:** Francisca Costa Cardoso
- **ID:** a112105
- **Foto:**
<img src="fotopgithub.jpg" alt="Foto de Perfil" width="150"/>

## Resumo
O objetivo deste trabalho prático foi definir uma expressão regular para validar palavras binárias que **não contêm** a sequência contígua "011".

Para evitar a formação de "011", a lógica foi estruturada da seguinte forma: 
- No início da palavra pode surgir qualquer quantidade de uns através de `1*`.
- A partir do momento em que surge o primeiro zero, nunca mais podem ocorrer dois uns seguidos. Assim, cada `1` tem de ser precedido por pelo menos um zero, formando blocos do tipo `(0+1)*`.
- No final da palavra, podem ainda surgir zeros adicionais através de `0*`.

## Lista de resultados
* [Expressão Regular resultante (er.txt)](er.txt)
