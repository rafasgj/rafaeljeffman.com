---
title: Implementação de um avaliador de linguagens regulares
section: Linguagens Formais e Autômatos
layout: lecture
last_occurrence: "2024-1"
copy: 2024
institution:
  name: Universidade Lasalle Canoas
  link: index.html
---

## Objetivo

Entender o processo de análise léxica a partir da utilização de autômatos finitos para o reconhecimento de linguagens regulares e a aplicação prática dos conceitos teóricos vistos em aula.

## Pré-requisitos

* Todos os alunos necessitarão de contas no site [Github](https://github.com)
* Para o desenvolvimento serão utilizados os seguintes componentes:
    * `git`
    * `python`
    * `behave`
    * `tox` (opcional)

## Tarefas

1. Criar um _fork_ do projeto [`automata_2024_t1`](https://github.com/exercicios-programacao/automata-2024-t1)
2. Deve ser criado um "módulo" com o nome `automata` com as seguintes funções:
    * `load_automata(filename: str): -> tuple(Q, Sigma, delta, q0, F)`
        * Esta função lê os dados de um autômato finito a partir de um arquivo de texto e retorna uma estrutura que representa o autômato.
    * `process(automata, word: List[String]): -> Dict[String:String]`
        * Esta função processa uma lista de palavras utilizando o autômato dado e retorna um mapa associando cada palavra ao resultado do automato.
        * Os resultados possíveis são `ACEITA`, caso a palavra seja aceita pelo autômato; `REJEITA`, caso a palavra seja rejeitada pelo autômato; e `INVÀLIDA`, caso a palavra seja inválida, ou seja, contenha um símbolo que não está no alfabeto.
3. O formato do arquivo de descrição do autômato é:
    ```
    <lista de símbolos do alfabeto, separados por espaço (' ')>
    <lista de nomes de estados>
    <lista de nomes de estados finais>
    <nome do estado inicial>
    <lista de regras de transição, com "origem símbolo destino">
```

    * Por exemplo:
    ```nohl
    a b
    q0 q1 q2 q3
    q0 q3
    q0
    q0 a q1
    q0 b q2
    q1 a q0
    q1 b q3
    q2 a q3
    q2 b q0
    q3 a q1
    q3 b q2
    ```
4. A função de leitura do arquivo deve validar se o formato do autômato está correto, e caso não esteja gerar uma exceção (`Exception`).
5. Serão fornecidos testes automatizados para a avaliação do trabalho. Os testes podem ser executadosu utilizando o utilitário `behave` ou o utilitário `tox`, que podem ser instalados em um ambiente virtual do Python.

## Entrega do trabalho

O aluno deverá criar um _pull request_ contra o repositório original do trabalho. O título do _pull request_ deve conter o nome do aluno e o corpo do _pull request_ pode conter um comentário sobre o trabalho.

Uma vez criado o _pull request_ ele pode ser atualizado a qualquer momento, até a data limite de entrega.

Na data limite, o _pull request_ receberá um _label_ de `AVALIADO`, um comentário com o resultado da avaliação, será fechado, e não poderá mais ser alterado.

No `LEX`, **todos** os alunos do grupo devem inserir, até a data limite, o link para o _pull request_ de entrega do trabalho.

A data máxima de entrega é dia **28 de maio de 2024**.

## Observações

* Nenhum arquivo fora do diretório `src` pode ser modificado.
* O trabalho deve ser realizado de forma individual.
* Todo código fornecido em aula pode ser utilizado no trabalho.
* Em caso de plágio, a nota atribuída ao trabalho será 0 (zero).

