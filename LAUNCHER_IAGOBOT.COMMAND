#!/bin/sh
echo Starting ChatBot
export PYTHONPATH=$(dirname $0)/libs:$(dirname $0)/src/:$(dirname $0)/src/ChatterBot-blacklist
cd $(dirname $0)/src
python -W ignore ./IAGOBOT.py
echo Done