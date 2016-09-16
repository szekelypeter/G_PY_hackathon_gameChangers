from Guns import Gun

class Player:

    def __init__(self, gameController, gun):
        self.__gameController = gameController
        self.__gun = gun
        self.__takeCover = False

    def getTakeCover(self):
        return self.__takeCover

    def setTakeCover(self, isTakeCover):
        self.__takeCover = isTakeCover

    def reload(self):
        self.__gun.currentAmmo = self.__gun.AMMO

    def shoot(self):
        self.__gun.currentAmmo -= 1
