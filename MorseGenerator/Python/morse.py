import gpiozero as gp
import keyboard as kb
import pygame
import random
from threading import Timer

pygame.init()
windLoop = pygame.mixer.Sound('./Audio/windLoop.ogg')
pigeons = []
flags = []

for i in range (0,3):
    pigeons.append(pygame.mixer.Sound('./Audio/pigeon' +str(i) +'.ogg'))
    flags.append(pygame.mixer.Sound('./Audio/flag' +str(i) +'.ogg'))

def playRandomP():
    pygame.mixer.Sound.play(pigeons[random.randrange(len(pigeons))])
    tP = Timer(random.randrange(2, 5), playRandomP)
    tP.start()
    
def playRandomF():
    pygame.mixer.Sound.play(flags[random.randrange(len(flags))])
    tF = Timer(random.randrange(4, 7), playRandomF)
    tF.start()
    
playRandomP()
playRandomF()
pygame.mixer.Sound.play(windLoop, loops= -1)

led = gp.LED(14)
code = '. . .   . -   - .   - . .   - - .   . -   -   .'
charCounter = 0
time = 0

def output():
    global time, charCounter
#    print('OFF')
    time = 0
    if code[charCounter] == '.':
        time = 0.5
        led.on()
    elif code[charCounter] == '-':
        time = 1.5
        led.on()
    elif code[charCounter] == ' ':
        time = 0.5
        led.off()
    print(code[charCounter])
    charCounter += 1
    if charCounter <= len(code) - 1:
        t = Timer(time, output)
    else:
        led.off()
        t = Timer(3, output)
        time = 0
        charCounter = 0
    t.start()
#    print('ON')
    
output()