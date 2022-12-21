#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: ${0} side"
	exit 1
fi

if [ "$1" != "white" -a "$1" != "black" ]; then
	echo "Usage: ${0} side"
	exit 1
fi

python3 $(dirname "$0")/src/main.py ${1}
