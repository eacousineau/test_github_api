#!/bin/bash
set -eux -o pipefail

cd $(dirname $0)/..
rm -rf ./venv && mkdir ./venv
python3 -m virtualenv -p python3 --system-site-packages ./venv
./venv/bin/pip install -I -r ./requirements.txt
