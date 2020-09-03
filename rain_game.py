import pygame
import sys
import random
import numpy

pygame.init()

width=800
height=600
speed=10
score=0
red=(255,0,0)
blue=(0,0,255)
yellow=(255,255,0)

bgcolor=(0,0,0)

playersize=50
playerpos=[width/2,height-2*playersize]

enemysize=50
enemypos=[random.randint(0,width- enemysize),0]
enemylist=[enemypos]


screen=pygame.display.set_mode((width,height))
score=0

myfont=pygame.font.SysFont('bitwise',36)

gameover=False
clock=pygame.time.Clock()

def drop_enemies(enemylist):
    delay = random.random()
    if len(enemylist) < 10 and delay <0.1 :
        xpos=random.randint(0,width-enemysize)
        ypos=0
        enemylist.append([xpos,ypos])
    return  score

def draw_enemy(enemylist):
    for enemypos in enemylist:
        pygame.draw.rect(screen, blue, (enemypos[0], enemypos[1], enemysize, enemysize))

def level(score,speed):
    if score < 20:
        speed=5
    elif score < 40:
        speed=6
    elif score<60:
        speed=8
    elif score< 89:
        speed=10
    else:
        speed=score/10 + 0.000000001


    return  speed



def updateenemypos(enemylist,score):
    for idx, enemypos in enumerate (enemylist):
        if enemypos[1]>= 0 and enemypos [1] < height:
            enemypos[1]+= speed
        else:
            enemylist.pop(idx)
            score+=1
    return score
def checkcollision(enemylist,playerpos):
    for enemypos in enemylist:
        if collision(playerpos,enemypos):
            return True
    return False




def collision(playerpos, enemypos):
    px = playerpos[0]
    py = playerpos[1]

    ex = enemypos[0]
    ey = enemypos[1]
    if ex >= px and ex < (px + playersize) or px >= ex and px < (ex + enemysize):
        if ey >= py and py < (py + playersize) or py >= ey and py < (ey + enemysize):
            return True
    return False



while not gameover:
    for event in pygame.event.get():
        #print((event))

        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            x = playerpos[0]
            y = playerpos[1]
            if event.key==pygame.K_LEFT:
                x-=playersize
            elif event.key==pygame.K_RIGHT:
                x+=playersize
            playerpos=[x,y]

    if playerpos[0]<=0 :
        playerpos[0]=0

    elif playerpos[0]>=800 :
        playerpos[0]=800 - playersize



    pygame.display.set_caption('rain game')



    screen.fill(bgcolor)

    speed=level(score,speed)
    draw_enemy(enemylist)
    drop_enemies(enemylist)
    score=updateenemypos(enemylist,score)
    text='score:'+ str(score)
    lable=myfont.render(text,1,yellow)
    screen.blit(lable,(width-200,height-40))


    pygame.draw.rect(screen,red,(playerpos[0],playerpos[1],playersize,playersize))

    if checkcollision(enemylist,playerpos):

        gameover = True
        print('game over!!!\t\t\t\t your score is :' + str(score))

    checkcollision(enemylist,playerpos)

    clock.tick(30)


    pygame.display.update()

