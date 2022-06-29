import gpiozero as gpio
from pydub import AudioSegment
from pydub.playback import play

ring = AudioSegment.from_wav('Audio/phoneRing.wav')
message = AudioSegment.from_wav('Audio/message.wav')
fullMessage = ring + message

dialStart = gpio.Button(14)
dialCount = gpio.Button(15)
count = 0
answer = [4,9,6,8,0,2,8,4]
playerInput = []

while True:
    if dialStart.isHeld:
        if dialCount.isPressed:
            count = count + 1
    if dialStart.isReleased:
        playerInput.append(count)
        if playerInput.len == answer.len:
            print("Good job")
            play(fullMessage)
            
        
    
            
        