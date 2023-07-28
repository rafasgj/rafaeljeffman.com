#!/bin/sh

TAG="$(whoami)/jekyll"

[ -d "${PWD}/.vendor/bundle" ] || mkdir -p "${PWD}/.vendor/bundle"


existing=$(podman images -f reference="localhost/${TAG}" --format "{{ .Repository }}")

[ -z "${existing}" ] && podman build -t "${TAG}" .

podman run \
    --volume "${PWD}:/srv/jekyll:Z" \
    --volume "${PWD}/.vendor/bundle:/usr/local/bundle:Z" \
    -p 4000:4000 \
    "${TAG}"

