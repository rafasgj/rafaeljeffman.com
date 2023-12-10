---
title: Projeto e Análise de Algoritmos
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-10-06
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-analise-algoritmos
---

## Algoritmos

* Não temos uma definição formal de algortimos, porém, podemos definir algoritmos intuitivamente como uma sequência finita de passos a serem executados sobre um conjunto de dados de entrada para obter a resposta de um problema.
* **Algoritmos Iterativos** são algoritmos definidos por meio de laços de repetição (_for_, _while_)
* **Algoritmos Recursivos** são algoritmos definidos a partir de chamadas recursivas.
* A ideia básica da definição de algoritmos, utilizando os métodos apresentados aqui é decompor os problemas em subproblemas mais simples, e então combinar os subproblemas para resolver o problema original.
* Ao trazer a análise de complexidade para a fase de projeto (_design_) de algoritmos, obtemos subsídios para a criação de algoritmos mais eficientes.

## Otimização Combinatória

* Campo da otimização matemática que consiste na busca de um objeto ótimo entre um conjunto finito de objetos, onde o cojunto de soluções viáveis é discreto ou pode ser reduzido a um cojunto discreto.
* Exemplos de problemas de otimização combinatória:
    * _Travelling Salesman Problem_ (TSP)
    * _Minimum Spanning Tree_ (Árvore geradora mínima)
    * _Knapsack Problem_ (Problema da Mochila)
* Na maioria dos problemas de otimização combinatória, a busca exaustiva é intratável, e são necessários algoritmos que reduzem rápidamente o espaço de soluções viáveis, ou que realizam aproximações da solução ótima.
* Entre as principais áreas de aplicação da otimização combinatória encontram-se:
    * Logistica
    * Otimização de cadeia de suprimentos
    * Desenvolvimento de redes de aeroportos, torres celulares, depósitos de produtos
    * Escalonamento de Serviços (táxis, funcionários)
    * Determinar o caminho ótimo para entregas de pacotes
    * Redes de distribuição e coleta de fluídos


## Algoritmos Gulosos (_Greed algorithms_)

* Útil na solução de problemas de otimização combinatória, cujas soluções possam ser alcançadas por uma sequência de decisões.
* Exemplos de uso:
    * Intercalação sucessiva ótima de listas
    * Caminhos de custo mínimo em grafos direcionadas
    * Árvore Geradora Mínima em grafos não-direcionados
    * Compressão de dados (Código de Huffman)
    * Escalonamento de tarefas
* A ideia básica da estratégia gulosa é construir por etapas uma resposta ótima.
* A cada etapa, seleciona-se o melhor elemento da entrada, decide-se se ele é viável ou não, e (caso seja viável) o elemento pasa a fazer parte da resposta.
* Após uma sequência de decisões, uma solução para o problema é alcançada.
* Nenhum elemento é examinado mais de uma vez, e ou o elemento fará parte da solução ou será descartado.
* O esquema geral de um algoritmo guloso é:
    * _Inicialização_
    : prepara entrada e resposta parcial inicial
    * _Iteração_
    : seleciona e remove elemento $e$ da entrada
    : analisa elemento $e$ como parte da solução
    : inclui elemento $e$ como parte da solução ou descarta-o
    * _Finalização_
    : Recupera a resposta final a partir da(s) resposta(s) parcial(is)

### Intercalação sucessiva ótima de listas

* Dadas três listas ordenadas $\\{L_1, L_2, L_3\\}$, com comprimentos respectivos $\\{m_1, m_2, m_3\\}$, qual a ordem que as listas devem ser intercaladas para que o número de comparações seja o menor possível?
* O caso mais simples do problema é a intercalação de duas listas $\\{L_a, L_B\\}$. O tamanho da lista resultante é $m_a + m_b$, e o número máximo de comparações para a intercalação de duas listas $\\{L_a, L_b\\}$ é $m_a + m_b - 1$.
* Assumindo que três listas de tamanhos $\\{15, 10, 5\\}$, podemos intercalar as listas seguindo as ordens:
    * $L_1 \rightarrow L_2, \(L_1 + L_2\) \rightarrow L_3$
    * $L_1 \rightarrow L_3, \(L_1 + L_3\) \rightarrow L_2$
    * $L_2 \rightarrow L_3, \(L_2 + L_3\) \rightarrow L_1$
* O custo de intercalar as listas é
    * $L_1, L_2, L_3$: $(15 + 10 - 1) + (15 + 10 + 5 - 1) = 53$
    * $L_1, L_3, L_2$: $(15 + 5 - 1) + (15 + 5 + 10 - 1) = 48$
    * $L_2, L_3, L_1$: $(10 + 5 - 1) + (10 + 5 + 15 - 1) = 43$
    * Logo, nesse caso, a melhor forma de intercalar as sequências é utilizar a ordem $\\{L_3, L_2, L_1\\}$
