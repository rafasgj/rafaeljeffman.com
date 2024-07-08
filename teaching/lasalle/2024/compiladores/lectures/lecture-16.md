---
section: 
title: Geração de Código
subtitle:
layout: lecture
last_occurrence: 
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/compiladores
---

## Criação da árvore de sintaxe

Gramática com regras semânticas:

```
E -> E1 + T { E.node = new Node('+', E1.node, T.node) }
E -> E1 * T { E.node = new Node('*', E1.node, T.node) }
E -> T      { E.node = T.node }
T -> ( E )  { T.node = E.node }
T -> id     { T.node = new Leaf(id, symtable.get(id)) }
T -> num    { T.node = new Leaf(num, (num.value, "const", "int")) }
```

## Código de 3 endereços (TAC - Three Address Code)

Para a geração do código alvo é interessante criar uma representação mais
simples, mais próxima do código de máquina, que permita descrever o programa
sendo compilado de uma forma que a tradução para diferentes arquiteturas de
computadores seja fácil.

Dessa forma, separamos o compilador em "_front end_" e "_back end_", e basta
criar um novo _back end_ para uma nova plataforma alvo para que a linguagem
implementada seja suportada nessa plataforma. Como é mais fácil traduzir o
código de 3 endereços para uma nova plataforma, facilita a portabilidade do
compilador.

O código de 3 endereços é uma representação linear de uma árvore sintática,
e é útil tanto para a otimização como para a geração de código alvo.
O código de 3 endereços é constituído de operações que envolvem, um
**operador**, atê três endereços de  **operandos** e uma atribuição. Por
exemplo, `r1 = i1 + i2`. Os _operandos_ podem ser uma **constante**,
um **nome**, ou um **temporário**

As seguintes instruções devem fazer parte do código de 3 endereços:

* Atribuição
    : na forma $x = \Psi(y, z)$, onde $\Psi$ é um operador binário (aritmético ou lógico)
    : na forma $x = \Psi(y)$, onde $\Psi$ é um operador unário, por exemplo `t3 = int(x)`
* Instruções de cópia
    : do tipo `x = y`
* Instruções de cópia indexada
    : do tipo `x = index(y, i)`, representando `x = y[i]`
* Atrtibuição de endereço e apontador
    : `x = &y`, `x = *y`, ou `*x= y`
* Desvios incondicionais
    : `goto label`
* Desvios condicionais
    : `if x goto label`
    : `False x goto labe}`
    : Desvios do tipo `if x `$\rho$` y goto label` podem ser omitidos uma vez que se pode utilizar `t = `$\rho$`(x, y); if t goto label`
* Chamadas de função
    : `param x`, para adicionar parâmetros;
    : `return x`, para retornar um valor.
    : `call name, n` para chamar a função com $n$ parâmetros. Note que o $n$ é necessário para que seja possível aninhar funções ($f(f(x))$)

Considere o código:

```c
do {
    i = i + 1;
} while (a[i] < v);
```

Assumindo que o tamanho de cada elemento do vetor $a$ seja $8$ _bytes_, temos os seguintes códigos de 3 endereços:

* Utilizando rótulos simbólicos:

```nohl
L:  t1 = i + 1
    i = t1
    t2 = i * 8
    t3 = a[t2]
    t4 = t3 < v
    if t4 goto L
```

* Utilizando posição numérica:

```nohl
100: t1 = i + 1
101: i = t1
102: t2 = i * 8
103: t3 = a[t2]
104: t4 = t3 < v
105: if t4 goto 100
```

## Tradução de Códico para TAC

### Expressões

```nohl
S -> id = E   { S.code = E.code ++ gera('id', '=', E.addr); }
E -> E1 + E2  {
                E.addr = new Temp();
                E.code = E1.code
                         ++ E2.code
                         ++ gera(E.addr, '=', E1.addr, '+', E2.addr);
              }
E -> - E1     {
                E.addr = new Temp();
                E.code = E1.code ++ gera(E.addr, '=', 'minus', E1.addr);
              }
E -> ( E1 )   { E.addr = E1.addr; E.code = E1.code; }
E -> id       { E.addr = get(id); E.code = null; }
```

### Fluxo de Controle

