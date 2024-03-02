---
title: "&tau;"
layout: section
lang: pt
copy: 2024
date: 2024-02-29
sections: []
abstract: |
    t é um projeto para a criação de um utilitário para o
    gerenciamento de listas de tarefas utilizando a linha
    de comando.
---

[`t`](https://github.com/rafasgj/t) é uma experiência em gerenciamento de _stress_ e _burnout_.

O objetivo do projeto é prover um _software_ simples e com o menor número de dependências possível para gerenciar uma lista de tarefas que precisam ser realizadas.

A interface do programa utiliza a linha de comando, e o gerenciamento dos dados é feito utilizando o [`jq`](https://github.com/jqlang/jq), que fornece uma lingagem para a manipulação de dados JSON utilisando o _shell_.

Até a última _release_, estas são as opções disponíveis:

```
usage: t [options] [ID|DESCRIPTION]

The default action is to list ('-l') tasks. If only a positional
parameter is provided, if it is a number (ID{, the details of a single
task is shown (same as '-l ID'), if it is a string (DESCRIPTION), a new
task is added to the task list (same as '-a DESC').

Version: 0.2.0

Options:
  -h              Print this help and exit.
  -V              Print version and exit.

  -a DESC         Add a new task.
  -d ID           Mark a task as done.
  -l [ID]         List all open tasks, or detail a single open task.
  -L [ID]         List all done tasks, or detail a silgle done task.
  -n ID           Add a note to task.
  -m ID           Modify a task.
                  Use toghether with any of '-w' and DESCRIPTION.
  -p              Purge all done tasks.
  -r ID           Remove a task.
  -s ORDER        Sort tasks by selected field. Valid options are:
                      due: Due date (defalt)
                      done: Done date (default for 'done tasks')
                      create: Creation date
                      description: Alphabetically by description
  -u ID           Mark task as undone.
  -w TIMESTAMP    When task is due (%Y-%m-%d [%H:%M])
```

