import pygame
import schedule

pygame.mixer.init(devicename="snd__rpi_hifiberry_dac Stereo")
baseLayers = []
oneShots = [], oneShotPool = []
convos = []
channels = []
chance = 50
time = 10000


preload()

def preload():
    for i in range(4):
        baseLayers[i] = pygame.mixer.Sound("./Audio/baseLayer" + i + ".ogg")
        oneShots[i] = pygame.mixer.Sound("./Audio/oneShot" + i + ".ogg")
        if i != 3:
            convos[i] = pygame.mixer.Sound("./Audio/convoLine" + i + ".ogg")
            channels[i] = pygame.mixer.Channel(i)
            
def playConvo():
    
        
    