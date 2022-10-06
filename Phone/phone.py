import gpiozero as gp
import subprocess as sp
from oscpy.client import OSCClient as oscC

osc = oscC("127.0.0.1", 8000)

dialCount = gp.Button(25)                                                                            
dialStart = gp.Button(24)
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
            osc.send_message(b"/correct", b"bang")
            print("Well done")
        else:
            osc.send_message(b"incorrect", b"bang")
            print("Try again")
        playerInput = []

dialCount.when_released = addCount
dialStart.when_released = dialRelease

while True:
    pass


