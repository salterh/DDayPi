import gpiozero as gp
import pygame

nextB = gp.Button(14)
prevB = gp.Button(15)
clueB = gp.Button(18)
ledB = gp.Button(23)
ledOut = gp.LED(24)

pygame.init()
global currentlyPlaying

currentlyPlaying = None
mainCount = -2
clueCount = -1
intros = []
LBClues = []
NCClues = []
MOClues = []
UDClues = []

def loadSounds():
    global intros, mainIntro, LBClues, NCClues, MOClues, UDClues
    
    mainIntro = pygame.mixer.Sound('./Audio/mainIntro.ogg')
    for i in range(0,4):
        intros.append(pygame.mixer.Sound('./Audio/intro' +str(i) +'.ogg'))
    for i in range(0,2):
        LBClues.append(pygame.mixer.Sound('./Audio/LBClue' +str(i) + '.ogg'))
        NCClues.append(pygame.mixer.Sound('./Audio/NCClue' +str(i) + '.ogg'))
    MOClues.append(pygame.mixer.Sound('./Audio/MOClue0.ogg'))
    UDClues.append(pygame.mixer.Sound('./Audio/UDClue0.ogg'))

loadSounds()

clues = [LBClues, NCClues, MOClues, UDClues]

def playNext():
    global mainCount, currentlyPlaying
    if currentlyPlaying != None:
        print("Stopping Current (Next)")
        pygame.mixer.Sound.stop(currentlyPlaying)
    mainCount+=1
    if mainCount > 3:
        mainCount = 3
    if mainCount == -1:
        print("Playing main...")
        pygame.mixer.Sound.play(mainIntro)
        currentlyPlaying = mainIntro
    else:
        print("Playing puzzle intro: " +str(mainCount))
        pygame.mixer.Sound.play(intros[mainCount])
        currentlyPlaying = intros[mainCount]
    
    
def playPrev():
    global mainCount, currentlyPlaying
    if currentlyPlaying != None:
        print("Stopping Current (Prev)")
        pygame.mixer.Sound.stop(currentlyPlaying)
    mainCount-=1
    if mainCount < 0:
        mainCount = 0
    if mainCount == -1:
        print("Playing main...")
        pygame.mixer.Sound.play(mainIntro)
        currentlyPlaying = mainIntro

    else:
        print("Playing puzzle intro: " +str(mainCount))
        pygame.mixer.Sound.play(intros[mainCount])
        currentlyPlaying = intros[mainCount]
    
    
def playClue():
    global mainCount, clueCount, currentlyPlaying
    if currentlyPlaying != None:
        pygame.mixer.Sound.stop(currentlyPlaying)
    clueCount+=1
    if clueCount > len(clues[mainCount]) - 1:
        clueCount = 0
    if mainCount != -1:
        print("Playing clue: " +str(clueCount) +" for puzzle: " +str(mainCount))
        pygame.mixer.Sound.play(clues[mainCount][clueCount])
        currentlyPlaying = clues[mainCount][clueCount]
    else:
        pygame.mixer.Sound.play(intros[mainCount])
        currentlyPlaying = mainIntro

nextB.when_pressed = playNext
prevB.when_pressed = playPrev
clueB.when_pressed = playClue

while True:
    if ledB.is_pressed:
        ledOut.on()
    else:
        ledOut.off()



