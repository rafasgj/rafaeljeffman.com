---
section: Paradigmas de Programação
title: Linguagens Imperativas
subtitle: Codificação utilizando a linguagem C
layout: lecture
last_occurrence: 2024-03-26
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/paradigmas
---

## Linguagem de Programação C

A linguagem de programação C é uma linguagem imperativa, estruturada, onde o foco do desenvolvimento é o controle da máquina na qual o programa será executado. A linguagem é largamente utilizada até os dias de hoje, principalmente em sistemas operacionais, pilhas de protocolos, _drivers_ de dispositivos e outros sistemas básicos. A linguagem é utilizada em todo tipo de arquitetura, desde microcontroladores (como Arduíno), sistemas embarcados ou em supercomputadores.

### Tipos de Dados

C é uma lingagem com um sistema de tipagem estática, onde as variáveis assumem uma única representação do tipo de dado.

Os principais tipos de dados são:

* **char**: a menor unidade de memória endereçável
* **int**: um valor inteiro do tamanho mais eficiente para o processador alvo
* **float**: Um número de ponto flutuante utilizando a representação de simples-precisão de acordo com o padrão IEEE 754. A precisão é de 6 dígitos.
* **double**: Um número de ponto flutuante utilizando a representação de dupla-precisão de acordo com o padrão IEEE 754. A precisão é de 15 dígitos.
* **void**: Um tipo de dado representando "nenhum dado". Não pode ser utilizado para declarar variáveis.
* Modificadores dos tipos de dados como _unsigned_, _signed_, _short_ e _long_, são utilizados para alterar o comportamento dos tipos de dados (em geral, dos tipos de dados inteiros).

Um tipo comum de qualificador de tipo utilizado é `const`, que define uma variável cujo valor não pode ser alterado.

### Palavras reservadas e características gerais da linguagem C

A linguagem C, como toda linguagem de programação imperativa, é baseada em comandos (_statements_). Todo comando da linguagem C termina com um símbolo ';' (ponto-e-vírgula). Um comando pode ser uma instrução da linguagem, uma atribuição ou uma chamada de subrotina.

Em todo ponto onde um comando pode ser utilizado, a liguagem C aceita um _bloco de código_, que são marcados pelos caracteres `{` e `}` e podem contér diversos comandos em um único bloco.

Nas versões mais atuais da linguagem C, a liguagem possui pouco menos de 60 palavras reservadas, porém, originalmente e na padronização ANSI, a linguagem possuía apenas 32 palavras reservadas:

<style>
table#keywords {
    margin: 0 auto;
}
table#keywords td {
    padding: 2px 20px;
}
</style>

|`auto`|`double`|`int`|`struct`|
|`break`|`else`|`long`|`switch`|
|`case`|`enum`|`register`|`typedef`|
|`char`|`extern`|`return`|`union`|
|`const`|`float`|`short`|`unsigned`|
|`continue`|`for`|`signed`|`void`|
|`default`|`goto`|`sizeof`|`volatile`|
|`do`|`if`|`static`|`while`|
{:id="keywords"}

#### Estruturas de Decisão

A linguagem C é uma linguagem estruturada e define diversas estruturas para facilitar a codificação de programas.

Existem duas construções para desvio condicional de execução, baseado em condições booleanas (_verdadeiro ou falso_):

* `if (<condição>) `_`comando`_
: Executa _`comando`_ (ou um bloco de código) quando a `<condição>` for verdadeira.
* `if (<condição>) `_`comando_T`_` else `_`comando_F`_
: Executa _`comando_T`_ (ou um bloco de código) quando a `<condição>` for verdadeira, ou executa _`comando_F`_ quando a `<condição>` for falsa.

Como a estrutura de decisão, por si só, é um comando da linguagem, podemos criar estruturas de decisão de múltiplas alternativas serializando estruturas de decisão:

```c
if (opt == 1)
    option_1();
else if (opt == 2)
    option_2();
else if (opt == 3)
    option_3();
else
    invalid_option();
```

Estruturas de decisão podem também ser aninhadas, no entanto deve ser tomado cuidado com os `if-else`, uma vez que um `else` sempre se refere ao `if` mais próximo:

