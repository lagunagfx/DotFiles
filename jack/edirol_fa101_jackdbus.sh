#!/bin/sh

jack_control start
jack_control ds firewire
jack_control dps device FA101
jack_control dps period 128
jack_control dps nperiods 3
jack_control dps rate 96000

sleep 10

a2j_control --ehw
a2j_control --start
