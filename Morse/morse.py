import gpiozero as gp
from threading import Timer
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 18)

code = '.   - .   - - .   . .   - .   .   '
charCounter = 0
time = 0

def output():
    global time, charCounter
    time = 0
    if code[charCounter] == '.':
        time = 0.5
        pixels.fill((255,137,18))
        pixels.show()
        print('ON')
    elif code[charCounter] == '-':
        time = 1.5
        pixels.fill((255,137,18))
        pixels.show()
        print('ON')
    elif code[charCounter] == ' ':
        time = 0.5
        pixels.fill((0,0,0))
        pixels.show()
        print('OFF')
    print(code[charCounter])
    charCounter += 1
    if charCounter <= len(code) - 1:
        t = Timer(time, output)
    else:
        t = Timer(5, output)
        time = 0
        charCounter = 0
    t.start()
    
output()

if __name__ == '__main__':
    while True:
        pixels.show()