```nohl
P -> S          { S.next = new Label(); P.code = S.code ++ label(S.next) }
S -> E          { S.code = E.code }
S -> if (B) S1 else S2
                {
                  B.true = new Label();
                  B.false = new Label();
                  S1.next = S2.next = S.next;
                  S.code = B.code
                           ++ label(B.true)
                           ++ S1.code
                           ++ gen("goto", S.next)
                           ++ label(B.false)
                           ++ S2.code
                }
S -> while (B) S1
                {
                   begin = new Label();
                   B.true = new Label();
                   B.false = S.next;
                   S1.next = begin;
                   S.code = label(begin)
                            ++ B.code
                            ++ label(B.true)
                            ++ S1.code
                            ++ gen('goto', begin)
                }
S -> S1 S2      {
                   S1.next = new Label();
                   S2.next = S.next;
                   S.code = S1.code ++ label(S1.next) ++ S2.code
                }

 ```

Podemos otimizar a criação de _labels_ quando não temos o _else_, utilizando:

```nohl
S -> if (B) then S1
                {
                    B.true = fall;
                    B.false = S1.next = S.next;
                    S.code = B.code ++ S1.code;
                }
```

### Tradução de Expressões Booleanas com Curto Circuito

```nohl
B -> true       { B.code = gen('goto', B.true); }
B -> false      { B.code = gen('goto', B.false); }
B -> not B1     { B1.true = B.false; B1.false = B.true; B.code = B1.code }
B -> B1 and B2  {
                  B1.true = new Label();
                  B1.false = B.false;
                  B2.true = B.true;
                  B2.false = B.false;
                  B.code = B1.code ++ label(B1.true) ++ B2.code;
                }
B -> B1 or B2   {
                  B1.true = new Label() if B.true == fall else B.true;
                  B1.false = fall;
                  B2.true = B.true;
                  B2.false = B.false;
                  B.code =
                     if B.true == fall then
                        (B1.code || B2.code || label(B1.true));
                     else
                        (B1.code ++ B2.code)
                }
B -> E1 relop E2
                {
                    test = gen(new Temp(), '=', E1.addr, relop, E2.addr)
                    S = if B.true != fall and B.false != fall then
                            (
                              gen('if', test.addr, 'goto', B.true)
                              ++ gen('goto', B.false)
                            )
                        elif B.true != fall then
                            (gen('if', test.addr, 'goto', B.true))
                        elif B.false != fall then
                            (gen('ifFalse', test.addr, 'goto', B.false)
                        else ()
                    B.code = E1.code ++ E2.code ++ test.code ++ S
                }
```

### Exemplo

Gerar o código para `if (a > b or b < c) then s`:

0. Como não temos `else`, então `B.true = fall` e `B.false = future`
1. Gerar código para `B1 or B2`
```nohl
    B1.true = new Label()   # L1
    B1.false = fall;
    B2.true = fall;
    B2.false = future;
```
    1. Gerar código para `B1 = a > b`
    ```nohl
        E1.code = null
        E1.addr = 'a'
        E2.code = null
        E2.addr = 'b'
        test.addr = new Temp()  # t1
        test.code = "t1 = a > b"
        # Como B1.true != fall e B1.false == fall
        B.code = ["t1 = a > b", "if t1 goto L1"]
    ```
    2. Gerar código para `a < c`
    ```nohl
        E1.code = null
        E1.addr = 'b'
        E2.code = null
        E2.addr = c'
        test.addr = new Label()  # t2
        test.code = "t2 = b < c"
        # Como B2.true == fall e B2.false != fall
        B.code = ["t2 = b < c", "ifFalse t2 goto future"]
    ```
2. Geramos o código do `or` (com `B.true = fall`):
```nohl
    B.code = [
        "t1 = a > b",
        "ifFalse t1 goto L1",
        "t2 = b < c",
        "ifFalse t2 goto future",
        "L1:"
    ]
```
3. E finalmente, geramos o código do `if`:
```nohl
    B.code = [
        "t1 = a > b",
        "if t1 goto L1",
        "t2 = b < c",
        "ifFalse t2 goto future",
        "L1:",
        S.code,
        "future:",
    ]   
```

