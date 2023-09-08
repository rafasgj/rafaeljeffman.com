#!/bin/bash

usage() {
    echo "usage: new_lecture.sh NICK [TITLE] [YEAR] [NAME] [INSTITUTION]"
}

[ "$#" -lt 1 ] || [ "$#" -gt 5 ] && usage && exit 1

declare -A lectures
lectures=(
    [analise-algoritmos]="Complexidade de Algoritmos e Análise de Desempenho"
    [engswlab]="Laboratório de Engenharia de Software"
    [sistemas-distribuidos]="Sistemas Distribuídos"
    [mobile]="Desenvolvimento para Dispositivos Móveis"
    [compiler]="Compiladores"
    [automata]="Linguagens Formais e Autômatos"
)

nick=$1
title=${2:-''}
year=${3:-$(date +"%Y")}
name=${4:-${lectures[${nick}]}}
institution=${5:-"Universidade LaSalle Canoas"}


BASEDIR="$(dirname $0)/.."
LECTURE="teaching/lasalle/lectures/${nick}"
LECTURE_DIR="${BASEDIR}/${LECTURE}"

next_lecture=$({ echo "lecture-00.md" ; ls -1 "${LECTURE_DIR}"; } | tail -n 1 | xargs basename -s .md | cut -d- -f2)

next_lecture=$(printf "lecture-%02d.md" $(echo "1 + ${next_lecture}" | bc -l))

source="${BASEDIR}/_utils/templates/lecture.md"
[ -f "${BASEDIR}/_utils/templates/${next_lecture}" ] && source="${BASEDIR}/_utils/templates/${next_lecture}"

sed -e "s/@TITLE@/${title}/g" -e "s/@DISCIPLINA@/${name}/g" -e "s/@YEAR@/${year}/g" -e "s/@INSTITUTION@/${institution}/g" -e "s/@NICK@/${nick}/g" < "${source}" > "${LECTURE_DIR}/${next_lecture}"

echo "Created lecture: ${LECTURE}/${next_lecture}"
