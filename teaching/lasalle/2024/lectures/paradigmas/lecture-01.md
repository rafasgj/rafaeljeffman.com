---
section: Paradigmas de Programação
title: Apresentação da Disciplina
subtitle:
layout: lecture
last_occurrence: 
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/paradigmas
extra_styles:
  - lecture
---

## Agenda

1. Plano de Ensino (previsão)
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
    2. Exibição de contúdo e exercícios em 2 períodos (2+2 _pomodoros_)
    3. Intervalo de 20 minutos
    4. Chamada após o intervalo
3. Apresentação do Professor
4. [Apresentação dos Alunos](https://forms.gle/ui9Rey6wRE72gx1L9){:target="\_blank"}(LEX)
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

## Paradigmas de Linguagens de Programação

* Por que estudar diferentes linguagens de programação?
    > `Se tudo que tu tem é um martelo,`
    > `todos os teus problemas são pregos.`
    * Acredita-se que a capacidade de raciocínio das pessoas é influenciada pelo poder de expressão da linguagem que utilizam para comunicar seus pensamentos.
    * O uso de abordagens diferentes para um mesmo problema pode trazer soluções melhores.
    * Quanto mais linguagens você conhece, mais fácil é aprender uma nova.
    * Melhor uso de linguagens já conhecidas
    * Avanço do processo de desenvolvimento de software
* Por que criar novas linguagens de programação?
    * Para resolver problemas específicos
    * Para atender domínicos específicos
* Domínios de Programação
    * Aplicações Científicas
        * Fortran
    * Aplicações Comerciais
        * COBOL
    * Aplicaçẽos de Infraestrutura
        * Ansible, Puppet, Chef, Terraform
    * Inteligência Artificial
        * LISP, Prolog
    * Sistemas Distribuídos
        * Erlang

## Revisão de Conteúdos

* Computadores de uso único
* Arquitetura de Computadores
    * Computadores de programas armazenados
    * Modelo de von Neumann
![Arquitetura de von Neumann](/images/vonneumann.png)
    * Processo de execução de uma instrução
* O que significa executar um programa num computador?
* Evolução das linguagens de programação
    * Código de máquina
    * Assembladores
    * FORTRAN
    * PL/1
    * ALGOL
    * COBOL
    * BASIC
    * Simula
    * LISP
    * PROLOG
    * Prolog
    * ADA
    * Smalltalk
    * C
    * Java
    * Python
    * Javascript
    * Rust
* Tipos de Dados
    * Representação de um valor
    * Operações sobre valores
* Estruturas de Dados
    * Vetores
    * Listas encadeadas
    * Árvores
    * Tabelas de Espalhamento
    * Grafos

## Como avaliar uma linguagem de programação?

**Não existem critérios amplamente aceitos para avaliar liguagens de programação.**

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
    : A linguagem **Python**, por outro lado, é conhecida por procurar apresentar um única forma para definir uma tarefa, e é, normalmente, considerada uma linguagem com alta legibilidada.
* Ortogonalidade
    : A ortogonalidade em uma linguagem de programação significa que um pequeno conjunto de construções primitivas pode ser combinado de a número relativamente pequeno de formas para construir as estruturas de controle e de dados da linguagem.
    : A ortogonalidade está intimamente relacionada à simplicidade, pois quanto mais ortogonal for o projeto de uma linguagem, menor é o número necessários de excessões às regras da linguagem.
    : Por exemplo, na linguagem **C**, o que significa `a + b` ?
    : Excesso de ortogonalidade também pode tornar uma liguagem mais complexa. As linguagens **ALGOL 68** e **Perl** são conhecidas por extrapolarem na ortogonalidade.
    : Liguagens funcionais são, em geral, mais simples, porque realizam tudo com uma única construção, uma chamada de função. No entanto, outros fatores como a eficiência, podem comprometer o uso dessas linguagens.
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
        : É importante que as sentenças indiquem, ao menos parcialemente, o significado da expressão.
        : Construções idênticas ou semelhantes, mas com significados diferentes, podem comprometer a legibilidade (por exemplo, os usos de `static` na linguagem **C**.

### Facilidade de escrita

* Domínio da Aplicação
    : A facilidade de escrita de uma linguagem deve ser avaliada em relação ao domínio ao qual a linguagem se aplica.

* Simplicidade e ortogonalidade
    : Uma lingagem com muitas construções diferentes levará os programadores a escolherem quais construções utilizar, fazendo com que aulguns recursos mais eficientes ou elegantes não sejam utilizados quando deveriam.
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

## Questões

1. Cite alguns dos recursos de linguagens de programação específicas que você conhe-ce, cujo objetivo seja um mistério para você.
2. Por que jamais teremos "a linguagem de programação definitiva"?
3. Quais são os elementos que você gostaria que existisse em uma linguagem de programação?
4. Quais elementos você acredita que atrapalham mais do que ajudam em uma linguagem de programação?
5. Em quantas linguagens de programação você consegue programar? Elas são realmente diferentes?
6. Qual é a próxima linguagem de programação que você deseja aprender?

## Para a próxima aula

* Sebesta, capítulos 2 e 3

## Recursos para essa disciplina

### Bibliografia

1. "SEBESTA, Robert. [**Conceitos de Lingagens de Programação**](https://integrada.minhabiblioteca.com.br/reader/books    /9788582604694/){:target='_blank'}. 11<sup>a</sup>. Ed. Bookman.Porto Alegre, 2018.
    * Capítulos 1 e 2

### Recursos Online

1. [The Python Tutorial](https://docs.python.org/3/tutorial/){:target="\_blank"}

### Tutoriais do Git

10. [Pro Git](https://git-scm.com/book/pt-br/v2) (Tradução parcial do livro para português do Brasil){:target="\_blank"}
11. [Git - Guia prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html){:target="\_blank"}: Um guia bem direto, sem muita explicação.
12. [Github - Início Rápido](https://docs.github.com/pt/get-started/quickstart){:target="\_blank"}

### Videos

1. [Aula Inaugural dos Cursos de TI e Inovação Unilasalle 2022/2](https://www.youtube.com/watch?v=pxsdiyHgZHs){:target="\_blank"}
2. [Motivação para Estudar - Prof. Clóvis de Barros Filho](https://www.youtube.com/watch?v=TRPBY_lxJfE){:target="\_blank"}
3. [Procrastinação: sua pior inimiga](https://www.youtube.com/watch?v=q3oEyBpoq3o) (Fredrik Reed, Tchelinux 2021)

