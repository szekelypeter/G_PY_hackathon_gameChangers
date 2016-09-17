import pygame

from Scenes import Scene
from pygame.locals import *

from Shared import GameConstants


class MenuScene(Scene):
    def __init__(self, gameController):
        super(MenuScene, self).__init__(gameController)
        self.addText(GameConstants.MENU_PLAY[0], background=GameConstants.RED, y_coordinate=GameConstants.MENU_PLAY[1])
        self.addText(GameConstants.MENU_HIGHSCORE[0],  y_coordinate=GameConstants.MENU_HIGHSCORE[1])
        self.addText(GameConstants.MENU_EXIT[0], y_coordinate=GameConstants.MENU_EXIT[1])
        self.__currentIndex = 0

    def render(self, centered=False, y=0):

        self.getGameController().fillBackGround()
        super(MenuScene, self).render(True)
        pygame.display.flip()

    def handleEvents(self, events):
        game = self.getGameController()
        game.playSound(GameConstants.SOUND_SCENE_MENU, indefinitely=0)
        for event in events:
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    self.changeText(GameConstants.MENU_PLAY[0], background=GameConstants.RED, index=0, y_coordinate=GameConstants.MENU_PLAY[1])
                    self.changeText(GameConstants.MENU_HIGHSCORE[0], background=[0, 0, 0], index=1, y_coordinate= GameConstants.MENU_HIGHSCORE[1])
                    self.changeText(GameConstants.MENU_EXIT[0], background=[0, 0, 0], index=2, y_coordinate=GameConstants.MENU_EXIT[1])
                    self.__currentIndex = 0
                if event.key == K_2:
                    self.changeText(GameConstants.MENU_PLAY[0], background=[0, 0, 0], index=0, y_coordinate=GameConstants.MENU_PLAY[1])
                    self.changeText(GameConstants.MENU_HIGHSCORE[0], background=GameConstants.RED, index=1, y_coordinate= GameConstants.MENU_HIGHSCORE[1])
                    self.changeText(GameConstants.MENU_EXIT[0], background=[0, 0, 0], index=2, y_coordinate=GameConstants.MENU_EXIT[1])
                    self.__currentIndex = 1
                if event.key == K_3:
                    self.changeText(GameConstants.MENU_PLAY[0], index=0, y_coordinate=GameConstants.MENU_PLAY[1])
                    self.changeText(GameConstants.MENU_HIGHSCORE[0], background=[0, 0, 0], index=1, y_coordinate= GameConstants.MENU_HIGHSCORE[1])
                    self.changeText(GameConstants.MENU_EXIT[0], background=GameConstants.RED, index=2, y_coordinate=GameConstants.MENU_EXIT[1])
                    self.__currentIndex = 2
                if event.key == K_4:
                    if self.__currentIndex == 0:
                        self.getGameController().setScene(GameConstants.SCENE_OPTION_PLAYER_MODE)
                    if self.__currentIndex == 1:
                        self.getGameController().setScene(GameConstants.SCENE_HIGHSCORE)
                    if self.__currentIndex == 2:
                        exit()
