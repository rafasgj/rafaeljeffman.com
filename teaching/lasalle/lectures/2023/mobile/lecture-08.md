---
title: Interfaces utilizando listas.
subtitle: Desenvolvimento para Dispositivos Móveis
layout: lecture
last_occurrence: 2023-09-22
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-mobile
---

## Assunto

1. Interfaces utilizando listas
    * A maioria das aplicações para **celulares** utilizam listas.
    * Cada componente da lista pode ser visto como um _container_ que é desenhado independentemente dos outros.
2. Listas com o React Native:
    * Listas simples: [FlatList](https://reactnative.dev/docs/flatlist)
    * Listas divididas em seções: [SectionList](https://reactnative.dev/docs/sectionlist)
    * As listas do React Native são eficientes do ponto de vista de renderização, desenhando o mínimo de elementos necessários.
3. Alguns cuidados no uso de listas
    * A atualização não é automática.
    * A atualização dos dados do objeto que armazena os dados exibidos na lista não força a sua atualização.
    * É necessário o uso de um dado extra (`extraData`) para forçar a atualização dos dados.

## Questões

1. **Implementação**: Altere o exemplo com atualização para que seja possível remover um elemento.


## Recursos para essa aula

* [Exemplo de **FlatList** com atualização](https://snack.expo.dev/@rafasgj/673059)
* [Exemplo de **FlatList** com _renderItem_ customizado](https://snack.expo.dev/@rafasgj/673059)
