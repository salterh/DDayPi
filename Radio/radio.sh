#!/bin/bash

echo loading Puredata radio.pd 
puredata -audioaddoutdev "snd_rpi_hifiberry_dac" radio.pd
