import gpiozero as gpio
import pygame
import numpy
import random
import asyncio
import time

freqRange = 150
freq1Pot = gpio.MCP3008(channel=0)
freq2Pot = gpio.MCP3008(channel=1)
volPot = gpio.MCP3008(channel=2)
counter = 0

def scale(oldValue, oldMin, oldMax, newMin, newMax):
    return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin) + newMin)

def setMiddle():
    global middle
    middle = random.randrange(0, 1000)
    print(middle)

def preload():
    setMiddle()
    global noise
    global sample
    pygame.mixer.init(frequency=44100)
    noiseList = numpy.random.uniform(-1,1,44100)
    noise = pygame.mixer.Sound(noiseList)
#    sample = pygame.mixer.Sound("./Audio/sample.wav")
    pygame.mixer.Sound.play(noise, loops=-1)
#    pygame.mixer.Sound.play(sample, loops=-1)

preload()

while True:
    freq1 = scale(freq1Pot.value, 0, 1, 0, 1000)
    freq2 = scale(freq2Pot.value, 0, 1, 0, 1000)
    combi = (freq1+freq2) / 2
    if abs(combi - middle) < freqRange:
        if combi >= middle:
            scaled = scale(combi, middle, middle + freqRange, 1, 0)
        else: scaled = scale(combi, middle, middle - freqRange, 1, 0)
    else: scaled = 0
    print(scaled)
#    sample.set_volume(scaled * volPot.value)
    noiseVol = scale(scaled, 0,1,1,0) * volPot.value
    noise.set_volume(noiseVol)
    time.sleep(0.2)
