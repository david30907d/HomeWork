#!/bin/bash
#find a given command on the search path
## the pathname found or a failure message is displayed
cmd="$1"
path=$(echo $PATH | tr ':' ' ') ## : is replaced by a space
for dir in $path
do
	if [[ -x "$dir/$cmd" ]]
		then
		echo "FOUND: $dir/$cmd"
		exit 0
	fi
done
echo "$cmd not on $PATH"
