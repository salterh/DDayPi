#!/bin/bash

echo Loading Puredata phone.pd
puredata -nogui -audioaddoutdev "snd_rpi_hifiberry_dac" phone.pd &
echo Loading Python phone.py
python3 phone.py

