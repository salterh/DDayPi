import gpiozero as gpio
from pydub import AudioSegment
from pydub.playback import play
import random

freq1 = gpio.RotaryEncoder(15, 18)
freq2 = gpio.RotaryEncoder(23, 24)
vol = gpio.RotaryEncoder(7, 1)
freqRange = 150

def scale(oldValue, oldMin, oldMax, newMin, newMax):
    return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin) + newMin)

def setCentre():
    global center = random.range(0, 1000)


            
