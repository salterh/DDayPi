import speech_recognition as sr
import pygame
import keyboard
intros = []

pygame.mixer.init(44100,-16,2,1024)
test = pygame.mixer.Sound("Audio/intro0.wav")
print(test)

##for i in range(0, 4):
##    intros.append(pygame.mixer.Sound("./Audio/intros" +str(i) +".wav"))
##    print("Loaded " +str(i+1) +" audio file(s)")

r = sr.Recognizer()

def begin():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        print("Starting...")
        myText = r.recognize_sphinx(audio, "en-GB")
        myText = myText.lower()
        print("You said " +myText)
        if "hello" in myText:
            print("Good job")
            
while True:
    if keyboard.read_key() == "p":
        print(pygame.mixer.Sound(test).play())