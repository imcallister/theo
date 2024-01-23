import pygame as pg

class Paddle(pg.sprite.Sprite):

    speed = 0

    def __init__(self, color, width, height):

        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()



BLACK = (  0,  0,  0)

WHITE = (255, 255, 255)

RED = (255,   0,   0)

GREEN = (  0, 255,  0)

BLUE = (255, 255, 255)

game_on = True

def main():
    pg.init()

    SCREEN = pg.display.set_mode((1280, 960), pg.FULLSCREEN)

    paddle1 = Paddle(WHITE, 500, 150)    

    clock = pg.time.Clock()

    all_sprites_list = pg.sprite.Group()  
    all_sprites_list.add(paddle1)


    paddle1.rect.x = 640
    paddle1.rect.y = 480

    while game_on:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                return
            
        all_sprites_list.draw(SCREEN)
        pg.display.flip()
        clock.tick(40)

main()