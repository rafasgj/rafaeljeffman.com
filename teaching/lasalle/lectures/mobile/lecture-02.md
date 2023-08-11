---
title: Revisão dos conceitos de desenvolvimento Web
subtitle: Desenvolvimento para Dispositivos Móveis
layout: lecture
last-occurrence: 
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-mobile
---

## Assunto

1. Revisão sobre desenvolvimento Web
    1. Estado de uma aplicação
    2. Arquitetura cliente-servidor
    3. Processamento no servidor vs. Processamento no cliente
2. Revisão de HTML
3. Revisão de CSS
4. Revisão sobre JavaScript
    1. Variáveis:
        * Sempre use `const` quando o valor não deve ser alterado. ex.: `const x = 5;`
        * Sempre use `const` quando o tipo de dado não deve ser alterado. ex.: [Arrays e Objetos](https://repljs.com/new?local=c5bbc08c-393c-4926-9ae9-c9d43764dd35){:target="\_blank"}
        * Use `let` somente quando não for possível usar `const`. ex.: `let y =3;`
    2. Índices de _Arrays_ são `base-0`.
    3. _Strings_ são imutáveis.
    4. Tuplas são semelhantes a arrays, porém, são imutáveis. ex.: `const t = #[1,2,3,4,5]`
    5. Funções são [parecidas com as funções de outras linguagens](https://www.w3schools.com/js/js_functions.asp) como Java ou C.
    6. Podemos definir funções usando a _sintaxe de flecha_ (_arrow syntax_), quando necessitamos de uma função:
```javascript
const data = [1,2,3,4,5]
data.map((value) => { value * 2})
```
5. Sugestões de pesquisa para a próxima aula
    1. [TypeScript Tutorial](https://www.w3schools.com/typescript/index.php)(W3Scchools)
    2. [React Quick Start](https://react.dev/learn)
    3. [React Interactive Tutorial](https://react-tutorial.app/)

## Questões

1. **Projeto:** Crie uma calculadora com operações básicas utilizando apenas HTML, CSS e Javascript. Como essa aplicação se comporta em diferentes dispositivos?
2. **Projeto:** Publique sua calculadora como um _site_ estático no Github Pages

## Recursos para essa aula

### Tutoriais Desenvolvimento Web

1. [HTML Tutorial](https://www.w3schools.com/html/)(W3Schools)
2. [CSS Tutorial](https://www.w3schools.com/Css/)(W3Schools)
3. [Sass Tutorial](https://www.w3schools.com/sass/)(W3Schools)
4. [JavaScript Tutorial](https://www.w3schools.com/js/DEFAULT.asp)(W3Schools)

### REPL Javascript

1. [REPL JS](https://repljs.com): _Read-Eval-Print-Loop_ Javascript

### Tutoriais do Git

10. [Pro Git](https://git-scm.com/book/pt-br/v2) (Tradução parcial do livro para português do Brasil)
11. [Git - Guia prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html): Um guia bem direto, sem muita explicação.
12. [Github - Início Rápido](https://docs.github.com/pt/get-started/quickstart)
