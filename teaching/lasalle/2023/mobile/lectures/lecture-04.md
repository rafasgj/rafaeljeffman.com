---
title:  Uso de mockups. Manipulação de dados e atualização de tela com React.
section: Desenvolmimento para Dispositivos Móveis
layout: lecture
last_occurrence: 
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-mobile
---

## Assunto

1. Uso de mockups.
    * Uma forma _barata_ de testar a estrutura de uma aplicação é criar _mockups_ de telas para testar a interação com o usuário.
    * Os mockups podem ser criados em papel ou utilizando diversos softwares.
    * Um software bastante utilizado para criação de mockups é o [Figma](https://www.figma.com)
2. Manipulação de dados e autalização de tela com React.
    * Variáveis locais não são persisistidas entre "rederizações"
    * Alterar valores de variáveis locais não  renderizações
    * Utilizando o `useState` _hook_ coneseguimos:
        * Uma variável de estado que mantém os dados entre "renderizações".
        * Uma função _setter_ para atualizar variáves e acionar as "renderizações" do componente.
    * Quando você tem múltiplas variáveis de estado, se elas forem alteradas junto, é melhor que sejam agrupadas em um objeto e este seja atualizada uma única vez, disparando a "renderização" apenas uma vez.


## Questões

1. Crie um _mockup_ de interface utilizando o Figma e os [widgets oficiais da Apple](https://www.figma.com/community/file/1248375255495415511).
2. Implemente a interface planejada utilizando React Native.

## Recursos para essa aula

### Ferramentas Online

* [Figma](https://www.figma.com)
* [Apple Design Resources – iOS 17 and iPadOS 17](https://www.figma.com/community/file/1248375255495415511)
* [Material 3 Design Kit](https://www.figma.com/community/file/1035203688168086460)
* [Android UI Kit](https://www.figma.com/community/file/1237551184114564748)

### Tutorias/Documentação

* [React State](https://reactnative.dev/docs/state)
* [React Native - Learn the Basics - State](https://reactnative.dev/docs/tutorial#state)
* [React - State: A Component's Memory](https://react.dev/learn/state-a-components-memory)
