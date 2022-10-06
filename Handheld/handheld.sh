#!/bin/bash

echo Loading Puredata handheld.pd
puredata -nogui -audioaddoutdev "snd_rpi_hifiberry_dac" handheld.pd &
echo Loading Python handheld.py
python3 handheld.py