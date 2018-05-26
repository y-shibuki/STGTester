import pygame
#from pygame.locals import *
from pygame.locals import Rect

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
        self.speed = 3
        self.direction = {"right": False,"left": False,"up": False,"down": False}

    def move(self):
        if self.direction["right"] == True:
            self.x += self.speed
        if self.direction["left"] == True:
            self.x -= self.speed
        if self.direction["down"] == True:
            self.y += self.speed
        if self.direction["up"] == True:
            self.y -= self.speed

    def draw(self, pygame, screen):
        pygame.draw.rect(screen, (170,170,170), Rect(self.x - self.width/2,self.y - self.height/2,self.width,self.height))

