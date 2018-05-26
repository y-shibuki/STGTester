import pygame
#from pygame.locals import *

class Enemy:
    """敵クラス

    プロパティ:
    x y -- 敵の中心座標
    """

    def __init__(self):
        #敵の中心座標をセットして初期化する
        self.x = -100
        self.y = 50
        self.width = 30
        self.height = 50
        self.time = 0
        self.death_flag = True
    
    def move(self):
        self.x += 4
        self.time += 1

    def draw(self, pygame, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x,self.y), 20)