import gpiozero as gpio
import pygame
import numpy
import random
import asyncio

freqRange = 150
freq1Pot = gpio.MCP3008(channel=0)
freq2Pot = gpio.MCP3008(channel=1)
volPot = gpio.MCP3008(channel=2)
counter = 0

def scale(oldValue, oldMin, oldMax, newMin, newMax):
    return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin) + newMin)

def setMiddle():
    global middle
    middle = random.range(0, 1000)

def preload():
    global noise
    global sample
    pygame.mixer.init(frequency=44100)
    noiseList = numpy.random.uniform(-1,1,44100)
    noise = pygame.mixer.Sound(noiseList)
#    sample = pygame.mixer.Sound("./Audio/sample.wav")
    pygame.mixer.Sound.play(noise, loops=-1)
#    pygame.mixer.Sound.play(sample, loops=-1)

def timerFunc():
    counter+=1
    if counter > 30:
        setCentre()

preload()

while True:
    combi = (freq1Pot.value / freq2Pot.value) / 2
    if abs(combi - middle) > range:
        if (combi >= middle): scaled = scale(combi, middle, middle + freqRange, 1, 0)
        else: scaled = scale(combie, middle, middle - freqRange, 1, 0)
    else: scaled = 0
#    sample.set_volume(scaled * volPot.value)
    noise.set_volume(scale(scaled, 0, 1, 1, 0) * volPot.value)
        
    


     

    
