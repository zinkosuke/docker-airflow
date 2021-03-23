#!/bin/bash

mode=${1:-development}
DKR_REPOSITORY=${DKR_REPOSITORY:-airflow-local}
DKR_TAG=${DKR_TAG:-latest}

usage() {
    cat << EOS
Usage: ./scripts/docker_build.sh [mode]

Args:
  mode: Required (default dev).'

Environment variables:
  DKR_REPOSITORY: Docker repository name (default: airflow-local).
  DKR_TAG       : Docker tag (default: latest).
EOS
    exit 2
}

build_development() {
    set -x
    docker build --force-rm --no-cache --rm --target=development \
        -t ${DKR_REPOSITORY}:${DKR_TAG} .
    [ "${DKR_TAG}" = "latest" ] && exit
    docker tag ${DKR_REPOSITORY}:${DKR_TAG} ${DKR_REPOSITORY}:latest
}

build_production() {
    set -x
    docker build --force-rm --no-cache --rm \
        -t ${DKR_REPOSITORY}:${DKR_TAG} .
    [ "${DKR_TAG}" = "latest" ] && exit
    docker tag ${DKR_REPOSITORY}:${DKR_TAG} ${DKR_REPOSITORY}:latest
}

case "${mode}" in
    development)
        build_development
        ;;
    production)
        build_production
        ;;
    *)
        usage
        ;;
esac
