#!/bin/bash

# Program: parameters.sh

usage() {
    cat<<EOF
usage: parameters.sh [-h] [-i VALOR] [-v|-vv|-vvv...] [POSICIONAL...]

Opções:

    -i VALOR      Uma opção que aceita um valor como parâmetro.
    -v            Uma opção que aceita contagem de vezes que aparece.
    -h            Uma opção que pode ou não ser utilizado.

    POSICIONAL    Parâmetros posicionais.
EOF
}

VERBOSE=0
unset VALUE

while getopts "hi:v" OPT
do
    case "${OPT}" in
        h) usage && exit 0  ;;
        v) VERBOSE=$((VERBOSE + 1)) ;;
        i) VALUE="${OPTARG}" ;;
        *) echo "ERRO: Opção inválida: ${OPT}" && exit 1 ;;
    esac
done

# Usando um "array" com as opções posicionais.
POSICIONAIS=(${@:OPTIND})

echo "Número de parâmetros posicionais: ${#POSICIONAIS[@]}"
echo "Parâmetros: ${POSICIONAIS[@]}"
echo "Primeiro parâmetro: ${POSICIONAIS[0]}"

# usando as opções com ${1}
shift $((OPTIND - 1))
echo "Número de parâmetros posicionais: $#"
echo "Parâmetros: $*"
echo "Primeiro parâmetro: ${1}"

[ -z "${VALUE}" ] && echo "VALUE: (null)" || echo "VALUE: ${VALUE}"
echo "Número de 'v': ${VERBOSE}"
