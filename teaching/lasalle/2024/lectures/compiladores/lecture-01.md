---
section: 
title: Apresentação da Disciplina
subtitle:
layout: lecture
last_occurrence: 2024-03-06
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/compiladores
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
    * Mais ferramentas importantes: [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/)
2. Dinâmica das aulas
    1. Dúvidas
    2. Exibição de contúdo e exercícios em 2 períodos (2+2 _pomodoros_)
    3. Intervalo de 20 minutos
    4. Chamada após o intervalo
3. Apresentação do Professor
4. [Apresentação dos Alunos](https://forms.gle/yYRXLrj8hLqzKf1T7) (LEX)
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

## Compiladores

* Tipos de ferramentas para criação de programas
    * Compiladores
    * Interpretadores
    * Transpiladores (Tradutores)
    * Bytecode
* Linguagens de Programação
    * Linguagens imperativas
    * Linguagens orientadas a objetos
    * Linguagens de programação lógica
    * Linguagens funcionais
    * Linguagens específicas de domínio
* Arquiteturas de Computadores
    * monoprocessamento, time sharing, processamento concorrente, processamento distribuído
    * x86, ARM, Power, microcontroladores...
    * cache, persistência
    * máquinas de registradores ou de pilhas
    * bare metal, máquinas virtuais, sistemas embarcados
* Processo de execução de um programa
    * Dados devem estar em memória
    * Dados devem estar no processador (CPU ou ULA)
    * Em geral, usam o conceito de _fetch, execute, store_
    * Loader, Linker
* Fases de um compilador

![Fases de compilação](/images/compiler_sebesta.png)


## Revisão de Conteúdos

* Processamento de Arquivos
* Expressões Regulares e Linguagens Regulares
* Gramáticas Livres de Contexto
* Recursão
* Árvores
* Grafos
* Mapas

## Questões

1. Qual a diferença entre compilador e interpretador? Quais as vantagens e desvantagens de cada um?
2. Quais as vantagens que podemos esperar ao utilizar um tradutor/transpilador?

## Exercícios de Programação

1. Implemente uma lista encadeada em Python
2. Implemente uma árvore binária de pesquisa em Python
3. Implemente uma função que verifique se um grafo é ou não conectado em Python
4. Implemente um programa em Python que abra um arquivo texto e crie um histograma das palavras existentes no texto, ignorando pontuações, números de capítulos, etc. Você pode testar o programa no livro [Dom Casmurro](/files/lasalle/domcasmurro.txt).
    * Quão eficiente é o seu programa em relação ao tempo de processamento?
    * Quão eficiente é o seu programa em relação ao uso de memória?


## Recomendação de leitura para esta aula

1. Livro do Dragão, Capítulo 1
2. Capítulo 1 do livro
    * SEBESTA, Robert. [**Conceitos de Lingagens de Programação**](https://integrada.minhabiblioteca.com.br/reader/books/9788582604694){:target="\_blank"}. 11<sup>a</sup>. Ed. Bookman.Porto Alegre, 2018.


## Material para a próxima aula

1. Leitura rápida sobre autômatos, expressões regulares do livro
    * Menezes, Paulo Blath. [**Linguagens Formais e Autômatos**](https://integrada.minhabiblioteca.com.br/reader/books/9788577807994){:target="\_blank"}. 6<sup>a</sup> ed. Bookman, 2011.
2. Se você não tem, crie uma conta no Github.
3. Se você não conhece, faça pelo menos um tutorial básico do Git.

## Recursos para essa disciplina

### Bibliografia

1. AHO, Alfred V.; LAM, Monica S.; SETHI, Ravi; ULLMAN, Jeffrey B. **Compilers: Principles, Techniques, & Tools** 2<sup>a</sup> Ed. Addisson Wesley. 2006. (_Livro do Dragão Roxo_)
2. LOUDEN, Kenneth C. [**Compiladores : princípios e práticas**](https://integrada.minhabiblioteca.com.br/reader/books/9788522128532){:target="\_blank"}. Cengage Learning, 2004.

### Recursos Online

1. [The Python Tutorial](https://docs.python.org/3/tutorial/){:target="\_blank"}
2. [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/){:target="\_blank"}
3. [PLY on Github](https://github.com/dabeaz/ply){:target="\_blank"}
4. [CS143 Compilers](https://web.stanford.edu/class/cs143/){:target="\_blank"} (Stanford)

### Tutoriais do Git

10. [Pro Git](https://git-scm.com/book/pt-br/v2){:target="\_blank"} (Tradução parcial do livro para português do Brasil)
11. [Git - Guia prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html){:target="\_blank"}: Um guia bem direto, sem muita explicação.
12. [Github - Início Rápido](https://docs.github.com/pt/get-started/quickstart){:target="\_blank"}

### Videos

1. [Aula Inaugural dos Cursos de TI e Inovação Unilasalle 2022/2](https://www.youtube.com/watch?v=pxsdiyHgZHs){:target="\_blank"}
2. [Motivação para Estudar - Prof. Clóvis de Barros Filho](https://www.youtube.com/watch?v=TRPBY_lxJfE){:target="\_blank"}
3. [Procrastinação: sua pior inimiga](https://www.youtube.com/watch?v=q3oEyBpoq3o){:target="\_blank"} (Fredrik Reed, Tchelinux 2021)

