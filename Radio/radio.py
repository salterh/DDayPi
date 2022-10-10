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
    
def scale(oldValue, oldMin, oldMax, newMin, newMax):
    return (((oldValue - oldMin) * (newMax - newMin)) / (oldMax - oldMin) + newMin)

def set_middle():
    middleOne = random.randrange(0, 1000)
    middleTwo = random.randrange(0, 1000)
    print(middleOne, middleTwo)

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
    if num < (middle + range) and num > (middle - range):
        if num < middle:
            return scale(num, middle - range, middle, 0, 1)
        elif num > middle:
            return scale(num, middle, middle + range, 1, 0)
    else:
        return 0


freqRange = 500
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


while True:
    schedule.run_pending()
    print(freq1Pot.value, freq2Pot.value, volPot.value)
    freq1Scaled = freq1Pot.value * 1000
    freq2Scaled = freq2Pot.value * 1000
    
    check_if_dials_changed(freq1Scaled, freq2Scaled, volPot.value)
    freqOne = calculate_dial_distance_from_middle(freq1Scaled, middleOne, freqRange)
    freqTwo = calculate_dial_distance_from_middle(freq2Scaled, middleTwo, freqRange)
    
    sampleVol = (freqOne + freqTwo) / 2
    
    osc.send_message(b"/sampleVol", [sampleVol])
    noiseVol = scale(sampleVol, 0, 1, 1, 0)
    osc.send_message(b"/noiseVol", [noiseVol])
    osc.send_message(b"/mainVol", [volPot.value])
    
    
