#!/bin/sh

alsamidi_check() {
	if [ $# -eq 1 ];
	PORT="$1"
	then
		if [ ! -z "$( aconnect -l | grep $PORT )" ];
		then
			printf "%s found.\n" $PORT
			return 0
		else
			printf "ERROR : %s not found.\n" $PORT
			return 1
		fi
	fi
}

alsamidi_connect() {
	if [ $# -eq 2 ];
	then
		SRC="$1"
		DST="$2"
	
		alsamidi_check $SRC && alsamidi_check $DST && aconnect $SRC $DST && printf "Connected ALSA MIDI port %s to %s.\n" "$SRC" "$DST"
	fi
}

alsamidi_connect UM-1SX TD-3
alsamidi_connect UM-1SX Rocket
alsamidi_connect UM-1SX Streichfett

exit 0
