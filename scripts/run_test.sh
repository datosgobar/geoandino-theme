#!/usr/bin/env bash
set -e
DIR=$(dirname "$0")
cd ${DIR}/..

# TODO: Remove this
export CATALOG_URL="http://geonetwork:8080/"

echo "Running django-nose's tests"
python manage.py test
echo "pytest OK :)"
