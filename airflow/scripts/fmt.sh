#!/bin/sh
set -x

isort -rc .

black .
