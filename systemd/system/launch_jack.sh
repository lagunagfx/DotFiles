#!/bin/sh

systemctl --user stop pipewire.socket
sleep .5
systemctl --user stop pipewire.service
sleep .5

jackd -S -R -d net -a 192.168.1.15 -p 19000 -C 0 -P 2 -n jackberry1 -l 3 &
sleep 1
a2jmidid -e &
