#!/bin/bash

usage() {
    cat << EOS
Usage: ./scripts/docker_push.sh

Environment variables:
  DKR_REPOSITORY: Docker repository name (required).
  DKR_TAG       : Docker tag (required).
EOS
    exit 2
}

[ "${DKR_REPOSITORY}" = "" ] && usage
[ "${DKR_TAG}" = "" ] && usage
set -eux
docker push ${DKR_REPOSITORY}:${DKR_TAG}
