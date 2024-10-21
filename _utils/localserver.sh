#!/bin/sh

SCRIPTDIR="$(realpath $(dirname "$0"))"
TOPDIR="$(dirname "${SCRIPTDIR}")"

TAG="$(whoami)/site_server"

[ -d "${TOPDIR}/.vendor/bundle" ] || mkdir -p "${TOPDIR}/.vendor/bundle"

PLATFORM="$(uname)"

if [ "$PLATFORM" == "Linux" ]
then
    VOLOPT="Z"
else
    VOLOPT="rw"
fi

existing=$(podman images -f reference="localhost/${TAG}" --format "{{ .Repository }}")

if [ -z "${existing}" ] || [ "$1" == "-b" ]
then
    shift 1
    podman build -t "${TAG}" "${SCRIPTDIR}"
fi

podman run \
    --volume "${TOPDIR}:/srv/jekyll:${VOLOPT}" \
    --volume "${TOPDIR}/.vendor/bundle:/usr/local/bundle:${VOLOPT}" \
    --detach \
    --rm \
    --read-only \
    --name jekyll_server \
    -p ${1:-4000}:4000 \
    "${TAG}" \
    bundle exec jekyll serve --trace --incremental
