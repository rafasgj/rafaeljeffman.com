#!/bin/sh

SCRIPTDIR="$(realpath $(dirname "$0"))"
TOPDIR="$(dirname "${SCRIPTDIR}")"

TAG="$(whoami)/site_server"

[ -d "${TOPDIR}/.vendor/bundle" ] || mkdir -p "${TOPDIR}/.vendor/bundle"


existing=$(podman images -f reference="localhost/${TAG}" --format "{{ .Repository }}")

if [ -z "${existing}" ] || [ "$1" == "-b" ]
then
    shift 1
    podman build -t "${TAG}" "${SCRIPTDIR}"
fi

podman run \
    --volume "${TOPDIR}:/srv/jekyll:rw" \
    --volume "${TOPDIR}/.vendor/bundle:/usr/local/bundle:rw" \
    -p ${1:-4000}:4000 \
    "${TAG}"

