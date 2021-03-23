#!/bin/bash

usage() {
    cat << EOS
Usage: ./scripts/docker_push.sh

Environment variables:
  DKR_REPOSITORY: Docker repository name (required).
  DKR_TAG       : Docker tag (required).
EOS
    exit 1
}

push_production() {
    set -x
    docker push ${DKR_REPOSITORY}:latest
    [ "${DKR_TAG}" = "latest" ] && exit
    docker push ${DKR_REPOSITORY}:${DKR_TAG}
}

[ "${DKR_REPOSITORY}" = "" ] && usage
[ "${DKR_TAG}" = "" ] && usage
push_production
