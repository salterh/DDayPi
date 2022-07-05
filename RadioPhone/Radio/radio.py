import gpiozero as gpio
import pygame
import numpy
import random

def preload():
    global noise
    global sample
    pygame.mixer.init(frequency=44100)
    noiseList = numpy.random.uniform(-1,1,44100)
    noise = pygame.mixer.Sound(noiseList)
#    sample = pygame.mixer.Sound("./Audio/sample.wav")
    setup()

def setup():
    pygame.mixer.Sound.play(noise, loops=-1)
    print(noise.get_raw())

preload()

while True:
    global vol
    vol = scale(volPot.value,-1,1,0,1)
    noise.set_volume(vol)
    

#freq1Pot = gpio.RotaryEncoder(15, 18)
#freq2Pot = gpio.RotaryEncoder(23, 24)
#volPot = gpio.RotaryEncoder(7, 1)
freqRange = 150

def scale(oldValue, oldMin, oldMax, newMin, newMax):
    return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin) + newMin)

def setCentre():
    global center
    center = random.range(0 + freqRange, 1000 - freqRange)
     

    
