import pygame
from pygame.locals import *

from Scenes import Scene
from Shared import GameConstants
from Shared.Images import images


class OptionPlayerModeScene(Scene):

    def __init__(self, gameController):
        super(OptionPlayerModeScene, self).__init__(gameController)
        self.addText(GameConstants.GAME_MODE_SINGLE[0], background=GameConstants.BLACK, y=GameConstants.GAME_MODE_SINGLE[1], y_coordinate=GameConstants.GAME_MODE_SINGLE[1])
        self.addText(GameConstants.GAME_MODE_MULTI[0], y=GameConstants.GAME_MODE_MULTI[1], y_coordinate=GameConstants.GAME_MODE_MULTI[1])
        self.background = images["menu"]
        self.__currentIndex = 0

    def render(self, centered=False, y=0):
        self.getGameController().fillBackGround()
        self.getGameController().getScreen().blit(self.background, (0, 0))
        super(OptionPlayerModeScene, self).render(False)
        pygame.display.flip()

    def handleEvents(self, events):
        gameController = self.getGameController()
        for event in events:
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
            # if event.type == JOYBUTTONDOWN:
            #     if gameController.joy1.get_button(0) == True:
                    self.changeText(GameConstants.GAME_MODE_SINGLE[0], background=GameConstants.RED, index=0,
                                    y=GameConstants.GAME_MODE_SINGLE[1], y_coordinate=GameConstants.GAME_MODE_SINGLE[1])
                    self.changeText(GameConstants.GAME_MODE_MULTI[0], background=GameConstants.BEIGE, index=1,
                                    y=GameConstants.GAME_MODE_MULTI[1], y_coordinate=GameConstants.GAME_MODE_MULTI[1])
                    self.__currentIndex = 0
                # if gameController.joy1.get_button(1) == True:
                if event.key == K_2:
                    self.changeText(GameConstants.GAME_MODE_SINGLE[0], background=GameConstants.BEIGE, index=0,
                    y=GameConstants.GAME_MODE_SINGLE[1], y_coordinate=GameConstants.GAME_MODE_SINGLE[1])
                    self.changeText(GameConstants.GAME_MODE_MULTI[0], background=GameConstants.BLACK, index=1,
                    y=GameConstants.GAME_MODE_MULTI[1], y_coordinate=GameConstants.GAME_MODE_MULTI[1])
                    self.__currentIndex = 1
                # if gameController.joy1.get_button(10) == True:
                if event.key == K_4:
                    if self.__currentIndex == 0:
                        self.getGameController().setScene(GameConstants.SCENE_PLAY_SINGLE)
                    if self.__currentIndex == 1:
                        self.getGameController().setScene(GameConstants.SCENE_PLAY_MULTI)
                    if self.__currentIndex == 2:
                        exit()
