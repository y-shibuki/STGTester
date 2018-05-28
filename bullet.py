import pygame
import global_data as G
import math

class Bullet:
    """弾クラス

    プロパティ:
    x y -- 敵の中心座標
    """

    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.a = angle
        self.s = speed
        self.width = 0
        self.height = 0
        self.time = 0
        self.death_flag = False

    def move(self):
        self.x += math.cos(self.a * math.pi * 2) * self.s
        self.y += math.sin(self.a * math.pi * 2) * self.s
    
    def isDisappear(self):
        if self.x > G.WIDTH + G.B_DISAPPEAR_MARGIN or \
           self.x < -G.B_DISAPPEAR_MARGIN or \
           self.y > G.HEIGHT + G.B_DISAPPEAR_MARGIN or \
           self.y < -G.B_DISAPPEAR_MARGIN:
            self.death_flag = True

    def draw(self, pygame, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x),int(self.y)), 5)