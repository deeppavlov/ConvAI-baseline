# Conversational Intelligence Challenge baseline solution

It is based on two papers: 
* Neural Question Generation from Text: A Preliminary Study
https://arxiv.org/abs/1704.01792

* Bidirectional Attention Flow for Machine Comprehension
https://arxiv.org/abs/1611.01603

We are using forked repo of Allen AI2 bi-att-flow: https://github.com/allenai/bi-att-flow

## Requirements
* Docker ver. 17.03+:

Ubuntu: https://docs.docker.com/engine/installation/linux/ubuntu/#install-using-the-repository
Mac: https://download.docker.com/mac/stable/Docker.dmg
Docker-compose ver. 1.13.0+: https://docs.docker.com/compose/install/

* Python 3
* ZeroMQ

pyzmq dependencies: 
   * Ubuntu ```sudo apt-get install libzmq3-dev``` 
   * or for Mac ```brew install zeromq --with-libpgm```

Python packages will be installed by setup script.

## Setup
run ```setup.sh```

Setup will download docker images, models and data files, so you have no need to download any of that by youself.

## Bot
Simply run:
```python3 bot_code/bot.py```
