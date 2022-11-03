#!/bin/bash

sleep 5
echo Loading Puredata phone.pd
puredata -audioaddoutdev "snd_rpi_hifiberry_dac" /home/pi/DDayPi/Phone/phone.pd &
sleep 5
echo Loading Python phone.py
python3 /home/pi/DDayPi/Phone/phone.py &

