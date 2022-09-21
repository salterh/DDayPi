import gpiozero as gp
import subprocess

subprocess.call("puredata -nogui -audioaddoutdev \"snd_rpi_hifiberry_dac\" playSound.pd", shell=True)

dialCount = gp.Button(23)                                                                            
dialStart = gp.Button(18)
count = -1
answer = [1,1,1]
playerInput = []

def addCount():
    global count
    count+=1
    
def dialRelease():
    global data
    global count
    global playerInput
    if count >= 10:
        count = 0
    playerInput.append(count)
    count = -1
    if len(playerInput) == len(answer):
        if playerInput == answer:
            print("Done")
            subprocess.call("puredata -nogui -audioaddoutdev \"snd_rpi_hifiberry_dac\" playSound.pd", shell=True)
        else:
            print("Try again")
        playerInput = []

dialCount.when_released = addCount
dialStart.when_released = dialRelease

while True:
    pass


