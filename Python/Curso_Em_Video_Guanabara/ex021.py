# Faca um programa em python que abra e reproduza um áudio de arquivo em MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()