import gpiozero as gpio
import pygame
import numpy
import random
import time

freqRange = 150
freq1 = 0, freq2 = 1000
middle = 500, range = 150
counter = 0

freq1Pot = gpio.MCP3008(0)
freq2Pot = gpio.MCP3008(1)
volPot = gpio.MCP3008(2)

def preload():
    global noise
    global sample
    pygame.mixer.init(frequency=44100)
    noiseList = numpy.random.uniform(-1,1,44100)
    noise = pygame.mixer.Sound(noiseList)
    sample = pygame.mixer.Sound("./Audio/sample.wav")
    setup()

def setup():
    pygame.mixer.Sound.play(noise, loops=-1)
    countUp()
    
    
def countUp():
    counter += 1
    if counter > 30:
        setMiddle()
        counter = 0
    print(counter)
    time.sleep(1)
    countUp()
    
def reset():
    counter = 0

def scale(oldValue, oldMin, oldMax, newMin, newMax):
    return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin) + newMin)

def setCentre():
    global middle
    middle = random.range(0 + freqRange, 1000 - freqRange)

def print_val():
    print(testPot.steps)
    print(testPot.value)
    
testPot = gpio.RotaryEncoder(20,21, wrap = False, max_steps = 100)
testPot.when_rotated = print_val
    
while True:
    freq1 = freq1Pot.value
    freq2 = freq2Pot.value
    combi = (freq1 + freq2) / 2
    scaled = 0
    if abs(combi - middle) < range:
        if combi >= centre: scaled = scale(combi, middle, middle + range, 1, 0)
        else: scaled = scale(combi, middle, middle - range, 1, 0)
    else scaled = 0
    sample.set_volume(scaled * volPot.value)
    noise.set_volume(scale(scaled, 0, 1, 1, 0) * volPot.value)
