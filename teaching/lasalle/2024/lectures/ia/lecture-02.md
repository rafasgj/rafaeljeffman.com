---
section: Inteligência Artificial
title: Objetivos, Solução de Problemas, Raciocínio
subtitle:
layout: lecture
last_occurrence: 2024-03-11 
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/ia
---
<style>
dt {
    font-size: 115%;
    margin-top: 10px;
}
</style>

## O que é Inteligência Artificial?

* O que é inteligência?
* O que é ser inteligente?

Alguns autores já definiram inteligência, em relação a inteligência artificial, como **comportamento com eficácia comparável à humana**. Outros preferem definições mais abstratratas como _realizar a ação correta_, ao que chamamos de **racionalidade**.

Variam também o motivo pelo qual se define um ser inteligente, pelo **processo de pensamento** ou **raciocínio**, ou pelo **comportamento inteligente**, ou seja uma caracterização externa.

1. Agindo humanamente: o Teste de Turing
    : Baseado na pergunta _Podem as máquinas pensar?_, frase de um artigo de Alan Turing (1950) onde é proposto um teste onde, após interação com um sistema que responde ações de um interrogador humano, considera-se que o sistema é inteligente se o interrogador não consegue dicernir se o ator do sistema é humano ou não.
    : Conceitos necessários para o sucesso no teste incluem:
        * Processamento de Linguagem Natural
        * Representação de Conhecimento
        * Raciocínio automatizado
        * Aprendizagem de Máquina
    : Uma variação do teste proposta como _Teste de Turing Total_, incluiria _visão computacional_, _reconhecimento de voz_, _robótica_.  

2. Pensando humanamente, a abordagem de modelagem cognitiva
    : Para tentar simular a forma de pensamento humano, precisamos conhecer como o ser humano pensa, através, por exemplo:
        * Introspecção: pensear sobre o nosso pensamento enquanto ele ocorre
        * experimentos psicológicos
        * imagens do cérebro
    : O campo da **ciência cognitiva** é fascinante, e tenta juntar modelos computacionais e psicologia para entender e simular o funcionamento do cérebro humano.

3. Pensando racionalmente: as _regras do pensamento_
    : Aristóteles (325 A.C.) foi uma das primeiras pessoas a tentar codificar a forma como raciocinamos, e criou padrões para estruturas de argumentos (os **silogismos**) que semper trariam conclusões corretas dado premisas corretas. O exemplo clássico é "Sócrates é um homem, todos os homens são mortais, logo, Sócrates é mortal". Estas "leis do pensamento" deram início ao estudo da **lógica**.
    : O principal problema desta abordagem é que exigem uma _certeza_ das afirmações que na prática não existem no mundo real. A **teoria da probabilidade** ajuda a mitigar essa limitação, permitindo raciocínio rigoroso a partr de informações incertas e imprecisas.

4. Agindo racionalmente: a abordagem de agentes racionais
    : Um **agente** é, simplesmente, algo que atua. Espera-se que um **agente inteligente** opere autonomamente, perceba o ambiente em que está inserido, persista por um longo período, adapte-se a mudanças e busque objetivos. Um **agente racional** é um agente que atua de forma a obter o melhor resultado possível, mesmo frente a incertezas.
    : A inteligência artificial tem focado na construção de agentes que **fazem a coisa certa**

### Máquinas Benéficas (_Beneficial Machines_)

Uma das dificuldades de se definir o que significa _fazer a coisa certa_ é fazer com que uma máquina autonoma entenda que nem sempre a melhor de decisão é a decisão correta.

Por exemplo, para um carro autonomo, cujo objetivo é _chegar a um destino com segurança_, o sistema precisa entender que _mesmo que o mais seguro seja não sair da garagem_, é necessário correr algum risco ou não será possível chegar a nenhum destino.

Uma vez que o sistema foi convencido que precisa sair da garagem, como definir que as suas ações mais seguras sejam seguras não apenas para si, mas para outros veículos? Como fazer com que o sistema não importune outros veículos enquanto tenta atingir seus objetivos? Quanto o veículo deve frear ou acelerar, pensando no conforto dos passageiros?

Esse tipo de questão é particularmente importante e difícil de responder quando pensamos na interação homem-máquina.

## Fundamentos da Inteligência Artificial

A inteligência artificial, hoje em dia, é uma multi-disciplinar, e sofreu influência de várias áreas como:

