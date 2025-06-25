#!/bin/sh

DIRECTORY="$(dirname $0)"
SCRIPT_DIR="$(realpath "${DIRECTORY}")"



while [ -f "$1" ]
do
    filename="$1"
    shift

    PAGELANG=$(sed -n '1 { /^---/ { :a N; /\n---/! ba; p } }' < "${filename}" | sed '$ s/---/.../' | python -c "import sys, yaml; data=yaml.safe_load(sys.stdin); print('pt_BR' if data and data.get('lang','pt') == 'pt' else 'en_US')")

    unset LIST
    declare -a LIST=()

    mapfile -t LIST < <(cat "${filename}" | \
        sed -e '1 { /^---/ { :a N; /\n---/! ba; d} }' \
            -e '/```/,/```/d' \
            -e 's/{%[^%]*%}//' \
            -e 's/`[^`]*`//' \
            -e '/[^\$]\$[^\$]\$/d' \
            | aspell --mode markdown --master ${PAGELANG} --home-dir="${SCRIPT_DIR}" --personal="custom_dict.${PAGELANG}.aspell" list | sort | uniq)

    if [ ${#LIST[@]} -ne 0 ]
    then
        echo "================================================================"
        echo " ${filename}" - ${PAGELANG} - "${#LIST[@]}" errors
        echo "================================================================"
        printf "%s\n" "${LIST[@]}"
    fi
done
