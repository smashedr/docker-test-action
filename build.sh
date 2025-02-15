docker build src --platform linux/amd64 --tag ghcr.io/smashedr/docker-test-action:v1
act -j test -e event.json --action-offline-mode "$@"
