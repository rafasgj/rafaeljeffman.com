#!/bin/bash

if [ $# -lt 4 ]
then
    echo "usage: new_course.sh COURSE INSTITUTION NICKNAME STARTDATE [LECTURE_COUNT]"
    exit 1
fi

TOPDIR=$(dirname $(dirname $(realpath "$0")))

DISCIPLINA="$1"
INSTITUTION="$2"
NICKNAME="$(echo $3 | tr '[:upper:]' '[:lower:]':-)"
STARTDATE="${4}"
LECTURES="${5:-20}"

YEAR=$(echo ${STARTDATE} | cut -d "-" -f 1)

institution="$(echo $INSTITUTION | tr '[:upper:]' '[:lower:]')"
TARGETDIR="${TOPDIR}/teaching/${institution}/${YEAR}"

[ -d "${TARGETDIR}" ] || mkdir "${TARGETDIR}"

echo "Creating skeleton for: ${TARGETDIR}/${NICKNAME}.md"

cat << EOF >"${TARGETDIR}/${NICKNAME}.md"
---
title: ${DISCIPLINA}
institution: ${INSTITUTION}
nickname: ${NICKNAME}
start: ${STARTDATE}
layout: class_plan
section: ${INSTITUTION}
sections:
extra_styles:
  - cronograma
  - page_summary
objectives:
requirements:
competences:
learning_unities:
grading:
  g1:
    t1: 4.0
    p1: 6.0
  g2:
    t2: 4.0
    p2: 6.0
references:
lectures:
EOF

for i in $(seq ${LECTURES})
do
    echo -e "  - topics:\n    - \n    lecture: false" >> "${TARGETDIR}/${NICKNAME}.md"
done

echo "---" >> "${TARGETDIR}/${NICKNAME}.md"