* Algoritmo para a intercalação de listas
    * Seja $L$ o conjunto de listas ordenadas a serem intercaladas
    * Enquanto quanto $\|L\| \gt 1$
        * Escolha as duas menores listas de $L$ e remova-as de $L \; \(L \leftarrow L - \\{L', L''\\}\)$
        * $L^\* \leftarrow \text{interc}\(L', L''\)$
        * $L \leftarrow L \cup L^\*$
    * A resposta estará contida em $L$

#### Análise da complexidade

* O laço é executado $n$ vezes, sendo $n = \|L\|$
* A escolha das duas listas menores tem complexidade $O(n)$ para uma lista, ou $O(\log{n})$ para um _heap_ binário
* A intercalação das listas executa $m_a + m_b - 1$ comparações
: Como estamos interessados no pior caso (análise pessimista), assimos que todas as listas tem o mesmo tamnho $m$, e o número de operações para a intercalação é $2m - 1$
* A adição da lista ao conjunto de lista tem complexidade $O(1)$

* Com isso temos o seguinte cálculo para a complexidade de tempo:
    * **Com arrays**
    : $$
\begin{eqnarray}
    O(1) + n \cdot (O(n) + (2m - 1) + O(1)) \\
    = O(1) + O(n^2) + O(n\cdot m) + O(n)
\end{eqnarray}
$$
    : Consideramos a complexidade pessimista como $O(n^2)$ ou $O(n\cdot m)$ quando $m \gt n$
    * **Com _heap_ binario**
    : $$
\begin{eqnarray}
    O(n) + n \cdot (O(\log n) + (2m - 1) + O(1)) \\
    = O(n) + O(n\log n) + O(n \cdot m) + O(n)
\end{eqnarray}
$$
    : Consideramos a complexidade pessimista como $O(n\cdot m)$, para $m \gt \log{n}$.


### Menor caminho em um grafo direcionado a partir de uma única origem

* Dado um grafo simples ponderado direcionado $G = \(V, E\)$, com pesos positivos nas aresas, e um vértice inicial $s$, tal que $s \in V$, determine o menor caminho $s \rightarrow v$, tal que $v \in V$.
* Algoritmo
    * $\text{dist} = \\{\infty \| \|\text{dist}\| = \|V\|\\}$
    * $\text{dist}\[s\] = 0$
    * $n = \|V\|$ 
    * para k de 1 até n
        * $e \leftarrow$ vértice $v_j \| v_j \in V$, com a $\text{dist}\[j\]$ mínima
        * $V = V - \\{e\\}$
        * para cada $v_i \in V$
            * $c = \text{dist}\[j\] + \text{custo}(v_j, v_i)$
            * se $c \lt \text{dist}\[i\]$ então $\text{dist}\[i\] \rightarrow c$
    * $\text{dist}$ contém a resposta

## Programação Dinâmica (_Dynamic programming_)

* A programação dinâmica é indicada para problemas de otimização combinatória onde não parece fácil chegar diretamente a uma sequência ótima.
* Veja as [notas de aula sobre programação dinâmica](lecture-13)

## Divisão e conquista (_Divide and Conquer_)

* Método mais geral para o projeto de algoritmos, baseado na recursão
* A ideia básica é decompor o problema em subproblemas menores independentes, resolver os subproblemas, e combinar os resultados dos subproblemas para resolver o problema original.
* **Análise de Complexidade de Tempo**
    * O custo dos algoritmos desenvolvido por divisão e conquista pode ser definido pela recursão $T(n) = aT(n/b) + D(n) + C(n)$, onde $D(n)$ é o custo da subdivisão em subproblemas, $C(n)$ é o custo de combinar os subproblemas e $aT(n/b)$ é o custo de solução dos subproblema, onde $a$ é o número de subproblemas a cada divisão e $1/b$ é o tamanho do subproblema.
    * A complexidade de tempo será obtida a partir da solução da recursão $T(n)$. Veja as [notas de aula sobre recursão](lecture-06)

## Questões

1. Utilizando o método de divisão e conquista, crie algoritmos recursivos para:
    1. Busca linear
    2. Busca binária
    3. Encontrar o menor elemento

2. Utilizando o método guloso, defina um algoritmo para obter a árvore geradora mínima de um grafo $G=(V,E)$

3. Utilizando programação dinâmica, solucione o problema do [máximo _subarray_](https://en.wikipedia.org/wiki/Maximum_subarray_problem).
<div class="read_more">
    <div id="resposta_questao_3" style="display:none">
        <blockquote>
        <p>A ideia do algoritmo, utilizando a ideia de sufixos, é guardar a soma atual e a melhor soma.</p>
        <p>Dado um <em>array</em> $a[1:n]$, e dois arrays $S[0:n]$ e $B[0:n]$, onde $S[0] = B[0] = -\infty$</p>
        <ul>
        <li>$S[j] = \text{max}\{a[j], a[j] + S[j-1] \}$</li>
        <li>$B[j] = \text{max}\{B[j-1], S[j] \}$</li>
        </ul>
        <p><a href="javascript:hide_answer('questao_3')">Ocultar resposta</a></p>
        </blockquote>
    </div>
    <div id="pergunta_questao_3" style="display:none">
        <a href="javascript:show_answer('questao_3')">Ver dica de resposta</a>
    </div>
</div>
<script defer>hide_answer('questao_3')</script>

## Recursos para essa aula

### Bibliografia

* Toscani, Laira Vieira; Veloso, Paula A. S.; _Cap 5: Projeto e Análise de Algoritmos_. In.: **Complexidade de Algoritmos**. 3<sup>a</sup> Ed. Porto Alegre, Bookman, 2012.
