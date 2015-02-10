import pygame
import sys
import random
import os
from pygame.image import load
from time import sleep
pygame.init()


screen= pygame.display.set_mode((640,480))
pygame.display.update()
ys=[200,210,220,230,240,250]
xs=[240,240,240,240,240,240]
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
img=pygame.Surface((10,10))
img.fill(black)
q=70
l=20
score=0
sc=0
appleimage = pygame.Surface((5, 5));
appleimage.fill(red);
applepos=(random.randint(10,600),random.randint(70,450))
pygame.display.set_caption('Snake')
clock=pygame.time.Clock()
dirs=2
loading=load('Menu\\Snake Menu.png')
dot=load('Menu\\loadDot.png')
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
    else:return False
f = pygame.font.SysFont('Arial', 30);
def die(sc):
    fi=open('highscores.txt','a+')
    highsc=fi.read()
    
    while(True):
        

        t=f.render('GAME OVER : YOUR SCARE WAS : %d' % sc, True, (blue));
        screen.blit(t, (30,240));
        
        if sc<int(highsc):
            t1=f.render('THE HIGH SCORE IS : %s' % highsc, True, (blue))
            screen.blit(t1,(60,350))
            pygame.display.update()
            fi.close()
            
        else:
            t1=f.render('CONGRATULATIONS!!!YOU BEAT THE HIGH SCORE',True,(blue))
            screen.blit(t1,(10,350))
            highsc=str(sc)
            pygame.display.update()
            fi.close()
            os.remove('highscores.txt')

            fil=open('temp.txt','w')
            
            fil.write(highsc)
            fil.close()
            os.rename('temp.txt','highscores.txt')
            
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit();sys.exit(0)
        
                

screen.fill(white)
screen.blit(loading,(100,30))
pygame.display.update()
screen.blit(dot,(255,400))
pygame.display.update()
sleep(1)
screen.blit(dot,(290,400))
pygame.display.update()
sleep(1)
screen.blit(dot,(325,400))
pygame.display.update()
sleep(1)
screen.blit(dot,(360,400))
pygame.display.update()
sleep(1)
screen.blit(dot,(395,400))
pygame.display.update()
sleep(1)
while(True):


    if score>5:
        q=q-5
        score=0
    pygame.time.delay(q)
    screen.fill(white)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit();sys.exit(0)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP :
                if dirs!=0:
                    dirs = 2;
                else:
                    dirs = 0
            elif e.key == pygame.K_DOWN :
                if dirs!=2:
                    dirs = 0;
                else:
                    dirs = 2
            elif e.key == pygame.K_LEFT :
                if dirs!=1:
                    dirs = 3;
                else:
                    dirs=1
                    
            elif e.key == pygame.K_RIGHT :
                if dirs!=3:
                    dirs = 1;
                else:
                    dirs=3

    i = len(xs)-1
    while i >= 2:
        if collide(xs[0], xs[i], ys[0], ys[i], 10, 10, 10, 10):die(sc)
        i-= 1
    if collide(xs[0], applepos[0], ys[0], applepos[1], 10, 5, 10, 5):
        score+=1;sc+=1
        xs.append(900);
        ys.append(900);
        applepos=(random.randint(10,600),random.randint(70,450))
                    
            
    i= len(xs)-1
    while i>0:
        xs[i]=xs[i-1]
        ys[i]=ys[i-1]
        i-=1
    
    if dirs==0:
        if ys[0]>480:
            ys[0]=0
        else:
            ys[0]+=10
    if dirs==1:
        if xs[0]>640:
            xs[0]=0
        else:
            xs[0]+=10
    if dirs==2:
        if ys[0]<10:
            ys[0]=480
        else:
            ys[0]-=10
    if dirs==3:
        if xs[0]<10:
            xs[0]=640
        else:
            xs[0]-=10
    screen.fill(white)
    st=f.render('SCORE : %d'%sc,True,(blue))
    screen.blit(st,(10,10))
    for i in range(0,len(ys)):
        screen.blit(img,(xs[i],ys[i]))
    screen.blit(appleimage, applepos)
                

    pygame.display.update()


        


        

    
        
        
            
