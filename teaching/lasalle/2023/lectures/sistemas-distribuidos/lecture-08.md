---
title: Exercícios
subtitle: Sistemas Distribuídos
layout: lecture
last_occurrence: 2023-21-09
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-sistemas-distribuidos
---

<style>
td { border: solid thin #022; padding: 10px 15px 5px 15px; vertical-align: top; width: 50%; }
th { border: solid thin #022; background-color: #ccc; padding: 10px 15px 5px 15px; vertical-align: top; width: 50%; text-align: center !important; font-weight: 600 !important; }
</style>

> **Nota**: Todas as questões foram extraídas de provas do ENADE, e podem ter sofrido alterações.

## Questão 1

Um sistema monitora o deslocamento de um carro por maio do registro em um banco de dado, de segundo em segundo, das medidas de dois acelerômetros: um na direção langitudinal do movimento do carro, um na direção transversal.

O projeto desse sistema é decomposto em três subprojetos. O primeiro, denominado MÓDULO\_1, formado por _hardware_ e _software_, é embarcado no carro e dotado de sistema de comunicação com a Internet por GPRS. O segundo, MÓDULO\_2, é um projeto de _software_ aplicativo executado em plataforma Android para _tablet_ ou _smartphone_, para exibição de relatórios para usuários. O terceiro subprojeto, MÓDULO\_3, é formado por _hardware_ e _software_ instalado em um servidor em nuvem com conexão dedicada permanente com a internet.

O projeto tem as seguintes especificações:
* o MÓDULO\_1 comunica-se com o MÓDULO\_3 para enviar as leituras obtidas. Como o carro nem sempre está em área de cobertura de celular, é possível que uma comunicação possa enviar as leituras de até um dia inteiro;
* o MÓDULO\_2 comunica-se com o MÓDULO\_3 para obter os dados exibidos no relatório;
* os relatórios indicam os valores máximos de velocidade e aceleração e as respectivas posições do carro quando eles foram atingidos.

A partir dessas informações, avalie as afirmações a seguir:

1. O MÓDULO\_1 deve ter capacidade de armazenamento de dados suficiente para um dia de leituras, a serem enviadas para o MÓDULO\_3.
2. Todos os subprojetos têm interface de comunicação pela internet e a interface com o usuário é feita no MÓDULO\_2.
3. O melhor local para se executar o processamento dos dados para o relatório é o MÓDULO\_1, que está sempre conectado e tem maior capacidade de processamento.
4. O melhor local para se instalar o banco de dados para as leituras é o MÓDULO\_3, que dispõe de maior capacidade de armazenamento e conexão permanente com a internet.

É correto apenas o que se afirma em:

* 1 e 3
* 2 e 3
* 2 e 4
* 1, 2 e 4
* 1, 3 e 4
{:class="lettered"}

Justifique as afirmações consideradas falsas.


## Questão 2

Quando um computador é multiprogramado, ele geralmente tem múltiplos processos ou _threads_ que competem pela CPU ao mesmo tempo.  Essa situação ocorre sempre que dois ou mais processos estão simultaneamente no estado pronto. Se somente uma CPU se encontrar disponível, deverá ser feita uma escolha de qual processo executar em seguida. A parte do sistema operacional que faz a escolha é chamada de escalonador, e o algoritmo que ele usa é o algoritmo de escalonamento.
<span class="bibtex">TANENBAUM, A. S. Sistemas Operacionais Modernos.<br/>3. ed., São Paulo: Pearson, 2010 (adaptado)</span>

Considerando que em ambientes diferentes são necessários algoritmos diferentes de escalonamento, garantindo assim que seja maximizado o uso de seus recursos, assinale a opção que apresenta um algoritmo de escalonamento seguido do tipo de ambiente no qual deva ser implementado.

* Primeiro a chegar, último a sair (_first in, last out_ - FILO); propício para sistemas de tempo real.
* Escalonamento por taxas monotônicas (_rate monotonic scheduling_ - RMS); propício para sistemas em lote.
* Tarefa mais curta primeiro; propício para sistemas interativos.
* Escalonamento por chave circular (_round-robin_); propício para sistemas de tempo real.
* Escalonamento por prioridades; propício para sistemas interativos.
{:class="lettered"}


## Questão 3

Durante parte do tempo, um processo está ocupado realizando computações internas e outras coisas que não levam a condições de corrida. No entanto, às vezes, um processo tem de acessar uma memória compartilhada ou arquivos, ou realizar outras tarefas críticas que podem levar a corridas. Essa parte do programa onde a memória compartilhada é acessada é chamada de região crítica ou seção crítica. Se conseguíssemos arranjar as coisas de maneira que dois processos jamais estivessem em suas regiões críticas ao mesmo tempo, poderíamos evitar as corridas. Embora essa exigência evite as condições de corrida, ela não é suficiente para garantir que processos em paralelo cooperem de modo correto e eficiente usando dados compartilhados. Precisamos que quatro condições se mantenham para chegar a uma boa solução.

1. Dois processos jamais podem simultaneamente estar dentro de suas regiões críticas.
2. Nenhuma suposição pode ser feita a respeito de velocidades ou de número de CPUs.
3. Nenhum processo executando fora de sua região crítica pode bloquear qualquer processo.
4. Nenhum processo deve ser obrigado a esperar eternamente para entrar em sua região crítica.

Em um sentido abstrato, o comportamento que queremos é mostrado na figura a seguir:

![Exclusão mútua usando regiões críticas](files/lecture-08/exclusao_mutua_usando_regioes_criticas.png){:style="max-width:70%"}
<span class="bibtex">TANENBAUM, A. S. Sistemas Operacionais Modernos.<br/>4. ed. Versão para Biblioteca Virtual Pearson.<br/>São Paulo: Pearson Education do Brasil, p. 83, 2016 (adaptado)</span>
{:style="margin:0 auto;text-align:center"}


Considerando o texto e a figura apresentados, avalie as asserções a seguir e a relação proposta entre elas.

1. Em algumas situações, a exclusão mútua pode ser obtida por meio da desabilitação da interrupção controlada pelo Sistema Operacional, não sendo permitido que o seu controle seja feito pelo usuário.
<span style="display:block; text-align:center; font-weight: 400">PORQUE</span>
2. A desabilitação da interrupção é uma técnica que pode impedir que o processador que está executando um processo em sua região crítica seja interrompido para executar outro código, sendo mais eficiente em sistemas de multiprocessadores devido a quantidade de processos concorrentes.

A respeito dessas asserções, assinale a opção correta:

* As asserções 1 e 2 são proposições verdadeiras, e a 2 é uma justificativa correta da 1.
* As asserções 1 e 2 são proposições verdadeiras, mas a 2 não é uma justificativa correta da 1.
* A asserção 1 é uma proposição verdadeira, e a 2 é uma proposição falsa.
* A asserção 1 é uma proposição falsa, e a 2 é uma proposição verdadeira.
* As asserções 1 e 2 são proposições falsas.
{:class="lettered"}

Justifique as afirmações consideradas falsas, ou por que a afirmação são 2 não justifica a afirmação 1.


## Questão 4

Um programador inexperiente está desenvolvendo um sistema _multithread_ que possui duas estruturas de dados diferentes, `E1` e `E2`, as quais armazenam valores inteiros. O acesso concorrente a essas estruturas é controlado por semáforos. Durante a sua execução o sistema dispara as _threads_ `T1` e `T2` simultaneamente. A tabela a seguir possibilita uma visão em linhas rerais dos algolritmos dessas _threads_:

|  `T1` | `T2` |
| :---- | :--- |
| Aloca `E1` | Aloca `E2` |
| Calcula a média `M1` | Calcula a soma `S1` de todos os valores de `E2` |
| Aloca `E2` | Aloca `E1` |
| Calcua a média `M2` dos valores de `E2` | Calcula a soma `S2` de todos os valores de `E1` |
| Calcula `M3 = M1 + M2` | Calcula `S3 = |S1 - S2|` |
|Soma `M3` em todos os valores de `E2` | Subtrai `S2` de todos os valores de `E1` |
| Libera `E1` | Libera `E2` |
| Libera `E2` | Libera `E1` |

Durate a execução do referido programa, é possível que:

* não ocorra _deadlock_, porue a sequência de alocação dos recursos impede naturalmente o problema.
* ocorra _deadlock_, que pode ser evitado se o programador tomar o cuidado de não executar cálculos entre um pedido de alocação e outro.
* ocorra _deadlock_, sendo a probabilidade dessa ocorrência tão baixa e sua consequência tão inócua que não haverá comprometimento do programa.
* não ocorra _deadlock_, desde que o programador use semáforos para controlar o acesso às estruturas de dados, o que é suficiente para evitar o problema.
* ocorra _deadlock_, que pode ser evitado se o programador tomar o cuidade de solicitar o acesso às estruturas de dados na mesma ondem em ambas as _threads_.
{:class="lettered"}

Justifique as respostas consideradas incorretas.

