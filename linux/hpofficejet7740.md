---
title: Utilizando a impressora HP OfficeJet Pro 7740 em rede
subtitle: Ou, apenas um review da HP OfficeJet Pro 7740
section: Linux
layout: main
copy: 2022
date: 2023-09-06
tags:
  - linux
  - impressão
  - fedora
abstract: O uso de impressoras no Linux melhorou consideravelmente nos últimos 20 anos, mas eu não esperava esse nível de facilidade ao utilizar uma impressora em rede, mesmo num sistema atual.
---

Gosto muito de fotografia e de imprimir minhas fotos em papéis _fine-art_. Tenho (ou tinha) uma impressora Epson Stylus Pro 3380 para impressão fine-art em tamanhos até A2 (ou um pouco maior no comprimento), com tinta de pigmento mineral. É uma excelente impressora fotográfica, com péssimo custo-benefício para usar como impressora de escritório, e, o pior de tudo, não há mais cartuchos de tinta disponíveis, uma vez que o modelo foi descontinuado há vários anos.

Para resolver o problema de impressão de escritório adquiri uma HP OfficeJet Pro 7740. Uma impressora laser colorida que imprime até o tamanho A3, imprime em dupla face, e possui um _scanner_ (que pretendo configurar mais tarde) e mais um monte de opções eu eu jamais vou utilizar.

Sim, eu imprimo em A3, e não, não vou imprimir fotos numa impressora laser. _Horses for courses_.

Comecei esse texto com o objetivo de mostrar como configurar essa impressora (que acaba de chegar - 20023-09-06) para impressão a partir de uma máquina Linux (Fedora), com a impressora conectada via rede WiFi. O que eu não esperava é que eu não precisaria fazer **absolutamente nada** no lado do Linux para que a impressora funcionasse.

## Configurando a impressora

Após retirar os milhares de adesivos azuis que prendem as partes da impressora para o transporte, ligá-la na rede elétrica, e instalar os cartuchos (com um sistema fácil, mas péssimo e meio _solto_ de conexão), a impressora _realiza uma série de procedimentos muito bem ocultados e que certamente reduzem a vida útil dos cartuchos_. Uma página de alinhamento das cabeças de impressão é impressa e você está pronto para começar a ~~sofrer~~ utilizar a impressora, caso você vá usar a porta USB.

Para configurar como uma impressora de rede você pode usar uma conexão Ethernet, porém eu acabei utilizando o WiFi. A configuração é relativamente simples, porém minha rede, que não é oculta, não foi atomaticamente identificada pela impressora. Apesar disso, bastou inserir o nome da rede, a senha de conexão e a impressora configurou os serviços de impressão em rede.

E aqui começam os sustos, para o bem e para o mal.

A impressora _liga pra casa_ e configura algumas coisas direto com o fabricante. Eu comprei sabendo disso, não tive vontade de bloquear o acesso externo da impressora durante a configuração, mas recomendo que se faça isso, embora eu não tenha certeza de como ficará o processo de configuração.

O primeiro susto, negativo, é que a impressora se registra junto à HP para o tal do _HP ePrint_, um serviço da HP para impressão a partir de dispositivos móveis via um e-mail. Odeio essa intrusão do vendedor dos dispositivos na minha rede e nos meus dados. Desabilitar o serviço a partir da impressora é difícil ou impossíveil, utilize um browser para conectar ao IP da impressora e desabilitar o serviço (nesse caso, facilmente).

Outro serviço habilitado para impressão remota foi o WiFi Direct, mas esse eu _acho_ que foi culpa minha, embora eu não lembre de ter dito "ok, habilite mais essa forma de alguém acessar a impressora sem o meu conhecimento". Esse é bem mais fácil de desabilitar na impressora.

Outros serviços como AirPrint (Apple/iOS) e Google Cloud Product (Google/Android), aparentemente, só podem ser habilitados acessando a configuração via Web da impressora. Acho ótimo, pois posso não me preocupar com eles já que vem desabilitados por padrão.

A melhor parte dos protocolos de impressão de rede habilitados é o IPP. Uma vez configurada a rede, você pode dar um _hostname_ para a impressora e qualquer sistema que saiba imprimir via IPP irá encontrá-la e (aparentemente) saberá utilizá-la.

E aqui veio a melhor surpresa, como a impressora se anuncia via Bonjour, ela automagicamente apareceu nos diálogos de impressão do Fedora 38, numa instalação quase sem adições do [i3 Spin](fedoraproject.org/spins/i3){:target="\_blank"}. Bastou um `ping` no IP da impressora para o sistema se achar e disponibilizar a impressora para uso.

## Conclusão

Se passaram quase 20 anos desde a última vez que eu havia configurado uma impressora no Linux, e tanto para uso como uma impressora local como para impressão remota via IPP não eram simples. Houve uma evolução muito grande do lado do sistema operacional e do lado do suporte de fabricantes de hardware (mesmo que esse suporte ainda esteja muito aquém do desejado).

Hoje em dia, ao menos para impressão em rede em impressoras que provém esse suporte diretamente, o processo de configuraçõe está bastante simples, e os resultados de impressão bem satisfatórios.

Aparentemente o problema agora é "como manter meu ambiente seguro e controlado" ao invés de "vou ter que fazer um ritual pagão para isso funcionar".

Eu prefiro os dias atuais. Estou ficando velho, sem tempo a perder, e prefiro coisas que eu consiga controlar mais facilmente, e é bem melhor controlar meu ambiente de rede, do que ficar brigando com driver de impressão incompleto ou mal escrito.
