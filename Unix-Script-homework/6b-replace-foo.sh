#!/bin/bash
#find all the perl file and change its she-bang into #!/usr/local/bin/perl
for i in $@ #$@ contains all the file name you want to replace, it's a array of file name.
do 
	echo "all foo in ${i}	has been changed to uppercase"
	sed -i 's/foo/FOO/g' ${i}
done
exit 0

