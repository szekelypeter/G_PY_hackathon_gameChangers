import pygame
import math
from pygame.locals import *
import random
pygame.init()

display_width = 1280
display_height  = 700
screen = pygame.display.set_mode((display_width,display_height))

scene1 = pygame.image.load('background01.png').convert()
scene2 = pygame.image.load('background04.png').convert()
scene3 = pygame.image.load('background03.png').convert()
scene4 = pygame.image.load('background02.png').convert()
crossHair=pygame.image.load('crosshairs.png')
crossHairCenter=pygame.image.load('crosshairscenter.png')
radar= pygame.image.load('radar.png')

fronPossible=[288,568,1072,1412,1660,1888,2408,2896,3392,4292,4696,5044]
rightSidePossible=[384,1200,1536,2120,2504,3120,3520,3836,4920]
leftSidePossible=[4088,3676,3288,2688]
headPossible=[[48,380],[160,380],[36,224],[304,224],[456,280],[456,372],[568,56],[568,280],[680,280],[680,372],[884,348],[1776,280],
              [1776,372],[1888,56],[1888,280],[2000,280],[2000,372],[2160,220],[2168,380],[2280,380],[2776,276],[2776,372],[3008,276],
              [3008,372],[3392,192],[4144,372],[4208,372],[4292,184],[4396,372],[4460,372],[4576,276],[4576,372],[4808,276],[4808,372],[4944,328]]
listOfEnemies=[]


listOfColors=[scene1,scene2,scene3,scene4]

width=1280

clock = pygame.time.Clock()

currentposX=0
currentAngle=0
radarCenterX=1160
radarCenterY=380
listOfEnemiesX=[]
listOfEnemiesY=[]
listOfEnemiesXCurrent=[]
listOfEnemiesHeight=[]
listOfEnemiesWidth=[]
# listOfEnemiesX=[1200,3400,600,5000]
# listOfEnemiesY=[300,250,200,350]
# listOfEnemiesXCurrent=[0,0,0,0]
# listOfEnemiesHeight=[120,120,120,120]
# listOfEnemiesWidth=[60,60,60,60]
for i in range(10):
    side=random.randint(1,10)
    kind=random.randint(1,3)
    if 6>=side:
        if kind==1:
            listOfEnemies.append(pygame.image.load('chicken_head.png'))
        if kind==2:
            listOfEnemies.append(pygame.image.load('nun_head.png'))
        if kind == 3:
            listOfEnemies.append(pygame.image.load('clown_head.png'))
        number=random.randint(0,34)
        thechoosen=headPossible[number]
        first=thechoosen[0]
        second=thechoosen[1]
        listOfEnemiesX.append(first)
        listOfEnemiesY.append(second)
        listOfEnemiesXCurrent.append(0)
        listOfEnemiesHeight.append(60)
        listOfEnemiesWidth.append(60)
    if side==7 or side==8:
        if kind == 1:
            listOfEnemies.append(pygame.image.load('chicken_front.png'))
        if kind == 2:
            listOfEnemies.append(pygame.image.load('nun_front.png'))
        if kind == 3:
            listOfEnemies.append(pygame.image.load('clown_front.png'))
        number = random.randint(0, 11)
        listOfEnemiesX.append(fronPossible[number])
        listOfEnemiesY.append(380)
        listOfEnemiesXCurrent.append(0)
        listOfEnemiesHeight.append(120)
        listOfEnemiesWidth.append(60)
    if side==9:
        if kind == 1:
            listOfEnemies.append(pygame.image.load('chicken_right.png'))
        if kind == 2:
            listOfEnemies.append(pygame.image.load('nun_right.png'))
        if kind == 3:
            listOfEnemies.append(pygame.image.load('clown_right.png'))
        number = random.randint(0, 8)
        listOfEnemiesX.append(rightSidePossible[number])
        listOfEnemiesY.append(380)
        listOfEnemiesXCurrent.append(0)
        listOfEnemiesHeight.append(120)
        listOfEnemiesWidth.append(32)
    if side == 10:
        if kind == 1:
            listOfEnemies.append(pygame.image.load('chicken_left.png'))
        if kind == 2:
            listOfEnemies.append(pygame.image.load('nun_left.png'))
        if kind == 3:
            listOfEnemies.append(pygame.image.load('clown_left.png'))
        number = random.randint(0, 3)
        listOfEnemiesX.append(leftSidePossible[number])
        listOfEnemiesY.append(380)
        listOfEnemiesXCurrent.append(0)
        listOfEnemiesHeight.append(120)
        listOfEnemiesWidth.append(32)
print(listOfEnemies)
print(listOfEnemiesX)
print(listOfEnemiesY)

crossX=722
crossY=232


screen.blit(scene1, (currentposX, 0))
screen.blit(crossHair,(crossX,crossY))
screen.blit(crossHairCenter,(crossX+8,crossY+8))
screen.blit(radar, (radarCenterX,radarCenterY))
pygame.display.update()



gameExit=True

pygame.key.set_repeat(100, 5)
def drawBackground():
    if currentposX<=0 and currentposX>-width:
        screen.blit(listOfColors[0], (currentposX, 0))
        screen.blit(listOfColors[1],(currentposX+width,0))
    if currentposX<=-width and currentposX>-width*2:
        screen.blit(listOfColors[1], (currentposX+width, 0))
        screen.blit(listOfColors[2], (currentposX+width*2, 0))
    if currentposX<=-width*2 and currentposX>-width*3:
        screen.blit(listOfColors[2], (currentposX+width*2, 0))
        screen.blit(listOfColors[3], (currentposX +width*3, 0))
    if currentposX<=-width*3 and currentposX>=-width*4:
        screen.blit(listOfColors[3], (currentposX+width*3, 0))
        screen.blit(listOfColors[0], (currentposX +width*4, 0))

