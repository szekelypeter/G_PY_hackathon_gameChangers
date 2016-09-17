import pygame

from pygame.locals import *
from Scenes import Scene
from Shared import GameConstants



class StartScene(Scene):
    def __init__(self, gameController):
        super(StartScene, self).__init__(gameController)
        self.__sprites = [pygame.image.load(GameConstants.IMAGE_SCENE_START_LOADING_ONE),
                          pygame.image.load(GameConstants.IMAGE_SCENE_START_LOADING_TWO)]

    def render(self, centered=False, y=0):
        start_ticks = pygame.time.get_ticks()
        game = self.getGameController()
        game.playSound(GameConstants.SOUND_SCENE_START_LOADING_HORSE)
        while True:
            super(StartScene, self).render(True, -150)
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if round(seconds) % 2 == 0:
                self.getGameController().getScreen().blit(self.__sprites[0],
                                                          self.__sprites[0].get_rect(center=GameConstants.WINDOW_CENTER))
            else:
                self.getGameController().getScreen().blit(self.__sprites[1],
                                                          self.__sprites[1].get_rect(center=GameConstants.WINDOW_CENTER))
            pygame.display.flip()
            if seconds > GameConstants.LOADING_TIME:
                self.getGameController().setScene(GameConstants.SCENE_MENU)
                game.playSound(GameConstants.SOUND_SCENE_MENU, indefinitely=0)
                break

    def handleEvents(self, events):
        for event in events:
            if event.type == QUIT:
                exit()
