---
title: Aquiteturas e Processos Distribuídos
subtitle: Sistemas Distribuídos
layout: lecture
last_occurrence: 2023-08-24
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-sistemas-distribuidos
---

## Assunto

1. Arquiteturas
    > * Sistemas distribuidos são muito complexos, para controlar sua complexidade é necessário organizá-los adequadamente.
    > * **Arquitetura de Software** é a forma como organizamos os componentes de software de um sistema e como eles devem interagir.
    > * A especificação final da arquitetura de software é (também) denominada **arquitetura de sistema**.
    > * Uma meta importante de sistemas distribuídos é separar aplicações das plataformas subjacentes provendo uma camada de **_middleware_**.
    > * **Sistemas autonômicos** são sistemas que tomam providências adequadas em relação a eventos que o próprio sistema monitorou e identificou.
    
    1. Estilos arquitetônicos
        * Estilo arquitetônico: formulado em termos de como os componentes estão conectados, como se comunicam, e como são configurados para formar um sistema.
            * Arquitetura em Camadas
            * Arquitetura baseada em objetos
            * Arquitetura centrada em dados
            * Arquitetura baseada em eventos
        * Componente: unidade modular com interfaces requeridas e fornecidas bem definidas que é substituível dentro do seu ambiente.
        * Conector: Pode ser formado por facilidades para chamadas de procedimento remotas, passagem de mensagem ou fluxo de dados.
        * Arquitetura em Camadas: Um componente da camada $L_{i}$ pode chamar um componente da camada $L_{i-1}$, mas não o contrário. Requisições descem na hierarquia, enquanto resultados sobem.
        * Arquitetura baseada em Objetos: componentes são vistos como objetos e conectados por meio de chamada remota de procedimentos
        * Arquitetura centrada em Dados: processos se comunicam por meio de um repositório comum (passivo ou ativo) de dados.
        * Arquitetura baseada em eventos: em geral sistemas baseados em "publish/subscribe" com controle de notificações efetuado pelo middleware.
            * Arquiteturas baseada em eventos podem ser combinadas com arquiteturas centrada em dados, criando componentes desacoplados no tempo. 
    2. Arquiteturas de Sistemas
        * Arquiteturas centralizadas (ex.: cliente-servidor)
            > Operações idempotentes: quando aplicadas múltiplas vezes, deixam o sistema, sempre, no mesmo estado.

            * Muitas vezes utilizam protocolos de conexão confiáveis.
            * Camadas de Aplicação
                1. Nível de interface de usuário
                2. Nivel de processamento (Regras de Negócio)
                3. Nivel de dados
            * Mesmo com várias camadas, em geral, apenas duas máquinas são utilizadas, um cliente e um servidor.
            * Arquiteturas multidivididas: um servidor pode atuar com cliente de outro servidor (ex.: servidor de aplicação e de banco de dados)
            * Provê **distribuição vertical**.
            * Componentes logicamente diferentes em camadas diferentes.
        * Arquiteturas descentralizadas (ex.: _peer-to-peer_)
            * Provê **distribuição horizontal**.
            * Um cliente ou servidor pode ser fisicamente subdividido em partes logicamente equivalentes, mas cada parte opera em sua própria porção do conjunto completo de dados, equilibrando a carga.
            * Os processos em um sistema _peer-to_peer_ são todos iguais.
            * Arquiteturas peer-to-peer estruturadas
                * Distrubuted Hash Table (DHT): os itens de dados recebem uma chave e a cada nó é associado um grupo de chaves.
                * Content Addressable Network (CAN): o espaço de dados é dividido de forma semelhante à uma kD-tree de duas dimensões.
            * Arquiteturas peer-to-peer não-estruturadas:
                * A rede é um grafo aleatório.
                * Cada nó conhece alguns vizinhos e tem apenas uma visão parcial da rede.
                * Superpares: Nós com conhecimento de um índice de itens de dados. Cria uma rede hierárquica. Ex. Content Delivery Network (CDN)
            * Arquiteturas Híbridas
                * Edge Server: servidores são colocados na borda da rede (fronteira entre a rede corporativa e a Internet).
                * Sistemas colaborativos: inicia como cliente-servidor (startup) e o nó entra no sistema descentralizado de colaboração. Ex.: BitTorrent
3. Processos
    1. Threads
        * Paralelismo intra-nó.
        * Um processo no sistema operacional tem, pelo menos, uma thread.
        * Threads são como _processos leves_, reduzindo o custo de troca de contexto.
        * Comunicação entre threads vs. Comunicação entre processos
        * Acesso a dados compartilhados: mutex vs. semáforos


## Questões

1. Arquiteturas
    1. Se um cliente e um servidor forem colocados longe um do outro, podemos ver a latência de rede dominar o desempenho global. Como podemos atacar esse problema?
    2. Qual é a diferença entre uma distribuição vertical e uma distribuição horizontal?
2. Processos
    1. Escreva um artigo de, no máximo 1 página, comparando `processos`, `threads de sistema` e `threads de usuário`.
3. **Projeto**:
    > Implementar um chat multi-usuário utilizando uma arquitetura distribuída, utilizando _threads_ tanto do lado do cliente como do lado do servidor.

<!-- Formato da mensagem, comandos a serem implementados, pelo menos dois servidores -->

## Recursos para essa aula

### Código

* [Cliente rudimentar de chat em Python](/files/lasalle/code/chat/client.py)
* [Servidor rudimentar de chat em Python](/files/lasalle/code/chat/server.py)


