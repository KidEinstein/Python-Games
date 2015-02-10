import pygame
import sys
from pygame.image import load
import random
dirs=0
pygame.init()
s= pygame.display.set_mode((420,640))
pygame.display.update()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
q=[10,20,30,40,50,60,70]
sc=2
score=0
img=pygame.Surface((5,10))
img.fill(white)
y1=[0,10,20,30]
y2=[60,70,80,90]
y3=[120,130,140,150]
y4=[180,190,200,210]
y5=[240,250,260,270]
y6=[300,310,320,330]
y7=[360,370,380,390]
y8=[420,430,440,450]
y9=[480,490,500,510]
y10=[540,550,560,570]
y11=[600,610,620,630]
ys=(y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11)
x=[30,165,300]
c=1;
Cars=['CarsEdit\Red.png','CarsEdit\Blue.png','CarsEdit\Green.png','CarsEdit\Orange.png',\
      'CarsEdit\LightGreen.png','CarsEdit\Pink.png','CarsEdit\Purple.png',\
      'CarsEdit\Turquoise.png','CarsEdit\Yellow.png','CarsEdit\DarkBlue.png']
car1=load('car1.png')
car=load(Cars[0])
hourglass=load(img)
clock=pygame.time.Clock()
clock1=pygame.time.Clock()
ze=[]
zc=650
zc1=650
zc2=650
zc3=650
time=[i for i in range(0,620)]

##name=['blahh\gameover (1).png','blahh\gameover (2).png','blahh\gameover (3).png','blahh\gameover (4).png','blahh\gameover (5).png','blahh\gameover (6).png',\
##      'blahh\gameover (7).png','blahh\gameover (8).png','blahh\gameover (9).png','blahh\gameover (10).png','blahh\gameover (11).png','blahh\gameover (12).png',\
##      'blahh\gameover (13).png','blahh\gameover (14).png','blahh\gameover (15).png','blahh\gameover (16).png','blahh\gameover (17).png','blahh\gameover (18).png',\
##      'blahh\gameover (19).png','blahh\gameover (20).png']


name=['GameOver\GO (1).png','GameOver\GO (2).png','GameOver\GO (3).png','GameOver\GO (4).png',\
      'GameOver\GO (5).png','GameOver\GO (6).png','GameOver\GO (7).png','GameOver\GO (8).png',\
      'GameOver\GO (9).png','GameOver\GO (10).png','GameOver\GO (11).png','GameOver\GO (12).png',\
      'GameOver\GO (13).png','GameOver\GO (14).png','GameOver\GO (15).png','GameOver\GO (16).png',\
      'GameOver\GO (17).png','GameOver\GO (18).png','GameOver\GO (19).png','GameOver\GO (20).png']
timer=pygame.Surface((10,1))
timer.fill(red)

def collide(rp,en,ey):
    if rp==en:
        if ey>400 and ey<550:
            return True


        
##EDIT-1
while(True):
    s.fill(white)
    title=load('StartPage\Title.png')
    startB=load('StartPage\StartButton.png')
    infoB=load('StartPage\InfoButton.png')
    s.blit(title,(30,40))
    s.blit(startB,(100,300))
    s.blit(infoB,(100,400))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit();sys.exit(0)
    pygame.display.update()


while(True):
    
    
    ze=[0,140,280,420,560]
    s.fill(black)
    clock.tick(q[sc])
    if zc>640:
        car1=load(random.choice(Cars))
        carpos=random.choice(x)
        rancar1=random.choice(ze)
        zc=-50-rancar1
    if zc1>640:
        car2=load(random.choice(Cars))
        carpos1=random.choice(x)
        rancar2=random.choice(ze)
        zc1=-50-rancar2
    if zc2>640:
        car3=load(random.choice(Cars))
        carpos2=random.choice(x)
        if(rancar1==rancar2):
            ze.remove(rancar1)
        rancar3=random.choice(ze)
        zc2=-50-rancar3


        
##    if zc3>640:
##        carpos3=random.choice(x)
##        if(rancar2==rancar3):
##            ze.remove(rancar2)
##        if(rancar1==rancar3):
##            ze.remove(rancar1)            
##        rancar4=random.choice(ze)  
##        zc3=-50-rancar4


        

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit();sys.exit(0)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP :
                if (sc<6):
                    sc+=1
            elif e.key == pygame.K_DOWN :
                if (sc>0):
                    sc-=1
            elif e.key == pygame.K_LEFT :
                if (c>0):
                    c-=1             
            elif e.key == pygame.K_RIGHT :
                if(c<2):
                    c+=1
    for i in ys:
        for j in i:
            
            s.blit(img,(130,j))
            s.blit(img,(265,j))
    s.blit(car1,(carpos,zc))
    s.blit(car2,(carpos1,zc1))
    s.blit(car3,(carpos2,zc2))
    #s.blit(car1,(carpos3,zc3))
    zc+=10
    zc1+=10
    zc2+=10
    if collide(x[c],carpos1,zc1):
        break
    if collide(x[c],carpos2,zc2):
        break
    if collide(x[c],carpos,zc):
        break
        
    #zc3+=10    
    for i in ys:
        k=len(i)-1
        while k>0:
            i[k]=i[k-1]
            k-=1
        if i[0]>640:
            i[0]=0
        else:
            i[0]+=10

    s.blit(car,(x[c],480))
    
    score+=1
    for i in time:
        s.blit(timer,(405,i))
    s.blit(hourglass,(400,620))
    pygame.display.update()






            
s.fill(black)
font = pygame.font.Font(None, 36)
text = font.render("SCORE : %d" % score, 1, (black))
print score
while (True):
    for i in range(20):
        gm=load(name[i])
        s.blit(gm,(13,0))
        s.blit(text,(140,400))
        pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit();sys.exit(0)

    

