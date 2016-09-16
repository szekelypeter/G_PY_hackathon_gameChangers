from Guns import Gun
from Players.Team import Team
from Shared import GameObject


class Player(GameObject):

    def __init__(self, gameController, gun, image, position):
        self.__gameController = gameController
        self.__gun = gun
        self.__takeCover = False
        
        super(Player, self).__init__(image, position)

    def getTakeCover(self):
        return self.__takeCover

    def setTakeCover(self, isTakeCover):
        self.__takeCover = isTakeCover

    def reload(self):
        self.__gun.currentAmmo = self.__gun.AMMO

    def shoot(self):
        self.__gun.currentAmmo -= 1
