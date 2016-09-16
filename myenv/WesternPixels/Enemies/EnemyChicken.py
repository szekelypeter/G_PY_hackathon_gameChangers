from Enemies import Enemy


class EnemyChicken(Enemy):

    def __init__(self, gameController, gun, image, position, shootingTime):
        super(EnemyChicken, self).__init__(gameController, gun, image, position, shootingTime)

    def reload(self):
        pass