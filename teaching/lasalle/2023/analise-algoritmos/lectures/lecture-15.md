---
title: Computabilidade e Complexidade
section: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-11-13
keywords:
  - Teoria da Computação
  - Decidibilidade
  - Intratabilidade
  - Classes de Complexidade
  - Complexidade de Algoritmos
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023/analise-algoritmos
  link: /teaching/lasalle/2023/analise-algoritmos
---

## O Tamanho de Conjuntos Infinitos

* Georg Cantor em 1873, criou o método da diagonalização, com o objetivo de medir o tamanho de um conjunto infinito.
* Como determinar o tamanho de um conjunto infinito?
: Não precisamos determinar isso, queremos apenas determinar que um conjunto infinito é maior que o outro conjunto, também infinito.
* Dois conjuntos tem o mesmo tamanho se for possível emparelhar os elementos de um deles com os elementos do outro.
: Dessa forma, comparamos o tamanho relativo dos conjuntos, sem recorrer a contagem dos elementos.
: O mesmo princípio pode ser aplicado a conjuntos infinitos.
* Suponha que tenhamos uma função $f : A \rightarrow B$, e $f$ é uma função **um-para-um**, ou seja $f(a) \neq f(b)$.
* Uma função **sobrejetora** é uma função que atinge todos elementos do contradomínio, ou seja $\forall b \in B, \exists{a} \in A \| f(a) = b$. 
* Uma função de **correspondência** é uma função _sobrejetora_ e _um-para-um.
* Se existe uma _função de correspondência_ $A \rightarrow B$, significa que $\|A\| = \|B\|$.
* Por exemplo:
    * Dado o conjunto $\mathbb{N}$ e a função $f: \mathbb{N} \rightarrow \varepsilon, f(n) = 2n$, o tamanho de $\mathbb{N}$ e $\varepsilon$ é o mesmo.
* Um conjunto é **contável** se é finito ou se tem o mesmo tamanho de $\mathbb{N}$

### O Método da Diagonalização

* Seja $\mathbb{Q} = \\{ \frac{m}{n} \| m,n \in \mathbb{N} \\}$, o conjunto dos números racionais positivos.
* Criando uma matriz $n \times m$, onde cada elemento $M(i, j) = \frac{i}{i}$ e listando os elementos nas diagonais, obtemos uma relação entre $\mathbb{Q}$ e $\mathbb{N}$, provando que $\mathbb{Q}$ é _contável_.

### Prova que $\|\mathbb{R}\| \gt \|\mathbb{N}\|$

* O conjunto dos números reais, $\mathbb{R}$ é maior que $\mathbb{N}$ e é incontável.
: Podemos provar essa afirmação por contradição, utilizando o método da diagonalização.

1. Supomos que exista uma função de correspondência $f: \mathbb{N} \rightarrow \mathbb{R}$
2. Construa uma tabela $m \times n$ utilizando números binários.
3. Para todo o numero $s_i$ da lista de números gerados, $\\{s_1, s_2, \cdots, \s_n\\}, crie um número concatenando o _i-ésimo_ bit do $i-ésimo$ número, invertendo o _bit_.
4. O número gerado não estará lista, e como todos os números deveriam estar na lista, isso mostra que a hipótese não pode ser verdadeira.
5. Por contradição, mostramos que o conjunto $\mathbb{R}$ não é contável, e é maior que o conjunto $\mathbb{N}$.

## Decidibilidade

* Problemas de Decisão são problemas definidos por uma função $f: A \rightarrow \\{\text{yes}, \text{no}\\}.
* Todo problema de decisão pode ser visto como a aceitação ou não de uma cadeia de caracteres $w$ por uma linguagem (ou seja, pode ser reconhecida por uma Máquina de Turing).
* Nem toda a linguagem é Turing-reconhecível.
    * Prova:
        * O conjunto de todas as cadeias $\Sigma^{\*}$ é contável, para qualquer alfabeto $\Sigma$.
        : Primeiro temos as cadeias de comprimento 0, depois as de comprimento 1, depois as de comprimento 2, e assim por diante.
        * O conjunto de todas as Máquinas de Turing é contável, porque cada máquina de turing tem uma codificação em uma cadeia $\langle M \rangle$.
        : _Todo programa pode ser visto como uma string_.
        * O conjunto de todas as linguagens sobre o alfabeto $\Sigma=\\{0, 1\\}$ é _incontável_.
        * Logo, existem mais problemas de decisão do que existem Máquinas para solucioná-los.

### Problema da Parada

* Definimos uma máquina de Turing que determina se uma outra máquina de Turing irá aceitar uma entrada:

$$
A_{\text{MT}} = \{\langle M, w\rangle |  M \in \text{MT e M aceita w} \}
$$

* $A_{\text{MT}}$ define o _problema de aceitação_.
> Para provar que o problema da aceitação é indecidível, utilizamos o _problema da parada_, que será formalmente definido mais adiante.
* O problema da parada é indecidível
* Prova (por contradição):
    * Supomos que $A_{\text{MT}}$ seja decidível.
    * Suponha que $H$ seja um decisor para $A_{\text{MT}}$: dada uma MT $M$ e uma entrada $w$, $H$ para e aceita se $M$ aceita $w$, e $H$ para e rejeita $M$ se $M$ falhar em aceitar $w$:
