import pygame
import sys
import random
from pygame.image import load
import os
import Snake
import race_f
import hangman_n
pygame.init()
screen= pygame.display.set_mode((480,640))
pygame.display.update()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
MPOS=0,0
background=load('Main Menu\Main Menu.png')
Dracer_b=load('Main Menu\Buttons\\2Dracer.png')
Hangman_b=load('Main Menu\Buttons\Hangman.png')
Snake_b=load('Main Menu\Buttons\Snake.png')
racer_b=Dracer_b.get_rect()
hangman_b=Hangman_b.get_rect()
snake_b=Snake_b.get_rect()
screen.fill(white)
screen.blit(background,(33,20))
screen.blit(Snake_b,(180,275))
snake_b=snake_b.move(180,275)
#print snake_b
screen.blit(Dracer_b,(180,375))
racer_b=racer_b.move(180,375)
#print racer_b
screen.blit(Hangman_b,(180,475))
hangman_b=hangman_b.move(180,475)
#print hangman_b
while(True):
    pygame.display.set_caption('SAS Games')
    MPOS=0,0
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit();sys.exit(0)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            MPOS=pygame.mouse.get_pos()
            #print MPOS
    if(snake_b.collidepoint(MPOS)):
        print 'snake'
        Snake.game_snake()
    elif(racer_b.collidepoint(MPOS)):
        print 'racer'
        race_f.game_race()
    elif(hangman_b.collidepoint(MPOS)):
        print 'hangman'
        hangman_n.game_hang()
    screen= pygame.display.set_mode((480,640))
    screen.fill(white)
    screen.blit(background,(33,20))
    screen.blit(Snake_b,(180,275))
    screen.blit(Dracer_b,(180,375))
    screen.blit(Hangman_b,(180,475))
    pygame.display.update()
