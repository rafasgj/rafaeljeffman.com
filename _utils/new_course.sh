#!/bin/bash

mode="class_plan"
if [ "$1" == "-t" ]
then
    mode="tutor"
    shift 1
fi

if [ $# -lt 4 ]
then
    echo "usage: new_course.sh [-t] COURSE INSTITUTION NICKNAME STARTDATE [LECTURE_COUNT]"
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
layout: ${mode}
section: ${INSTITUTION}
sections:
extra_styles:
  - cronograma
  - page_summary
objectives:
requirements:
competences:
learning_unities:
references:
EOF

if [ "${mode}" != "tutor" ]
then

cat << EOF >>"${TARGETDIR}/${NICKNAME}.md"
grading:
  g1:
    t1: 4.0
    p1: 6.0
  g2:
    t2: 4.0
    p2: 6.0
lectures:
EOF

for i in $(seq ${LECTURES})
do
    echo -e "  - topics:\n    - \n    lecture: false" >> "${TARGETDIR}/${NICKNAME}.md"
done

else  # mode != tutor

cat << EOF >>"${TARGETDIR}/${NICKNAME}.md"
grading:
  - name: g1
    deliverables:
    - code: t1
      weight: 10.0
      brief: "Implement ..."
      url: lecture/t1
      due: 9
  - name: g2
    deliverables:
    - code: t2
      weight: 10.0
      brief: "Write an article ..."
      url: lecture/t2
      due: 19
EOF

fi

echo "---" >> "${TARGETDIR}/${NICKNAME}.md"
