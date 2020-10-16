#!/bin/sh
set -x

isort -rc --check-only .
CODE=$((${CODE:-0} + ${?}))

black --check .
CODE=$((${CODE:-0} + ${?}))

flake8
CODE=$((${CODE:-0} + ${?}))

mypy
CODE=$((${CODE:-0} + ${?}))

exit ${CODE}