def drawEnemies():
    global currentposX, radarSign, currentAngle, radar, crossY, crossX
    for i in range(len(listOfEnemiesX)):
        alpha = listOfEnemiesX[i] / 5120 * 360
        alphar = math.radians(alpha)
        sin = math.sin(alphar)
        cos = math.cos(alphar)
        circle = pygame.draw.circle(screen, (255, 0, 0),
                                    [int(radarCenterX + sin * 50 + 50), int(radarCenterY - cos * 50 + 50)], 5)
        if currentposX < -3 * width:
            if 4 * width + currentposX + listOfEnemiesX[i] > 0:
                listOfEnemiesXCurrent[i]=4 * width + currentposX + listOfEnemiesX[i]
                screen.blit(listOfEnemies[i],(4 * width + currentposX + listOfEnemiesX[i], listOfEnemiesY[i]))
        if -listOfEnemiesX[i] - listOfEnemiesWidth[i] < currentposX and -listOfEnemiesX[i] + listOfEnemiesWidth[i] > currentposX - width:
            listOfEnemiesXCurrent[i]=listOfEnemiesX[i] + currentposX
            screen.blit(listOfEnemies[i],(listOfEnemiesX[i] + currentposX, listOfEnemiesY[i]))
def draw():
    drawBackground()
    drawEnemies()
    screen.blit(crossHair, (crossX, crossY))
    screen.blit(crossHairCenter, (crossX + 8, crossY + 8))
    screen.blit(rot_center(radar, currentAngle), (radarCenterX, radarCenterY))
    pygame.display.update()

def paff():
    for i in range(len(listOfEnemiesX)):
        x=0
        y=0
        if listOfEnemiesXCurrent[i]-20<crossX+8 and listOfEnemiesXCurrent[i]+60>crossX+8:
            if listOfEnemiesY[i]-20<crossY+8 and listOfEnemiesY[i]+120>crossY+8:
                if listOfEnemiesXCurrent[i]-crossX-8<20 and listOfEnemiesXCurrent[i]-crossX-8>0:
                    x=20-(listOfEnemiesXCurrent[i]-crossX-8)
                elif listOfEnemiesXCurrent[i]-crossX-8<=0 and listOfEnemiesXCurrent[i]-crossX-8>=20-listOfEnemiesWidth[i]:
                    x=20
                elif listOfEnemiesXCurrent[i]-crossX-8<20-listOfEnemiesWidth[i] and listOfEnemiesXCurrent[i]-crossX-8>-listOfEnemiesWidth[i]-20:
                    x=abs(listOfEnemiesXCurrent[i]-crossX-8+listOfEnemiesWidth[i])
                if listOfEnemiesY[i]-crossY-8<20 and listOfEnemiesY[i]-crossY-8>0:
                    y = 20-(listOfEnemiesY[i] - crossY - 8)
                elif listOfEnemiesY[i]-crossY-8<=0 and listOfEnemiesY[i]-crossY-8>=20-listOfEnemiesHeight[i]:
                    y = 20
                elif listOfEnemiesY[i]-crossY-8<listOfEnemiesHeight[i] and listOfEnemiesY[i]-crossY-8>-listOfEnemiesHeight[i]-20:
                    y = abs(listOfEnemiesY[i] - crossY - 8 + listOfEnemiesHeight[i])
                shot=random.randint(0,400)
                if shot<=x*y:
                    del listOfEnemies[i]
                    del listOfEnemiesX[i]
                    del listOfEnemiesY[i]
                    del listOfEnemiesXCurrent[i]
                    del listOfEnemiesWidth[i]
                    del listOfEnemiesHeight[i]
                    # listOfEnemies.remove(listOfEnemies[i])
                    # listOfEnemiesX.remove(listOfEnemiesX[i])
                    # listOfEnemiesY.remove(listOfEnemiesY[i])
                    # listOfEnemiesXCurrent.remove(listOfEnemiesXCurrent[i])
                    # listOfEnemiesWidth.remove(listOfEnemiesWidth[i])
                    # listOfEnemiesHeight.remove(listOfEnemiesHeight[i])
                    print(listOfEnemies)
                    print(listOfEnemiesX)
                    print(listOfEnemiesY)
                    break
    draw()

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def moveLeftRight(change,changeAngle):
    global currentposX, radarSign, currentAngle,radar,crossY,crossX
    if currentposX < -width*4:
        currentposX = 0
    if currentposX> 0:
        currentposX=-width*4
    currentposX += change
    currentAngle += changeAngle
    if currentAngle==360:
        currentAngle=0
    if currentAngle==-360:
        currentAngle=0
    draw()

def moveUpDown(change):
    global currentposX, radarSign, currentAngle,radar,crossY,crossX
    crossY +=change
    if crossY<0:
        crossY=0
    if crossY>464:
        crossY=464
    draw()



while gameExit:
    changeX=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX=10
                changeAngle=0.703125
                moveLeftRight(changeX,changeAngle)
            elif event.key == pygame.K_RIGHT:
                changeX=-10
                changeAngle=-0.703125
                moveLeftRight(changeX,changeAngle)
            elif event.key==pygame.K_UP:
                changeY=-4
                moveUpDown(changeY)
            elif event.key==pygame.K_DOWN:
                changeY=4
                moveUpDown(changeY)
            elif event.key==pygame.K_SPACE:
                paff()

