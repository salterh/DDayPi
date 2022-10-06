#!/bin/bash

echo loading Puredata radio.pd 
puredata -nogui -audioaddoutdev "snd_rpi_hifiberry_dac" radio.pd &
echo Loading Python radio.py
python3 radio.py