from Enemies import Enemy


class EnemyCatOctopus(Enemy):

    def __init__(self, gameController, gun, image, position, shootingTime):
        super(EnemyCatOctopus, self).__init__(gameController, gun, image, position, shootingTime)

    def reload(self):
        pass