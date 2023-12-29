[Sub - Recursão] Fractal - EXERCÍCIO SUB DO BEM

Descrição
Roberta é uma cientista que trabalha em um projeto de modelagem de terreno para criar ambientes virtuais realistas para jogos e simulações. Ela deseja gerar paisagens naturais que incluam montanhas, vales, rios e planícies de maneira realista. No entanto, a topografia natural exibe complexidade em várias escalas, e ela deseja usar fractais para representar essa complexidade.

Um fractal é uma estrutura geométrica que exibe auto-semelhança em diferentes escalas. Em outras palavras, um fractal é um objeto matemático que se repete infinitamente, de forma semelhante, independentemente de quão profundamente você o examine.

https://i.imgur.com/NIRi3cb.gif https://cdn.discordapp.com/attachments/1137902400544452628/1166807083862216865/Fractal.gif?ex=65550f47&is=65429a47&hm=3865414986d1d50661549113efd0c455bb66af79c27a84f9bc5a0198e99655cf&.gif

Apesar da aplicação, Roberta nunca realmente aplicou recursividade fractal com as próprias mãos e resolve começar com um problema mais simples. Desta forma, ela conseguirá expandir a partir dali para alcançar seu objetivo. Foi assim que ela pediu a sua ajuda para implementar essa primeira versão. Essa versão, consiste em um fractal em forma de H, cujo padrão consiste em múltiplos "Hs" menores em suas extremidades, dispostos de forma auto-semelhante em todo o padrão, criando uma imagem que se assemelha a um fractal "H" de acordo com uma profundidade. Saiba mais sobre o Fractal H

Sua tarefa é criar um programa em Python que rode uma simulação desta estrutura que leia a profundidade do fractal H e preencha uma matriz com as células "vazias" ou "preenchidas", imprimindo a matriz completa.

Atenção:
A entrada será a profundidade do fractal, ou seja, a quantidade de estruturas em forma de H a partir do caso base.

Utilize uma matriz 128x128, em que se a célula for vazia imprime o caractere ' ', e se for cheia imprime o 'H' . O fractal começa no centro da matriz. Então, cada "perna" do H ocupa 25% da área para cada direção.

O Google existe, e uma hora vocês vão chegar neste link, então já vou deixar ele aqui: Implementação do Fractal H com Turtle