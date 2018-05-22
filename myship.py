import pygame
from pygame.locals import *

class MyShip:
    """自機クラス

    プロパティ:
    x y -- 自機の中心座標
    """

    def __init__(self, x, y):
        #自機の中心座標をセットして初期化する
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50

    def draw(self, pygame, screen):
        pygame.draw.rect(screen, (170,170,170), Rect(self.x - self.width/2,self.y - self.height/2,self.width,self.height))

