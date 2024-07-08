---
title: Comunicação Orientada a Fluxo e Sincronização em _Threads_
section: Sistemas Distribuídos
layout: lecture
last_occurrence: 2023-09-14
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-sistemas-distribuidos
---

## Assuntos

1. Comunicação Orientada a Fluxo
    * O fluxo da comunicação é importante.
    * A temporização tem efeito sobre a correção da informação.
    * Exemplos: fluxo de áudio ou vídeo.
    * Suporte para mídia contínua
        * Toda troca de informações é dependente do tempo.
        * Em mídia contínua as relações temporais dos dados são fundamentais para interpretar corretamente o seu significado.
        * A mídia discreta é caracterizada por relações temporais não serem relevantes para sua interpretação.
        * **Fluxo de Dados**
            * Modo de transmissão **assíncrono**
            : os itens de dados em um fluxo são transmitidos um após o outro, sem restrição de temporização.
            : É um caso típico de fluxos discretos de dados.
            * Modo de transmissão **síncrono**
            : inclui um atraso fim-a-fim para cada unidade em um fluxo de dados.
            : Uma unidade de dados pode ser transmitida com mais rapidez do que o atraso máximo tolerado, mas não de forma mais lenta.
            * Modo de transmissão **isócrono**:
            : Requer que as unidades de dados sejam transferidas no tempo certo. Nem antes, nem depois.
            : O atraso fim-a-fim tem um limite máximo e um limite mínimo, denominados _variações de atraso delimitado_.
            : Esse modo de transmissão é crucial na representação de áudio e vídeo, por exemplo.
        * Fluxos **simples** consistem de uma única sequência de dados (uma _stream_).
        * Fluxos **complexos** consistem de vários fluxos simples relacionados(múltiplas _streams_).
    * Qualidade de Serviço (QoS - _Quality of Service_)
        * QoS para fluxos contínuos de dados referem-se principalmente à pontualidade, ao volume e à confiabilidade.
        * Propriedades importantes:
            * Taxa de bits requerida pelos dados
            * Atraso máximo até o estabelecimento de sessão
            : quando uma aplicação pode começar a enviar dados
            * Atraso máximo fim-a-fim
            : quanto tempo até que uma unidade de dados chegue a um receptor
            * Máxima variância de atraso, ou _vibração_.
            * Máximo atraso da viade de ida e volta.
        * Na Internet, que utiliza o protocolo IP, temos que aceitar o fato que a comunicação é feita por um serviço de datagramas de melhor esforço.
        : O protocolo IP permite o descarte de pacotes sempre que o nó achar necessário.
        * Imposição de QoS
            * Dado que o sistema subjacente (IP) só oferece um serviço de entrega de melhor esforço, um sistema distribuído deve tentar ocultar o máximo possível a falta de qualidade de serviço.
            * É possível marcar pacotes como pacotes de **serviços diferenciados**, e inseri-los em alguma classe de **repasse acelerado**, dando maior prioridade aos pacotes. Há também as classes de **repasse garantido**.
            : Com isso é possível separar pacotes sensíveis ao tempo de pacotes não críticos.
            * Além dessas soluções em nível de rede, é possível criar outras alternativas nos níveis mais altos, como _buffers_ para reduzir a variância de atraso.
            * Outro problema é a perda de pacotes na comunicação, e como no caso do fluxo contínuo de dados não é possível requisitar o reenvio do pacote, é preciso aplicar **correção de erro de envio** (FEC - _forward error correction_).
            : Uma técnica comum é codificar os pacotes de saída de modo que seja necessário receber $k$ de $n$ pacotes para reconstruir o suficiente dos dados (com $k \le n$).
            : Por exemplo, ao invés de enviar diversos quadros sequênciais num mesmo pacote, são enviados quadros intercalados, de forma que a perda de um pacote gere uma falha recuperável na _stream_.
            : O problema dessa abordagem é que o _buffer_ do receptor deve ser maior, incorrendo em mais atraso na aplicação recebedora.
        * Sincronização de Fluxos
            * Exemplos: áudio estéreo, vídeo com áudio, slides com áudio
            * Um atraso de $\sim{20} \mu{s}$ é suficiente para distorcer o efeito estéreo do áudio.
            * Só podemos sincronizar os fluxos entre unidades de dados.
            : O que representa uma unidade de dados depende do nível de abstração no qual o fluxo de dados é visto.
            : Por exemplo, para o áudio estéreo a sincronização deve ser realiazada a cada $20\mu{s}$, considerando áudio com qualidade de CD (dois canais, 16-bits, 44.100Hz) cada unidade de dados teria, no máximo, 4 amostras.
            : Quadros de vídeo devem ser apresentados com frequências bem mais baixa, com 24Hz (cinema), 25Hz (PAL), 30Hz (NTSC) ou 60Hz (HD), portanto o número de amostras de áudio subiria para cerca de 1500 amostras, para manter o áudio sincronizado com o vídeo (_lipsync_). (No caso de áudio estéreo, esse sincronismo deve ser adicionado.)
            : Na prática, trabalha-se com unidades maiores, tolerando-se imperfeições.
            * Mecanismos de Sincronização
                * Leitura e escrita obedecendo limitações de tempo
                : Toda carga de sincronização fica para a aplicação.
                * Interfaces de alto nível para lidar com a sincronização
                : Dependem de informação de sincronização
                * Uma prática comum é forcer a informação de sincronização de modo implícito, pela multiplexação de diferentes fluxos em um único fluxo que contém todas as unidades de dados, incluindo as de sincronização.
                : Os padrões MPEG adotam essa abordagem, sendo formados por um número ilimitado de fluxos contínuos e discretos que podem ser fundidos em um único fluxo.
                : Cada fluxo do MPEG é codificado em um **fluxo de pacotes** que transporta uma marca de tempo, e então esses fluxos de pacotes são multiplexados em um **fluxo de programa** que consiste de pacotes de tamanho variados, todos com a mesma base de tempo. No lado do recebedor, essas marcas de tempo são utilizadas para demultiplexar e sincronizar os fluxos.
                * Para simplificar a sincronização ela deve ser realizada no remetente, que é o ator que "conhece" os fluxos sem atraso ou perdas de pacote devido a comunicação.
