#!/bin/sh

docker container stop $(docker container ls |grep hellobottledocker | awk -F ' ' '{print $1}')
