#!/bin/sh

usage() {
    cat <<EOF
usage: new_page.sh [-h] [-i LANG] [-l LAYOUT] FILENAME [TITLE SECTION [[SUBTITLE]]]
EOF
}

read_data() {
    if [ -z "${PRINTED}" ] && [ "$#" -eq 1 ]
    then
        PRINTED="yes"
        >&2 echo -e "Press <Enter> for empty fields.\n"
    fi
    name=$1
    declare -n var_name=$1
    shift
    [ "$#" -gt 0 ] && var_name="$*" || read -e -n 200 -p "${name}: " ${!var_name}
}

LAYOUT="main"
lang="pt"

while getopts ":hi:l:" opt
do
    case $opt in
        h) usage && exit 0 ;;
        i) lang="${OPTARG}" ;;
        l) LAYOUT="${OPTARG}" ;;
        *) usage && exit 1 ;;
    esac
done

shift $((OPTIND - 1))

[ $# == 0 ] && usage && exit 1

FILENAME="${1}"
shift
mkdir -p "$(dirname ${FILENAME})"

NEED_SUBTITLE="NO"
[ -z "${1}" ] && NEED_SUBTITLE="" || NEED_SUBTITLE="NO"

read_data SECTION "$2"
read_data TITLE "$1"
[ -n "$1" ] && [ -z "$3" ] || read_data SUBTITLE "$3"

cat <<EOF >"${FILENAME}"
---
title: ${TITLE}
subtitle: ${SUBTITLE}
layout: ${LAYOUT}
section: ${SECTION}
sections: []
tags: []
lang: ${lang}
copy: $(date +"%Y")
date: $(date +"%Y-%m-%d")
abstract:
---

* What to accomplish?
* Why is it needded?
* How to do it?
* When to do it?
* Wrap up / Action items

EOF

