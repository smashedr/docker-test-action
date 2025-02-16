source version.txt
docker build src --platform linux/amd64 --tag "ghcr.io/smashedr/docker-test-action:${VERSION}"
act -j test -e event.json --action-offline-mode "$@"
