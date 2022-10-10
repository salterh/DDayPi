import gpiozero as gp
from threading import Timer

led = gp.LED(14)
code = '. . .   . -   - .   - . .   - - .   . -   -   .'
charCounter = 0
time = 0

def output():
    global time, charCounter
    time = 0
    if code[charCounter] == '.':
        time = 0.5
        led.on()
        print('ON')
    elif code[charCounter] == '-':
        time = 1.5
        led.on()
        print('ON')
    elif code[charCounter] == ' ':
        time = 0.5
        led.off()
        print('OFF')
    print(code[charCounter])
    charCounter += 1
    if charCounter <= len(code) - 1:
        t = Timer(time, output)
    else:
        led.off()
        t = Timer(3, output)
        time = 0
        charCounter = 0
    t.start()
    
output()