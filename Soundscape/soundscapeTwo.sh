#!/bin/bash

echo Loading Puredata soundscapeTwo.pd
puredata -nogui -audioaddoutdev "snd_rpi_hifiberry_dac" soundscapeTwo.pd
