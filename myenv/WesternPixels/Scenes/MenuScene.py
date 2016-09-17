import pygame

from Scenes import Scene
from pygame.locals import *

from Shared import GameConstants


class MenuScene(Scene):
    def __init__(self, gameController):
        super(MenuScene, self).__init__(gameController)
        self.addText(GameConstants.MENU_PLAY[0], x=300, background=GameConstants.BLACK, y=GameConstants.MENU_PLAY[1], y_coordinate=GameConstants.MENU_PLAY[1])
        self.addText(GameConstants.MENU_HIGHSCORE[0], x=300, y=GameConstants.MENU_HIGHSCORE[1], y_coordinate=GameConstants.MENU_HIGHSCORE[1])
        self.addText(GameConstants.MENU_EXIT[0], x=300,y=GameConstants.MENU_EXIT[1], y_coordinate=GameConstants.MENU_EXIT[1])
        self.background = pygame.image.load(GameConstants.IMAGE_SCENE_MENU)
        self.__currentIndex = 0

    def render(self, centered=False, y=0):

        self.getGameController().fillBackGround()
        self.getGameController().getScreen().blit(self.background, (0, 0))
        super(MenuScene, self).render(False)
        pygame.display.flip()

    def handleEvents(self, events):
        game = self.getGameController()
        game.playSound(GameConstants.SOUND_SCENE_MENU, indefinitely=0)
        for event in events:
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    self.changeText(GameConstants.MENU_PLAY[0], background=GameConstants.BLACK, x=300,index=0, y=GameConstants.MENU_PLAY[1], y_coordinate=GameConstants.MENU_PLAY[1])
                    self.changeText(GameConstants.MENU_HIGHSCORE[0], x=300,index=1, y=GameConstants.MENU_HIGHSCORE[1], y_coordinate= GameConstants.MENU_HIGHSCORE[1])
                    self.changeText(GameConstants.MENU_EXIT[0], x=300,index=2, y=GameConstants.MENU_EXIT[1], y_coordinate=GameConstants.MENU_EXIT[1])
                    self.__currentIndex = 0
                if event.key == K_2:
                    self.changeText(GameConstants.MENU_PLAY[0],x=300, index=0, y=GameConstants.MENU_PLAY[1], y_coordinate=GameConstants.MENU_PLAY[1])
                    self.changeText(GameConstants.MENU_HIGHSCORE[0], background=GameConstants.BLACK, x=300,index=1, y=GameConstants.MENU_HIGHSCORE[1], y_coordinate= GameConstants.MENU_HIGHSCORE[1])
                    self.changeText(GameConstants.MENU_EXIT[0],  x=300,index=2, y=GameConstants.MENU_EXIT[1], y_coordinate=GameConstants.MENU_EXIT[1])
                    self.__currentIndex = 1
                if event.key == K_3:
                    self.changeText(GameConstants.MENU_PLAY[0], index=0, x=300,y=GameConstants.MENU_PLAY[1], y_coordinate=GameConstants.MENU_PLAY[1])
                    self.changeText(GameConstants.MENU_HIGHSCORE[0],  x=300,index=1, y=GameConstants.MENU_HIGHSCORE[1], y_coordinate= GameConstants.MENU_HIGHSCORE[1])
                    self.changeText(GameConstants.MENU_EXIT[0], background=GameConstants.BLACK, index=2, x=300,y=GameConstants.MENU_EXIT[1], y_coordinate=GameConstants.MENU_EXIT[1])
                    self.__currentIndex = 2
                if event.key == K_4:
                    if self.__currentIndex == 0:
                        self.getGameController().setScene(GameConstants.SCENE_OPTION_PLAYER_MODE)
                    if self.__currentIndex == 1:
                        self.getGameController().setScene(GameConstants.SCENE_HIGHSCORE)
                    if self.__currentIndex == 2:
                        exit()
