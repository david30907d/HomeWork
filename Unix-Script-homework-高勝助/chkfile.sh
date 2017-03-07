#!/bin/sh
# filetest.sh -- Checks whether files exists and is readable
[ $# -ne 1 ] && { echo "Usage: $0 file" ; exit 1 ; }
if [ -f $1 ]; then # [ -f $1 ] means whether $1 exist and is a file 
	if [ ! -r $1 ] ; then # -r means $1 is readable
		echo "File exists but is not readable"
	else
		echo "File is readable"
	fi
else
	echo "File doesn't exist"
fi
