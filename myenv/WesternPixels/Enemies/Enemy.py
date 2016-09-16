from Shared import GameObject

class Enemy(GameObject):

    def __init__(self, gameController, gun, image, position, shootingTime):
        self.__health = None
        self.__gameController = gameController
        self.__gun = gun
        self.__shootingTime = shootingTime
        super(Enemy, self).__init__(image, position)

    def reload(self):
        pass

    def getHealth(self):
        return self.__health

    def getShootingTime(self):
        return self.__shootingTime