---
layout: main
section: Shellscript
tags:
  - linux
  - shellscript
title: Conceitos Básicos de Programação Shell
copy: 2022
date: 2022-06-12
---

Neste artigo são revisados alguns conceitos básicos da codificação de programas, voltados para a criação de _scripts shell_, e são apresentados alguns conceitos específicos desse ambiente.

## Estruturas de Programação

Ao programar para um _shell_ POSIX, principalmente os baseados no Bourne Again Shell (_bash_), encontramos diversas estruturas comuns a outros ambientes e linguagens de programação.

* [Estruturas de Decisão](#estruturas-de-decisão)
* [Estruturas de Repetição](#estruturas-de-repetição)

### Estruturas de Decisão

As estruturas de decisão avaliam uma condição e desviam a execução do programa de acordo com o resultado dessa avaliação. O resultado da condição é sempre `verdadeiro` ou `falso`.

#### if-then-elif-else

O `if` é o comando utilizado para executar um trecho de código apenas quando a `<condição>` for verdadeira. Opcionalmente, pode ser utilizado o `else`, cujo código só será executado caso a `<condição>` seja falsa.

Utiliza-se o comando `fi` para marcar o fim de um bloco `if-then-else`.

```sh
if <condição>
then
    # condição 1 é `verdadeiro`
else  # opcional
    # condição 1 é `falso`
fi
```

É possivel aninhar diversos comandos `if`, e o `else` encontrado será sempre do último `if` aberto, ou seja, do último `if` que não tem um `fi` correspondente.

```sh
if #1
then
    if #2
    then
        # código
    else # do if #2
        #código
    fi  # fim do if #2
fi # o if #1 não tem else.
```

Quando temos um teste logo após o `else`, ao invés de utilizar `else if`, o que exigiria utilizar dois `fi`, podemos associar o `elif` ao `if` original.

```sh
if <condição 1>
then
    # condição 1 é `verdadeiro`
elif <condição 2> # opcional
then
    # condição 1 é `falso` e condição 2 é `verdadeiro`
else  # opcional
    # condição 1 é `falso` e condição 2 é `falso`
fi
```

Veja um exemplo:

```sh
#!/bin/sh

if [ $1 -gt 10 ]
then
    echo greater than 10
elif [ $1 -lt 10 ]
then
    echo less than 10
else
    echo equal to 10
fi
```

#### case-in

A construção `case-in` é semelhante ao `switch-case` em outras linguagens de programação. Um `VALOR` é comparado a padrões, e se este `VALOR` for representado pelo padrão em questão, o código associado ao padrão é executado até que se encontre o duplo ponto-e-vírgula (`;;`).;

Quando associamos o mesmo código a dois ou mais padrões diferentes, separamos os padrões usando o `pipe` (`|`). Nesse caso, o código será executado quando `VALOR` for associado a qualquer um dos padrões.

```sh
case <VALOR> in
    pattern 1)
        # código 1
        ;;
    pattern 2 | pattern 3)
        # código 2
        ;;
    *)
        # código 3
        ;;
esac
```

A avaliação de padrões utilizado é a mesma do _shell_, por exemplo o padrão `[0-9][0-9]*` poderia ser utilizado para selecionar qualquer número inteiro, com um ou mais dígitos.

Usualmente, o último padrão do `case-in` é o `*)`, que aceita "qualquer quantidade de caracteres, independente do caracter", ou seja, aceita qualquer padrão de `VALOR`, e funciona como uma opção `default`.

O próximo exemplo implementa a solução para o mesmo problema apresentado anteriormente, mas utilizando `case-in` ao invés de `if-then-else`:

```sh
#!/bin/sh

case "$1" in
    -[0-9]* | [0-9] ) echo less than 10 ;;
    10 ) echo equal to 10 ;;
    * ) echo greater than 10 ;;
esac
```

##### _falltrough_

Podem existir situações onde você deseja continuar a execução de um código de um padrão para o próximo. Nesse caso, você pode utilizar `;&` no lugar de `;;` para representrar o _falltrough_ no `case-in`:

```sh
#!/bin/sh

case "$1" in
    aa* ) echo "Muitos 'a'!" ;&
    *) echo "Esse texto sempre aparecerá..." ;;
esac
```


### Estruturas de Repetição

Utilizamos estruturas de repetição para executar o mesmo bloco de código diversas vezes. O número de vezes que o código será repetido pode depender dos elementos de uma lista, ou da ocorrência de um evento.

#### for-in

A estrutura de repetição `for-in` executa um bloco de código uma vez para cada um dos elementos de uma lista, e, a cada execução, atribui o próximo elemento da lista a uma variável.

No exemplo, as letras são impressas, uma por linha:

```bash
for VAR in a b c d e f g
do
    echo "Letra: ${VAR}"
done
```

Podemos utilizar o comando `seq` para executar o laço um número específico de vezes:

```bash
for INDICE in $(seq 10)
do
    if [ $((INDICE % 2)) -eq 0 ]
    then
        echo "${INDICE} é par."
    else
        echo "${INDICE} é impar."
    fi
done
```

#### while

O comando `while` executa um bloco de código enquanto uma determinada condição for verdadeira.

```bash
while <condição>
do
    # condição é verdadeira
done
```

Por exemplo, podemos executar a leitura de um valor até que o número correto seja inserido:

```bash
while [ ${NUM:-0} -ne 10 ]
do
    read -p "Menor número positivo de dois digitos? " NUM
done
```

Note que o bloco de código pode nunca ser executado se a condição for inicialmente `falsa`, por exemplo `while false`, ou o bloco nunca terminará se ela for sempre verdadeira (_loop_ infinito), como em `while true`.

#### continue e break

Dentro de uma estrutura de repetição, podemos utilizar os comandos `break` e `continue` para executar um "salto" dentro do _script_.

O comando `break` encerra a execução do _loop_, saltando para o comando imediatamente após o `done`. Já o comando `continue`, retorna ao início do _loop_, forçando uma nova iteração (no caso do `for-in` utilizando um novo elemento da lista).

```sh
for INDICE in $(seq 100)
do
    if [ $((INDICE % 50 )) -eq 0 ]
    then
        echo -e "T\n"
        break
    fi
    if [ $((INDICE % 10 )) -eq 0 ]
    then
        echo -n "X"
        continue
    fi
    echo -n "-"
done
```

### Avaliação de Verdadeiro/Falso no _shell_

Para o _shell_ um resultado `verdadeiro` em uma condição do `if` significa que o _programa_ executado para avaliar a condição terminou sem retornar um código de erro.

O código de erro do último programa executado pelo _shell_ pode ser recuperado utilizando `$?`. Por exemplo, ao executar o comando `true`, que sempre retorna `verdadeiro`, o resultado de `echo $?` será `0`, por outro lado, ao executar o comando `false`, que sempre retorna falso, o resultado será `1`

```none
$ true
$ echo $?
0
$ false
$ echo $?
1
```

Um comando que permite comparar valores é o comando `test` (que é equivalente ao comando `[`, porém o segundo requer que o último parâmetro seja `]`). Esse comando pode executar diversas comparações, como verificar se um _string_ é vazia (`-z`), se um arquivo existe (`-f`), ou se um número `A` é maior que um número `B` (`${A} -gt ${B}`), entre outros testes.

Por esse motivo, o comando `if` normalmente é visto como `if [ <teste> ]`.

No entanto, qualquer comando pode ser utilizado como `condição` para o `if`. Por exemplo, podemos executar um trecho de código caso uma cópia de arquivo tenha sido executada corretamente:

```sh
if cp "${src}" "${dest}"
then
    # executa código se a cópia de arquivo for executada
fi
```

#### Relações entre condições

Quando precisamos relacionar duas ou mais condições podemos utilizar, em linguagens de programação, os conectores lógicos AND e OR. Podemos também negar uma condigção com o NOT.

Se temos uma expressão `cond1 AND cond2`, a expressão só será verdadeira se as duas condições forem verdadeiras. Podemos representar o `AND` no _shell_ com `&&`. Por exemplo, `true && true` é `verdadeiro`, `true && false` é `falso` e `[ 10 -gt 2 ] && [-100 -lt 0]` é `verdadeiro`.

No caso de existir uma expressão `cond1 OR cond2`, a expressão será verdadeira se qualquer uma das duas condições forem verdadeiras. Podemos representar o `OR` no _shell_ com `||`. Por exemplo, `true || true` é `verdadeiro`, `true || false` é `verdadeiro`, `false || true` é verdadeiro, e `false || false` é `falso`.

Como o _shell_ faz o que chamamos de _avaliação de curto circuito_, ou seja, ele para de executar a avaliação da expressão quando já sabe o resultado, podemos, em algumas situações, usar a relação de condições para substituir um `if`. Esse tipo de construção só é recomendado em situações simples, pois pode deixar o código mais difícil de ler:

```none
$ true && false && echo "YES" || echo "NO"
NO
$ true && true && echo "YES" || echo "NO"
YES
$ true && ! false && echo "YES" || echo "NO"
YES
```

Outra operação importante sobre condições é a negação da condição (NOT), ou seja, o resultado da condição é invertido e um resultado `verdadeiro` vira `falso`, e vice-versa. No _shell_ a negação é representada por `!`.

Podemos utilizar a negação para executar algo apenas quando a condição for `falsa`, e queremos, por exemplo, evitar a utilização do `else`:

```
if ! cp ${src} ${dest}
then
   # código executado apenas em caso de falha na cópia.
fi
```
