---
title: T1 - Linguagen imperativa/procedural.
subtitle:  Linguagem de programação C.
section: Paradigmas de Programação
layout: lecture
last_occurrence: "2024-1"
copy: 2024
institution:
  name: Universidade Lasalle Canoas
  link: index.html
---

## Objetivo

Compreender o processo de desenvolvimento utilizando liguagens imperativas/procedurais, desenvolvendo uma estrutura de dados genérica com a linguagem de programação C.

## Pré-requisitos

* Todos os alunos necessitarão de contas no site [Github](https://github.com)
* Para o desenvolvimento serão utilizados os seguintes componentes:
    * `git`
    * compiladores C e C++
    * `make`
    * `Catch2`
    * `valgrind`

## Tarefas

* Criar um `fork` do projeto [`paradigmas_2024_t1`](https://github.com/exercicios-programacao/paradigmas_2024_t1)
* Implementar uma lista encadeada genérica com a seguinte interface de programação:
    * `void Lista_new(Lista* lista, int data_size, void (*free_data)(void*))`
    * `void Lista_delete(Lista* lista)`
    * `int Lista_isEmpty(Lista* lista)`
    * `int Lista_size(Lista* lista)`
    * `void Lista_pushFront(Lista* lista, void* valor)`
    * `void Lista_pushBack(Lista* lista, void* valor)`
    * `void Lista_search(Lista* lista, void* chave, int (*cmp)(void*,void*))`
    * `void Lista_first(Lista* lista, void* dest)`
    * `void Lista_last(Lista* lista, void* dest)`
    * `void Lista_current(Lista* lista, void* dest)`
    * `void Lista_next(Lista* lista, void* dest)`
    * `void Lista_remove(Lista* lista, void* chave, int (*cmp)(void*,void*))`
    * `void Lista_removeCurrent(Lista* lista)`
    * `void Lista_insertAfter(Lista* lista, void* dado)`
* Será fornecido um sistema para a compilação e testes automatizados, assim como um _arquivo header_ com as funções que devem ser implementadas.
    * O sistema de compilação utilizará o `make`, o sistema de testes automatizados o `Catch2` e a ferramenta `valgrind`.
        * Para compilar o programa utilize `make`.
        * Para executar os testes automatizados utilize `make test`.
        * Para executar os testes das tarefas extras utilize `make test_extra`.
        * Para executar o teste do `valgrind` utilize `make memtest`.


### Tarefas Extras

As tarefas extras são opcionais, e deve ser indicado no _pull request_ se elas foram realizadas.

* Modificar a estrutura para uma lista duplamente encadeada e adicionar os procedimentos:
    * `void Lista_previous(Lista* lista, void* dest)`
    * `void Lista_insertBefore(Lista* lista, void* dado)`


## Avaliação

* A nota será atribuída baseada nos resultados dos testes automatizados.
* O trabalho tem peso **3.0** na nota do **G1**, sendo **2.5** para a implementação, **0.5** para o teste de vazamento de memória com o `valgrind` e **0.5** para as tarefas extras caso todas sejam concluídas com sucesso.

## Entrega do trabalho

Um único aluno do grupo de alunos que trabalhou na execução do trabalho deverá criar um _pull request_ contra o repositório original do trabalho. O título do _pull request_ é livre, porém o corpo deve conter os **nomes completos** de todos os alunos do grupo, e a informação se as tarefas extras foram ou não executadas.

Uma vez criado o _pull request_ ele pode ser atualizado a qualquer momento, até a data limite de entrega.

Na data limite, o _pull request_ receberá um _label_ de **AVALIADO**, um comentário com o resultado da avaliação, será fechado e não poderá mais ser alterado.

No [LEX](https://lex2.unilasalle.edu.br){:target="\_blank"}, todos os alunos do grupo devem inserir, até a data limite, o link para o _pull request_ de entrega do trabalho.

A data máxima de entrega é dia **27 de abril de 2024**.

# Observações

* O trabalho poderá ser realizado em grupos de até 3 (três) alunos.
* Todo código utilizado em aula pode ser utilizado no trabalho.
* Em caso de plágio, a nota atribuída ao tabalho será 0 (zero).

