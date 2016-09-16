from Shared import GameObject

class Enemy(GameObject):

    def __init__(self, gameController, gun, image, position):
        self.__health = None
        self.__gameController = gameController
        self.__gun = gun
        self.__shootingTime = None
        super(Enemy, self).__init__(image, position)

    def reload(self):
        pass
