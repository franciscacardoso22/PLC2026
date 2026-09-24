# TPC1: Expressão Regular para Cadeias Binárias sem "011"

## Autor
- **Nome:** Francisca Costa Cardoso
- **ID:** a112105
- **Foto:**
<img src="fotopgithub.jpg" alt="Foto de Perfil" width="150"/>

## Resumo
O objetivo deste trabalho prático foi definir uma expressão regular para validar palavras binárias que **não contêm** a sequência contígua "011".

Para evitar a formação de "011", a lógica foi estruturada da seguinte forma: 
- O símbolo `1`só pode aparecer de forma isolada (`1`) ou imediatamente precedido por um único zero (`01`).
- Usando a alternativa `(1|01)*`, qualquer combinação destes elementos impede que surjam dois `1`s seguidos após um zero.
- No final da palavra, podem ainda surgir qualquer quantidade de zeros através de `0*`.

## Lista de resultados
* [Expressão Regular resultante (er.txt)](er.txt)
