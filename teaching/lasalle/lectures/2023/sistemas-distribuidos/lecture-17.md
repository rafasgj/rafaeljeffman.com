---
title: Exercícios e Revisão
subtitle: Sistemas Distribuídos
layout: lecture
last_occurrence: 2023-11-23
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-sistemas-distribuidos
---

## Questão 1

Uma alternativa para o aumento de desempenho de sistemas computacionais é o uso de processadores com múltiplos núcleos, chamados multicores. Nesses sistemas, cada núcleo, normalmente, tem as funcionalidades completas de um processador, já sendo comuns, atualmente, configurações com 4, 8 e 10 núcleos, chegando até 64 núcleos . Com relação ao uso de processadores multicores, e sabendo que threads são estruturas de execução associadas a um processo, que compartilham suas áreas de código e dados, mas mantêm contextos independentes, analise as seguintes asserções.

```nohl
Ao dividirem suas atividades em múltiplas threads que podem
ser executadas paralelamente, aplicações podem se beneficiar
mais efetivamente dos diversos núcleos dos processadores
multicores
```

<span style="display:block; text-align:center; font-weight: 400">PORQUE</span>

```nohl
o sistema operacional nos processadores multicores pode alocar
os núcleos existentes para executar simultaneamente diversas
seqüências de código, sobrepondo suas execuções e, normalmente,
reduzindo o tempo de resposta das aplicações às quais estão
associadas.
```

Acerca dessas asserções, assinale a opção correta.

* As duas asserções são proposições verdadeiras, e a segunda é uma justificativa correta da primeira.
* As duas asserções são proposições verdadeiras, mas a segunda não é uma justificativa correta da primeira.
* A primeira asserção é uma proposição verdadeira, e a segunda, uma proposição falsa.
* A primeira asserção é uma proposição falsa, e a segunda, uma proposição verdadeira.
* Tanto a primeira quanto a segunda asserções são proposições falsas.
{:class="lettered"}

## Questão 2

Sistemas distribuídos são aqueles dispostos em computadores distintos e autônomos, que trabalham juntos para dar a impressão de ser um único sistema, com acesso local a seus usuários. Uma característica importante nesses sistemas é a transparência. Acerca das formas de transparência de um sistema distribuído, assinale a alternativa correta.

* A transparência de acesso oculta diferenças na apresentação de dados e no modo de acesso a um recurso.
* A transparência de replicação oculta que um recurso pode ser movido para outro computador quando em uso.
* A transparência de migração oculta que um recurso pode ser compartilhado por diversos usuários, ao mesmo tempo.
* A transparência de relocação está presente no sistema quando a falha e a recuperação de um recurso são feitas de forma imperceptível ao seu usuário.
* A transparência de localização permite que um recurso possa ser movido de uma localização para outra.
{:class="lettered"}


## Questão 3

Segundo Andrew Tanembaum (2007) Sistema Distribuído é uma coleção de computadores independentes que se apresenta ao usuário como um sistema único e consistente. Assinale a alternativa correta a respeito de um sistema de informação distribuído.

* A distribuição de tarefas se dá a partir de requisições do usuário, que indica o endereço do servidor onde deseja executar tal tarefa.
* Em uma rede de computadores há servidores dedicados a atender pedidos dos clientes e estes, por sua vez, têm função exclusiva de requisitantes.
* Todos os computadores de uma rede executam tarefas de cliente e servidor, quando se deseja integrá-los em uma arquitetura de sistemas distribuídos.
* A transparência de acesso é uma característica dos sistemas distribuídos que permite que recursos sejam acessados sem que sua localização seja determinada.
* Em um sistema de objetos distribuídos é possível invocar métodos de um objeto, ainda que este não esteja presente no computador do usuário. 
{:class="lettered"}


## Questão 4

Uma antiga empresa de desenvolvimento de software resolveu atualizar toda sua infraestrutura computacional adquirindo um sistema operacional multitarefa, processadores multi-core (múltiplos núcleos) e o uso de uma linguagem de programação com suporte a threads.  O sistema operacional multitarefa de um computador é capaz de executar vários processos (programas) em paralelo. Considerando esses processos implementados com mais de uma thread (multi-threads).

Esse cenário é até hoje muito comum, e para mostrar que você está apto a auxiliar uma empresa nesta situação, responda as seguintes questões:

1. Corrija a seguinte frase de forma que ela seja verdadeira:
"Threads de diferentes processos compartilham memória."

2. Como sistemas monoprocessados (um único processador com um único _core_) podem ser projetados de forma a permitir a execução de sistemas _multi-thread_ ?

3. Caso a migração do sistema da empresa fosse realizada para um sistema distribuído, qual seria o plano de migração da empresa e que riscos ela deveria se preparar para enfrentar? Como é possível mitigar esses riscos?


