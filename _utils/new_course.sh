#!/bin/sh

if [ $# -lt 3 ]
then
    echo "usage: new_course.sh COURSE INSTITUTION NICKNAME [STARTDATE]"
    exit 1
fi

TOPDIR=$(dirname $(dirname $(basename "$0")))

DISCIPLINA=$1
INSTITUTION=$2
NICKNAME="$(echo $3 | tr '[:upper:]' '[:lower:]')"
STARTDATE=${4:-"$(expr $(date "+$Y") + 1)-01-01"}

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
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
  - topics:
    lecture: false
---
EOF
