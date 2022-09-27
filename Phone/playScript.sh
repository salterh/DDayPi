#!/bin/bash

echo Loading Puredata playSound.pd
puredata -nogui -audioaddoutdev "snd_rpi_hifiberry_dac" playSound.pd &
echo Loading Python phoneInput.py
python3 phoneInput.py

