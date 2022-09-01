import gpiozero as gp
import pygame

pygame.mixer.init(devicename="snd_rpi_hifiberry_dac Stereo")
phoneRing = pygame.mixer.Sound("./Audio/phoneRing.ogg")

dialCount = gp.Button(23)                                                                            
dialStart = gp.Button(18)
count = -1
answer = [1,2,3,4,5,6,7,8,9,10]
playerInput = []

def addCount():
    global count
    count+=1
    print(count)
    
def dialRelease():
    global count
    global playerInput
    if count >= 10:
        count = 0
    playerInput.append(count)
    print(playerInput)
    count = -1
    if len(playerInput) == len(answer):
        if playerInput == answer:
            print('Good job')
#            play(fullMessage)
        else:
            print('Try again')
        playerInput = []

dialCount.when_released = addCount
dialStart.when_released = dialRelease

while True:
    if dialStart.is_pressed:
        print('working')