```c
if (teste_1) if (teste_2) com_teste_2(); else sem_teste_1();
```

Note que no exemplo anterior o `else` está associado a `if (teste_2)` e não existe um `else` associado a `if (teste_1)`.

O uso de blocos de código e identação correta, embora desnecessário para o compilador, pode ajudar a melhorar a legibilidade do código:

```c
if (teste_1) {
    if (teste_2) {
        com_teste_2()
    } else {
        sem_teste_1();
    }
}
```

Este trecho gera o mesmo código executável que a versão anterior, no entanto é mais fácil de entender os seus efeitos.

Outra estrutura de decisão é o `switch-case`, que permite que a execução do código recomece a partir de um ponto onde um valor está associado a uma variável ou expressão:

```c
switch (<expressão>) {
    case <valor_1>:
        <comandos>
        break;
    case <valor_2>:
        <comandos>
        break;
    default:
        <comandos>
}
```

A diretiva `default` é utilizada nos casos em que nenhum dos valores definidos é o valor da expressão avaliada.

Note o uso das diretivas `break`, uma vez que o código recomeça a execução a partir do ponto onde o `case` equivalente é igual ao valor da expressão, porém, sem o `break`, a execução continuará pelos outros comandos dos outros `case`. Com o uso do `break`, a execução avançará, imediatamente para o comando após o `switch`.

Em alguns momentos pode ser útil ter uma estrutura de decisão sendo avaliada como uma expressão, ao invés de um comando, e, para esses casos, a linguagem C oferece um **operador ternário**, com a forma `<expressão> ? <valor_T> : <valor_F>`. O resultado da expressão é `<valor_T>` se `<expressão>` for verdadeira, e `<valor_F>`, caso contrário.

> Nota: o uso do operador ternário deixa, em geral, o código menos legível, portanto seu uso deve ser restrito aos poucos caso em que ele melhora a leitura do código.


#### Estruturas de Repetição

A linguagem C tem suporte a três estruturas de repetição. As mais comuns são `for` e `while`, mas a estrutura `do...while` também pode ser utilizada.

```c
for ( <inicialização>; <condição>; <expressão> ) <comando>
```

O comando `for` tem três seções opcionais. A primeira seção permite a inicialização de variáveis que serão utilizadas durante a iteração. Em muitos casos uma variável local é decralada nessa seção, sendo que o escopo dessa variável é somente o `for`, não sendo acessível após a sua execução. A segunda seção é um condição booleana, e o `<comando>` só é executado se a condição for verdadeira. Se não for definida, a condição do `for` é considerada `TRUE`. Na maioria dos casos, a condição está associada a uma variável declarada na inicialização do `for`. A terceira seção é executada após uma iteração do `<comando>`, e antes de uma nova avaliação da `<condição>`. A `<expressão>` será avaliada, e, em geral, é utilizada para alterar a variável declarada na primeira seção.

Por exemplo, para executar um comando 10 vezes, podemos utilizar:

```c
for (int i = 0; i < 10; i++) comando();
```

Para facilitar a leitura e modificação do código, é uma boa prática sempre associar o `for` a um bloco de código, mesmo que apenas um comando seja executado.

```c
for (int i = 0; i < 10; i++) {
    comando();
}
```

Usualmente, quando queremos executar um _loop infinito_ na linguagem C, utilizamos o `for`, sem nenhuma das seções definidas:

```c
for(;;) {
    /* executa os comandos até que um comando termine o loop */
}
```

O comando `while` executa um comando ou bloco de código enquanto uma condição booleana for verdadeira. O comando pode nunca ser executado, caso a condição não seja verdadeira na sua primeira avaliação.

```c
while (<condição>) <commando>
```

O comando `do/while` executa um bloco de código enquanto uma condigção booleana for verdadeira. Como a condição é avaliada apenas após a execução do comando, sabemos que o comando será executado, ao menos, uma vez.

```c
do <comando> while (<condição>);
```


### Declaração de variáveis

A declaração de variáveis deve incluir `<tipo> <identificador>` e, opcionalmente, uma inicialização do valor.

