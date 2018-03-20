# Metodos Numéricos

## Introdução

Quando estudamos calculo na universidade, vemos diversos conceitos novos e aplicáveis no dia a dia. Desde aplicações em problemas simples de física até em problemas avançados como mecânica dos fluidos.

Contudo, fazemos diversas hipóteses para resolver os problemas, tais como considerar que as funções que trabalhamos são funções compostas de funções simples ou assumir que EDOs são de coeficientes constantes e de que EDOs são lineares, o que na maioria das vezes não é verdade. Tais hipóteses frequentemente não são boas para os nossos problemas e abrimos mão de obtermos uma solução analítica(seja porque é dificil, seja porque é impossível) e aceitamos ter valores aproximados.

Para isso serve Calculo Numérico: Utilizar os conceitos aprendidos em Calculo e aplicar em algoritmos que resolvam e achem soluções para os problemas, mesmo que aproximadas. Devido aos métodos serem aplicáveis no computador, existem erros envolvidos(aproximação numérica e truncamento devido ao hardware) e quanto mais precisão ser necessária, maior o custo computacional.

Devido à necessidade de aumentar a precisão implicar em aumentar o custo computacional, melhorar os algoritmos para que não aumente tanto o custo computacional é uma boa ideia e devido a isso existe uma grande teoria matemática que envolve o Calculo Numérico. Estudando esses algoritmos e analisando os erros envolvidos é possível escolher o melhor para cada aplicação.

Os livros de Calculo Numérico normalmente apresentam os algoritmos em pseudocódigos ou em [Fortran](https://pt.wikipedia.org/wiki/Fortran): uma linguagem pouca utilizada atualmente embora seja muito eficiente para calculo numérico. Por estarmos lidando com algoritmos para fins didáticos, optou-se por uma linguagem de sintaxe simples(Fortran não é simples) e então foi escolhida a linguagem [Python](https://pt.wikipedia.org/wiki/Python) em que prioriza a legibilidade do código sobre a velocidade ou expressividade.

Visite o [wiki](https://github.com/CarlosAdir/Metodos-Numericos/wiki), pois nele estão contidos os textos para entendimento. Os outros READMEs dentro de cada pasta explicam apenas a organização das pastas e informam pouco sobre os algoritmos.

## Objetivo

Implementar algoritmos de Calculo Numérico em Python e criar tutoriais de como utilizar os algoritmos implementados([veja o wiki](https://github.com/CarlosAdir/Metodos-Numericos/wiki)). Isso somente para fins didáticos.

## Organização

A organização desse repositório segue uma ordem indicada pelo livro Análise Numérica de Richard L. Burden e J. Douglas Faires. Seguindo a mesma ordem dos capitulos:

#### [Metodos Numéricos](https://github.com/CarlosAdir/Metodos-Numericos/wiki)

1. [ ] Preliminares matemática e análises de erros
2. [X] [Soluções de equações em uma variável](https://github.com/CarlosAdir/Metodos-Numericos/wiki/2:Solucoes-de-equacoes-uma-variavel)
3. [X] [Interpolação e aproximação polinomial](https://github.com/CarlosAdir/Metodos-Numericos/wiki/3:Interpolacao-e-aproximacao-polinomial)
4. [X] [Derivadas Numéricas e Integração](https://github.com/CarlosAdir/Metodos-Numericos/wiki/4:Derivadas-Numéricas-e-Integracao)
5. [X] [Equações diferenciais ordinárias de valor inicial](https://github.com/CarlosAdir/Metodos-Numericos/wiki/5:Equacoes-diferenciais-ordinarias-de-valor-inicial)
6. [ ] [Métodos diretos para resolver sistemas lineares](https://github.com/CarlosAdir/Metodos-Numericos/wiki/6:Metodos-diretos-para-resolver-sistemas-lineares)
7. [ ] [Técnicas Iterativas na Algebra de Matrizes](https://github.com/CarlosAdir/Metodos-Numericos/wiki/7:Tecnicas-Iterativas-na-Algebra-de-Matrizes)
8. [ ] Teoria da Aproximação
9. [ ] Aproximando autovalores
10. [ ] Soluções numéricas de sistema de equações não lineares
11. [ ] Problemas de valores de contorno para EDOs
12. [ ] Soluções numéricas para EDPs

## Como contribuir

Caso queira se tornar um colaborador ou tenha ideias, códigos, dicas de implementação, contate através do e-mail carlos.adir.leite@gmail.com para maiores informações.

## Autores

Autor | e-mail
------|-------
Carlos Adir | carlos.adir.leite@gmail.com