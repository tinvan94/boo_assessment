
FROM ubuntu:16.04
ARG PYTHON_VERSION=3.9.11

# change suffix _x to any new value to force a rebuild
RUN echo 191210_c

# deb package initials
RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y build-essential curl git wget

# install dependencies required when run :soffice binary  ref. https://github.com/microsoft/vscode/issues/13089
RUN apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

RUN apt -y install libgeos-dev


RUN echo 200121_a

# install pyenv
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer \
    | bash
ENV PATH=$HOME/.pyenv/bin:$PATH
RUN git clone https://github.com/pyenv/pyenv.git /tmp/pyenv && \
    cd /tmp/pyenv/plugins/python-build && \
    ./install.sh && \
    rm -rf /tmp/pyenv

RUN python-build $PYTHON_VERSION /usr/local/

# update pip
RUN python -m pip install --upgrade pip
RUN python -m pip install wheel

# install pipenv
RUN python -m pip install pipenv

# set utf8 to fix error when running pipenv > Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment  # ref. https://github.com/docker-library/python/issues/13#ref-pullrequest-164133459
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# create THIS_APP folder
WORKDIR /app

# change suffix _x to any new value to force a rebuild
RUN echo 191210_b

# pipenv setup
ENV PIPENV_VERBOSITY=-1
    # skip any pipenv warning
ENV PIPENV_VENV_IN_PROJECT=1
    # .venv in same folder
ENV PIPENV_CACHE_DIR=/root/.pipenv/cache
    # cache folder hoping it faster

# install pip packages
COPY ./Pipfile      ./
COPY ./Pipfile.lock ./
RUN pipenv install

# bundle app source
COPY . .

# for documentation on port - gunicorn default port 5000  #NOTE we can custom this port later with docker-compose
EXPOSE 8000

CMD PYTHONPATH=`pwd`  pipenv run python main.py