```c
int inteiro = 123456;
char valor = 13;
char letra = '0';
```

É possível declarar _arrays_ de tamanho estático em C, onde o tanhanho do array não pode ser alterado:

```c
char buffer[2000];  // declara um array de 2000 caracteres.
int numeros[100];   // declrara um array de 100 inteiros.
```

Os _arrays_ são áreas contíguas de memória utilizados para armazenar valores de um único tipo de dado.

É possível declarar um _array_ estático sem definir o seu tamanho específico, porém os dados devem ser definidos na inicialização do array.

```c
char digitos[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
int fibonacci[] = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 };
```

A inicialização de variáveis é obrigatória no caso do uso do qualificador `const`:

```c
const float pi = 3.141592;
const int value;
value = 123;   // Erro de compilação: assignment of read-only variable
```


### Declaração de subrotinas

Todo código em C é escrito dentro de subrotinas. O ponto de entrada de um programa C é a subrotina `main` que tem como assinatura `int main(int, char**)`. Subrotinas podem ou não retornar valores, e possuem uma lista opcional de parâmetros, os quais funcionam como variáveis locais da subrotina.

Por exemplo, um programa simples pode ser descrito em uma única subrotina:

```c
int main(int argc, char **argv) {
    for (int i = 1; i < 100; i += 2) {
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

Espera-se que o retorno da subrotina main seja `0` quando o programa termina sem erros, ou um valor diferente de `0` quando o programa termina devido a um erro no processamento.

Uma subrotina que não retorna nenhum valor deve ter `void` como tipo de retorno:

```c
void imprime_numero(int numero) {
    printf("%d\n", numero);
}
```

As subrotinas da linguagem C podem ser definidas de forma recursiva, no entanto, nenhum tipo de otimização é realizado (como _tail recursion_), e as chamadas não são diferentes de chamadas convencionais de subrotinas.

```c
/*
 * Uma imprlementação quadrática do cálculo do
 * n-ésimo número de Fibonacci.
 */
int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n-1) + fibonacci(n-2);
}
```


## Ponteiros e Alocação Dinâmica de Memória

Ponteiros são uma forma de acesso indireto ao valor de uma variável, enquanto uma váriavel de um tipo de dado qualquer possui um valor que representa aquele tipo de dado, uma variável que é um ponteiro para um tipo de dado contém, como valor, um endereço de memória no qual existe um valor com o tipo de dado esperado. Quando declaramos uma variável como `int *pi`, estamos dizendo que `pi` contém um endereço de memória, e na posição de memória deste endereço encontra-se um valor do tipo `int`.

Para acessar o valor indireto de um ponteiro utilizamos o operador `*`. Para acessar o endereço de memória de uma variável utilizamos o operador `&`, como no seguinte exemplo:

```c
int i = 10;
int *pi = &i;
int x = *pi;  // x = 10
```

Podemos utilizar o operador `*` para atribuir um valor a posição de memória apontada por um ponteiro. Note que isso pode ter o efeito colateral de alterar o valor de uma variável:

```c
int i = 10;
int *pi = &i;
*pi = 9;  // i == 9
```

A aritmética de ponteiros é uma característica marcante da linguagem C, trazendo grande flexibilidade (e complexidade) à linguagem. Por exemplo, permitindo que os dados de um _array_ sejam acessados como ponteiros:

```c
int vi[] = {1, 10, 100};
printf("%d\n", *(vi + 2));  // imprime '100\n' no console
```

No exemplo anterior estamos imprimindo _o conteúdo do endereço de dois elementos além do endereço da variável `vi`_. Como a linguagem C sabe o endereço de `vi` (`int vi[]` é muito parecido com `int *vi`), e sabe o que tipo de dado apontado por `vi` é um inteiro, a expressão `(vi + 2)` retorna o endereço de memória de `vi` adicionado de dois elementos inteiros (um número de _bytes_ equivalente a `2 * sizeof(int)`), e o uso do operador `*` recupera o valor contido no endereço. 

Deve se tomar cuidado em como a expressão é construida, pois dependendo da expressão o resultado pode ser diferente:

```c
int vi[] = {1, 10, 100};
printf("%d\n", *vi + 2);  // imprime '3\n' no console
```

Note que a diferença é sutil, e nessa nova expressão estamos somando o valor 2 ao valor existente no endereço apontado pela variável `vi` (o endereço do primeiro elemento do _array_).

O uso de ponteiros nos permite tirar proveito da alocação dinâmica de memória em C:

```c
#include <stdlib.h>
#include <math.h>

