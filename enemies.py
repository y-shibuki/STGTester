from enemy import SimpleEnemy

class Enemies:
    """
    Enemyクラスの管理クラス

    プロパティ:
    
    """
    def __init__(self):
        self.enemy_datas = []
        self.addEnemy(SimpleEnemy(1))

    def addEnemy(self,enemy_data):
        self.enemy_datas.append(enemy_data)
    
    def reloadEnemy(self):
        for enemy_data in self.enemy_datas:
            enemy_data.isDisappear()
            if enemy_data.death_flag == True:
                self.enemy_datas.remove(enemy_data)

    def move(self):
        for enemy_data in self.enemy_datas:
            enemy_data.move()

    def draw(self, pygame, screen):
        for enemy_data in self.enemy_datas:
            enemy_data.draw(pygame, screen)      