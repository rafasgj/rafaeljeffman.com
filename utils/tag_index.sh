#!/bin/sh

trap "exit 1" ERR

DIRECTORY="$(readlink -f $(dirname ${0}))"
TOPDIR="$(readlink -f "${DIRECTORY}/..")"

venv=$(mktemp -d)

python -m venv "${venv}"
. "${venv}/bin/activate"

pip install --upgrade pip
pip install -r requirements.txt

python "${DIRECTORY}/keyword_index.py"

rm -rf "${venv}"
