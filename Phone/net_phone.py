import gpiozero as gp
import subprocess as sp
from oscpy.client import OSCClient as oscC
import schedule

osc = oscC("127.0.0.1", 8000)

dialCount = gp.Button(25)                                                                            
dialStart = gp.Button(24)
count = -1

def addCount():
    global count
    count+=1
    
def dialRelease():
    global count
    print(count)
    osc.send_message(b"/play", [count])
    count = -1
    

dialCount.when_released = addCount
dialStart.when_released = dialRelease

while True:
    pass