int main(int argc, char **argv) {
    int *vi = (int*) malloc(3*sizeof(int))
    for (int i = 0; i < 3; i++) {
        vi[i] = (i + 1) * 10;
    }
    printf("%d\n", vi[2]);  // imprime '30\n' no console
    free(vi);
}
```

> Lembre-se que sempre que há alocação dinâmica de memória (com `malloc`, `calloc` ou `realloc`), é necessário liberar a memória explicitamente com `free`, ou ocorrerá _memory leak_.)

Um outro uso para ponteiros é utilizar um dos argumentos de uma função como argumento de saída dessa função. Por exemplo, se uma função deve retornar um código de erro e um valor calculado, não é possível definir esses dois valores como retorno da função, uma vez que C só aceita um valor de retorno, mas podemos retornar um código de erro, e preencher o valor da variável, passando um ponteiro para ela como parâmetro:

```c
int preenche_var(int *output) {
    if (esta_tudo_certo()) {
        *out = calcula_valor();
        return 0;
    }
    return COD_ERRO;
}

void codigo_cliente() {
    int err, valor;

    if (err = preenche_var(&valor)) {
        // alguma coisa deu errado e "err" tem o código do erro.
    } else {
        // tudo certo e "valor" tem o valor atribuído em preenche_var()
    }
}

```

Um dos usos avançados de ponteiros é para permitir que uma função seja passada como parâmetro para outra função. O principal uso dessa técnica é permitir a composição de funções ou polimorfismo. É uma técnica bastante comum em linguagens funcionais ou que implementam algumas contruções funcionais.

No exemplo a seguir, o programa imprime `Valor gerado: 2` e `Valor gerado: 3`. Note que as funções `retorna_par` e `retorna_impar`, não são chamadas até serem necessárias, e são chamadas no momento que se atribui o valor a `valor_gerado` com a chamada `gerador()`.

```c
#include <stdio.h>

int retorna_par() {
    return 2;
}

int retorna_impar() {
    return 3;
}

void imprime_valor(int (*gerador)()) {
    int valor_gerado = gerador();
    printf("Valor gerado: %d\n", valor_gerado);
}

int main(int argc, char** argv) {
    imprime_valor(retorna_par);
    imprime_valor(retorna_impar);
}
```

### Strings

A linguagem de programação C não possui um tipo de dado específico para a representação de _strings_ (cadeias de caracteres). Para obter um tipo de dado semelhante, a linguagem utiliza um _array_ de caracteres (`char*`) terminado com um caracter nulo '`\0`' (ou o valor inteiro 0) em conjunto com uma série de funções definidas na biblioteca padrão em `string.h`.

Por exemplo, é possível comparar duas _strings_ com o seguinte código:

```c
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 3)
        return 1;
    return strcmp(argv[1], argv[2]);
}
```

## Tipos de Dados definidos pelo usuário

Em C, podemos definir tipos com a diretiva `typedef`. Por exemplo, podemos definir um tipo de dado específico para uma arquitetura:

```c
#ifdef ARCH_1
typedef int size_t;
#else
typedef char size_t;
#endif
```

Se a macro `ARCH_1` estiver definida, o tipo `size_t` será equivalente a `int`, caso contrário, será equivalente a char. A vantagem dessa definição de um nome é facilitar a implementação de um sistema, que agora pode depender do tipo `size_t`, o qual terá o tipo adequado para a arquitetura específica.

Outra forma de definir tipos de dados é por meio das diretivas `union` e `struct`. A diretiva `struct` (não veremos `union` nessa disciplina) cria um registro com vários campos de dados, que por sua vez tem o seu tipo específico, por exemplo:

```c
struct Telefone {
    int code;
    int area;
    int prefix;
    int number;
};
```

Note que o uso de `struct` não define um novo tipo de dado como faz `typedef`, e o uso da estrutura na declaração de uma variável é um pouco diferente:

```c
struct Telefone fone;
fone.code = 55;
fone.area = 51;
fone.prefix = 9123;
fone.number = 1000;
```

Podemos transformar a `struct` em um tipo utilizando o `typedef`:

```c
typedef struct {
    int code;
    int area;
    int prefix;
    int number;
} Telefone;

