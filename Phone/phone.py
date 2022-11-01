import gpiozero as gp
import subprocess as sp
from oscpy.client import OSCClient as oscC
import schedule

osc = oscC("127.0.0.1", 8000)

dialCount = gp.Button(25)                                                                            
dialStart = gp.Button(24)
count = -1
answer = [1,2,3]
playerInput = []
time_count = 0

def addCount():
    global count
    count+=1
    time_count = 0
    
def dialRelease():
    global count
    global playerInput
    time_count = 0
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
            osc.send_message(b"/incorrect", b"bang")
            print("Try again")
        playerInput = []
        
def check():
    time_count += 1
    if time_count > 30:
        playerInput = []
        time_count = 0
    print(time_count)

dialCount.when_released = addCount
dialStart.when_released = dialRelease
schedule.every(1).seconds.do(check)

while True:
    schedule.run_pending()


