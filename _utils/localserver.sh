#!/bin/sh

SCRIPTDIR="$(realpath $(dirname "$0"))"
TOPDIR="$(dirname "${SCRIPTDIR}")"

TAG="$(whoami)/site_server"

[ -d "${TOPDIR}/.vendor/bundle" ] || mkdir -p "${TOPDIR}/.vendor/bundle"


existing=$(podman images -f reference="localhost/${TAG}" --format "{{ .Repository }}")

[ -z "${existing}" ] && podman build -t "${TAG}" "${SCRIPTDIR}"

podman run \
    --volume "${TOPDIR}:/srv/jekyll:Z" \
    --volume "${TOPDIR}/.vendor/bundle:/usr/local/bundle:Z" \
    -p 4000:4000 \
    "${TAG}"

