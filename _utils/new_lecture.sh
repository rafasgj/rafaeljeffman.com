#!/bin/bash

usage() {
    echo "usage: new_lecture.sh NICK [TITLE] [YEAR] [NAME] [INSTITUTION]"
}

die() {
    echo -e "\033[31;1mERROR: $*\033[0m" >&2
    exit 1
}


[ "$#" -lt 1 ] || [ "$#" -gt 5 ] && usage && exit 1

declare -A lectures
lectures=(
    [analise-algoritmos]="Complexidade de Algoritmos e Análise de Desempenho"
    [engswlab]="Laboratório de Engenharia de Software"
    [sistemas-distribuidos]="Sistemas Distribuídos"
    [mobile]="Desenvolvimento para Dispositivos Móveis"
    [compiler]="Compiladores"
    [formais]="Linguagens Formais e Autômatos"
    [ia]="Inteligência Artificial"
    [paradigmas]="Paradigmas de Programação"
)

nick=$1
title=${2:-''}
year=${3:-$(date +"%Y")}
name=${4:-${lectures[${nick}]}}
institution=${5:-"Universidade LaSalle Canoas"}


BASEDIR="$(dirname $0)/.."
LECTURE="teaching/lasalle/lectures/${year}/${nick}"
LECTURE_DIR="${BASEDIR}/${LECTURE}"
mkdir -p "${LECTURE_DIR}"

next_lecture=$({ echo "lecture-00.md" ; ls -1 "${LECTURE_DIR}" || die "Invalid lecture directory: ${LECTURE_DIR}" ; } | sed -e "/index/d" | tail -n 1 |  xargs basename -s .md | cut -d- -f2)

next_lecture=$(printf "lecture-%02d.md" $(echo "1 + ${next_lecture}" | bc -l))

source="${BASEDIR}/_utils/templates/lecture.md"
[ -f "${BASEDIR}/_utils/templates/${next_lecture}" ] && source="${BASEDIR}/_utils/templates/${next_lecture}"

sed -e "s/@TITLE@/${title}/g" -e "s/@DISCIPLINA@/${name}/g" -e "s/@YEAR@/${year}/g" -e "s/@INSTITUTION@/${institution}/g" -e "s/@NICK@/${nick}/g" < "${source}" > "${LECTURE_DIR}/${next_lecture}" || die "Failed to create lecture!"

echo "Created lecture: ${LECTURE}/${next_lecture}"
