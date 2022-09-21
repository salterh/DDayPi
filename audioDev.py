import pygame
import pygame._sdl2.audio as sdl2_audio

pygame.init()

def get_devices():
    return sdl2_audio.get_audio_device_names()

print(get_devices())