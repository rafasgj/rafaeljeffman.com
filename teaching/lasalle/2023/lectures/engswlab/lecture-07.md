---
title: Exercícios
section: Laboratório de Engenharia de Software
layout: lecture
last_occurrence: 2023-09-19
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-engswlab
---

> **Nota**: Todas as questões foram extraídas de provas do ENADE, e podem ter sofrido alterações.

## Questão 1

_Duas técnicas comumente utilizadas para ampliar as informações básicas sobre requisitos são personas
e cenários. Frequentemente usadas juntas, essas técnicas se complementam de forma a trazer detalhes
realísticos que possibilitam ao desenvolvedor explorar as atividades atuais do usuário, uso futuro de
novos produtos e visões futuristas de novas tecnologias. Elas também podem guiar o desenvolvimento
ao longo do ciclo de vida do produto._
<span class="bibtex">ROGERS, Y.; PREECE, J.; SHARP, H. Interaction Design: beyond human-computer interaction.<br/>5. ed. Indianapolis, IN, USA: John Wiley & Sons, Inc., 2019 (adaptado).</span>

Com base no texto apresentado e sobre os objetivos do uso de personas e cenários em um processo de
elicitação de requisitos, avalie as afirmações a seguir.

1. O uso de personas e cenários, em um processo de elicitação, explicita algumas situações que
aparecem implícitas nos requisitos.
2. O uso de personas e cenários, em um processo de elicitação, ajuda o projetista a entender melhor
o impacto das decisões de projeto.
3. O uso de personas e cenários, em um processo de elicitação, facilita a especificação formal
e não-ambígua dos requisitos de interação.
4. O uso de personas e cenários, em um processo de elicitação, lembra à equipe de desenvolvimento
que pessoas reais usarão o produto.

É correto o que se afirma em:

*  1 e 3
*  1 e 4
*  2 e 3
*  1, 2 e 4
*  2, 3 e 4
{:class="lettered"}

Justifique as afirmações consideradas falsas.

## Questão 2 ##

_O surgimento das metodologias ágeis eliminou o gerenciamento baseado em planos, substituindo-o
pelo planejamento incremental. A documentação de projeto foi reduzida ao mínimo e deixou de ser
previsto um gerente de projeto. Infelizmente, esse tipo de abordagem não atende as necessidades das
organizações, em que gerentes de negócio necessitam acompanhar o andamento dos projetos, controlar
orçamento, estabelecer prioridades e atualizar seus planos de negócio. Nesse contexto, foi desenvolvido
o SCRUM, um framework para a organização de projetos ágeis. O SCRUM prevê dois indivíduos: o
Scrum Master e o Product Owner, que são responsáveis por atuar como interface entre a equipe de
desenvolvimento e a organização._
<span class="bibtex">SOMMERVILLE, I. Engineering Software Products: An Introduction to Modern Software Engineering.<br/> Boston: Pearson, 2019 (adaptado).</span>

Em relação à metodologia _Scrum_, avalie as afirmações a seguir.
1. O papel do _Scrum Master_ é guiar a equipe no uso efetivo da metodologia _Scrum_.
2. O papel do _Product Owner_ é garantir o foco no produto, evitando que o mesmo se perca em questões técnicas menos relevantes.
3. Tanto o _Scrum Master_ como o _Product Owner_ têm autoridade direta sobre a equipe.

É correto o que se afirma em

* 2, apenas.
* 3, apenas.
* 1 e 2, apenas.
* 1 e 3, apenas.
* 1, 2 e 3.
{:class="lettered"}

Justifique as afirmações consideradas incorretas.


## Questão 3 ##

Uma empresa pretende desenvolver um sistema de folha de pagamento cujo processo de modelagem utilizará UML (Unified Modeling Language). Essa empresa tem três tipos de colaborador: o comissionado, o horista e o assalariado. Todos os colaboradores registram, para efeito de controle, o número de horas trabalhadas no mês. Adicionalmente, os comissionados registram o valor do percentual de comissão e o valor total de vendas acumulado no mês; os horistas registram o valor recebido por hora; e os assalariados registram o valor do salário.

Cada colaborador pertence a um departamento e cada departament possui pelo menos um colaborador. No final de cada mês, cada departament deve calcular o salário dos seus colaboradores da seguinte forma: os comissionados devem receber o valor total das vendas multiplicado pela porcentagem independentemente do número de horas trabalhadas; os horistas devem receber o valor da hora trabalhada multipilcado pelo número de horas trabalhadas; e os assalariados devem receber o valor nominal do salário.

