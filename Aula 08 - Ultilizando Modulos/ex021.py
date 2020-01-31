
import pygame

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

"""
# Este codigo foi o que o professor passou e deu erro
import pygame

pygame.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
pygame.event.wait()
"""