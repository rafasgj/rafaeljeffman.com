---
section: Paradigmas de Programação
title: Linguagens de Programação, compiladores e interpretadores.
subtitle: Da criação à execução do programa
layout: lecture
last_occurrence: 
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/paradigmas
---

## O que vamos ver nessa disciplina?

* Diferentes formas de programar um computador
    * Linguagens Imperativa: **C** (com uma pitada de **Assembly**)
    * Programação em lógica: **Prolog**
    * Programação funcional: **Haskell**
    * Programação orientada a objetos: **Java** (com uma pitada de **Io**)
    * Programação concorrente
    * Programação multi-paradigma: **Python**
* Como nossos códigos viram programas.

## Como avaliar uma linguagem de programação?

**Não existem critérios amplamente aceitos para avaliar linguagens de programação.**

No entanto, alguns critérios acabam por se destacar ao fazer com que algumas linguagens tenham seu uso mais difundido que outras. Lembre-se que por não existir uma aceitação universal, esses critérios também são controversos, e possuem uma (forte) tendência pessoal.

### Legibilidade

Programas, em geral, não são _escritos e esquecidos_. Programas devem ser revistos, mantidos, corrigidos, e, talvez, melhorados. Em geral, no ciclo de vida de um software, o maior tempo (e custo) de um programa é o seu período de manutenção.

A legibilidade também afeta, diretamente, a facilidade de se desenvolver um código com uma equipe.

* Simplicidade
    : Uma linguagem com poucas construções básicas é mais fácil de aprender e facilita a leitura do código.
    : A existência de diversas formas de executar uma mesma tarefa pode levar a códigos de difícil compreensão. Veja o exemplo da linguagem **C++**:
        ```cpp
        count = count + 1;
        count += 1;
        count++;
        ++count;
        ```
    : A linguagem **Perl** é conhecida por ser uma linguagem de difícil compreensão, dadas as diversas formas de executar uma mesma tarefa.
    : A linguagem **Python**, por outro lado, é conhecida por procurar apresentar um única forma para definir uma tarefa, e é, normalmente, considerada uma linguagem com alta legibilidade.
* Ortogonalidade
    : A ortogonalidade em uma linguagem de programação significa que um pequeno conjunto de construções primitivas pode ser combinado de a número relativamente pequeno de formas para construir as estruturas de controle e de dados da linguagem.
    : A ortogonalidade está intimamente relacionada à simplicidade, pois quanto mais ortogonal for o projeto de uma linguagem, menor é o número necessários de exceções às regras da linguagem.
    : Por exemplo, na linguagem **C**, o que significa `a + b` ?
    : Excesso de ortogonalidade também pode tornar uma linguagem mais complexa. As linguagens **ALGOL 68** e **Perl** são conhecidas por extrapolarem na ortogonalidade.
    : Linguagens funcionais são, em geral, mais simples, porque realizam tudo com uma única construção, uma chamada de função. No entanto, outros fatores como a eficiência, podem comprometer o uso dessas linguagens.
* Tipos de Dados
    : A capacidade de definir tipos de dados de usuário também auxilia a legibilidade.
    : Compare os dois códigos a seguir (**C** e **Python**):
        ```c
        int process_user_option(int option);

        int flag = 0;
        while (flag != 9999) {
            display_menu();
            flag = process_user_option(
                get_user_option()
            );
        }
        ```
        ```python
        def process_user_option(option : int) -> bool :
            """Processa opção do usuário."""


        running : bool = True
        while running:
            display_menu();
            running = process_user_option(
                get_user_option()
            )
        ```
