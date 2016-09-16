import pygame


class Scene:

    def __init__(self, gameController):
        self.__gameController = gameController
        self.__text = []

    def render(self):
        for text in self.__texts:
            self.__gameController.screen.blit(text[0], text[1])

    def getGameController(self):
        return self.__gameController

    def handleEvents(self, events):
        pass

    def clearText(self):
        self.__texts = []

    def addText(self, string, x=0, y=0, color=[255, 255, 255], background=[0, 0, 0], size=17):
        font = pygame.font.Font(None, size)
        print(string)
        self.__texts.append([font.render(string, True, color, background), (x, y)])
