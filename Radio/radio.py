import gpiozero as gp
import subprocess as sp
import random
import schedule
from oscpy.client import OSCClient as oscC

def count():
    global counter
    counter += 1
    if counter > 30:
        counter = 0
        dataOne   = []
        dataTwo   = []
        dataVol   = []
        set_middle()
        
    print(counter)
    
def scale(oldValue, oldMin, oldMax, newMin, newMax):
    return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin) + newMin)

def set_middle():
    middleOne = random.randrange(0, 1000)
    middleTwo = random.randrange(0, 1000)

def check_if_dials_changed(pot1, pot2, pot3):
    dataOne.append(pot1)
    dataTwo.append(pot2)
    dataVol.append(pot3)
    
    differenceOne = max(dataOne) - min(dataOne)
    differenceTwo = max(dataTwo) - min(dataTwo)
    differenceVol = max(dataVol) - min(dataVol)
    
    if differenceOne > 30 and differenceTwo > 30 and differenceVol > 30:
        counter = 0
        
def calculate_dial_distance_from_middle(num, middle, range):
    if abs(num - middle) > range:
        return 0
    else:
        return scale(num - middle, 0, range, 1, 0)


freqRange = 150
middleOne = 250
middleTwo = 750

freq1Pot  = gp.MCP3008(channel=1)
freq2Pot  = gp.MCP3008(channel=2)
volPot    = gp.MCP3008(channel=3)

counter   = 0
dataOne   = []
dataTwo   = []
dataVol   = []

set_middle()
schedule.every(1).seconds.do(count)

osc = oscC("127.0.0.1", 8000)
osc.send_message(b"/noiseVol", [1])
osc.send_message(b"/sampleVol", [0])

while True:
    schedule.run_pending()
    
    freq1Scaled = freq1Pot.value * 1000
    freq2Scaled = freq2Pot.value * 1000
    volScaled   = volPot.value * 1000
    
    check_if_dials_changed(freq1Scaled, freq2Scaled, volScaled)
    freqOne = calculate_dial_distance_from_middle(freq1Scaled, middleOne, freqRange)
    freqTwo = calculate_dial_distance_from_middle(freq2Scaled, middleTwo, freqRange)
    
    sampleVol = ((freqOne / 1000) + (freqTwo / 1000)) / 2
    #print(sampleVol)
    osc.send_message(b"/sampleVol", [sampleVol])
    
    noiseVol = scale(sampleVol, 0, 1, 1, 0)
    #print(noiseVol)
    osc.send_message(b"/noiseVol", [noiseVol])
    
    
