
from Shared import GameObject

class Enemy(GameObject):

    def __init__(self, gameController, gun):
        self.health = None
        self.gameController = gameController
        self.gun = gun
        self.shootingTime = None

    def reload(self):
        pass


