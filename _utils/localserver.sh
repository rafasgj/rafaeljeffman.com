#!/bin/bash -eu

SCRIPTDIR="$(realpath $(dirname "$0"))"
TOPDIR="$(dirname "${SCRIPTDIR}")"

TAG="$(whoami)/site_server"

[ -d "${TOPDIR}/.vendor/bundle" ] || mkdir -p "${TOPDIR}/.vendor/bundle"

PLATFORM="$(uname)"

existing="$(podman images -f reference="localhost/${TAG}" --format "{{ .Repository }}" | tr -d " ")"

if [ -z "${existing}" ] || [ "${1:-""}" == "-b" ]
then
    [ "${1:-""}" == "-b" ] && shift 1
    podman build -t "${TAG}" "${SCRIPTDIR}"
fi

podman run \
    --volume "${TOPDIR}:/srv/jekyll:rw" \
    --detach \
    -it \
    --rm \
    --read-only \
    --name jekyll_server \
    -p ${1:-4000}:4000 \
    "${TAG}"
