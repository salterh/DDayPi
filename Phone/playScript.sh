#!/bin/bash

echo Attempting to play message

aplay message.ogg

SDL_AUDIODRIVER="alsa" AUDIODEV="hw:1,0" ffplay message.ogg
