from Enemies import Enemy


class EnemyNun(Enemy):

    def __init__(self, gameController, gun, image, position, shootingTime):
        super(EnemyNun, self).__init__(gameController, gun, image, position, shootingTime)

    def reload(self):
        pass