---
title: _Hashing_ e Tabelas _Hash_ (_Hashtables_)
section: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-09-18
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023/analise-algoritmos
  link: /teaching/lasalle/2023/analise-algoritmos
---

## Assunto

1. Direct Access Array
    * Armazena um item de chave $k$ no índice $k$ do array.
    * Se o tamanho da maior chave, $u$, satifizer a restricão $u \le 2^{w}$, onde $w$ é o tamanho em bits da palavra da máquina, a complexidade de tempo de acesso, inserção, e exclusão $\Theta(1)$.
    * Complexidade de expaço $\Omega(k)$, para $k \gg n$

2. _Hashtables_
    * Objetivo é armazenar $m$ chaves, onde $m = \Theta(n)$, de um universo de chaves $\mathcal{U}$ tal que $\|\mathcal{U}\| \gg m$.
    * Utilizamos uma relação $h :\mathcal{U} \rightarrow \\{0, 1, \dots, m-1\\}$
    * Exemplos de aplicação:
        : Dicionários em Python
        : Compiladores e Interpretadores (tabela de símbolos)
        : Rede (mapeamento IP$\rightarrow$host)
        : Procura de substring
        : Sincronização de arquivos
    * Problemas:
        1. Chaves não são inteiros não-negativos
        2. _Birthday Problem_
            : Em um grupo de **366** pessoas, a probabilidade de duas pessoas nascerem no mesmo dia é **1.0**.
            : Dado que $u \gg m$, haverá uma ocorrência onde $h(a) = h(b)$, para $a \neq b$, causando uma colisão de chaves.
    * _Prehash_
        : Uma função $h(k): \mathbb{K} \rightarrow \mathbb{N}$
    * _Closed Addressing_ (_Chaining_)
        * Quando $h(a) = h(b)$, ou seja, ocorre uma colisão de chaves.
        * A entrada $m[h(k)]$ da tabela armazena uma lista encadeada de valores, ao invés de um único valor.
    * Assumindo que $h(k)$ resulta em uma distribuição uniforme, independente de $h(k_{i})$.
        : O tamanho esperados das listas é $\alpha = \frac{n}{m}$ (_fator de carga_)
        : Logo, o tamanho das lista é $\Theta(1)$ se $m = \Theta(n)$.
        : A complexidade de tempo é $O(1 + \| \alpha \|)$
    * Funções _Hash_
        1. Método da Divisão: $h(k) = k\mod{m}$
        : Só é boa se $m$ é primo e não está próximo a $2^x$ ou $10^x$.
        2. Método da Multiplicação: $h(k) = [(ak)\mod{2^{w}}] \gg (w-r)$
        : funciona bem quando $a$ é ímpar e fica próximo do meio entre $2^{r-1}$ e $2^{r}$
        : $w$ é o tamanho da palavra da máquina (ex.: 64-bits)
        : $r$ é o número de bits, tal que $m = 2^{r}$
        3. Universal hashing: $h(k) = [(ak+b) \mod p] \mod m$
        : $a$ e $b$ são números randômicos no conjunto $\\{0, 1, \dots, p-1\\}$
        : $p$ é um número prime tal que $p \gt \|\mathcal{U}\|$
        : No pior caso, $k_1 \neq k_2$ com $P_{a,b}\\{h(k_1) = h(k_2)\\} = \frac{1}{m}$
    * _Open Addressing_
        * A função hash é dada por $h(k, p): \mathcal{K} \times \mathbb{N} \rightarrow \mathbb{N}$
        * Se $p = {0, 1, \dots, p}$, o custo para encontrar uma entrada vaga na tabela é $O(p) = O(n)$, no pior caso.
        * A probabilidade de encontrar uma entrada vaga na tabela é inversamente proporcional a $\alpha$ (_fator de carga_)
        * Linear probing: $h(k, p) = (h\prime(k) + p) \mod m$
        * Quadratic probing: $h(k, p) = (h\prime(k) + p + p^2) \mod m$
        * Double hashing: $h(k, p) = (h_1(k) + ph_2(k)) mod m
            : $h_2(k)$ e $m$ devem ser _primos relativos_
            : $m = 2^r$ e $h_2(k)$ é impar para todo $k$.
    * _Cukoo Hashing_
        * Utiliza $i$ funções _hash_, e cada uma se refere a uma tabela de tamanho $\frac{m}{i}$.
        * Sempre que há uma colisão na tabela $j$, o elemento é inserido nessa tabela $j$ e o elemento existente na tabela $j$ inserido na tabel $(j + 1) \mod i$.
        * Caso haja um ciclo na inserção a tabela precisa ser aumentada (_rehash_)
        * Como um ciclo pode se revelar em $O(n)$, é comum as implementações utilizarem um número máximo de tentativas de inserção de $O(\log{n})$ e se não for possível a inserção assumir a existência de um ciclo.
        * Quando maior o tamanho da tabela maior o número de evento _chache miss_.
        * Tem excelente resultado para tabelas de tamanho médio/grande com 3 chaves e $\alpha \approx 0.9$.
        * Complexidade de Tempo:
            * Busca: $O(1)$
            * Inserção: $O(1)$ amortizada
    * _Robin Hood Hashing_
        * Move os elementos de forma semelhante ao _linear probing_, porém só move o elemento atual se a distância dele para a posição original (PSL - _probe sequence length_) for menor do que a do elemento na tabela.
        * Trabalha de forma muito melhor com _cache_ do que _Cukoo Hashing_.
        * Tem bom resultado com tabelas onde $\alpha \approx 0.9$.
* Complexidade de Tempo para operações em tabelas _hash_
    * Expectativa de O(1) para inserção e busca.
    * Expectativa de O(1) para exclusão, porém pode ser necessário utilizar exclusão lógica.
    * Operações como `min`, `max`, `previous` e `next` tem $O(n)$
     

## Questões

1. **Projeto**: Implemente uma tabela hash utilizando:
    * Cukoo Hashing
    * Robin Hood Hashing

## Recursos para essa aula

* [Hashtable](https://en.wikipedia.org/wiki/Hash_table)
* [An Overview of Cukoo Hashing](https://cs.stanford.edu/~rishig/courses/ref/l13a.pdf)
* [Robin Hood Hashing](https://programming.guide/robin-hood-hashing.html)
* [A new approach to Analyzing Robin Hood Hashing](https://arxiv.org/pdf/1401.7616.pdf)
* [Cukoo Hashing](https://en.wikipedia.org/wiki/Cuckoo_hashing) (Wikipedia)
* [Hopscotch Hashing](https://en.wikipedia.org/wiki/Hopscotch_hashing) (Wikipedia