$$
H(\langle M, w \rangle)
\begin{cases}
\textit{aceite} & \text{se M aceita w}\\
\textit{rejeite} & \text{se M não aceita w}\\
\end{cases}
$$

    * Agora construimos uma nova MT $D$, que utiliza $H$ como uma função e retorna o oposto do resultado de $H$, ou seja $D(\langle M \rangle) = \text{inverso}(H(M, \langle M \rangle))$:
$$
D(\langle M \rangle)
\begin{cases}
\textit{aceite} & \text{se M rejeita}\; \langle M \rangle\\
\textit{rejeite} & \text{se M aceita}\; \langle M \rangle\\
\end{cases}
$$

    * Se executarmos $D(\langle D \rangle)$ independente do que $D$ faça, ela é obrigada a fazer o contrário, o que é obviamente uma contradição.
    * Utilizado a diagonalização:
        * Criamos uma matriz $M \times \langle M \rangle$ e a cada par $(i, j) adicionamos _aceita_ caso a entrada seja aceita, e deixamos em branco caso rejeite ou entre em loop.
        * Criamos uma matriz $M \times \langle M \rangle$ com o resultado de $H(\langle M, \langle M \rangle\rangle)$
        * Adicionamos a essa matriz as entradas $D$ e $\langle D \rangle$.
        * Cada entrada na linha $D$ será o inverso dos valores na diagonal da matriz.
        * Na posição $(D, \langle D \rangle)$ não podemos definir o valor, pois ele é o inverso do próprio valor.


## Redutibilidade

* Uma **redução** é uma maneira de converter um problema em outro de forma que a solução para a segundo problema possa ser utilizada para resolver o primeiro.
* A redutibilidade não diz nada sobre a solubilidade dos problemas individuais, mas sobre a possibilidade de solução de um problema na presença da solução de outro.
* Por exemplo, o problema de medir a área de um retângulo pode ser reduzido a medir o comprimento de suas arestas.
* A redutibilidade desempenha um papel fundamental nas teorias de computabilidade e complexidade, pois ao reduzirmos um problema a outro, podemos demonstrar se é ou não solucionável, e qual a complexidade esperada.
* Definimos o problema da parada como:

$$
\text{PARA}\_{\text{MT}} = \{\langle M, w \rangle | \text{M é uma MT e M pára sobre a entrada w}\}
$$

* Prova:
    * Supondo a existência de uma MT $R$ que decide $\text{PARA}\_{\text{MT}}$, crie uma MT $S$:
        * $S =$ Sobre a entrada $\langle M, w \rangle$ (uma cotdificação de uma MT $M$ e uma cadeia $w$):
            1. Rode MT $R$ sobrea entrada $\langle M, w \rangle$
            2. Se $R$ rejeita, _rejeite_.
            3. Se $R$ aceita, simule $M$ sobre $w$ até que ela pare.
            4. Se $M$ aceitou, _aceite_, caso contrário _rejeite_. 
    * Claramente, se $R$ decide $\text{PARA}\_{\text{MT}}$, $S$ decide $A\_{\text{MT}}$, e como $A\_{\text{MT}}$ é indecidível, $\text{PARA}\_{\text{MT}}$ também deve ser indecidível.


### Classes de Complexidade

* Na teoria da computabilidade, a tese de Church-Turing implica que todos os modelos razoáveis de computação são equivalentes.
* Na teoria da complexidade, a escolha do modelo afeta a complexidade de tempo das liguagens.

* $\text{R}$
    * Conjunto de todos os problemas solucionáveis em tempo finito (todos os problemas computáveis)
    * Sabemos que $\overline{\text{R}} \gt \text{R}$
* $\text{P}$
    * Problemas solucionáveis em tempo polinomial por uma máquina de Turing determinística.
        * $n^{O(1)}$, onde $n$ é o tamanho da entrada
* $\text{EXP}$
    * Problemas solucionáveis um tempo exponencial por uma máquina de Turing determinística.
        * $2^{n^{O(1)}}$
* $\text{NP}$
    * Problemas de decisão, solucionáveis em tempo polinomial por uma máquina de Turing não-determinística
    * Toda decisão de qual caminho seguir sempre leva a _sim_.
    * Exemplos de problemas $\text{NP}$
        * Problema de satisfatibilidade booleana
        * 3-partition
        * Tetris
        * Caminho Hamiltoniano
        * Problema do Caixeiro Viajante
    * Não podemos provar, porém acredita-se que $\text{P} \ne \text{NP}$
* $\text{NP-complete}$
    * Definição
        1. É um problema de decisão
        2. A solução pode ser verificada em tempo polinomial
        3. Outros problemas em $\text{NP}$ podem ser reduzidos ao problema, em tempo polinomial.
    * Se um problema $\text{NP-complete}$ tiver um algoritmo em tempo polinomial, todos terão, e $\text{P} = \text{NP}$
    * Exemplos de problemas $\text{NP-complete}$
        * SAT
        * 3-SAT
        * 3-partition
* $\text{NP-hard}$
    * Definição
        1. $L \in \text{NP}$
        2. Para toda linguagem $L^{\prime} \in \text{NP}$, existe uma redução de tempo polinomial $L^{\prime} \rightarrow L$

## Recursos para essa aula

### Bibliografia

* Sipser, Michael. **Introdução à Teoria da Computação**. Caps. 4,5 e 7. Cengage Learning.2015.

### Recursos Online

* [Cantor's Diagonal Argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument)

