---
layout: main
section: Raspberry Pi
tags:
  - raspberry-pi
  - installation
  - Fedora
  - Ubuntu
  - NetBSD
title: Instalação de um Sistema Operacional no Raspberry Pi 4
copy: "2022-2023"
date: 2023-09-13
---

> **Nota**: Tanto a [documentação oficial do Raspberry Pi](https://www.raspberrypi.com/software/), quanto a do Sistema Operacional que você escolheu continua sendo a melhor fonte de informação sobre a instalação do sistema, tente, antes de seguir qualquer coisa dita aqui, utilizar os documentos oficiais.

Instalar um sistema no Raspberry Pi não é difícil, no entanto, algumas operações nem sempre são claras, ou as ferramentas utilizadas não estão disponíveis, ou o sistema que você deseja não é oficialmente suportado.

O objetivo aqui é reunir informação que auxilie na instalação de sistemas operacionais no Raspberry Pi 4 utilizando a ideia do _menor esforço possível_.

Os sistemas testados foram os que eu utilizei, ou utilizo regularmente, e, em alguns casos, as instruções servirão para outras versões do Raspberry Pi (além do Raspberry Pi 4, eu também uso algumas versões do 1 e o ZeroW).

A partir do Raspberry Pi 4, é possível inicializar o sistema a partir de um disco externo (USB), como meus objetivos são testes rápidos ou usar o Raspberry Pi com "o menor _footprint_ físico possível", eu faço todas as instalações utilizando um cartão de memória micro-SD.

O uso de um micro-SD como disco de sistema deixa o sistema um pouco mais lento (Raspberry Pi 4) e é uma questão de tempo para que o sistema do arquivo do cartão seja corrompido e ele precise ser recuperado ou reconstruído. Leve isso em consideração ao planejar o uso do Raspberry Pi, incluindo a necessidade de _backup_ de dados, replicação e restauração do sistema.

<div class="tag-list">Sistemas testados:</div>

* [Raspberry Pi OS](raspberry-pi-os-installation)
* [Fedora](fedora-installation)
* [Ubuntu Server](ubuntu-installation)

