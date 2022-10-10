#!/bin/bash

echo Loading Puredata soundscapeOne.pd
puredata -nogui -audioaddoutdev "snd_rpi_hifiberry_dac" soundscapeOne.pd
