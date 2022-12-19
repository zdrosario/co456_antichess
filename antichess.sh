#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: ${0} side"
	exit 1
fi

if [ "$1" != "white" -a "$1" != "black" ]; then
	echo "Usage: ${0} side"
	exit 1
fi

# TODO: make runnable from any dir?
python3 ./src/main.py ${1}
