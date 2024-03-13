---
section: Compiladores
title: Revisão, Processo de Compilação, Características de Linguagens de Programação
subtitle:
layout: lecture
last_occurrence: 2024-03-13
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/compiladores
---

## Revisão de Conteúdos

* Listas
    * Arrays
    * Pilhas
    * Filas
* Grafos
* Árvores
* Gerenciamento de memória
* Sistemas operacionais


## Processo de Compilação

* Compiladores vs. Interpretadores
    * Compiladores produzem arquivos executáveis a partir do código fonte
    * Interpretadores executam o código fonte, linha a linha.
* Máquinas virtuais (para bytecode) 
    * Um compilador gera um arquivo com instruções para a máquina virtual (bytecode)
    * A máquina virtual interpreta o bytecode
* Trasnpiladores
    * Traduzem código de uma linguagem de programação para outra.
        * TypeScript
        * Teal
        * Objective-C e C with Classes

### Questões

1. Qual a vantagem e desvantagens no uso de:
    * Compiladores
    * Interpretadores
    * Máquinas virtuais

## Fases de um compilador

![Fases de compilação](/images/compiler_sebesta.png){:style="max-width: 80vw !important; min-height: 700px !important;"}

* Análise léxica
    : Divide o código fonte em unidades léxicas, lexemas, que são elementos válidos da linguagem
    : Inicializa a Tabela de Símbolos
    : Por exemplo, a frase **O chachorro comeu o biscoito.**{:style="font-size:120%"}, possui os lexemas `<'O', artigo>`, `<'cachorro', substantivo>`, `<'comeu', verbo>`, `<'o', artigo>`, `<'biscoito', substantivo>`.
    : Como saber onde começa e termina uma palavra da linguagem?
        : _Ocach orroc o meu obis coito_{:style="font-size:120%"}
* Análise sintática
    : Junta as palavras e verifica se a ordem dos lexemas é válida dentro da linguagem.
    : Atualiza a tabela de símbolos
    : Cria uma árvore sintática da lingagem
* Análise semântica
    : Percorre a árvore sintática e avalia se as operações executadas são permitidas dados os tipos de dados das expressões.
    : Cria anotações ou modifica a árvore sintática.
    : Tenta entender o que o programa está tentando fazer, o que é extremamente difícil, logo, compiladores fazem uma análise semântica limita, em geral, apenas procurando inconsistências.
    : Exemplo: **Pedro disse que Pedro deixou seu trabalho em casa?**{:style="font-size:120%"}
    : Ambiguidades em linguagens de programação levam a problemas de análise do código, o que pode dificultar o uso da linguagem.
* Geração de código intermediário
    : Utilizamos um código intermediário para representar o conhecimento do programa e facilitar as fases de otimização e geração de código.
* Otimização
    : Alterar o programa para...
        : Executar mais rápido
        : Utilizar menos memória
        : Consumir menos energia
        : Realizar menos comunicação em rede
        : Diminuir as consultas aos dados
    : A otimização também não é uma etapa fácil para o compilador
        : `x = y * 0` nem sempre pode ser otimizada para `x = 0` (ex.: `NaN`)
* Geração de código alvo
    : Tradução do código intermediário para o código alvo.
    : O código alvo pode ser _assembler_ relocável ou _bytecode_


## Linguagens de Programação

* Modelos de linguagens de programação
    * Imperativas
    * Funcionais
    * Declarativas
    * Lógicas
    * Específicas de domínio
    * Orientadas a objetos
        * na verdade é uma característica que pode ser adicionada a qualquer um dos outros modelos de linguagem.

* Por que existem tantas linguagens?
    * Porque as necessidades de cada domínio são diferentes, e muitas vezes conflitantes.

* Por que ainda criamos novas linguagens, mesmo com algumas tão bem estabelecidas nos seus domínios?
    * Porque os computadores mudaram e problemas que existiam antes não existem mais, e novos problemas são mais relevantes ou possíveis de serem solucionados agora.

* O que é uma boa linguagem de programação?
    * Não existe uma métrica universalmente aceita.
    * Nem as características que nos guiariam para escolher uma são universalmente aceitas.
        * Legibilidade
        * Facilidade de escrever
        * Confiabilidade
        * Portabilidade
    * Linguagens muito utilizadas são linguagens boas?
        * Não necessariamente...
            * C/C++ tem uma curva de aprendizagem íngreme
            * Java tem o problema de se escrever demais
            * Javascript tem o problema de ser um amontoado de alterações
            * Python tem uma virtual machine lenta e (até hoje) não é paralelizável
            * Perl é dificílima de ler
            * PHP é PHP...

* O maior custo de uma nova linguagem é o treinamento dos programadores e sem programadores, a linguagem morre.


## Exercícios

1. Estudar/executar qualquer [tutorial de Git sugerido na Aula 1](lecture-01#tutoriais-do-git).
2. Terminar o [exercício sobe histograma de palavras da Aula 1](lecture-01#exercicio-histograma-texto).

## Recursos para essa aula

## Bibliografia

1. Capítulo 1 do livro
    * AHO, Alfred V.; LAM, Monica S.; SETHI, Ravi; ULLMAN, Jeffrey B. **Compilers: Principles, Techniques, & Tools** 2<sup>a    </sup> Ed. Addisson Wesley. 2006. (_Livro do Dragão Roxo_)
2. Capítulos 1 e 2 do livro
    * SEBESTA, Robert. [**Conceitos de Linguagens de Programação**](https://integrada.minhabiblioteca.com.br/reader/books/9788582604694){:target="\_blank"}. 11<sup>a</sup>. Ed. Bookman.Porto Alegre, 2018.

## Videos

* Aulas 2 e 3 do curso de Stanford [CS143 Compiles](https://www.youtube.com/watch?v=RCxE5vdgUTA&list=PLoCMsyE1cvdUZRe1udlyjpzTww1U5olL2&index=2) 

## Material para a próxima aula

### Bibliografia

1. Capítulo 2 do livro
    * AHO, Alfred V.; LAM, Monica S.; SETHI, Ravi; ULLMAN, Jeffrey B. **Compilers: Principles, Techniques, & Tools** 2<sup>a</sup> Ed. Addisson Wesley. 2006. (_Livro do Dragão Roxo_)
2. Aulas 2, 3 e 4 do curso [CS143 - Compilers](https://web.stanford.edu/class/cs143) da Universidade de Stanford

### Videos

1. Aula 7 a 15 do curso de Stanford [CS143 - Compilers](https://www.youtube.com/watch?v=LAqwEPEMsaM&list=PLoCMsyE1cvdUZRe1udlyjpzTww1U5olL2&index=7) (as aulas 4, 5, e 6 mostram a linguagem de programação, Cool, que está sendo implementada).
    * Embora os vídeos sejam relativos a próxima aula, esse conteúdo será revisto ao longo de todo o G1, logo, não é preciso ver _todos_ os vídeos até a próxima aula, você pode dividir em, aproximadamente, 3 vídeos por semana, por 3 semanas.


