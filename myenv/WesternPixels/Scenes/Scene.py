import pygame

from Shared import GameConstants


class Scene:

    def __init__(self, gameController):
        self.__gameController = gameController
        self.__texts = []

    def render(self, centered=False, y=0):
        for text in self.__texts:
            if centered:
                self.__gameController.getScreen().blit(text[0], text[0].get_rect(center=(GameConstants.WINDOW_CENTER[0],
                                                                                GameConstants.WINDOW_CENTER[0] + y +
                                                                                         text[2])))
            else:
                self.__gameController.getScreen().blit(text[0], text[1])

    def getGameController(self):
        return self.__gameController

    def handleEvents(self, events):
        pass

    def clearText(self):
        self.__texts = []

    def addText(self, string, x=300, y=0, color=[255, 255, 255], background=GameConstants.BEIGE, size=35, y_coordinate=0):
        font = pygame.font.Font(None, size)
        self.__texts.append([font.render(string, True, color, background), (x, y), y_coordinate])

    def changeText(self, string, x=300, y=0, color=[255, 255, 255], background=GameConstants.BEIGE, size=35, index=-1, y_coordinate=0):
        font = pygame.font.Font(None, size)
        self.__texts[index] = [font.render(string, True, color, background), (x, y), y_coordinate]
