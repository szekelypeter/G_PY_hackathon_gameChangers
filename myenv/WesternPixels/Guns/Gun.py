class Gun:

    def __init__(self, ammo, power, crossHairs):
        self.AMMO = ammo
        self.__currentAmmo = self.AMMO
        self.__power = power
        self.__crossHairs = crossHairs

    def getCurrentAmmo(self):
        return self.__currentAmmo

    def setCurrentAmmo(self, ammo):
        self.__currentAmmo = ammo

    def getPower(self):
        return self.__power

    def getCrossHairs(self):
        return self.__crossHairs
