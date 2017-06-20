# Conversational Intelligence Challenge baseline solution

It is based on two papers:
* Neural Question Generation from Text: A Preliminary Study
https://arxiv.org/abs/1704.01792

* Bidirectional Attention Flow for Machine Comprehension
https://arxiv.org/abs/1611.01603

We are using forked repo of Allen AI2 bi-att-flow: https://github.com/allenai/bi-att-flow

## Requirements
* Docker ver. 17.03+:
    * Ubuntu: https://docs.docker.com/engine/installation/linux/ubuntu/#install-using-the-repository
    * Mac: https://download.docker.com/mac/stable/Docker.dmg
    * Docker-compose ver. 1.13.0+: https://docs.docker.com/compose/install/
* Python 3
* ZeroMQ
* pyzmq dependencies:
    * Ubuntu: ```sudo apt-get install libzmq3-dev```
    * Mac: ```brew install zeromq --with-libpgm```

Python packages will be installed by ```setup.sh``` script.

## Cloning
It you're using git version 1.6.5+, you could clone with dependencies:

```git clone --recursive git@github.com:MIPTDeepLearningLab/ConvAI-baseline.git```

If you're using earlier versions of git, or if you have the repo downloaded without ```--recursive```, you should clone dependency repos additionally:

```bash
git clone git@github.com:MIPTDeepLearningLab/ConvAI-baseline.git
cd ConvAI-baseline
git submodule update --init --recursive
```

## Setup
Run ```setup.sh```

Setup will download docker images, models and data files, so you have no need to download any of that by yourself.

### Telegram integration
To make your bot work, you need to run it first time. It will create ```bot_code/config.ini``` file with stubs for secret tokens from Telegram. You need to register your our bot [here](https://core.telegram.org/bots#botfather) and replace stub tokens with provided ones.

##  Running
```./bot.sh start|stop|restart|status```
