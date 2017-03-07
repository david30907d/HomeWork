#!/bin/bash
#argCheck.sh -- Checks whether files exists and is readable
[[ $# != 1 && $# != 2 ]] && { echo "Wrong number of argument" ; exit 1 ; }
if [ $# == 2 ]; then
	from=$1
	to=$2
	echo "from is ${1}, to is ${2}"
else
	to=$1
	echo "to is ${1}"
fi
exit 0
