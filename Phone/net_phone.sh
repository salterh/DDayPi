#!/bin/bash

sleep 5
echo Loading Puredata net_phone.pd
puredata -audioaddoutdev "snd_rpi_hifiberry_dac" /home/pi/DDayPi/Phone/net_phone.pd &
sleep 5
echo Loading Python net_phone.py
python3 /home/pi/DDayPi/Phone/net_phone.py &

