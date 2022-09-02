import pygame
import threading as thr
import random

pygame.init()
pygame.mixer.init(devicename="snd_rpi_hifiberry_dac Stereo")

baseLayers = []
oneShots = []
oneShotPool = []
convos = []
convoCounter = 0;
channels = []
ONESHOTEND = pygame.USEREVENT + 0
CONVOLINEEND = pygame.USEREVENT + 1

extW = ".wav"
extO = ".ogg"

def preload():
    for i in range(6):
        #Channel 0 is for conversations, 1 is for oneShots
        channels.append(pygame.mixer.Channel(i))
        if i == 0:
            channels[i].set_endevent(CONVOLINEEND)
        elif i == 1:
            channels[i].set_endevent(ONESHOTEND)
        #The rest are for baseLayers
    for i in range(4):
        baseLayers.append(pygame.mixer.Sound("./Audio/baseLayer" + str(i) + extW))
        channels[i+2].play(baseLayers[i], loops= -1)
        oneShots.append(pygame.mixer.Sound("./Audio/oneShot" + str(i) + extW))
        if i < 3:
            convos.append(pygame.mixer.Sound("./Audio/convoLine" + str(i) + extO))

def playOneShot():
    if len(oneShotPool == 0):
        oneShotPool = oneShots
    if len(oneShotPool > 1):
        index = random.randrange(0, len(oneShotPool))
    else:
        index = 0
    print("Playing: " + index)
    channels[1].queue(oneShotPool.pop(index))
    oneShotTimer = thr.Timer(random.uniform(10,40), playOneShot)
    oneShotTimer.start()

def playConvo():
    global convoCounter
    channels[0].play(convos[convoCounter])
    #print("Playing: ", str(convoCounter))
    convoCounter += 1

            
preload()
playConvo()
playOneShot()
            
while True:
    for event in pygame.event.get():
        if event.type == CONVOLINEEND:
            if convoCounter > 2:
                #print("Finishing up...")
                convoCounter = 0
                convoTimer = thr.Timer(random.randrange(10.0,20.0), playConvo)
                convoTimer.start()
            else:
                playConvo()
            