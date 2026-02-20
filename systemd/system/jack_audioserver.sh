#!/bin/sh

if [ ! -z "$( aplay -l | grep UMC404HD )" ];
then
	jackd -S -R -d alsa -d hw:U192k -p 512 -n 3 -r 48000 -H -X seq
fi

#jackd -S -R -d net -a 192.168.1.15 -p 19000 -C 4 -P 4 -i 2 -o 2 -n jackberry1 -l 3
#jackd -R -S -d alsa -d hw:UA101 -p 512 -n 3 -r 48000 -H -X seq
