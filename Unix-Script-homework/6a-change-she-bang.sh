#!/bin/bash
#find all the perl file and change its she-bang into #!/usr/local/bin/perl
arr=$(ls *.pl )
for i in $arr
do 
	sed -i '1c #!/usr/local/bin/perl' ${i} 
	echo "she-bang of ${i} has been changed"
done
exit 0