2. Comunicação Multicast
    * É a comunicação executada a partir de um remetente para múltiplos receptores.
    * _Gossiping_
        * O objetivo principal dos **protocolos epidêmicos** é propagar as informações rapidamente entre um grande conjunto de nós usando apenas informações locais.
        * Não há nenhum componente central que coordena a disseminação de informações.
        * Um nó, em um sistema distribuído que contém dados que devem ser espalhados para outros nó é denominado **infectado**.
        * Um nó que ainda não tenha os dados é denominado **suscetível**.
        * Um nó que não está disposto ou esteja incapacitado de propagar os dados é denominado **removido**.
        * Consideraremos que temos como distinguir os dados novos de dados antigos porque estes receberam uma marca de tempo ou tem uma versão associada.
        * Podemos considerar que os nós propagam _atualizações_.
        * Há três abordagens para troca de atualizações utilizando modelos de **antientropia**:
            * Apenas enviar atualizações
            : É uma abordagem ruim, pois quando poucos nós são **suscetíveis**, é difícil um desses nós ser escolhidos para o envio.
            * Apenas receber atualizações
            : é uma abordagem melhor, pois quando mais nós **infectados**, mais fácil é para um nó **suscetível** escolher um desses nós.
            * Receber e enviar atualizações
            : Ainda é a melhor estratégia de disseminação dos dados.
        * Se uma **rodada** for definida como o período em que cada um dos $n$ nós terá tomado, no mínimo uma vez, a iniciativa de trocar atualizações com outro nó escolhido aleatoriamente, podemos mostrar que o número de rodadas para propagar uma única atualização leva $O(\log(n))$ rodadas.
        * Uma variante específica dessa abordagem é a **propagação de boato** (_gossiping_).
        * No **gossiping** um nó $P$ tenta propagar para um nó $Q$, se o nó $Q$ já foi atualizado, $P$ pode perder o interesse na propagação, dada uma probabilidade de $1/k$.
        * Não há garantia que todos os nós serão atualizados no **gossiping**. Existe uma fração de nós que permanecem suscetíveis dada pela equação $s = e^{-(k+1)}$
        * Combinar **antientropia** com **gossiping** resolverá o problema de alguns nós não serem _infectados_.
    * Remoção de Dados
        * Algoritmos epidêmicos são bons para propagar alterações, porém a propagação da remoção de um dado é difícil.
        * Um dado removido localmente pode ser recriado a partir da propagação de uma cópia velha do mesmo dado, uma vez que será interpretada com atualização de um dado não existente.
        * A solução é tratar a remoção como uma atualização de dados, propagando um **certificado de óbito**.
        * A remoção definitiva do dado pode ser efetuada utilizando um marcador de tempo máximo no _certificado de óbito_.
