import gpiozero as gp
import subprocess as sp
from oscpy.client import OSCClient as oscC
import schedule

osc = oscC("127.0.0.1", 8000)
print("Starting")

dialCount = gp.Button(25)                                                                            
dialStart = gp.Button(24)
count = -1

def addCount():
    global count
    count+=1
    print(count)
    
def dialRelease():
    global count
    print("release: ", count)
    osc.send_message(b"/play", [count])
    count = -1
    
def dialPressed():
    print("Working")
    
dialCount.when_released = addCount
dialStart.when_released = dialRelease
dialStart.when_pressed = dialPressed

while True:
    pass


