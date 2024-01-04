#!/bin/sh

usage() {
    cat <<EOF
usage: new_page.sh [-h] [-l LAYOUT] FILENAME [TITLE [SUBTITLE [SECTION]]]
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

TITLE=${1:-$(read -p "Title: "; echo ${REPLY})}
SUBTITLE=${2:-$(read -n 200 -p "Subtitle: "; echo ${REPLY})}
SECTION=${2:-$(read -n 200 -p "Section: "; echo ${REPLY})}

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

