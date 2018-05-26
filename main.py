# coding: utf-8
import pygame
from pygame.locals import *
import sys
from myship import MyShip
from enemies import Enemies

#Pygameの初期化
pygame.init()
SCREEN_SIZE = (400,400)

def main():
    #SCREEN_SIZEの画面を作成
    screen = pygame.display.set_mode(SCREEN_SIZE)
    #タイトルバーの文字列をセット
    pygame.display.set_caption(u"シューティングゲーム")
    #FPSの取得
    clock = pygame.time.Clock()

    myship = MyShip(50,50)

    enemies = Enemies()
    
    while True:
        #FPSを60に設定
        clock.tick(60)

        #背景色の設定
        screen.fill((255,255,255))

        # ***いろんな処理*** #
        myship.move()
        enemies.move()

        myship.draw(pygame,screen)
        enemies.draw(pygame,screen)

        #画面の更新
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT: myship.direction["right"] = True
                elif event.key == K_LEFT: myship.direction["left"] = True
                if event.key == K_UP: myship.direction["up"] = True
                elif event.key == K_DOWN: myship.direction["down"] = True
            elif event.type == KEYUP:
                if event.key == K_RIGHT: myship.direction["right"] = False
                elif event.key == K_LEFT: myship.direction["left"] = False
                if event.key == K_UP: myship.direction["up"] = False
                elif event.key == K_DOWN: myship.direction["down"] = False

if __name__ == "__main__":
    main()
