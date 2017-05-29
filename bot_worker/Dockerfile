FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04
MAINTAINER Denis Antyukhov <aphex@mit.edu>

ENV CUDA_ROOT=/usr/local/cuda \
    TF_BINARY_URL="https://ci.tensorflow.org/view/Nightly/job/nightly-matrix-linux-gpu/TF_BUILD_IS_OPT=OPT,TF_BUILD_IS_PIP=PIP,TF_BUILD_PYTHON_VERSION=PYTHON2,label=gpu-linux/lastSuccessfulBuild/artifact/pip_test/whl/tensorflow_gpu-0.12.0rc0-cp27-none-linux_x86_64.whl"

RUN apt-get update && apt-get install -y --no-install-recommends \
        software-properties-common \
        build-essential \
        curl \
        git \
        wget \
        libfreetype6-dev \
        libzmq3-dev \
        pkg-config \
        rsync \
        unzip \
        libhdf5-dev \
        zip \
        zlib1g-dev \
        libhdf5-dev \
        libyaml-dev \
        gfortran \
        libopenblas-dev \
        liblapack-dev \
        nano \
        htop \
        screen \
        bash-completion \
        python-dev \
        python-nose \
        python-numpy \
        python-h5py \
        python-yaml \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3

#################
# python2 stuff #
#################

RUN wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py && \
    pip --no-cache-dir install \
        tqdm \
        click \
        ipykernel \
        jupyter \
        matplotlib \
        cython \
        nltk \
        scikit-learn \
        plotly \
        pandas \
        xlrd \
        lxml \
        emoji \
        python_telegram_bot

RUN pip install --upgrade ${TF_BINARY_URL} --user

VOLUME ["/lm_1b", "/data", "/output"]
