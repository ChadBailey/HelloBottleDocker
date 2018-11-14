#!/bin/sh

docker container stop $(docker container ls -a -q | grep hellobottledocker)
