import pygame
from pygame.locals import *

from Scenes import Scene
from Shared import GameConstants
from Shared.Images import images
from Shared.Sounds import sounds


class StartScene(Scene):
    def __init__(self, gameController):
        super(StartScene, self).__init__(gameController)
        self.__sprites = [images["loading horse 1"],
                          images["loading horse 2"]]

    def render(self, centered=False, y=0):
        start_ticks = pygame.time.get_ticks()
        game = self.getGameController()
        game.playSound(sounds["loading horse"])
        while True:
            super(StartScene, self).render(True, -150)
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if round(seconds) % 2 == 0:
                self.getGameController().getScreen().blit(self.__sprites[0],(0, 0))
            else:
                self.getGameController().getScreen().blit(self.__sprites[1],(0, 0))
            pygame.display.flip()
            if seconds > GameConstants.LOADING_TIME:
                self.getGameController().setScene(GameConstants.SCENE_MENU)
                game.playSound(sounds["menu"])
                break

    def handleEvents(self, events):
        for event in events:
            if event.type == QUIT:
                exit()