* Filosofia
    * Como chegar a conclusões válidas?
    * Como a mente surge a partir de um cérebro físico?
    * De onde vem o conhecimento?
    * Como o conhecimento leva a uma ação?
    * Onde entra a ética na Inteligência Artificial?
        * Utilitarismo: decisões racionais que se baseiam na máxima utilidade deveriam ser aplicáveis a qualquer esfera da atividade humana.
        * Ética Deontológica (Immanuel Kant): "fazer a coisa certa" é determinado não pelos resultados, mas sim pelas leis universais que regem o convívio social dos seres humanos.
* Matemática
    * Quais formalismos de regras nos levam a conclusões válidas?
    * O que pode ser computado?
    * Como raciocinar com informações incertas?
    * Uma vez que o problema é computável, ele é solucionável em tempo adequado, ou seja, o problema é tratável?
* Economia
    * Como tomar uma decisão de acordo com nossas preferências?
    * Como fazer algo quando outros não acompanham?
    * Como realizar uma ação que só vai trazer resultados num futuro distante?
* Neurociência
    * Como o cérebro processo informações?
* Psicologia
    * Como humanos e animais pensam e agem?
* Engenharia/Ciência da Computação
    * Como criar uma máquina eficiente?
* Teoria de Controle e Cibernética
    * Como artefatos operam sobre seu próprio controle?
* Linguística
    * Como a linguagem se relaciona com o pensamento?

## Estado da Arte

* Visão computacional
    : Melhora em detecção de objetos de 72% para 98%, ganhando do ser humano.
    : Resposta a questões visuais (abertas) em 68%, ainda bem inferior aos 83% do ser humano.
* Velocidade de treinamento caiu por um fator de 100.
* Linguagem: acurácia ao responder questões em um banco de dados pré-definido superior a dos seres humanos.
* Em relação aos seres humanos:
    : Em 2019, sistemas de IA são mais eficientes que seres humanos em Xadrez, Go, Poker, Pac-Man, Jeopardy!, detecção de objetos na ImageNet, reconhecimento de voz em domínios limitados, Quake 3, Dota 2, StarCraft 2, diversos jogos do Atari 2600, detecção de cancer de pele e próstata e no diagnóstico de retinopatia diabética.
* Veículos Robóticos:
    * Carros: eles já estão entre nós, porém já tivemos acidentes fatais.
    * Aéreos: em Ruanda, drones entregam sangue para hospitais. No mundo todo, os EUA entregam, outras coisas.
* Locomoção com pernas: quadrúpedes e bípedes se movem em alta velocidade
* Planejamento e escalonamento: Diversas aplicações já fazem uso: militares, Nasa, Uber
* Tradução por máquinas: em domínios limitados a tradução já é equivalente ou melhor que a do ser humano.

## Riscos e Benefícios da IA

* Armas letais
* Vigilância e persuasão
* Decisões com viés
* Impacto na empregabilidade
* Aplicações com segurança crítica
* Cybersegurança

## Exercícios

1. Implemente uma árvore binária em Python, onde cada nó da árvore é uma tupla contendo `(nó_esquerdo, nó_direito, valor)`, de forma que os seguintes algoritmos possam ser executados:

```python
def pre_order(node, function):
    if node is not None:
        left, right, valor = node
        pre_order(left, function)
        pre_order(right, function)
        function(valor)

def in_order(node, function):
    if node is not None:
        left, right, valor = node
        in_order(left, function)
        function(valor)
        in_order(right, function)

def post_order(node, function):
    if node is not None:
        left, right, valor = node
        function(valor)
        post_order(left, function)
        post_order(right, function)
```
Por exemplo, a chamada `in_order([((None, None, 1), (None, None, 2), 3), ((None, None, 5), (None, None, 7), 6),  4], print)` produz a saída
```
1
2
3
4
5
6
7
``` 
> Embora não seja necessário, e não seja recomendado, você pode implementar a árvore como uma árvore binária de pesquisa.

## Preparação para a próxima aula

* Capítulo 2 do livro [**Inteligência artificial : uma abordagem moderna.**](https://integrada.minhabiblioteca.com.br/reader/books/9788595159495){:target='\_blank'}
* Capútulo 3, até a seção 3.4 (inclusa) do livro [**Inteligência artificial : uma abordagem moderna.**](https://integrada.minhabiblioteca.com.br/reader/books/9788595159495){:target='\_blank'}
* Lecture 3 e 4 do curso [MIT 6034 Artificial Intelligence](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/video_galleries/lecture-videos/) (en)

## Recursos para essa aula

### Bibliografia

* Capítulo 1 do livro [**Inteligência artificial : uma abordagem moderna.**](https://integrada.minhabiblioteca.com.br/reader/books/9788595159495){:target='\_blank'}

### Videos

* Lecture 1 e 2 do curso [MIT 6034 Artificial Intelligence](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/video_galleries/lecture-videos/) (en)

