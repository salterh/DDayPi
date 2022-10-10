#!/bin/bash

echo Loading Puredata flag.pd
puredata -nogui -audioaddoutdev "snd_rpi_hifiberry_dac" flag.pd &
echo Loading Python morse.py
python3 morse.py