## Questão 5


Acerca do conceito de sistemas distribuídos, analise as proposições abaixo.

1. Um sistema distribuído é uma coleção de computadores autônomos conectados por uma rede e equipados com um sistema de software distribuído.
2. Um sistema distribuído é uma coleção de computadores independentes, que aparenta ao usuário ser um computador único.
3. Em um sistema distribuído a falha de um computador do qual nunca se ouviu falar faz com que seu computador ou software pare completamente de funcionar.
4. multiprocessadores são sistemas fortemente acoplados, enquanto que multicomputadores são sistemas fracamente acoplados.

Estão corretas as proposições:

* 1, 2 e 3, apenas.
* 1, 2 e 4, apenas.
* 1, 3 e 4, apenas. 
* 2, 3 e 4, apenas.
* 1, 2, 3 e 4.
{:class="lettered"}


## Questão 6

Um sistema distribuído é um conjunto de sistemas autônomos, interconectados por uma rede de comunicação, que se diferencia dos demais sistemas fracamente acoplados pela existência de um relacionamento mais forte entre os seus componentes. Tais componentes...

* podem estar localizados em uma rede local ou em uma rede distribuída e os tipos de sistemas operacionais que compõem o sistema distribuído não precisam ser necessariamente homogêneos.
* podem estar localizados em uma rede local ou em uma rede distribuída, mas os tipos de sistemas operacionais que compõem o sistema distribuído devem ser necessariamente homogêneos.
* devem estar localizados em uma rede local e os tipos de sistemas operacionais que compõem o sistema distribuído não precisam ser necessariamente homogêneos.
* devem estar localizados em uma rede local e os tipos de sistemas operacionais que compõem o sistema distribuído devem ser necessariamente homogêneos.
* devem estar localizados em uma rede distribuída e os tipos de sistemas operacionais que compõem o sistema distribuído devem ser necessariamente homogêneos.
{:class="lettered"}


## Questão 7


Analise as afirmativas a seguir, a respeito de sistemas distribuídos.

1. Em um sistema distribuído se uma máquina falha, o sistema precisa ser reinicializado e retoma as atividades do ponto que parou.
2. Um sistema distribuído pode evoluir de forma modular, incrementando o número ou capacidade das unidades, de acordo com as necessidades da aplicação.
3. A comunicação distribuída através de uma rede tem um custo adicional importante, introduzindo um acréscimo do tempo de transmissão de mensagens que é pelo menos uma ordem de grandeza superior ao da comunicação local.

Está(ão) correta(s) a(s) afirmativa(s):

* 1, apenas.
* 2, apenas.
* 1 e 2, apenas.
* 2 e 3, apenas.
* 1, 2 e 3.
{:class="lettered"}


## Questão 8

Considerando-se as características de um sistema distribuído e de acordo com:

1. Escalabilidade.
2. Segurança.
3. Concorrência.

Numere as afirmações:
* [&nbsp;&nbsp;&nbsp;] A criptografia pode ser usada para proporcionar proteção adequada para os recursos compartilhados e para manter informações em sigilo quando transmitidas em mensagens de uma rede.
* [&nbsp;&nbsp;&nbsp;] Os algoritmos usados para acessar os dados compartilhados devem evitar gargalos de desempenho, e os dados devem ser estruturados hierarquicamente para se obter os melhores tempos de acesso. Os dados acessados frequentemente podem ser replicados.
* [&nbsp;&nbsp;&nbsp;] A presença de múltiplos usuários em um sistema distribuído é uma fonte de pedidos concorrentes para seus recursos.
{:style="list-style:none;"}

Assinale a alternativa que apresenta a sequência CORRETA:

* 1 - 2 - 3.
* 3 - 2 - 1.
* 2 - 3 - 1.
* 2 - 1 - 3.
* 1 - 3 - 2
{:class="lettered"}


## Questão 9

Sabendo que a tolerância a falhas inclui os seguintes conceitos:

1. O requisito disponibilidade (_availability_) em um sistema distribuído está relacionado com a probabilidade de o sistema funcionar corretamente em dado momento e realizar suas funções em benefícios dos seus usuários.
2. O requisito confiabilidade (_reliability_) é definido em termos de intervalo de tempo ao invés de um “dado momento” como na “_availability_”, refere-se à habilidade do sistema funcionar continuamente sem falhas.
3. O requisito Segurança (_security_) refere-se à situação na qual um sistema falha temporariamente ou deixa de operar corretamente sem nenhum acontecimento catastrófico.
4. O requisito Manutenibilidade (_maintainance_) refere-se à capacidade do sistema em ser corrigido, talvez, automaticamente.

Projete um sistema tolerante a falhas, detalhando como as falhas que podem ocorrer são evitadas, contornadas ou corrigidas.
