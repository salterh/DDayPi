import gpiozero as gp
import pygame

pygame.init()
pygame.mixer.init(devicename="snd_rpi_hifiberry_dac Stereo")
pygame.mixer.music.load("message.wav")
pygame.mixer.music.play()

dialCount = gp.Button(23)                                                                            
dialStart = gp.Button(18)
count = -1
answer = [1,1,1]
playerInput = []

def addCount():
    global count
    count+=1
    
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
            playsound("message.wav")
        else:
            print('Try again')
        playerInput = []

dialCount.when_released = addCount
dialStart.when_released = dialRelease

while True:
    pass

