from Enemies import Enemy


class EnemyClown(Enemy):

    def __init__(self, gameController, gun, image, position, shootingTime):
        super(EnemyClown, self).__init__(gameController, gun, image, position, shootingTime)

    def reload(self):
        pass