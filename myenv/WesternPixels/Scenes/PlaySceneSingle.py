import random
import math
import pygame

from Maps import Map
from Scenes import Scene
from pygame.locals import *

from Shared import GameConstants


class PlaySceneSingle(Scene):
    crossX = 722
    crossY = 232
    currentposX, radarSign, currentAngle, radar,
    self.currentposX = 0
    self.currentAngle = 0
    self.radarCenterX = 1160
    self.radarCenterY = 380

    def __init__(self, gameController):
        super(PlaySceneSingle, self).__init__(gameController)
        self.map = Map()
        self.scene1 = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_BACKGROUND_ONE)
        self.scene2 = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_BACKGROUND_TWO)
        self.scene3 = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_BACKGROUND_THRREE)
        self.scene4 = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_BACKGROUND_FOUR)

        self.chickenFront = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_CHICKEN_FRONT)
        self.chickenHead = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_CHICKEN_HEAD)
        self.chickenLeft = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_CHICKEN_LEFT)
        self.chickenRight = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_CHICKEN_RIGHT)

        self.clownFront = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_CLOWN_FRONT)
        self.clownHead = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_CLOWN_HEAD)
        self.clownLeft = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_CLOWN_LEFT)
        self.clownRight = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_CLOWN_RIGHT)

        self.nunFront = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_NUN_FRONT)
        self.nunHead = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_NUN_HEAD)
        self.nunLeft = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_NUN_LEFT)
        self.nunRight = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_ENEMY_NUN_RIGHT)

        self.crosshairs = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_CROSSHAIRS)
        self.crosshairsCenter = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_CROSSHAIRS_CENTER)
        self.radar = pygame.image.load(GameConstants.IMAGE_SCENE_PLAY_RADAR)

        self.scene1 = self.scene1.convert()
        self.scene4 = self.scene2.convert()
        self.scene3 = self.scene3.convert()
        self.scene2 = self.scene4.convert()

        self.crossHair = self.crosshairs.convert()
        self.crossHairCenter = self.crosshairsCenter.convert()
        self.radar = self.radar.convert()

        self.headPossible = self.map.headPossible
        self.fronPossible = self.map.frontPossible
        self.leftSidePossible = self.map.leftSidePossible
        self.rightSidePossible = self.map.rightSidePossible

        self.currentposX = 0
        self.currentAngle = 0
        self.radarCenterX = 1160
        self.radarCenterY = 380



        self.changeX = 0

        self.listOfEnemies = []
        self.listOfEnemiesX = []
        self.listOfEnemiesY = []
        self.listOfEnemiesXCurrent = []
        self.listOfEnemiesHeight = []
        self.listOfEnemiesWidth = []

        self.listOfColors = [self.scene1, self.scene2, self.scene3, self.scene4]

        self.screen = self.getGameController().getScreen()

        self.width = GameConstants.SCREEN_SIZE[0]


    def render(self, centered=False, y=0):
        for i in range(10):
            side = random.randint(1, 10)
            kind = random.randint(1, 3)
            if 6 >= side:
                if kind == 1:
                    self.listOfEnemies.append(self.chickenHead)
                if kind == 2:
                    self.listOfEnemies.append(self.nunHead)
                if kind == 3:
                    self.listOfEnemies.append(self.clownHead)
                number = random.randint(0, 34)
                thechoosen = self.headPossible[number]
                first = thechoosen[0]
                second = thechoosen[1]
                self.listOfEnemiesX.append(first)
                self.listOfEnemiesY.append(second)
                self.listOfEnemiesXCurrent.append(0)
                self.listOfEnemiesHeight.append(60)
                self.listOfEnemiesWidth.append(60)
            if side == 7 or side == 8:
                if kind == 1:
                    self.listOfEnemies.append(self.chickenFront)
                if kind == 2:
                    self.listOfEnemies.append(self.nunFront)
                if kind == 3:
                    self.listOfEnemies.append(self.clownFront)
                number = random.randint(0, 11)
                self.listOfEnemiesX.append(self.fronPossible[number])
                self.listOfEnemiesY.append(380)
                self.listOfEnemiesXCurrent.append(0)
                self.listOfEnemiesHeight.append(120)
                self.listOfEnemiesWidth.append(60)
            if side == 9:
                if kind == 1:
                    self.listOfEnemies.append(self.chickenRight)
                if kind == 2:
                    self.listOfEnemies.append(self.nunRight)
                if kind == 3:
                    self.listOfEnemies.append(self.clownRight)
                number = random.randint(0, 8)
                self.listOfEnemiesX.append(self.rightSidePossible[number])
                self.listOfEnemiesY.append(380)
                self.listOfEnemiesXCurrent.append(0)
                self.listOfEnemiesHeight.append(120)
                self.listOfEnemiesWidth.append(32)
            if side == 10:
                if kind == 1:
                    self.listOfEnemies.append(self.chickenLeft)
                if kind == 2:
                    self.listOfEnemies.append(self.nunLeft)
                if kind == 3:
                    self.listOfEnemies.append(self.clownLeft)
                number = random.randint(0, 3)
                self.listOfEnemiesX.append(self.leftSidePossible[number])
                self.listOfEnemiesY.append(380)
                self.listOfEnemiesXCurrent.append(0)
                self.listOfEnemiesHeight.append(120)
                self.listOfEnemiesWidth.append(32)



        self.screen.blit(self.scene1, (self.currentposX, 0))
        self.screen.blit(self.crossHair, (crossX, crossY))
        self.screen.blit(self.crossHairCenter, (crossX + 8, crossY + 8))
        self.screen.blit(radar, (self.radarCenterX, self.radarCenterY))
        pygame.display.update()


        pygame.key.set_repeat(100, 5)

    def drawBackground(self):
        if currentposX <= 0 and currentposX > -self.width:
            self.screen.blit(self.listOfColors[0], (currentposX, 0))
            self.screen.blit(self.listOfColors[1], (currentposX + self.width, 0))
        if currentposX <= -self.width and currentposX > -self.width * 2:
            self.screen.blit(self.listOfColors[1], (currentposX + self.width, 0))
            self.screen.blit(self.listOfColors[2], (currentposX + self.width * 2, 0))
        if currentposX <= -self.width * 2 and currentposX > -self.width * 3:
            self.screen.blit(self.listOfColors[2], (currentposX + self.width * 2, 0))
            self.screen.blit(self.listOfColors[3], (currentposX + self.width * 3, 0))
        if currentposX <= -self.width * 3 and currentposX >= -self.width * 4:
            self.screen.blit(self.listOfColors[3], (currentposX + self.width * 3, 0))
            self.screen.blit(self.listOfColors[0], (currentposX + self.width * 4, 0))

    def drawEnemies(self):
        global currentposX, radarSign, currentAngle, radar, crossY, crossX
        for i in range(len(self.listOfEnemiesX)):
            alpha = self.listOfEnemiesX[i] / 5120 * 360
            alphar = math.radians(alpha)
            sin = math.sin(alphar)
            cos = math.cos(alphar)
            circle = pygame.draw.circle(self.screen, (255, 0, 0),
                                        [int(self.radarCenterX + sin * 50 + 50), int(self.radarCenterY - cos * 50 + 50)], 5)
            if currentposX < -3 * self.width:
                if 4 * self.width + currentposX + self.listOfEnemiesX[i] > 0:
                    self.listOfEnemiesXCurrent[i] = 4 * self.width + currentposX + self.listOfEnemiesX[i]
                    self.screen.blit(self.listOfEnemies[i], (4 * self.width + currentposX + self.listOfEnemiesX[i], self.listOfEnemiesY[i]))
            if -self.listOfEnemiesX[i] - self.listOfEnemiesWidth[i] < currentposX and -self.listOfEnemiesX[i] + self.listOfEnemiesWidth[
                i] > currentposX - self.width:
                self.listOfEnemiesXCurrent[i] = self.listOfEnemiesX[i] + currentposX
                self.screen.blit(self.listOfEnemies[i], (self.listOfEnemiesX[i] + currentposX, self.listOfEnemiesY[i]))

    def draw(self):
        self.drawBackground()
        self.drawEnemies()
        self.screen.blit(self.crossHair, (crossX, crossY))
        self.screen.blit(self.crossHairCenter, (crossX + 8, crossY + 8))
        self.screen.blit(self.rot_center(radar, currentAngle), (self.radarCenterX, self.radarCenterY))
        pygame.display.update()

    def paff(self):
        for i in range(len(self.listOfEnemiesX)):
            x = 0
            y = 0
            if self.listOfEnemiesXCurrent[i] - 20 < crossX + 8 and self.listOfEnemiesXCurrent[i] + 60 > crossX + 8:
                if self.listOfEnemiesY[i] - 20 < crossY + 8 and self.listOfEnemiesY[i] + 120 > crossY + 8:
                    if self.listOfEnemiesXCurrent[i] - crossX - 8 < 20 and self.listOfEnemiesXCurrent[i] - crossX - 8 > 0:
                        x = 20 - (self.listOfEnemiesXCurrent[i] - crossX - 8)
                    elif self.listOfEnemiesXCurrent[i] - crossX - 8 <= 0 and self.listOfEnemiesXCurrent[
                        i] - crossX - 8 >= 20 - self.listOfEnemiesWidth[i]:
                        x = 20
                    elif self.listOfEnemiesXCurrent[i] - crossX - 8 < 20 - self.listOfEnemiesWidth[i] and \
                                                    self.listOfEnemiesXCurrent[i] - crossX - 8 > -self.listOfEnemiesWidth[
                                i] - 20:
                        x = abs(self.listOfEnemiesXCurrent[i] - crossX - 8 + self.listOfEnemiesWidth[i])
                    if self.listOfEnemiesY[i] - crossY - 8 < 20 and self.listOfEnemiesY[i] - crossY - 8 > 0:
                        y = 20 - (self.listOfEnemiesY[i] - crossY - 8)
                    elif self.listOfEnemiesY[i] - crossY - 8 <= 0 and self.listOfEnemiesY[i] - crossY - 8 >= 20 - \
                            self.listOfEnemiesHeight[i]:
                        y = 20
                    elif self.listOfEnemiesY[i] - crossY - 8 < self.listOfEnemiesHeight[i] and self.listOfEnemiesY[
                        i] - crossY - 8 > -self.listOfEnemiesHeight[i] - 20:
                        y = abs(self.listOfEnemiesY[i] - crossY - 8 + self.listOfEnemiesHeight[i])
                    shot = random.randint(0, 400)
                    if shot <= x * y:
                        del self.listOfEnemies[i]
                        del self.listOfEnemiesX[i]
                        del self.listOfEnemiesY[i]
                        del self.listOfEnemiesXCurrent[i]
                        del self.listOfEnemiesWidth[i]
                        del self.listOfEnemiesHeight[i]
                        break
        self.draw()

    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def moveLeftRight(self, change, changeAngle):
        global currentposX, radarSign, currentAngle, radar, crossY, crossX
        if currentposX < -self.width * 4:
            currentposX = 0
        if currentposX > 0:
            currentposX = -self.width * 4
        currentposX += change
        currentAngle += changeAngle
        if currentAngle == 360:
            currentAngle = 0
        if currentAngle == -360:
            currentAngle = 0
        self.draw()

    def moveUpDown(self, change):
        global currentposX, radarSign, currentAngle, radar, crossY, crossX
        crossY += change
        if crossY < 0:
            crossY = 0
        if crossY > 464:
            crossY = 464
        self.draw()


    def handleEvents(self, events):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.changeX = 10
                    changeAngle = 0.703125
                    self.moveLeftRight(self.changeX, changeAngle)
                elif event.key == pygame.K_RIGHT:
                    self.changeX = -10
                    changeAngle = -0.703125
                    self.moveLeftRight(self.changeX, changeAngle)
                elif event.key == pygame.K_UP:
                    changeY = -4
                    self.moveUpDown(changeY)
                elif event.key == pygame.K_DOWN:
                    changeY = 4
                    self.moveUpDown(changeY)
                elif event.key == pygame.K_SPACE:
                    self.paff()

