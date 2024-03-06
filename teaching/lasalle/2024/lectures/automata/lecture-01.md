---
section: Linguagens Formais e Autômatos
title: Apresentação da Disciplina
layout: lecture
last_occurrence: 2024-03-07
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/automata
---

## Apresentação da disciplina

1. Plano de Ensino
2. Avaliação
    * Baseada em entregas individuais
    1. Exercícios
    2. Trabalhos de implementação
    3. Provas G1 e G2
    4. Prova de substituição de grau
    5. ChatGPT e assemelhados
3. Logística da Disciplina
    * Divisão da aula
        * Solução de dúvidas, correção de exercícios (15 min)
        * Exposição de conteúdo (1h)
        * Intervalo (30 min)
        * Exposição de conteúdo / Exercícios (1h)
        * Preparação para a próxima aula (15 min)
    * Ferramentas: Computador de inteligência natural, lápis, papel e caneta
    * Outras ferramentas: Python, Git, Github
2. Dinâmica das aulas
    1. Dúvidas
    2. Exibição de conteúdo e exercícios em 2 períodos (2+2 _pomodoros_)
    3. Intervalo de 20 minutos
    4. Chamada após o intervalo
3. Apresentação do Professor
4. [Apresentação dos Alunos](https://forms.gle/JSzpZpr2krttj8Sp7) (LEX)
    1. Em qual semestre do curso você se posiciona?
    2. Por que você escolheu esse curso?
    3. Você trabalha ou trabalhou na área de TI? Qual cargo você ocupa (ou ocupou)?
    4. Quais linguagens de programação você consegue programar?
    5. O que você espera dessa disciplina?
    6. O que te atrapalha para estudar?
    7. O que tu gosta que o professor faça em aula?
    8. O que tu não gosta que o professor faça em aula?
5. Organize-se, você tem pouco tempo e muitas atividades!    
    1. Bullet Journal
    2. TODO-list
    3. Pomodoro
    4. GTD
    
* Qual é o teu objetivo?
* O que tu faz para atingir o teu objetivo?
{:class="lettered" style="font-size:150%"}

<!--
Formulário: https://forms.gle/ftfAfqGZgMHCjcNKA
-->

--------

## Autômatos, Computabilidade e Complexidade

O principal objetivo desta disciplina é explorar a questão

> Quais são as capacidades e limitações dos computadores?

Outras questões que surgem ao longo dessa disciplina são:

* Por que estudar Teoria da Computação?
* Por que são necessários formalismos matemáticos?
* Como aplicar a Teoria da Computação no dia a dia?

Durante os anos de 1930-1950, matemáticos estavam preocupados em responder a questão "o que é computável?".

Nesse período foram criadas as bases para o que hoje chamamos de Ciência da Computação. Foram estudados problemas como verificação de programas e a verificação da veracidade matemática (que não são computáveis), e foram criados modelos computacionais, como os automatos finitos e a Máquina de Turing, na tentativa de formalizar o problema.

Desde os anos 1960, o principal problema que tentamos responder é "o que é computável na prática?", onde obtemos formas de medir o tempo ou o espaço necessário para se chegar a uma solução de um problema que sabemos ser computável. Utilizando os mesmos formalismos, tentamos entender por que alguns problemas podem ser resolvidos de forma eficiente (como a ordenação de elementos) e outros são tão complexos que se tornam intratáveis (como o problema do Caixeiro Viajante).

Entender porque um problema é solucionável, e se existe uma forma eficiente de resolvê-lo é muito importante, e, até hoje, não sabemos se alguns problemas simplesmente não tem resposta, ou se não sabemos o suficiente para encontrar uma resposta.

> `"We have a very limited knowledge of computation."` (Michael Sipser, 2020)

### Teoria da Complexidade

Podemos classificar os problemas computacionais em três tipos básicos: os de fácil solução, os de difícil solução, e os insolucionáveis. Problemas como a ordenação de elementos, ou a procura de rotas entre dois pontos são fáceis de resolver. Problemas como o escalonamento com restrições são difíceis de solucionar. Alguns problemas simplesmente não podem ser resolvidos com um computador.

A Teoria da Complexidade busca resposta para uma pergunta que intriga os cientistas da computação há muito tempo, _o que faz alguns problemas computacionalmente difíceis e outros fáceis?_ Esta, ainda hoje, é uma pergunta sem resposta.

Uma aplicação muito interessantes da teoria da complexidade é a criptografia. Uma vez que na maioria dos sistemas procuramos obter formas mais rápidas de solucionar um problema, no campo da criptografia, o objetivo é encontrar um problema de difícil solução para quem não conheça a chave criptográfica, para que seja virtualmente impossível quebrar o código secreto.


### Teoria da Computabilidade

Durante a primeira metade do século XX, matemáticos com Kurt Gödel, Alan Turing e Alonzo Chuch descobriram que certos problemas básicos não podem ser resolvidos por computadores. Entre as conseqüências desse resultado estava o desenvolvimento dos modelos teóricos de computadores, que ajudariam na construção de computadores reais.

As teorias de complexidade e computabilidade estão intimamente relacionadas. Na teoria da complexidade o objetivo é classificar os problemas como fáceis e difíceis, enquanto na teoria da computabilidade, a classificação dos problemas é entre os problemas que são solucionáveis e os que não o são. A teoria da computabilidade introduz vários dos conceitos usados na teoria da complexidade.

### Teoria de Autômatos

A teoria dos autômatos no auxilia na definição de modelos matemáticos de computação. Um desses modelos, o _autômato finito_, é utilizado em processamento de textos, compiladores e projetos de hardware. Um outro modelo, a _gramática livre de contexto_ é utilizada na definição de linguagens de programação e em inteligência artificial.

A relativa simplicidade dos modelos apresentados pela teoria dos autômatos é excelente para se começar a estudar a teoria da computação. As teorias da computabilidade e da complexidade requerem uma definição precisa de um _computador_, e o teoria dos autômatos permite praticar com definições formais de computação.

## Revisão de Conteúdos

### Conjuntos

Veja a página sobre [Conjuntos](/teaching/cs/math/sets)

### Sequências e Uplas

Uma **sequência** é uma lista de objetos em uma ordem arbitrária. Em geral, descrevemos a lista entre parênteses:

$$
(73, 11, 17)
$$

Em um conjunto, a ordem e a repetição de objetos não são relevantes, mas em uma sequência sim. A lista $\(14, 93, 22\)$ não é igual a lista $\(93, 14, 22\)$, nem a lista $\(a, b, c\)$ é igual a lista $\(a, a, b, b, b, c\)$.

Como no casos dos conjuntos, sequências poder ser finitas ou infinitas. As sequências finitas são frequentemente chamadas de **uplas**. Uma sequência com $k$ elementos é uma _k-upla_, logo, a sequência $\(1, 2, 3\)$ é uma _3-upla_, e a sequência $\(a, b\)$ uma 2-upla. Uma _2-upla_ é normalmente chamada de **par*.

Sequências e conjuntos não precisam ser homogêneos, podendo conte qualquer tipo de objeto, como em

$$
\{1, 5, 8, \text{"Hello"}\}
$$

Sequências e conjuntos são objetos como qualquer outro, logo, podemos ter sequências de sequências, sequências de conjuntos, conjuntos de sequências, ou conjuntos de conjuntos (como o _conjunto das partes (powerset)_.

Note que a definição de uma sequência pode ser utilizada para demonstrar que o produto cartesiano não é uma operação comutativa ou associativa, uma vez que o resultado do produto são sequências.

### Funções e Relações

Veja a página [Funções e Relações](/teaching/cs/math/functions).

### Grafos

> Uma ótima introdução a grafos pode ser encontrada no [Cap. 09 do livro Fundamentals of Computer Science](http://infolab.stanford.edu/~ullman/focs/ch09.pdf){:target="\_blank"}

Veja a página [conceitos sobre Grafos](/teaching/cs/graphs).


### Cadeias e Linguagens

Um **alfabeto** é um conjunto não-vazio e finito de símbolos. Utilizamos as letras gregas $\Sigma$ ou $\Gamma$ para referenciar alfabetos. São exemplos de alfabetos:

$$
\begin{align}
\Sigma_1 &= \{0, 1\} \\
\Sigma_2 &= \{a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z\} \\
\Gamma &= \{1, 2, 3, x, y, z\} \\
\end{align}
$$

Uma _string_ (ou _cadeia_) _sobre um alfabeto_, é uma sequência finitas de símbolos daquele alfabeto, escritos de forma sequencial, por exemplo $0011010$ é uma cadeia sobre $\Sigma\_1$. Cadeias de símbolos são blocos básicos fundamentais em ciência da computação.

Se $w$ é uma cadeia soblre um alfabeto $\Sigma$, o **comprimento** de $w$, representado por $\|w\|$ é o número de símbolos que a cadeia contém. A cadeia de comprimento _zero_ ($\|w\| = 0)$ é chamada de **cadeia vazia** (ou **string vazia**) e é representada por $\varepsilon$. A _string vazia_ desempenha o papel do 0 em um sistema numérico.

Seja $w$ uma _string_ de comprimento $n$, sobre o alfabeto $\Sigma$, podemos escrever $w = w_1w_2w_3{\cdots}w_n$ onde $w_i \in \Sigma$. O **reverso** de $w$, representado por $w^{\mathcal{R}}$, é obtido escrevendo-se $w$ na ordem inversa, ou seja, $w^\mathcal{R} = w_{n}w_{n-1}{\cdots}w_3w_2w_1$.

Uma subcadeia $z$ é uma **subcadeeia** de $w$ se $z$ aparece consecutivamente dentro de $w$, por exemplo $cada$ é uma subcadeia de $abracadabra$, mas não é uma subcadeia de $cadeia$.

Dada uma cadeia $x$ de comprimento $m$ e uma cadeia $y$ de comprimento $n$ a **concatenação** de $x$ e $y$, escrita como $xy$, é a cadeia obtida concatenando-se $y$ ao final de $x$, com em $x_1{\cdots}x_my_1{\cdots}y_m$. Ao concatenar uma cadeia com ela mesma, podemos utilizar a notação com expoente:

$$
x^k = \overbrace{xx{\cdots}x}^{k}
$$

A **ordenação lexicográfica** de cadeias é a mesma ordenação que encontramos no dicionário. Porém, em _linguagens formais_, utilizamos uma variação da ordenação lexicográfica, onde as cadeias mais curtas sempre precedem as mais longas. Esta ordenação é conhecida por **shortlex** ou **radix**. Apesar disso, nos textos da disciplina os três termos podem ser utilizados significando o mesmo tipo de ordenação, por exemplo, a ordenação lexicográfica de todas as cadeias sobre o alfabeto $\Sigma = \{0,1\}$ é:

$$
(\varepsilon, 0, 1, 00, 01, 10, 11, 000, \dots)
$$

Uma **linguagem** é um conjunto de cadeias.


### Lógica Booleana

Veja a página sobre [lógica booleana](/teaching/cs/logic/boolean)


## Questões

1. Forneça uma descrição informal para os seguintes conjuntos:
    * $\\{1, 3, 5, 7, \dots\\}$
    * $\\{\dots, -4, -2, 0, 2, 4 \dots\\}$
    * $\\{n \| n = 2m \text{ para algum } m \text{ em } \mathbb{N} \\}$
    * $\\{n \| n = 2m \text{ para algum } m \text{ em } \mathbb{N} \text{ e } n=3k \text{ para algum } k \text{ em } \mathbb{N} \\}$
    * $\\{w \| w \text{ é uma cadeia de 0s e 1s e } w \text{ é igual a } w^\mathcal{R}\\}$
    {:class="lowerlettered"}

2. Forneça descrições formais para os seguintes conjuntos:
    * O conjunto contendo os números 1, 10 e 100.
    * O conjunto contendo todos os números inteiros que são maiores que 5.
    * O conjunto contendo todos os números naturais que são menores que 5.
    * O conjunto contendo a cadeia `ada`
    * O conjunto contendo a cadeia vazia
    * O conjunto contendo absolutamente nada.
    {:class="lowerlettered"}

3. Seja $A$ o conjunto $\{x, y, z\}$ e $B$ o conjunto $\{x, y\}$
    * $A$ é um subconjunto de $B$?
    * $B$ é um subconjunto de $A$?
    * $A \cup B =$ 
    * $A \cap B =$
    * $A \times B = $
    * Qual o _conjunto das partes_ de $A$?
    * $A \subseteq B $ ?
    * $B \subset A $ ?
    {:class="lowerlettered"}

4. Se um conjunto $A$ tem $a$ elementos e um conjunto $B$ tem $b$ elementos, quantos elementos estão em $A \times B$? Explique a sua resposta.

5. ...

## Preparação para a próxima aula

1. [Livro do Sipser](#sipser), seções [`0.3`](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862/pageid/39){:target="\_blank"} e [`0.4`](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862/pageid/43){:target="\_blank"} .
2. [Livro do Hopcroft](#hopcroft), capítulo 1.
3. Aulas 1 e 2 de [MIT 6.042j Mathematics for Computer Science 2010](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/){:target="\_blank"}
4. Aulas .... de [MIT 6.042j Mathematics for Computer Science 2019](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/course/){:target="\_blank"}

## Recursos para essa disciplina

### Bibliografia

1. SIPSER, Michael. [**Introdução a Teoria da Computação**](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862){:id="sipser" target="\_blank"}. Cengage Learning. 2015
2. HOPCROFT, John E.; ULLMAN, Jeffrey D.; MOTWANI, Rajeev. **Introdução à Teoria de Autômatos, Linguagens e Computação**{:id="hopcroft"}. Tradução da 2<sup>a</sup> Ed. Elsevier, 2002.
3. LEHMAN, Eric; LEIGHTON, F. Thomson; MAYER, Albert R. [**Mathematics for Computer Science**](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf){:target="\_blank"}. MIT. 2015
4. AHO & ULLMAN. [**Foundations of Computer Science**](http://infolab.stanford.edu/~u    llman/focs.html) - fora de catálogo.

### Recursos Online

1. [MIT 18.040j Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/){:target="\_blank"} - Michael Sipser
2. [MIT 6.042j Mathematics for Computer Science 2019](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/course/){:target="\_blank"} - _Unit 1 - Proofs_ (2019)
3. [MIT 6.042j Mathematics for Computer Science 2010](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010){:target="\_blank"} - Inclui video aulas (2010)
4. [Stanford CS154 - Introduction to the Theory of Computation 2020](https://www.youtube.com/playlist?list=PLjG2IDGftWft9Y11xC0sfgeT5jyTJqB-i){:target="\_blank"} - Omer Reingold (2020)

### Tutoriais Python

- [The Python Tutorial](https://docs.python.org/3/tutorial/){:target="\_blank"}

#### Python Behave

- [Behave official tutorial](https://behave.readthedocs.io/en/stable/tutorial.html)
- [BDD em Python com Behave](https://www.youtube.com/watch?v=BMrDPStzHcI): vídeo focado no uso de Selenium, mas é uma boa introdução ao Behave
- [Gherkin by Example - Python](https://github.com/gherkin-by-example/python-behave)
- [Não programe ao acaso]( https://www.youtube.com/watch?v=3xoAaBu8390) - Tchelinux 2021: apresentação sobre uso de Gherkin (e o behave) para a especificação de requisitos. 

### Tutoriais do Git

1. [Pro Git](https://git-scm.com/book/pt-br/v2){:target="\_blank"}: Tradução parcial do livro para português do Brasil
2. [Git - Guia prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html){:target="\_blank"}: Um guia bem direto, sem muita explicação.
3. [Github - Início Rápido](https://docs.github.com/pt/get-started/quickstart){:target="\_blank"}

### Videos

1. [Aula Inaugural dos Cursos de TI e Inovação Unilasalle 2022/2](https://www.youtube.com/watch?v=pxsdiyHgZHs){:target="\_blank"}
2. [Motivação para Estudar - Prof. Clóvis de Barros Filho](https://www.youtube.com/watch?v=TRPBY_lxJfE){:target="\_blank"}
3. [Procrastinação: sua pior inimiga](https://www.youtube.com/watch?v=q3oEyBpoq3o){:target="\_blank"} (Fredrik Reed, Tchelinux 2021)

