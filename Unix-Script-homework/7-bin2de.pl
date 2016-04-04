#!/usr/bin/perl
# bin2de.pl:, Converts binary numbers to decimal

foreach $i (@ARGV){
	$bin = $i;
	@arr=split(//,$i);
	#//means split nothing, so it'll return a array.
	$length = @arr;#the value of @arr is its length.
	@arr=reverse(@arr); #reverse.
	$ans=0;
	$mul=1;
	foreach $j (@arr){
		$ans+=($j*$mul);
		$mul*=2;
	}
	print("the decimal of $bin is : $ans\n");
}
