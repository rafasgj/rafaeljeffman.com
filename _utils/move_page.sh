#!/bin/sh

SCRIPTDIR="$(realpath $(dirname "$0"))"
TOPDIR="$(dirname ${SCRIPTDIR})"
TEMPLATEDIR="${SCRIPTDIR}/templates"

if [ "${PWD}" != "${TOPDIR}" ]
then
    >&2 echo "This script must be executed from repository root."
    exit 1 
fi

mkdir -p "$(dirname "${2}")" 2>/dev/null

git mv "$1" "$2"
sed -e "s#@URL@#/${2%.*}#" < "${TEMPLATEDIR}/redirect.md" > "$1"
git add "$1"

echo "Review these documents..."
grep -rl "$(basename "$1" ".md")" --exclude-dir=_* --exclude-dir=.vendor --exclude-dir=.git
