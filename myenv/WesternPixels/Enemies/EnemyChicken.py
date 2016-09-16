from Enemies import Enemy


class EnemyChicken(Enemy):

    def __init__(self, gameController, gun, image, position):
        super(EnemyChicken, self).__init__(gameController, gun, image, position)