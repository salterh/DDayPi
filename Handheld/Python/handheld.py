import gpiozero as gp
from oscpy.client import OSCClient as oscC

osc = oscC("127.0.0.1", 8000)
osc.send_message(b"/test", [42])

nextB = gp.Button(14)
prevB = gp.Button(15)
clueB = gp.Button(25)
ledB = gp.Button(23)
ledOut = gp.LED(24)

mainCount = -1
clueCount = -1

def playNext():
    print("Next")
    mainCount += 1
    if mainCount > 4:
        mainCount = 4
    osc.send_message(b"/next", [mainCount])
    
    
def playPrev():
    print("Prev")
    if mainCount < 0:
        mainCount = 0
    osc.send_message(b"/prev", [mainCount])
    
    
def playClue():
    print("Clue")
    if mainCount != 0:
        osc.send_message(b"/clue", b"bang")
    
nextB.when_pressed = playNext
prevB.when_pressed = playPrev
clueB.when_pressed = playClue

while True:
    if ledB.is_pressed:
        ledOut.on()
    else:
        ledOut.off()



