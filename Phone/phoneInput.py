import gpiozero as gp
import subprocess as sp

dialCount = gp.Button(25)                                                                            
dialStart = gp.Button(24)
count = -1
answer = [1,1,1]
playerInput = []
##sp.call("puredata -nogui -audioaddoutdev \"snd_rpi_hifiberry_dac\" playSound.pd", shell=True)


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
            print("Done")
            sp.call("puredata -nogui -audioaddoutdev \"snd_rpi_hifiberry_dac\" playSound.pd", shell=True)
        else:
            print("Try again")
        playerInput = []

dialCount.when_released = addCount
dialStart.when_released = dialRelease

while True:
    pass


