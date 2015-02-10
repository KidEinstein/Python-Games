def game_race():
    import pygame
    import sys
    from pygame.image import load
    import random
    import datetime
    w=[4000,6000,8000,10000,12000,14000,16000,18000]
    dist=-w[0]
    lvl=0
    gt=0
    dirs=0
    pygame.init()
    s= pygame.display.set_mode((420,640))
    pygame.display.set_caption('2D Racers')
    pygame.display.update()
    red = (255,0,0)
    grey = (64,64,64)
    green = (0,255,0)
    blue = (0,0,255)
    darkBlue = (0,0,128)
    white = (255,255,255)
    black = (0,0,0)
    pink = (255,200,200)
    font = pygame.font.Font(None, 36)
    ##EDIT-4 START
    #Speed List
    q=[10,20,30,40,50,60,70,80,90,100]
    ##EDIT-4 END
    #Lane Counter
    sc=2
    score=0
    img=pygame.Surface((5,10))
    img.fill(white)
    t1=datetime.datetime.now()
    tot1=t1.second+(t1.minute*60)+(t1.hour*60*60)
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
    Cars=['Dracer\CarsEdit\Blue.png','Dracer\CarsEdit\Green.png','Dracer\CarsEdit\Orange.png',\
          'Dracer\CarsEdit\LightGreen.png','Dracer\CarsEdit\Pink.png','Dracer\CarsEdit\Purple.png',\
          'Dracer\CarsEdit\Turquoise.png','Dracer\CarsEdit\Yellow.png','Dracer\CarsEdit\DarkBlue.png']
    car1=load(random.choice(Cars))
    car=load('Dracer\CarsEdit\Red.png')
    hourglass=load('Dracer\Extras\HourEdit.png')
    clock=pygame.time.Clock()
    clock1=pygame.time.Clock()
    ze=[]
    zc=650
    zc1=650
    zc2=650
    zc3=650
    time=[i for i in range(0,620)]


    name=['Dracer\GameOver\GO (1).png','Dracer\GameOver\GO (2).png','Dracer\GameOver\GO (3).png','Dracer\GameOver\GO (4).png',\
          'Dracer\GameOver\GO (5).png','Dracer\GameOver\GO (6).png','Dracer\GameOver\GO (7).png','Dracer\GameOver\GO (8).png',\
          'Dracer\GameOver\GO (9).png','Dracer\GameOver\GO (10).png','Dracer\GameOver\GO (11).png','Dracer\GameOver\GO (12).png',\
          'Dracer\GameOver\GO (13).png','Dracer\GameOver\GO (14).png','Dracer\GameOver\GO (15).png','Dracer\GameOver\GO (16).png',\
          'Dracer\GameOver\GO (17).png','Dracer\GameOver\GO (18).png','Dracer\GameOver\GO (19).png','Dracer\GameOver\GO (20).png']
    timer=pygame.Surface((10,1))
    timer.fill(red)

    def collid(rp,en,ey):
        if rp==en:
            if ey>400 and ey<550:
                return True

    def infoPage():
        infoPage=load('Dracer\StartPage\InfoPage.png')
        backB=load('Dracer\StartPage\BackButton.png')
        while(True):
            MPOS=0,0
            s.fill(white)
            s.blit(infoPage,(50,20))
            s.blit(backB,(200,550))
            bb_rect=backB.get_rect()
            BB_rect=bb_rect.move(200,550)
            for f in pygame.event.get():
                if f.type == pygame.QUIT:
                    return
                    #pygame.quit();sys.exit(0)
                elif f.type == pygame.MOUSEBUTTONDOWN:
                    MPOS=pygame.mouse.get_pos()
                    if(BB_rect.collidepoint(MPOS)):
                        return
            pygame.display.update()

    title=load('Dracer\StartPage\Title.png')
    startB=load('Dracer\StartPage\StartButton.png')
    infoB=load('Dracer\StartPage\InfoButton.png')
    while(True):
        MPOS=0,0
        s.fill(white)
        s.blit(title,(30,40))
        s.blit(startB,(100,300))
        s.blit(infoB,(100,400))
        sb_rect=startB.get_rect()
        SB_rect=sb_rect.move(100,300)
        ib_rect=infoB.get_rect()
        IB_rect=ib_rect.move(100,400)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
                #pygame.quit();sys.exit(0)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                MPOS=pygame.mouse.get_pos()
        if(SB_rect.collidepoint(MPOS)):
            break 
        elif(IB_rect.collidepoint(MPOS)):
            infoPage()
        pygame.display.update()

    while(True):
        flag=0
        disrem=font.render("Metres to go : %d" % int(-dist+480), 1, (pink))
        level=font.render("Level : %d" % int(lvl+1), 1, (red))
        
        ze=[50,190,330,470]
        s.fill(grey)
        s.blit(disrem,(0,0))
        s.blit(level,(0,20))
        clock.tick(q[sc])
        if zc>640:
            car1=load(random.choice(Cars))
            carpos=random.choice(x)
            rancar1=random.choice(ze)
            zc=-rancar1
        if zc1>640:
            car2=load(random.choice(Cars))
            carpos1=random.choice(x)
            rancar2=random.choice(ze)
            zc1=-rancar2
        if zc2>640:
            
            car3=load(random.choice(Cars))
            carpos2=random.choice(x)
            rancar3=random.choice(ze)
            zc2=-rancar3
            if(abs(rancar1-rancar2)<=180 or abs(rancar1-rancar3)<=180 or abs(rancar2-rancar3)<=180):

                flag=1
                zc2=700
                #print 'flag 1'

    ##    print rancar1
    ##    print rancar2
        if gt>620:
            break
        t2=datetime.datetime.now()
        tot2=t2.second+(t2.minute*60)+(t2.hour*60*60)
        tdel=tot2-tot1
        tot1=tot2
        if tdel>0:
            gt+=20

        pygame.draw.lines(s,red,False,((0,dist),(400,dist)),4)
        dist+=10
        if dist>480:
            gt=0
            lvl+=1
            dist=-w[lvl]



            

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
                #pygame.quit();sys.exit(0)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP :
                    if (sc<9):##EDIT-4 6=9 (9 speeds upto 100)
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
        if(flag!=1):
            s.blit(car3,(carpos2,zc2))
    ##    else:
    ##        print 'not displayed'
        #s.blit(car1,(carpos3,zc3))
        zc+=10
        zc1+=10
        zc2+=10
        if collid(x[c],carpos,zc):
            break
        if collid(x[c],carpos1,zc1):
            break
        if flag!=1:
            
            if collid(x[c],carpos2,zc2):

                break
    ##    else:
    ##        print 'collision avoided'
            
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
        for i in range(gt,620):
            s.blit(timer,(405,i))
        s.blit(hourglass,(400,620))
        pygame.display.update()






                
    s.fill(black)

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
                return
                #pygame.quit();
                #sys.exit(0)
                

        