Telefone fone;
```

Um outro uso do typedef é permitir a criação de estruturas recursivas, como as estruras utilizadas em árvores:

```c
typedef struct _treenode {
    int key;
    struct _treenode* left;
    struct _treenode* right;
} TreeNode;
```

## Exercícios

* Escreva um programa que pergunta ao usuário um número, e, se o número for maior que zero, imprime a soma de todos os número inteiros e positivos menores ou iguais ou número do usuário.

* Escreva um programa que pergunta um número ao usuário e imprime esse número na tela. O programa só pode aceitar que números inteiros e maiores que zero sejam inseridos, caso contrário o programa deve enviar uma mensagem de erro e pedir que o usuário digite um novo número.

* Escreva um programa que pergunta o nome do usuário e escreve a mensagem `"Olá, <nome_do_usuário>!"` na tela.

* Escreva um programa que aceita como parâmetro de linha de comando uma série de números e calcula a média desses números.

* Escreva um programa que aloca dinâmicamente um vetor de inteiros, preenche o vetor com valores aleatórios, calcula a média, o menor valor e o maior valor do vetor.
    * Você consegue fazer o mesmo programa utilizado aritmética de ponteiros?

* Escreva um programa que permite que o usuário crie um registro de contatos (até 20 contatos), e possa consultar contatos, alterar contatos, inserir novos contatos e excluir contatos.

## Preparação para a próxima aula

* [Capítulo 8](https://integrada.minhabiblioteca.com.br/reader/books/9788521632474/epubcfi/6/36[%3Bvnd.vst.idref%3Dchapter08]!/4) e [Capítulo 12](https://integrada.minhabiblioteca.com.br/reader/books/9788521632474/epubcfi/6/44[%3Bvnd.vst.idref%3Dchapter12]!/4) do livro [Linguagem C](https://integrada.minhabiblioteca.com.br/reader/books/9788521632474/)(Luís Damas, 10<sup>a</sup> edição).

* [Capítulo 10 - Porteiros](https://integrada.minhabiblioteca.com.br/reader/books/9788595152090/epubcfi/6/36[%3Bvnd.vst.idref%3DB9788535291063000109]!/4/2/4/4[B9788535291063000109]/1:7[eir%2Cos]) e [Capítulo 11 - Alocação Dinâmica](https://integrada.minhabiblioteca.com.br/reader/books/9788595152090/epubcfi/6/38[%3Bvnd.vst.idref%3DB9788535291063000110]!/4/2/6/6[s0010]/2[st0010]/1:13[ni%C3%A7%2C%C3%A3o]) do livro [Linguagem C - Completa e Descomplicada](https://integrada.minhabiblioteca.com.br/reader/books/9788595152090)

## Recursos para essa aula

* Estruturas de decisão, iteração, declaração de variáveis, funções e procedimentos da linguagem C, que podem ser encontrados nos livros da Bibliografia para essa aula.

### Bibliografia

* MIZRAHI, Victorine Viviane. **Treinamento em Linguagem C**. 2<sup>a</sup> Edição. Pearson Prentice Hall. São Paulo. 2008.

* DAMAS, Luís. [**Linguagem C**](https://integrada.minhabiblioteca.com.br/reader/books/9788521632474/). 10<sup>a</sup> Edição. LTC. Rio de Janeiro. 2016.

* BACKES, André. [**Linguagem C - Completa e Descomplicada**](https://integrada.minhabiblioteca.com.br/reader/books/9788595152090). 2<sup>a</sup> Edição. LTC. Rio de Janeiro. 2023.

