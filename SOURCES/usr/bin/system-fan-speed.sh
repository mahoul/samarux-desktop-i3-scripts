#!/usr/bin/sh

if ! grep -q hypervisor /proc/cpuinfo; then

	speed=$(sensors | grep fan1 | awk '{print $2; exit}')
	if [ "$speed" != "" ]; then
	    speed_round=$(echo "scale=1;$speed/1000" | bc -l )
	    #echo "# $speed_round"
	    echo "$speed"
	else
	   echo "0"
	fi
else
	echo "0"
fi
