---
title: Controle de Versão e Metodologias Ágeis
section: Laboratório de Engenharia de Software
layout: lecture
last_occurrence: 2023-09-12
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-engswlab
---

## Assunto

1. Controle de Versão
    * É uma classe de sistemas cujo objetivo é gerenciar alterações em programas, documentos, ou qualquer coleção de informações.
    * Também chamado **controle de revisão** e **gerenciamento de código fonte**.
    * É um componte do [gerenciamento de configuração de software](https://en.wikipedia.org/wiki/Software_configuration_management){:target="\_blank"}.
    * As principais funções desses sistemas são armazenar metadados sobre as alterações ocorridas no sistema e permitir a recuperação de versões anteriores.
    * As principais arquiteturas desses sistemas são:
        * Centralizadas: onde um repositório central é utilizado como _fonte única de verdade_, e todas as modificações devem ser armazenadas nesse repositório. Ex.: CVS e Subversion
        * Distribuídos: onde cada repositório local é considerado um repositório completo e qualquer repositório pode, a qualquer momento, ser utilizado como fonte de modificações. Ex.: Mercurial e Git.
    * Permitem o desenvolvimento de versões simultâneas do mesmo sistema (_branching_)
    * Operações comuns:
        * **Annotate**/**Blame**
            : Verificar quem e quando alterou uma informação pela última vez.
        * **Branch**
            : Uma bifurcação no repositório criando duas linhas paralelas de desenvolvimento. O _branch_ principal é, às vezes, chamado de _trunk_.
        * **Checkout**
            : Criar uma cópia local a partir de um ponto específico do repositório
        * **Clone**
            : Copiar um repositório contendo todas as suas revisões.
        * **Commit**
            : Conjunto de alterações agrupadas em conjunto e seus meta-dados.
            : Ato de gravar as alterações efetuadas no repositório.
        * **Conflito**
            : Ocorre quando duas alterações diferentes são realizadas na mesma informação, a partir de um mesmo ponto de origem, e que o sistema não consegue reconciliar.
            : A **resolução do conflito**, nesse caso, deve ser feita manualmente, pelo usuário.
        * **Head**
            : O _commit_ mais recente de um _branch_.
        * **Label**/**Tag**
            : Uma marcação em um branch em relação a um evento importante (_release_, _sprint_, etc).
        * **Merge**
            : Reconciliação de dois conjuntos diferentes de alterações.
        * **Pull** / **Push**
            : Copiar revisões de um repositório para outro. _Pull_ é iniciada pelo repositório que recebe as alterações, _push_ é iniciada pelo repositório que envia as alterações.
        * **Pull request**
            : Uma requisição para que alterações sejam adicionadas a um _branch_. Em geral envolve revisão de código e um processo de aprovação.
    * Informação sobre alterações devem ser realizadas em mensagens de commit:
        * _Qual o motivo dessa alteração?_
        * _O que está sendo alterado?_
        * _Como a alteração resolve o problema?_

2. Metodologias Ágeis
    * Surgiram devido à adoção de software em larga escala
    * Seguem as ideias e princípios do [Manifesto para Desenvolvimento Ágil de Software](https://agilemanifesto.org/iso/ptbr/manifesto.html){:target="\_blank"}:
        * **Indivíduos e interações** mais que processos e ferramentas.
        * **Software em funcionamento** mais que documentação abrangente.
        * **Colaboração com o cliente** mais que negociação de contratos.
        * **Responder a mudanças** mais que seguir um plano.
    * Príncipios do Manifesto Ágil:
        * A maior prioridade é satisfazer o cliente com entrega contínua de software com valor agregado.
        * Mudanças nos requisitos são bem-vindas.
        * Entregas rápidas e frequentes de software funcional.
        * Pessoas do negócio e desenvolvedores devem trabalhar juntos.
        * Indivíduos motivados, com suporte e confiança.
        * O método mais eficiente de comunicação é face a face.
        * Software funcionando é a medida primária de progresso.
        * O desenvolvimento é sustentável, ou seja, todos envolvidos devem ser capazes de manter um ritmo constante indefinidamente.
        * Contínua atenção à excelencia técnica e bom design.
        * Simpliciade é essencial. (_Menos é mais._)
        * As melhores arquiteturas, requisitos e designs emergem de equipes auto-organizáveis.
        * Em intervalos regulares a equipe reflete sobre como se tornar mais eficaz.
    * Características comuns:
        * A especificação inicial não é detalhada até que precise ser implementada.
        * O sistema é desenvolvido a partir de uma série de incrementos.
        * Contratos são mais complexos, uma vez que o escopo do projeto não é exato.
        * Gerenciamento em projetos com muitas pessoas fica mais difícil.
        * Melhor utilizado em equipes pequenas de até 20-30 pessoas.

3. Extreme Programming
    * Se preocupa com práticas de programação
    * Captura requisitos a partir de histórias de usuário.
    * Releases curtos.
    * Utiliza alguma metodologia de desenvolvimento _test-first_, como [TDD - Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development){:target="\_blank"} e/ou [BDD - Behavior Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development){:target="\_blank"}.
    * Programação em pares.
    * Refatoração.
    * Propriedade coletiva.
    * Integração contínua.
    * Uso extensivo de frameworks de testes automatizados.

4. SCRUM
    * Foco no gerenciamento de projetos e equipes.
    * Ciclos de _sprint_ de uma a quatro semanas.
    * _Backlog_ de produto, com atividades priorizadas.
    * Envolvimento de toda equipe e do cliente/stakeholder durante o planejamento e a validação
    * Reuniões de status diárias e rápidas:
        * _O que me bloqueia?_
        * _O que eu vou fazer._
        * _O que eu fiz._
    * Figura de um _Product Owner_ que prioriza as atividades do backlog.


## Recursos para essa aula

### Tutoriais

1. [Pro Git](https://git-scm.com/book/pt-br/v2){:target="\_blank"}: Tradução parcial do livro para português do Brasil.
2. [Git - Guia prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html){:target="\_blank"}: Um guia bem direto, sem muita explicação.
3. [Github - Início Rápido](https://docs.github.com/pt/get-started/quickstart){:target="\_blank"}

### Bibliografia

1. Sutherland, Jeff. **Scrum: A Arte de Fazer o Dobro do Trabalho na Metade do Tempo**. 2<sup>a</sup> Ed. LeYa. 2016.
2. [Version Control](https://en.wikipedia.org/wiki/Version_control){:target="\_blank"}: Wikipedia

### Repositórios

1. [Gherkin by example](https://github.com/gherkin-by-example)