Considerando essa situação e que o modelo que será elaborado para representá-la utilizará herança e polimorfismo, desenhe um diagrama ULM que contenha:

* as classes que representam as entidades mencionadas (departamento, colaborador e seus tipos);
* as respectivas associações, atributos e métodos, não sendo necessário tipar os atributos;
* eventuais classes abstratas com a indicação da restrição `{abstract}`;
* a multiplicidade de papel das associações;
* ao lada de cada ocorrência do método para cálculo do pagamento, sua definição na forma de uma expressão que combine os valores dos atributos da classe.


## Questão 4 ##

Considere os seguintes requisitos para desenvolvimento de uma solução para uma rede de restaurantes fast-food:
> Quando o _status_ de um pedido é atualizado, todos os dispositivos dos envolvidos devem receber a informação. Os sistemas a ser atualizados incluem os acessados pelo entregador, pela linha de produção e pela central de atendimento. Espera-se ainda que outros sistemas possam ser incluídos futuramente (por exemplo, sistema de pedido _on-line_ do cliente), devendo se comportar da mesma forma.

Considerando esse contexto, avalie as asserção a seguir e a relação proposta entre elas:
1. O requisito apresentada pode ser implementado com a utilização do padrão de projeto _Observer_,
<span style="display:block; text-align:center; font-weight: 400">PORQUE</span>
2. O padrão de projeto _Observer_ realiza o estilo arquitetural cliente-servidor, no qual a servidor é responsável por enviar notificações aos clientes sempre que houver atualização em alguma informação de interesse.

A respeito dessas asserções, assinale a opção correta:

* As asserções 1 e 2 são proposições verdadeiras, e a 2 é uma justificativa correta da 1.
* As asserções 1 e 2 são proposições verdadeiras, mas a 2 não é uma justificativa correta da 1.
* A asserção 1 é uma proposição verdadeira e a 2 é uma proposição falsa.
* A asserção 1 é uma proposição false e a 2 é uma proposição verdadeira.
* As asserções 1 e 2 são proposições falsa.
{:class="lettered"}

Justifique as afirmações consideradas falsas, ou por que a afirmação 2 não é justificativa correta da 1.


## Questão 5 ##

O encapsulamento é um mecanismo da programação orientada a objetos no qual os membros de uma classe (atributos e métodos) constituem uma caixa preta. O nível de visibilidade dos membros pode ser definido pelos modificadores de visibilidade `privado`, `público` e `protegido`.

Com relação ao comportamento gerado pelos modificadores de visibilidade, assinale a opção correta.

* Um atributo privado pode ser acessado pelos métodos privados da própria classe e pelos métodos protegidos das suas classes descendentes.
* Um atributo privado pode ser acessado pelos métodos públicos da própria classe e pelos métodos públicos das suas classes descendentes.
* Um membro público é visível na classe à qual ele pertence, mas não é visível nas suas classes descendentes.
* Um método protegido não pode acessar os atributos privados e declarados na própria classe.
* Um membro protegido é visível na classe à qual pertence e em suas classes descendentes.
{:class="lettered"}

Justifique porque as outras alternativas não estão corretas.


## Questão 6 ##

Os métodos ágeis são fundamentados no desenvolvimento e entrega incremental tendo em vista atender aos requisitos dos clientes. Eles agrepam um conjunto de princípios provenientes do manifesta ágil, tais como:
* envolvimento do cliente;
* entrega incremental;
* pessoas, não processos;
* aceitação das mudanças;
* manutenção da simplicidade.

O _Scrum_ é um exemplo de método ágil de gerenciamento de projetos. Avalie as afirmações a seguir sobre a relação edo _Scrum_ com os princípios do manifesto ágil.

1. O _Scrum_ adota a entrega incremental por meio de _Sprints_.
2. O _Scrum_ adota a simplicidade por meio do uso da programação em pares.
3. O _Scrum_ adota o envolvimento do cliente com a priorização e a negociação dos requisitos na concepção de _Sprints_.

É correto o que se afirma em

* 2, apenas
* 3, apenas
* 1 e 2, apenas
* 1 e 3, apenas
* 1, 2 e 3 

Justifique as afirmações consideradas incorretas.


## Questão 7 ##

