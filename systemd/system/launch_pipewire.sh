#!/bin/sh

#pw-cli -m lm libpipewire-module-netjack2-driver '{ driver.mode=sink net.ip=192.168.1.21 net.port=19000 audio.ports=-1 midi.ports=1 netjack2.client-name=raspberry }' &
pw-cli -m lm libpipewire-module-netjack2-driver '{ net.ip=192.168.1.15 net.port=19000 audio.ports=2 midi.ports=1 netjack2.client-name=jackberry1 }' &
mpg123 $( cat ~/DotFiles/playlist/ibizaglobalradio.url )
