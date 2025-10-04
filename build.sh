#!/usr/bin/env bash

[[ ! -f "action.yml" ]] && echo "Wrong Directory" && exit 1
_IMAGE=$(grep -o 'ghcr.io/.*' action.yml | sed 's/".*//')
echo "Using image: ${_IMAGE}"
docker build --tag "${_IMAGE}" .
act -j test -e event.json --action-offline-mode "$@"
