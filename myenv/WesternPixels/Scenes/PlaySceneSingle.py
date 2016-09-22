import random

import math
import pygame
from pygame.locals import *

from Maps import Map
from Scenes import Scene
from Shared import GameConstants
from Shared.Images import images
from Shared.Sounds import sounds


class PlaySceneSingle(Scene):


    def __init__(self, gameController):
        super(PlaySceneSingle, self).__init__(gameController)
        self.map = Map()
        self.headPossible = self.map.headPossible
        self.fronPossible = self.map.frontPossible
        self.leftSidePossible = self.map.leftSidePossible
        self.rightSidePossible = self.map.rightSidePossible

        self.currentposX = 0
        self.currentAngle = 0
        self.radarCenterX = 1160
        self.radarCenterY = 380

        self.crossX = 622 #722
        self.crossY = 232

        self.width = GameConstants.ACTUAL_SCREEN_SIZE[0]

        self.currentAngle = 0

        self.listOfEnemiesSpecies= []
        self.listOfEnemies = []
        self.listOfEnemiesX = []
        self.listOfEnemiesY = []
        self.listOfEnemiesXCurrent = []
        self.listOfEnemiesHeight = []
        self.listOfEnemiesWidth = []

        self.listOfColors = [images["scene 1"], images["scene 2"], images["scene 3"], images["scene 4"]]

        self.screen = self.getGameController().getScreen()

        self.isRenderedOnce = False
        self.currentPaff = 1

        start_ticks = pygame.time.get_ticks()
        self.end_ticks = start_ticks + 15000
        print(self.end_ticks)




    def render(self, centered=False, y=0):
        if not self.isRenderedOnce:
            self.getGameController().fillBackGround()
            self.isRenderedOnce = True
            for i in range(20):
                side = random.randint(1, 10)
                kind = random.randint(1, 3)
                if 6 >= side:
                    if kind == 1:
                        self.listOfEnemies.append(images["chicken Head"])
                        self.listOfEnemiesSpecies.append("chicken")
                    if kind == 2:
                        self.listOfEnemies.append(images["nun Head"])
                        self.listOfEnemiesSpecies.append("nun")
                    if kind == 3:
                        self.listOfEnemies.append(images["clown Head"])
                        self.listOfEnemiesSpecies.append("clown")
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
                        self.listOfEnemies.append(images["chicken Front"])
                        self.listOfEnemiesSpecies.append("chicken")
                    if kind == 2:
                        self.listOfEnemies.append(images["nun Front"])
                        self.listOfEnemiesSpecies.append("nun")
                    if kind == 3:
                        self.listOfEnemies.append(images["clown Front"])
                        self.listOfEnemiesSpecies.append("clown")
                    number = random.randint(0, 11)
                    self.listOfEnemiesX.append(self.fronPossible[number])
                    self.listOfEnemiesY.append(380)
                    self.listOfEnemiesXCurrent.append(0)
                    self.listOfEnemiesHeight.append(120)
                    self.listOfEnemiesWidth.append(60)
                if side == 9:
                    if kind == 1:
                        self.listOfEnemies.append(images["chicken Right"])
                        self.listOfEnemiesSpecies.append("chicken")
                    if kind == 2:
                        self.listOfEnemies.append(images["nun Right"])
                        self.listOfEnemiesSpecies.append("nun")
                    if kind == 3:
                        self.listOfEnemies.append(images["clown Right"])
                        self.listOfEnemiesSpecies.append("clown")
                    number = random.randint(0, 8)
                    self.listOfEnemiesX.append(self.rightSidePossible[number])
                    self.listOfEnemiesY.append(380)
                    self.listOfEnemiesXCurrent.append(0)
                    self.listOfEnemiesHeight.append(120)
                    self.listOfEnemiesWidth.append(32)
                if side == 10:
                    if kind == 1:
                        self.listOfEnemies.append(images["chicken Left"])
                        self.listOfEnemiesSpecies.append("chicken")
                    if kind == 2:
                        self.listOfEnemies.append(images["nun Left"])
                        self.listOfEnemiesSpecies.append("nun")
                    if kind == 3:
                        self.listOfEnemies.append(images["clown Left"])
                        self.listOfEnemiesSpecies.append("clown")
                    number = random.randint(0, 3)
                    self.listOfEnemiesX.append(self.leftSidePossible[number])
                    self.listOfEnemiesY.append(380)
                    self.listOfEnemiesXCurrent.append(0)
                    self.listOfEnemiesHeight.append(120)
                    self.listOfEnemiesWidth.append(32)



            self.screen.blit(images["scene 1"], (self.currentposX, 0))
            self.screen.blit(images["crosshairs"], (self.crossX, self.crossY))
            self.screen.blit(images["crosshairs Center"], (self.crossX + 8, self.crossY + 8))
            self.screen.blit(images["radar"], (self.radarCenterX, self.radarCenterY))
            pygame.display.update()




    def drawBackground(self):
        if self.currentposX <= 0 and self.currentposX > -self.width:
            self.screen.blit(self.listOfColors[0], (self.currentposX, 0))
            self.screen.blit(self.listOfColors[1], (self.currentposX + self.width, 0))
        if self.currentposX <= -self.width and self.currentposX > -self.width * 2:
            self.screen.blit(self.listOfColors[1], (self.currentposX + self.width, 0))
            self.screen.blit(self.listOfColors[2], (self.currentposX + self.width * 2, 0))
        if self.currentposX <= -self.width * 2 and self.currentposX > -self.width * 3:
            self.screen.blit(self.listOfColors[2], (self.currentposX + self.width * 2, 0))
            self.screen.blit(self.listOfColors[3], (self.currentposX + self.width * 3, 0))
        if self.currentposX <= -self.width * 3 and self.currentposX >= -self.width * 4:
            self.screen.blit(self.listOfColors[3], (self.currentposX + self.width * 3, 0))
            self.screen.blit(self.listOfColors[0], (self.currentposX + self.width * 4, 0))

    def drawEnemies(self):
        for i in range(len(self.listOfEnemiesX)):
            alpha = self.listOfEnemiesX[i] / 5120 * 360
            alphar = math.radians(alpha)
            sin = math.sin(alphar)
            cos = math.cos(alphar)
            circle = pygame.draw.circle(self.screen, (255, 0, 0),
                                        [int(self.radarCenterX + sin * 50 + 50), int(self.radarCenterY - cos * 50 + 50)], 5)
            if self.currentposX < -3 * self.width:
                if 4 * self.width + self.currentposX + self.listOfEnemiesX[i] > 0:
                    self.listOfEnemiesXCurrent[i] = 4 * self.width + self.currentposX + self.listOfEnemiesX[i]
                    self.screen.blit(self.listOfEnemies[i], (4 * self.width + self.currentposX + self.listOfEnemiesX[i], self.listOfEnemiesY[i]))
            if -self.listOfEnemiesX[i] - self.listOfEnemiesWidth[i] < self.currentposX and -self.listOfEnemiesX[i] + self.listOfEnemiesWidth[
                i] > self.currentposX - self.width:
                self.listOfEnemiesXCurrent[i] = self.listOfEnemiesX[i] + self.currentposX
                self.screen.blit(self.listOfEnemies[i], (self.listOfEnemiesX[i] + self.currentposX, self.listOfEnemiesY[i]))
        pygame.display.update()

    def draw(self):
        self.drawBackground()
        self.drawEnemies()
        self.screen.blit(images["crosshairs"], (self.crossX, self.crossY))
        self.screen.blit(images["crosshairs Center"], (self.crossX + 8, self.crossY + 8))
        self.screen.blit(self.rot_center(images["radar"], self.currentAngle), (self.radarCenterX, self.radarCenterY))
        pygame.display.update()


    def paff(self):
        game = self.getGameController()
        if self.currentPaff == 1:
            game.playSound(sounds["puff 1"], indefinitely=0, gun=True)
            self.currentPaff = 2
        elif self.currentPaff == 2:
            game.playSound(sounds["puff 2"], indefinitely=0, gun=True)
            self.currentPaff = 3
        elif self.currentPaff == 3:
            game.playSound(sounds["puff 3"], indefinitely=0, gun=True)
            self.currentPaff = 4
        elif self.currentPaff == 4:
            game.playSound(sounds["puff 4"], indefinitely=0, gun=True)
            self.currentPaff = 5
        elif self.currentPaff == 5:
            game.playSound(sounds["puff 5"], indefinitely=0, gun=True)
            self.currentPaff = 6
        elif self.currentPaff == 6:
            game.playSound(sounds["puff 6"], indefinitely=0, gun=True)
            self.currentPaff = 7
        elif self.currentPaff == 7:
            game.playSound(sounds["puff 7"], indefinitely=0, gun=True)
            self.currentPaff = 1
        pygame.time.delay(350)
        for i in range(len(self.listOfEnemiesX)):
            x = 0
            y = 0
            if self.listOfEnemiesXCurrent[i] - 20 < self.crossX + 8 and self.listOfEnemiesXCurrent[i] + 60 > self.crossX + 8:
                if self.listOfEnemiesY[i] - 20 < self.crossY + 8 and self.listOfEnemiesY[i] + 120 > self.crossY + 8:
                    if self.listOfEnemiesXCurrent[i] - self.crossX - 8 < 20 and self.listOfEnemiesXCurrent[i] - self.crossX - 8 > 0:
                        x = 20 - (self.listOfEnemiesXCurrent[i] - self.crossX - 8)
                    elif self.listOfEnemiesXCurrent[i] - self.crossX - 8 <= 0 and self.listOfEnemiesXCurrent[
                        i] - self.crossX - 8 >= 20 - self.listOfEnemiesWidth[i]:
                        x = 20
                    elif self.listOfEnemiesXCurrent[i] - self.crossX - 8 < 20 - self.listOfEnemiesWidth[i] and \
                                                    self.listOfEnemiesXCurrent[i] - self.crossX - 8 > -self.listOfEnemiesWidth[
                                i] - 20:
                        x = abs(self.listOfEnemiesXCurrent[i] - self.crossX - 8 + self.listOfEnemiesWidth[i])
                    if self.listOfEnemiesY[i] - self.crossY - 8 < 20 and self.listOfEnemiesY[i] - self.crossY - 8 > 0:
                        y = 20 - (self.listOfEnemiesY[i] - self.crossY - 8)
                    elif self.listOfEnemiesY[i] - self.crossY - 8 <= 0 and self.listOfEnemiesY[i] - self.crossY - 8 >= 20 - \
                            self.listOfEnemiesHeight[i]:
                        y = 20
                    elif self.listOfEnemiesY[i] - self.crossY - 8 < self.listOfEnemiesHeight[i] and self.listOfEnemiesY[
                        i] - self.crossY - 8 > -self.listOfEnemiesHeight[i] - 20:
                        y = abs(self.listOfEnemiesY[i] - self.crossY - 8 + self.listOfEnemiesHeight[i])
                    shot = random.randint(0, 400)
                    if shot <= x * y:
                        if self.listOfEnemiesSpecies[i]=="chicken":
                            game.playSound(sounds["chicken"], indefinitely=0)
                        if self.listOfEnemiesSpecies[i] == "clown":
                            game.playSound(sounds["clown"], indefinitely=0)
                        if self.listOfEnemiesSpecies[i] == "nun":
                            game.playSound(sounds["nun"], indefinitely=0)
                        del self.listOfEnemiesSpecies[i]
                        del self.listOfEnemies[i]
                        del self.listOfEnemiesX[i]
                        del self.listOfEnemiesY[i]
                        del self.listOfEnemiesXCurrent[i]
                        del self.listOfEnemiesWidth[i]
                        del self.listOfEnemiesHeight[i]
                        break

        pygame.time.delay(250)
        self.draw()

    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image


    def moveLeftRight(self, change, changeAngle):
        if self.currentposX < -self.width * 4:
            self.currentposX = 0
        if self.currentposX > 0:
            self.currentposX = -self.width * 4
        self.currentposX += change
        self.currentAngle += changeAngle
        if self.currentAngle == 360:
            self.currentAngle = 0
        if self.currentAngle == -360:
            self.currentAngle = 0
        self.draw()

    def moveUpDown(self, change):
        self.crossY += change
        if self.crossY < 0:
            self.crossY = 0
        if self.crossY > 464:
            self.crossY = 464
        self.draw()


    def handleEvents(self, events):
        self.gameController = self.getGameController()
        changeX = 0
        for event in events:
            if event.type == QUIT:
                exit()
            if self.end_ticks <= pygame.time.get_ticks():
                print(pygame.time.get_ticks())
                print("VEGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            # if event.type == JOYAXISMOTION:
            #     if self.gameController.joy1.get_axis(0) < 0:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    changeX = 10
                    changeAngle = 0.703125
                    self.moveLeftRight(changeX, changeAngle)
                    return
                elif event.key == K_RIGHT:
                # elif self.gameController.joy1.get_axis(0) > 0:
                    changeX = -10
                    changeAngle = -0.703125
                    self.moveLeftRight(changeX, changeAngle)
                    return
                elif event.key == K_UP:
                # elif self.gameController.joy1.get_axis(1) < 0:
                    changeY = -4
                    self.moveUpDown(changeY)
                    return
                elif event.key == K_DOWN:
                # elif self.gameController.joy1.get_axis(1) > 0:
                    changeY = 4
                    self.moveUpDown(changeY)
                    return
            # if event.type == JOYBUTTONDOWN:
            #     if self.gameController.joy1.get_button(0) == True:
            #         exit()
            #     if self.gameController.joy1.get_button(10) == True:
                elif event.key == K_SPACE:
                    self.paff()
                    return

