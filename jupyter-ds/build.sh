#!/bin/bash

docker build . -t premiseo/jupyter-ds:latest

# Standalone run
# docker run --name jupyter-ds -p 127.0.0.1:8888:8888/tcp --rm -it premiseo/jupyter-ds:latest
