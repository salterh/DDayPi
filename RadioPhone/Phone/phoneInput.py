import gpiozero as gpio
from pydub import AudioSegment
from pydub.playback import play
import keyboard as kb

#ring = AudioSegment.from_wav('Audio/phoneRing.wav')
#message = AudioSegment.from_wav('Audio/message.wav')
#fullMessage = ring + message

dialStart = gpio.Button(14)
dialCount = gpio.Button(15)
count = 0
answer = [4,9,6,8,0,2,8,4]
playerInput = []

def addCount():
    global count
    count+=1
    print(count)
    
def dialRelease():
    global count
    global playerInput
    playerInput.append(count)
    print(playerInput)
    count = 0
    if len(playerInput) == len(answer):
        if playerInput == answer:
            print("Good job")
#            play(fullMessage)
        playerInput = []

dialStart.when_released = dialRelease

while True:
    if dialStart.is_held:
        if dialCount.isPressed:
            addCount()
    event = kb.read_event()
    if event.event_type == kb.KEY_DOWN:
        if event.name == 'w':
            addCount()
        elif event.name == 'e':
            dialRelease() 