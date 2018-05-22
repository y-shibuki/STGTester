# coding: utf-8
import pygame
from pygame.locals import *
import sys
from myship import MyShip

SCREEN_SIZE = (400,400)

def main():
    #Pygameの初期化
    pygame.init()
    #SCREEN_SIZEの画面を作成
    screen = pygame.display.set_mode(SCREEN_SIZE)
    #タイトルバーの文字列をセット
    pygame.display.set_caption(u"シューティングゲーム")

    myship = MyShip(50,50)

    while True:
        #背景色の設定
        screen.fill((255,255,255))

        # ***いろんな処理*** #
        myship.move()
        myship.draw(pygame,screen)

        #画面の更新
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()
            elif event.type ==KEYDOWN
                if event.key == K_RIGHT: myship.direction["right"] = True

if __name__ == "__main__":
    main()
