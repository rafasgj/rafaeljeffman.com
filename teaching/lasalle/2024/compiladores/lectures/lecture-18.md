---
section: Compiladores
title: Exercícios de Revisão
subtitle:
layout: lecture
last_occurrence: 
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/compiladores
---

<style>
table {
  border-collapse: collapse;
  margin: 0 auto;
}
thead, tr, td {
  border: thin solid black;
  margin: 0;
  padding: 5px;
}
td {
   min-width: 10ch;
   text-align: center;
}
</style>

## Questão 1

É chamado de compilação o processo de conversão do código escrito pelo programador para um arquivo binário que o computador consegue executar. Esse processo é realizado por um programa chamado compilador. Entre as diversas tarefas de um compilador, destaca-se a de identificar os possíveis erros sintáticos e semânticos.

Com base nessas informações, considere uma linguagem de programação em que a sintaxe de uma operação aritmética seja dada pela seguinte gramática livre de contexto:

```nohl
S → var '=' E ';' | var '=' E; S
E → E '+' E | E '-' E | E '*' E | E '/' E | '(' E ')' | var
```

Inspirado nessa gramática, um profissional submete a seguinte sentença ao compilador dessa linguagem de programação:

$$
a = a / (b - b);
$$

Com base na gramática da linguagem de programação e acerca do processo de análise sintática e semântica da sentença proposta pelo profissional, é correto afirmar que

* a gramática gera a sentença apresentada e o erro presente na expressão está fora do escopo das
análises sintática e semântica.
* a gramática gera a sentença apresentada, porém o analisador semântico transmitirá uma
mensagem de erro.
* o analisador léxico transmitirá uma mensagem de erro, pois a gramática não gera a sentença
apresentada.
* o analisador semântico transmitirá uma mensagem de erro, pois a gramática não gera a sentença
apresentada.
* a gramática gera a sentença apresentada, porém o analisador léxico transmitirá uma mensagem de erro
{:class="lettered"}

## Questão 2

Em um compilador, um analisador sintático descendente preditivo pode ser implementado com o auxílio de uma tabela construída a partir de uma gramática livre de contexto. Essa tabela, chamada tabela LL(k), indica a regra de produção a ser aplicada olhando-se o k-ésimo próximo símbolo lido, chamado _lookahead_(k). Pro motivo de eficiência, normalmente busca-se utilizar k=1. Considere a gramática livre de contexto G = ({X, Y, Z}, {a, b, c, d, e}, P, X), em que P é composto pelas seguintes regras de produção (onde `&` é a palavra vazia):

```nohl
X -> aZbXY | c
Y -> dX | &
Z -> e
```

Considere, ainda, a seguinte tablea LL(1), construída a partir da gramática G, sendo `$` o símbolo que representa o fim da cadeia. Essa tabela possui duas produções distintas na célula (Y, d), gerando, no analisador sintático, uma dúvida na escolha da regra de produção aplicada em determinados momentos da análise.

|:----:|:--:|:--:|:--:|:--:|:--:|:--:|
| | a | b | c | d | e | $ |
| X | X -> aZbXY | | X -> c | | | |
| Y | | | | Y -> dX <br/> Y -> `&` | | Y -> `&` |
| Z | | | | | Z -> e |

Considerando que o processo de construção dessa tabela LL(1), a partir da gramátiac G, foi seguido corretamente, a existência de duas regras de produção distintas na célula (Y, d), neste caso específico, resulta

* da ausência do símbolo de fim de cadeia (`$`) nas regras de produção.
* de um não-determinismo causado por uma ambiguidade na gramática.
* do uso incorreto do símbolo de cadeia vazia (`&`) nas regras de produção.
* da presença de duas regras de produção com um único terminal no corpo.
* da presença de duas regras de produção com o mesmo não-terminal na cabeça.
{:class="lettered"}

## Questão 3

Uma gramática livre de contexto (GLC) é um modelo computacional geralmente utilizado para definir linguagens de programação e, quando está de acordo com a Forma de Backus-Naur (BNF), permite que alguns operadores sejam utilizados no lado direito de suas producões, como o operador `|` (pipe) que indica seleção, o operador `[]` que indica que o operonda em questão é opcional, e o operador `*` que indica repetição de 0 (zero) ou mais vezes.

Projetar um compilador para uma determinada linguagem envolve, entre outras coisas, especificar quais são os símbolos válidos nesta linguagem, bem como quais são as regras sintáticas que a definem.