Uma loja pretende desenvolver um sistema cujo processo de modelagem utilizará UML
(_Unified Modeling Language_).

Essa empresa tem dois tipos de colaboradores, o atendente e o gerente, e a principal atividade a ser automatizada pelo sistema é o processamento de vendas, cuja execução é
altamente complexa. Dessa forma, a modelagem deve ser realizada de maneira estruturada e organizada, tendo como foco a sua reutilização em diferentes contextos.

Da conversa com a empresa, descobriu-se que:
* As vendas são realizadas quase integralmente por atendentes, entretanto, caso haja grande quantidade de clientes, os gerentes também podem
processar vendas, por exemplo.
* O processamento de vendas pode ser realizado considerando duas modalidades de pagamento: a prazo ou à vista, todavia, independentemente da forma de pagamento,
há um conjunto comum de ações que sempre são realizadas.
* As compras a prazo englobam dois modos de pagamento (via cartão de crédito e via boleto) que possuem ações comuns, mas que se diferem nas ações finais.
* Para algumas formas de processamento de vendas é aplicado um desconto sobre o valor total. O desconto deve ser aplicado sempre que o pagamento for realizado à vista ou quando
o pagamento for realizado via boleto com parcelamento em até seis vezes. Entretanto, a loja oferece como forma de pagamento boleto com parcelamento em até doze vezes.
* No processamento de vendas, após a confirmação do pagamento, é necessário emitir a nota fiscal dos produtos. Apenas em circunstâncias em que algum dos produtos vendidos não possam ser retirados na loja, deve ser possível solicitar a entrega pelo sistema.

Considerando a situação apresentada no texto, elabore um **Diagrama de Caso de Uso** completo para esse sistema, identificando os atores, os casos de uso e os relacionamentos.


## Questão 8 ##

O gestor de uma instituição seguradora solicitou ao desenvolvedor de software o projeto de uma solução
computacional para a instituição. Após executar a análise de requisitos, esse desenvolvedor esboçou o
diagrama UML (Unified Modeling Language), contendo os elementos apresentados na figura a seguir.

![Diagrama de Classe](files/lecture-07/diagrama-classe.png){:style="max-width: 70%"}
{:style="margin:0 auto;text-align:center"}

Em relação ao que é proposto no diagrama, avalie as afirmações a seguir.

1. A classe Seguro é a superclasse de uma hierarquia de herança múltipla.
2. O mecanismo de ligação entre as classes Segurado e Seguro é a associação.
3. As subclasses Residencial, Automotivo e Vida devem ser implementadas como classes abstratas.
4. É permitido que um Segurado possa adquirir várias apólices de Seguro.

É correto apenas o que se afirma em

* 1 e 3.
* 2 e 3.
* 2 e 4.
* 1, 2 e 4.
* 1, 3 e 4.
{:class="lettered"}

Justifique as alternativas incorretas.


## Questão 9 ##

No desenvolvimento do módulo de integração do sistema do SAMU com os sistemas de hospitais,
um analista gerou o seguinte diagrama de sequência.

![Diagrama de Sequência](files/lecture-07/diagrama-sequencia.png){:style="max-width:90%;"}
{:style="margin:0 auto;text-align:center"}

Com relação ao diagrama apresentado, avalie as asserções a seguir e a relação proposta entre elas.

1. As chamadas `4:procurarVaga()` e `5:procurarVaga()` são feitas simultaneamente (em paralelo) pela
API para minimizar o tempo de espera da chamada `2: procurarLeitos().`
<span style="display:block; text-align:center; font-weight: 400">PORQUE</span>
2. As chamadas `10:definirVaga()` e `12:definirVaga()` são feitas simultaneamente (em paralelo),
mas a espera do retorno é feita em sequência, o que aumentará o tempo de resposta.

A respeito dessas asserções, assinale a opção correta.

* As asserções 1 e 2 são proposições verdadeiras, e a 2 é uma justificativa correta da 1.
* As asserções 1 e 2 são proposições verdadeiras, mas a 2 não é uma justificativa correta da 1.
* A asserção 1 é uma proposição verdadeira, e a 2 é uma proposição falsa.
* A asserção 1 é uma proposição falsa, e a 2 é uma proposição verdadeira.
* As asserções 1 e 2 são proposições falsas.
{:class="lettered"}

Justifique as asserções falsas, ou por que a asserção 2 não é justificativa da asserção 1.
