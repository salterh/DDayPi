import gpiozero as gp
import pygame
import numpy
import random
import schedule

freqRange = 200
freq1Pot = gp.MCP3008(channel=0)
freq2Pot = gp.MCP3008(channel=1)
volPot = gp.MCP3008(channel=2)
counter = 0
data1 = []
data2 = []
dataV = []

def count():
    global counter
    counter += 1
    print(counter)
    if counter > 30:
        setMiddle()
        counter = 0
        data1 = []
        data2 = []
        dataV = []

def scale(oldValue, oldMin, oldMax, newMin, newMax):
    return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin) + newMin)

def setMiddle():
    global middle
    middle = random.randrange(0, 1000)

def preload():
    setMiddle()
    global noise
    global sample
    pygame.mixer.init(devicename="snd_rpi_hifiberry_dac Stereo")
    noiseList = numpy.random.uniform(-1,1,44100)
    noise = pygame.mixer.Sound(noiseList)
#    sample = pygame.mixer.Sound("./Audio/sample.wav")
    pygame.mixer.Sound.play(noise, loops=-1)
#    pygame.mixer.Sound.play(sample, loops=-1)
    
preload()
schedule.every(1).seconds.do(count)

while True:
    schedule.run_pending()
    freq1 = int(scale(freq1Pot.value, 0, 1, 0, 1000))
    print(freq1)
    freq2 = int(scale(freq2Pot.value, 0, 1, 0, 1000))
    volScale = int(scale(volPot.value, 0, 1, 0, 1000))
    data1.append(freq1)
    data2.append(freq2)
    dataV.append(volScale)
    difference1 = max(data1) - min(data1)
    difference2 = max(data2) - min(data2)
    differenceV = max(dataV) - min(dataV)
    if difference1 > 30 or difference2 > 30 or differenceV > 30:
        data1 = []
        data2 = []
        dataV = []
        counter = 0
    combi = (freq1+freq2) / 2
    if abs(combi - middle) < freqRange:
        if combi >= middle:
            scaled = scale(combi, middle, middle + freqRange, 1, 0)
        else: scaled = scale(combi, middle, middle - freqRange, 1, 0)
    else: scaled = 0
#    sample.set_volume(scaled * volPot.value)
    noiseVol = scale(scaled, 0,1,1,0) * volPot.value
    noise.set_volume(noiseVol)
    
