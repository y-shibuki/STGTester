from enemy import Enemy

class Enemies:
    """
    Enemyクラスの管理クラス

    プロパティ:
    
    """
    def __init__(self):
        self.enemy_datas = []
        self.addEnemy(Enemy())

    def addEnemy(self,enemy_data):
        self.enemy_datas.append(enemy_data)

    def move(self):
        for enemy_data in self.enemy_datas:
            enemy_data.move()

    def draw(self, pygame, screen):
        for enemy_data in self.enemy_datas:
            enemy_data.draw(pygame, screen)      