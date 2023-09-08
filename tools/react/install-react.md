---
title: Instalação do React Native no Linux
layout: main
section: Desenvolvimento para Dispositivos Móveis
tags:
  - react-native
  - dispositivos móveis
  - instalação
copy: 2023
date: 2023-09-08
---

O objetivo desse documento é resumir o processo de instalação das ferramentas necessárias para compilar e testar programas escritos com React Native e um emulador Android no Linux.

Mais informações podem ser obtidas na [página oficial do React Native](https://reactnative.dev/docs/environment-setup?guide=native){:target="\_blank"}

## Dependências

Para instalar o React Native você precisa ter instalado, na sua máquina, o Node.js versão 16 ou posterior, as ferramentas de linha de comando do React Native, o JDK e o Android Studio.

Se você utiliza Fedora Linux, você pode instalar as dependências do sistema com o comando

```nohl
# dnf install nodejs java-17-openjdk-devel
```

## Android Studio

A [instalação do Android Studio](install-androidstudio) deve incluir o `Android SDK`, o `Android SDK Platform` e o `Android Virtual Device`. Em geral, a instalação padrão do Andrdoid Studio já instala os pacotes necessários.

Adicione ao seu `${HOME}/.bash_profile` ou `${HOME}/.bashrc` as variáveis de ambiente para para que as ferramentas do React Native possam utilizar as ferramentas de compilação nativas.

```bash
export ANDROID_HOME=${HOME}/Android/Sdk
export PATH=$PATH:${ANDROID_HOME}/emulator
export PATH=$PATH:${ANDROID_HOME}/platform-tools
```
    > Nota: Se você utiliza um diretório `${HOME}/.bashrc.d`, o que eu recomendo, o ideal é adicionar um arquivo `android_setup` neste diretório.

## Watchman

Instale o `watchman` a partir dos arquivos [disponibilizados pelo projeto](https;//github.com/facebook/watchman/releases/latest){:target="\_blank"}, não utilize a versão dispnível nos repositórios do Fedora porque, em geral, são velhas demais (podendo, inclusive, não ter algumas correções de segurança).

Após baixar o pacote correto, instale-o com o comando:

```nohl
# dnf localinstall <nome-do-pacote>
```

Para maiores detalhes sobre a instalação do Watchman, [consulte as instruções de instalação do projeto](https://facebook.github.io/watchman/docs/install){:target="_blank"}

## Utilizando um dispositivo virtual

Abra o projeto `AwesomeProject/androd` no Android Studio, e você verá uma lista de _Android Virtual Devices_ disponíveis ao abrir o `AVD Manager`/`Device Manager`. Se você não tem um dispositivo com a versão que você deseja (aqui estamos utilizando "Tiramisu (33)"), crie um novo dispositivo (sugiro utilizar o modelo do tefone `Pixel` como base).

## Testando a instalação

Para utilizar a interface de linha de comando utilize o comando `npx`, que vem junto com o Node.js. Utilizando os comandos `npx react-native <comando>` você irá utilizar as ferramentas da versão mais recente da CLI.

Crie um novo projeto com o comando:

```nohl
$ npx react-native@latest init AwesomeProject
```

Se você ainda não tive o `react-native` instalado, será perguntado se você deseja instalar os pacotes necessários. Se você chegou até aqui, acredito que não seja a hora de dizer não: responda sim.

Para executar o projeto que você acabou de criar, inicie o `Metro` com o comando:

```nohl
# cd AwesomeProject
# npm start
```

Aparecerá, no terminal, um `menu` para escolher qual a versão a ser executada, escolha `a - android`.

Deixe o `Metro` executando em seu terminal, e em outro terminal execute

```nohl
$ npm run android
```

Pra alterar a sua aplicação, execute alterações no arquivo `App.tsx` e, no terminal do `Metro` pressione duas vezes a tecla `R` ou selecione `Reload` do `Dev Menu` (que pode ser acessado com `CTRL + R`.

## Problemas comuns

1. Emulador Android não inicia:
    : Verifique se as [variáveis de ambiente](android-env) estão corretas

2. (Android) Programa falha porque emulador não terminou a inicialização.
    : Espere o emulador terminar a inicialização e tente novamente.

3. (Android) Atualização da aplicação falha com o erro `INSTALL_FAILED_INSUFFICIENT_STORAGE`
    : Edite a configuração do dispositivo de forma que tenha um maior espaço de armazenamento, ou remova a aplicação anterior do dispositivo (por exemplo, no _widget_ `Settings` do dispositivo).

4. Ferramentas de linha de comando não estão instaladas corretamente
    : Verifique a instalação do SDK e seus pacotes. ([Esta pergunta do Stackoverflow](https://stackoverflow.com/questions/71303780/react-native-cant-find-proper-android-sdk-version) pode ajudar bastante nesse caso).

## Ferramentas úteis

* O `npx react-native doctor` fará uma análise do seu ambiente e mostrará possíveis erros.
    * Entre os erros mais comuns apresentados para cada elemento estão:
        * `Adb`
            : O `PATH` para `${ANDROID_HOME}/platform-tools` não foi configurado
            : O emulador não está rodando
        * `Jdk`
            : O Java JDK não foi corretamente instalado
        * `Android Studio`
        * `Android SDK`
            : A versão disponível do SDK não é compatível com a versão desejada.
        * `ANDROID_HOME`
            : O `ANDROID_HOME` não foi configurado corretamente

## Referências

* [React Native: Setting up the development environment](https://reactnative.dev/docs/environment-setup?guide=native){:target="\_blank"}


