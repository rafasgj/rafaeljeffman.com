---
title: Processos Distribuídos e Comunicação
section: Sistemas Distribuídos
layout: lecture
last_occurrence: 
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-sistemas-distribuidos
---
<style>
ul.OSI { counter-set: camada_osi 8; }
ul.OSI li::marker {
    content: counter(camada_osi, number) ". " ;
    font-weight: 600;
}
ul.OSI li {
    counter-increment: camada_osi -1;
    display: list-item;
}
</style>

## Processos Distribuídos

1. Threads em sistemas distribuídos
    * _Threads_ podem ser utilizadas para evitar bolqueios em chamadas bloqueantes, permitindo que outras ações do programa continuem executando.
    * Clientes _multithread_
        * O principal objetivo é oculta a latência de operações (rede, disco, etc).
        * Por exemplo, é comum a UI executar em uma thread de mais alta prioridade para mostrar ao usuário que o programa continua em execução, uma vez que operações de I/O podem demorar muito (principalmente operações em rede) e dar a impressão de travamento.
        * Um exemplo no uso de threads para otimizar o tempo de execução é a carga de imagens em paralelo, num _browser WWW_. Como as rotas podem ter tempos diferentes, e as imagens tamanhos diferentes, é possível carregar as imagens, pelo menos parcialmente, de forma mais rápida.
    * Servidores _multithread_
        * Podemos construir servidores onde o cliente conecta em uma _thread_ principal (_Dispatcher_), e a comunicação com cada cliente conectado em uma _worker thread_.
            : Nesse modelo, é comum o uso de uma _thread pool_ para limitar o número máximo de threads.

2. Virtualização
    * A virtualização de recursos é utilizada para...
    * Um _hypervisor_ é....
        * _Host hypervisor_
            : ...
            : Ex.: VirtualBox, QEMU
        * _Baremetal hypervisor_
            : ...
            : VMWare ESXi, VMWare vSphere
    * Virtualização de Recursos
        * processador, memória, hardware dedicado...
    * Virtualização de Hardware vs. Contexto
    * _Host OS_
    * _Guest OS_

3. Containers
    * Criam um ambiente de _user space_ isolado.

4. Servidores
    * Porta: Terminal no qual o serviço é provido. Algumas portas são definidas pela IANA.
        : ex.: DNS (porta 53), HTTP (porta 80), SSH (porta 22)
    * Tipos de servidores
        * _Stateless_: não guarda estado dos clientes
        * _Soft state_: mantém estado por tempo determinado (estado de sessão)
        * _Statefull_: guarda o estado de cada cliente. A recuperação em caso de reinício do servidor é complexa.
    * Clusters de servidores: aparecem com um único servidor para o cliente

5. Migração de código
    * Tipos de migração:
        * Segmento de código: migração de instruções
        * Segmento de recursos: arquivos, impressras, processos
        * Segmento de execução: estado de execução, pilha, contexto
    * Tipos de mobilidade:
        * Fraca: mobilidade de segmento código (ex.: Javascript, applets Java)
        * Forte: mobilidade mais geral, mais complexa e mais custosa (mobilidade de segmento de execução)

## Comunicação

1. Protocolos de comunicação
    * Toda comunicação em redes de computadores é realizada a partir de protocolos bem definidos.
    * Os protocolos de comunicação utilizados dependem da camada (_modelo OSI_) ao qual estão ligados
    * **Protocolos orientados a conexão**
    : Deve ser estabelecida uma conexão antes da comunicação (Ex.: POTS - _Plain Old Telephone Service_)
    : Garantem uma rota entre o remetente e o receptor.
    * **Protocolos sem conexão**
    : A rota entre o remetente e o repector não é conhecida no momento de envio. (Ex.: Correio)
    * Um conjunto de protocolos é conhecido como **pilha de protocolos** e funciona com cada novo protocolo adicionando um cabeçalho ao dados do protocolo anterior.

2. Camadas OSI
    > Nas camadas OSI os protocolos começam a transmissão na camada _7_ (aplicação) e avançam até a camada _1_ (Físico).
    
    * Aplicação
        : Protocolos de alto nível, definidos pelas aplicações. Ex.: HTTP, FTP
        : Os protocolos de _middleware_ são protocolos de aplicação.
    * Apresentação
    * Sessão
    * Transporte
        : Provê transparência de rede para as camadas superiores. Ex.: TCP, UDP
    * Rede
        : Roteamento $\rightarrow$ remetente conhece o receptor. Ex.: IP (transmissão de pacotes)
    * Enlace
        : Transmissão de frames, verificação de erros (ex.: CRC, checksum)
    * Físico
        : Responsável pela transmissão de _bits_. Ex.: Padrão RS-232-C (serial)
    {:class="OSI"}

3. Tipos de Comunicação
    * Persistente vs. Transiente
        * **Persistente**
        : A mensagem continua ativa até que seja entregue, independente do estado do remetente ou do receptor.
        * **Transiente**
        : A mensagem só continua ativa caso remetente e receptor estejam ativos.
    * Síncrona vs. Assíncrona
        * **Síncrona**
        : Transmissor e receptor têm que estar sincronizados para ocorrer a comunicação. Para se manter esta sincronia, é transmitido periodicamente um bloco de informação que ajuda a manter o emissor e receptor sincronizados.
        * **Assíncrona**
        : ...

    * Chamada de Procedimento Remoto
    * Linguagem de Programação de Interfaces (IDL - Interface Definition Language)

    * Exemplos de Comunicação
        * Comunicação transiente orientada a mensagem
            * Berkeley Socket TCP/IP
                * Primitivas: `socket`, `bind`, `listen`, `accept`, `connect`, `send`,  `recv` (_receive_), `close`
        * Comunicação persistente de mensagens
            * Sistemas de Filas de Mensagens
                * Primitivas: `put`, `get` (bloqueante/síncrona), `poll` (não bloqueante, assíncrona), `notify`