A linguagem de programação Java é uma linguagem com suporte à orientação a objetos que não permite herança múltipla e que premite que uma classe implemente múltiplas interfaces. A seguir, exibem-se trechos de código sintaticamente válidos na linguagem Java.

* Trecho 1
    : `class A extends B { }`
* Trecho 2
    : `class F implements C { }`
* Trecho 3
    : `class J extends A implements C, D { }`

No trecho 1, cria-se uma classe chamada `A` que herda de uma classe chamada `B`. No trecho 2, cria-se uma classe chamada `F` que implementa uma interface chamada `C`. No trecho 3, cria-se uma classe chamada `J' que herda de uma classe chamada `A` e implementa duas interfaces, chamadas `C` e `D`.

Considere que:
* `<classdecl>` é um não-terminal cujo intuito é dar origem a declarações de classe;
* `<classbody>` é um não-terminal cujo intuito é dar origem ao corpo de classes;
* os terminais aparecem entre aspas;
* <id> é um não-terminal cujo intuito é dar origem a qualquer identificador válido, como nomes de classe ous variáveis.

A gramática que especifica uma linguagem que não permita herança múltipla e que implemente zero ou mais interfaces, como na linguagem Java, é:

* `<classdecl> "class" <id> ["extends"] <id> <classbody>`
* `<classdecl> "class" <id> ("extends" <id>)* <classbody>`
* `<classdecl> "class" <id> ["extends"] <id> ["implements" ("," | <id>)*] <classbody>`
* `<classdecl> "class" <id> ["extends" <id>] ["implements" <id> ("," <id>)*] <classbody>`
* `<classdecl> "class" <id> ["extends" <id>] "implements" <id> ("," <id>)* <classbody>`
{:class="lettered"}

## Questão 4

Considere a implementação ede um compilador em que as etapas de análise léxica e sintática possam compartilhar o mesmo processador de forma concorrente. Considere, ainda, uma solução para o problema, cujo pseudocódigo é mostrado abaixo.

O analisador léxico lê lexemas e identifica os respectivos _tokens_ do arquivo-fonte por meio da chamada ao procedimento `Leia`. O analisador sintático verifica a sequência dos _tokens_ por meio da chamada ao procedimento `Case`. os dois processos compartilhas a constante `N` e as variáveis `buffer`, `vez` e `cont`.

* Compartilhado
```nohl
constante N = 10;
inteiro buffer[N], vez = 0, cont = 0;
```

* Analisador Léxico
```nohl
01  inteiro token, in = 0;
02  enquanto verdadeiro faça
03      Leia(token);
04      equanto cont = N - 1 aguarde;
05      equanto vez = 1 aguarde;
06      buffer[in] = token;
07      cont = cont + 1;
08      vez = 1;
09      in = (in + 1) mod N;
10  fim_enquanto
```

* Analisador Sintático:
```nohl
11  inteiro token, out = 0;
12  enquanto verdadeiro faça
13      enquanto cont = 0 aguarde;
14      enquanto vez = 0 aguarde;
16      token = buffer[out];
15      cont = cont - 1;
17      vez = 0;
18      out = (out + 1) mod N;
19      Case(token)
20  fim_enquanto
```

A partir da análise da solução, avalie as asserções a seguir e a relação proposta entre elas.

1. A eliminação da variàvel `cont` e das linhas 4, 7, 13 e 16 causa erro de sincronismo entre os processos,

**PORQUE**
{:style="text-align: center; margin: auto 0; width: 100%;"}

2. A variável `cont` é responsável pelo controle de acesso à sção crítica do código.
{:start="2"}

A respeito dessas asserções, assinale a opção correta.

* As asserções 1 e 2 são proposições verdadeiras, e a 2 é uma justificativa correta da 1.
* As asserções 1 e 2 são proposições verdadeiras, mas a 2 não é uma justificativa correta da 1.
* As asserções 1 é uma proposição verdadeira e a 2 é uma proposição falsa
* As asserções 1 é uma proposição falsa e a 2 é uma proposição verdadeira
* Ambas as proposições são falsas.
{:class="lettered"}

## Questão 5

Utilizando o código intermediário de três endereçoes numerado, mostre o código gerado para a seginte instrução:

```nohl
if a < 3 and b  > 10 and a < b then verdadeiro() else falso() ;
```

