#!/bin/sh

usage() {
    echo "usage: new_lecture.sh NICK NAME [TITLE] [YEAR] [INSTITUTION]"
}

[ "$#" -lt 2 ] || [ "$#" -gt 5 ] && usage && exit 1

nick=$1
name=$2
title=${3:-''}
year=${4:-$(date +"%Y")}
institution=${5:-"Universidade LaSalle Canoas"}

BASEDIR="$(dirname $0)/.."
LECTURE_DIR="${BASEDIR}/teaching/lasalle/lectures/${nick}"

next_lecture=$({ echo "lecture-00.md" ; ls -1 "${LECTURE_DIR}"; } | tail -n 1 | xargs basename -s .md | cut -d- -f2)

next_lecture=$(printf "lecture-%02d.md" $(echo "1 + ${next_lecture}" | bc -l))

source="${BASEDIR}/_utils/templates/lecture.md"
[ -f "${BASEDIR}/_utils/templates/${next_lecture}" ] && source="${BASEDIR}/_utils/templates/${next_lecture}"

sed -e "s/@TITLE@/${title}/g" -e "s/@DISCIPLINA@/${name}/g" -e "s/@YEAR@/${year}/g" -e "s/@INSTITUTION@/${institution}/g" -e "s/@NICK@/${nick}/g" < "${source}" > "${LECTURE_DIR}/${next_lecture}"
