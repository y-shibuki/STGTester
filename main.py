import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (400,400)

def main():
    #Pygameの初期化
    pygame.init()
    #SCREEN_SIZEの画面を作成
    screen = pygame.display.set_mode(SCREEN_SIZE)
    #タイトルバーの文字列をセット
    pygame.display.set_caption(u"シューティングゲーム")

    while True:
        #背景色の設定
        screen.fill((255,255,255))
        #画面の更新
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
