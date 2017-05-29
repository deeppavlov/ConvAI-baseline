#!/usr/bin/env bash

if [ ! -d data/train-v1.1.json ]; then
    wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json -O data/train-v1.1.json
fi

pip3 install -r bot_code/requirements.txt

# question generation
cd question_generation
./setup
cd $OLDPWD