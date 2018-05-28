import pygame
import global_data as G
from bullet import Bullet

class SimpleBullet(Bullet):
    """直進する弾

    プロパティ:
    x, y: xy座標
    angle: 角度
    number: 弾の個数
    interval: 弾の発射される間隔
    """

    def __init__(self, x, y, angle, number, interval):
        self.bullet_datas = []
        self.x = x
        self.y = y
        self.a = angle
        self.n = number
        self.interval = interval
        self.time = 0
        self.flag = False   #True この弾幕を消去する
    
    def move(self):
        self.time += 1
        if (self.time % self.interval) == 0:
            self.bullet_datas.append(Bullet(self.x, self.y, self.a, 5))
        
        for bullet_data in self.bullet_datas:
            bullet_data.move()
        
        if self.time >= (self.interval * (self.n - 1)):
            self.flag = True

    def draw(self):
        for bullet_data in self.bullet_datas:
            bullet_data.draw()
        