* Sintaxe
    * A sintaxe, definida pela gramática da linguagem, tem um efeito muito forte na legibilidade de programas.
    * O uso de _palavras especiais_, ou seja, identificadores com comportamentos associados, e o método para formar sentenças compostas ou grupos de sentenças é especialmente importante em construções de controle.
        : LISP
            ```lisp
        (if 'x < 0 (when_true x) (when_false x))
        ```
        : Python
            ```python
        if x == 0:
            print("x é 0")
        elif x < 0:
            print("x é menor que zero")
        else:
            print("x é maior que zero")
        ```
        : Swift
            ```swift
        switch x {
            case 0:
                print("x é 0")
            case _ where x < 0: 
                print("x é menor que zero")
            case _ where x > 0: 
                print("x é menor que zero")
        }
        ```
    * Forma e significado
        : É importante que as sentenças indiquem, ao menos parcialmente, o significado da expressão.
        : Construções idênticas ou semelhantes, mas com significados diferentes, podem comprometer a legibilidade (por exemplo, os usos de `static` na linguagem **C**.

### Facilidade de escrita

* Domínio da Aplicação
    : A facilidade de escrita de uma linguagem deve ser avaliada em relação ao domínio ao qual a linguagem se aplica.

* Simplicidade e ortogonalidade
    : Uma linguagem com muitas construções diferentes levará os programadores a escolherem quais construções utilizar, fazendo com que alguns recursos mais eficientes ou elegantes não sejam utilizados quando deveriam.
    : Em geral, é melhor uma linguagem de programação com menos construções e um conjunto consistente de regras para combiná-las (ortogonalidade).
    : Por outro lado, permitir qualquer combinação das primitivas dificulta a escrita de códigos corretos, pois fica mais difícil para o compilador detectar erros.

* Expressividade
    : Para linguagens de programação, a expressividade está relacionada a quão conveniente é especificar computações nessa linguagem.
    : APL é uma linguagem que possui um grande número de operadores e é possível definir muitas computações com um programa bem pequeno. No entanto, o grande número de operadores acaba por dificultar a escrita de programas, pois nem todos os símbolos serão diretamente acessíveis em um teclado convencional.

### Confiabilidade

Um programa é confiável na medida que executa de acordo com a sua especificação, em todas as condições.

A facilidade de escrita e leitura de uma linguagem impacta diretamente na confiabilidade, pois permite que seja mais fácil traduzir conceitos, talvez escritos em linguagem natural, para a linguagem de programação.

Outro aspecto que ajuda na confiabilidade é a capacidade do compilador de encontrar erros no processo de tradução do código fonte para o código alvo. Por exemplo, erros de acesso a memória (como em **Rust**) ou erros de gerenciamento de recursos. 

Linguagens com **tipagem forte** e **verificação de tipos** permitem uma série de análises do código durante o processo de compilação reduzindo os erros em tempo de execução. É muito mais barato corrigir problemas de compilação do que problemas de execução de um programa.

### Custo

* Custo de treinamento
* Custo de desenvolvimento
* Custo de manutenção
* Custo de execução
* Portabilidade
* Custo das ferramentas de desenvolvimento
* Produtividade

# Compilação, Interpretação e Bytecode

* Compilação
    : Processo que transforma o código fonte em código executável.
* Interpretação
    : Processo que transforma apenas a parte necessária do código fonte em código executável, e executa o trecho avaliado.
* Bytecode
    : O código fonte é compilado em um formato intermediário, e este formato intermediário é então interpretado por uma máquina virtual.


# Etapas de um compilador/interpretador

![Processo de compilação](/images/compiler_sebesta.png)


## Sintaxe e Semântica

Uma linguagem, natural ou artificial, possui um conjunto de palavras que são formadas utilizando um alfabeto específico.
**Lexemas** (ou **tokens**) são descrições de cada uma das palavras ou símbolos dessa linguagem, que carregam informações sobre a palavra em si.

**Sentenças** na linguagem são formadas por conjuntos de palavras da linguagem. A **sintaxe** da linguagem estabele regras de como as palavras podem ser organizadas para criar uma sentença válida na linguagem.
O conjunto de regras que descreve a sintaxe de uma linguagem é chamado de **gramática**.

A **semântica** de uma linguagem nos permite entender o signifcado de sentenças da linguagem, analisadas de acordo com a sua gramática.

## Questões

1. Cite alguns dos recursos de linguagens de programação específicas que você conhece, cujo objetivo seja um mistério para você.
2. Por que jamais teremos "a linguagem de programação definitiva"?
3. Quais são os elementos que você gostaria que existisse em uma linguagem de programação?
4. Quais elementos você acredita que atrapalham mais do que ajudam em uma linguagem de programação?
5. Em quantas linguagens de programação você consegue programar? Elas são realmente diferentes?
6. Qual é a próxima linguagem de programação que você deseja aprender?

## Para a próxima aula

* [Tutorial sobre a linguagem C](https://www.freecodecamp.org/portuguese/news/o-manual-do-iniciante-em-c-aprenda-o-basico-sobre-a-linguagem-de-programacao-c-em-apenas-algumas-horas/)
* Algum dos tutorias de Git da [Aula 1](lecture-01).

## Recursos para essa aula

### Bibliografia

1. "SEBESTA, Robert. [**Conceitos de Linguagens de Programação**](https://integrada.minhabiblioteca.com.br/reader/books    /9788582604694/){:target='_blank'}. 11<sup>a</sup>. Ed. Bookman.Porto Alegre, 2018.
    * Capítulos 1 a 3

