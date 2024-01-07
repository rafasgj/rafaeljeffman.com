#!/bin/sh

usage() {
    cat <<EOF
usage: new_page.sh [-h] [-l LAYOUT] FILENAME [TITLE SECTION [[SUBTITLE]]]
EOF
}

if [ "$1" == "-h" ]
then
    usage
    exit 0
fi

LAYOUT='main'
if [ "$1" == "-l" ]
then
    LAYOUT="$2"
    shift 2
fi

if [ $# == 0 ]
then
    usage
    exit 1
fi

FILENAME=${1}
shift

NEED_SUBTITLE="NO"
[ -z "${1}" ] && NEED_SUBTITLE="" || NEED_SUBTITLE="NO"

echo -e "Press <Enter> for empty fields.\n"
SECTION=${2:-$(read -n 200 -p "Section: "; echo ${REPLY})}
TITLE=${1:-$(read -p "Title: "; echo ${REPLY})}
SUBTITLE=${3:-$([ -z "${NEED_SUBTITLE}" ] && read -n 200 -p "Subtitle: "; echo ${REPLY})}

cat <<EOF >${FILENAME}
---
title: ${TITLE}
subtitle: ${SUBTITLE}
layout: ${LAYOUT}
section: ${SECTION}
sections: []
tags: []
lang: pt
copy: $(date +"%Y")
date: $(date +"%Y-%m-%d")
abstract:
---

EOF

