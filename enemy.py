import pygame
#from pygame.locals import *
import global_data as G
from bullets import SimpleBullet

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
        self.death_flag = False

    def move(self):
        pass
    
    def isDisappear(self):
        if self.x > G.WIDTH + G.E_DISAPPEAR_MARGIN or \
           self.x < -G.E_DISAPPEAR_MARGIN or \
           self.y > G.HEIGHT + G.E_DISAPPEAR_MARGIN or \
           self.y < -G.E_DISAPPEAR_MARGIN:
            self.death_flag = True

    def draw(self, pygame, screen):
        pygame.draw.circle(screen, (255,0,0), (int(self.x),int(self.y)), 20)

class SimpleEnemy(Enemy):
    """単純な動きを持つ単体敵

    プロパティ:
    pattern : 動きのパターン
              1 --- 画面を横切っていく
              2 --- 画面中心を縦断
              3 --- 画面中央上辺で停止
    """

    def __init__(self, pattern):
        super().__init__()
        self.pattern = pattern

        if self.pattern == 1:
            self.x = -G.E_DISAPPEAR_MARGIN + 10
            self.y = 40

        elif self.pattern == 2:
            self.x = G.WIDTH / 2
            self.y = -G.E_DISAPPEAR_MARGIN + 10

        elif self.pattern == 3:
            self.x = G.WIDTH / 2
            self.y = -G.E_DISAPPEAR_MARGIN + 10
    
    def move(self):
        if self.pattern == 1:
            self.x += 3

        elif self.pattern == 2:
            self.y += 3

        elif self.pattern == 3:
            if self.time < 50:
                self.y += 3
            elif self.time >= 50:
                pass

        self.time += 1

class SimplePairEnemy(Enemy):
    """単純な動きを複数で行う敵

    プロパティ:
    pattern : 動きのパターン
              1 --- 画面を複数が横切っていく
              2 --- 画面中央上辺で停止
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
        self.time += 1