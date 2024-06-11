import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()  #こうかとんrectの抽出
    kk_rct.center = 300, 200
    
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kk_img_x = tmr % 3200
        screen.blit(bg_img, [-kk_img_x, 0])
        screen.blit(bg_img2, [-kk_img_x + 1600, 0])
        screen.blit(bg_img, [-kk_img_x + 3200, 0])
        screen.blit(bg_img2, [-kk_img_x + 4800, 0])

        key_lst = pg.key.get_pressed()  #全てのキーの押下状態を取得
        if key_lst[pg.K_UP]:    #上キーを押したら
            kk_rct.move_ip(0, -1)
        if key_lst[pg.K_DOWN]:  #下キーを押したら
            kk_rct.move_ip(0, 1)
        if key_lst[pg.K_LEFT]:    #左キーを押したら
            kk_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]:  #右キーを押したら
            kk_rct.move_ip(1, 0)
        screen.blit(kk_img, kk_rct) #kk_imgをkk_rctの設定に従って貼り付け 
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()