3. Sincronização em _Threads_
    * Seções críticas são áreas de dados acessadas concorrentemente por _threads_ ou processos.
    * Por que é necessário sincronizar as _threads_?
        * Atomicidade de operações
        * Ordem de operaçẽs.
    * Primitivas de Sincronização
        * Todas as primitivas de sincronização são objetos globais compartilhados entre todas as _threads_.
        * Mutex
            * Mutex: _mutual exclusion_
            * Provê as funções `lock` e `unlock`.
            * Bloqueia a _thread_ se estiver no estado `locked`.
            * Mutexes Recursivos permitem e a mesma _thread_ bloqueie o mutex diversas vezes. O mutex só será liberado após a mesma _thread_ liberar o mutex o mesmo número de vezes que o bloqueou.
            : Mutexes recursivos são mais difíceis de trabalhar e mais sujeitos a erros.
            * Read/Write mutexes permitem operações de leitura mas não operações de escrita quando em `locked`. Múltiplas _threads_ podem obter um mutex de leitura, mas apenas uma _thread_ pode obter o mutex de escrita, e só conseguirá fazer isso se nenhuma _thread_ tiver bloquado e mutex de leitura.
        * Semáforos
            * Limita o número de _threads_ que podem acessar um recurso.
            * Quando uma _thread_ requisita um semáforo (`acquire`), um contador é decrementado, se o contador for 0 (zero), a _thread_ bloqueia até que alguma _thread_ libere o semáforo (`release`).
            * Qualquer _thread_ pode liberar o semáforo.
        * Variáveis condicionais
            * Oferecem as funções `wait`, `notify_one` e `notify_all`, além de um mecanismo para defini um **mutex** existente para bloquear o acesso à seção crítica.
            * Uma _thread_ chama `wait` em uma variável de condição e é bloqueada, uma outra _thread_ utiliza `notify_one` ou `notify_all` na variável de condição, ativando a(s) _thread(s)_ que estão bloquadas naquela variável.
    * Problemas comuns em sincronização
        * _Deadlock_
        : Ocorre quando uma _thread_ $U$ está bloqueando uma seção crítica $A$ e outra _thread_ $V$ está bloqueando uma seção crítica $B$, e a _thread_ $U$ tenta bloquear a seção crítica $B$ e a _thread_ $V$ tenta bloquear a seção crítica $A$ sem liberar seus respectivos bloqueios.
        * _Starvation_
        : Uma _thread_ espera indefinidamente por um recurso que nunca é liberado. Pode ser causada por diversos motivos, e é uma preocupação constante no _design_ de escalonadores com filas de prioridades.
        * Inversão de Prioridade
        : Ocorre quando uma _thread_ de maior prioridade fica bloqueada esperando uma _thread_ de menor prioridade liberar um recurso.


## Recursos para essa aula

### Bibliografia

1. Tanenbaum, Adrew S.; Van Steen, Maarten. **Sistemas Distribuídos: Princípios e Práticas.** Caps. 4 e 5. 2<sup>a</sup> Ed. Prentice Hall. [en-US](https://csc-knu.github.io/sys-prog/books/Andrew%20S.%20Tanenbaum%20-%20Distributed%20Systems.%20Principles%20and%20Paradigms.pdf)
2. Boyd, S.; Ghosh, A.; Prabhakar, B.; Shah, D. [Gossip Algorithms: Design Analysis and Applications](https://web.stanford.edu/~boyd/papers/pdf/gossip_infocom.pdf).
