---
title: Instalação do ambiente de desenvolvimento React Native.
layout: main
tags:
  - react-native
  - dispositivos moveis
  - linux
copy: 2022
date: 2022-09-11
---

> Tentei traduzir e resumir o processo de instalação das ferramentas necessárias para o desenvolvimento com o React Native. Os passos originais para a instalação podem ser encontrados no .

O React Native combina partes do desenvolvimento nativo com o React, uma biblioteca JavaScript desenvolvida para a criação de interfaces com o usuário. Para desenvolver utilizando o `React Native CLI`, você precisará isntalar as ferramentas de desenvolvimento dos sistemas alvo, Android ou iOS. O desenvolvimento para iOS irá exigir as ferramentas disponíveis no macOS, o desenvolvimento para Android pode ser feito em qualquer plataforma suportada.

Este tutorial mostar como instalar o ambiente de desenvolvimento para Android (utilizando Linux) e para Android e iOS (utilizando macOS). Alguns tópicos da instalação no Windows também são cobertos, no entanto não foram testados. Veja também o documento [_Environment Setup_](https://reactnative.dev/docs/environment-setup).

Para instalar o [React Native](https://reactnative.dev/){:target="_blank"}, você irá precisar instalar o [Node.js](https://nodejs.org){:target="_blank"} e uma série de pacotes utilizando o gerenciador de pacotes do Node, o `npm`.

Para instalar o Node.js em uma distribuição Linux, utilize o [gerenciador de pacotes da sua distribuição](https://nodejs.org/en/download/package-manager/){:target="_blank"}, para as versões recentes do [Fedora Linux](https://getfedora.org){:target="_blank"} utilize `dnf instal npm nodejs watchman` (ao contrario do que indica o site do Node.js). Se você utiliza Windows utilize o [Chocolatey](https://chocolatey.org/){:target="_blank"} um gerenciador de pacotes popular para a plataforma, e se você utiliza macOS, instale o `node` e o `watchman` utilizando o [Homebrew](https://brew.sh) (`brew install node watchman`).

É sugerido que se utilize a última versão do Node.js, no entanto, é preciso garantir que a versão seja pelo menos a 14.

## Android

Além do Node, você irá precisar, para o desenvolvimento para Android, de uma versão do Java JDK. No Linux, utilize o OpenJDK (Fedora: `dnf install java-latest-openjdk`, Debian: `apt install openjdk-17`).

Você também irá precisar do [Android Studio](https://developer.android.com/studio/index.html){:target="_blank"}. Garanta que, pelo menos, os componentes `Android SDK`, `Android SDK Platform` e `Android Virtual Device` serão instalados. Caso não seja possível configurar todos durante a instalação, você poderá configurá-los mais tarde.

Ao iniciar o Android Studio (versão 2021.2.1) pela primeira vez após a configuração, você deverá clicar em _`More actions...`_ e escolher `SDK Manager`, caso não exista a opção, clique em `Customize -> All settings` e selecione `Appeparance & Behavior -> System Settings -> Android SDK`. Selecione a versão `Android 12 (S)` do `Android SDK` (API Level 31), e clique em `Apply`.

Após instalar o Android Studio, configure o seu arquivo `~/.bashrc`, ou `~/.bash_profile`, ou `~/.zprofile` (ou o equivalente do seu _shell_) para conter:

<a name="android-env"/>

```bash
export ANDROID_SDK_ROOT=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_SDK_ROOT/emulator
export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools
```

Instale também o [Watchman](https://facebook.github.io/watchman). No Linux, se você usa o Fedora, utilize `dnf install watchman`, no Ubuntu, siga as instruções oficiais do Watchman para instalar a partir dos fontes. No macOS, utilize o Homebrew: `brew install watchman`. 


## Criando um novo projeto

Instale o `react-native` utilizando `npm -g install react-native`. Pode ser necessário que o usuário possua privilégios de administrador/superusuário.

Agoro você pode iniciar uma nova aplicação utilizando o comando `npx react-native init <nome do projeto>`, por exemplo:

```
npx react-native init HelloWorld
```

## Criando um dispositivo virtual para o Android

Antes de poder iniciar o dispositivo virtual, é necessário criar um dispositivo.

Utilizando o Android Studio abra o projeto Android disponível em `HelloWorld/android`:

```
<path_to_android_studio>/bin/studio.sh Contatos/android
```

Selecione `Tools -> Device Manager`, clique em `Create virtual device`, escolha um dos dispositivos disponíveis e clique `Next`, selecione a imagem de sistema `S, API Level 31`, e clique em `Download`. Após o _download_ da imagem, clique em `Next` e depois em `Finish`. Espere os processos executados pelo Android Studio terminarem e feche o programa.

## Testando a aplicação

Para testar a sua aplicação você precisará de um dispositivo virtual. Caso vocüe esteja desenvolvendo para Android, deverá [criar um dispositivo com o Android Studio](#criando-um-dispositivo-virtual-para-o-android), caso esteja desenvolvendo para iOS, você precisará do XCode, mas não precisa de nenhuma configuração extra.

Para executar a aplicação, utilizaremos o [Metro](https://facebook.github.io/metro/docs/concepts). Inicialize-o com:

```
npx react-native start
```

E inicie a execução da aplicação com `npx react-native run-android` para Android ou `npx react-native run-ios` para iOS.

### Problemas comuns

1. Emulador Android não inicia:
    : Verifique se as [variáveis de ambiente](android-env) estão corretas

2. (Android) Programa falha porque emulador não terminou a inicialização.
    : Espere o emulador terminar a inicialização e tente novamente.

3. (Android) Atualização da aplicação falha com o erro `INSTALL_FAILED_INSUFFICIENT_STORAGE`
    : Edite a configuração do dispositivo de forma que tenha um maior espaço de armazenamento, ou remova a aplicação anterior do dispositivo (por exemplo, no _widget_ `Settings` do dispositivo).
