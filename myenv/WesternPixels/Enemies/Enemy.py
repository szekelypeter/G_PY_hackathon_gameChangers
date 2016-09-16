
from Shared import GameObject

class Enemy(GameObject):

    def __init__(self, gameController, gun):
        self.__health = None
        self.__gameController = gameController
        self.__gun = gun
        self.__shootingTime = None

    def reload(self):
        pass


