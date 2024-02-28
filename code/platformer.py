import pygame as pg

BLACK = (  0,  0,  0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,  0)
BLUE = (  0,  0, 255)

class Guy(pg.sprite.Sprite):

    speed = 0
    
    def _init_(self, color, width, height, start_x, start_y):
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def move_left(self):
        current_x = self.rect.x
        self.rect.x = current_x - 20

    def move_right(self):
        current_x = self.rect.x
        self.rect.x = current_x + 20


def main():
    pg.init()

    SCREEN = pg.display.set_mode((0,0), pg.FULLSCREEN)
    screen_boundary = SCREEN.get_rect()

    guy_start_x = 1300
    guy_start_y = 500

    lkey_down = False
    rkey_down = False

    guy1 = Guy(RED, 100, 200, guy_start_x, guy_start_y)

    clock = pg.time.Clock()

    guy_alive = True

    all_sprites_list = pg.sprite.Group()
    all_sprites_list.add(guy1)

    while guy_alive:
        if lkey_down == True:
            guy1.move_left()
        if rkey_down == True:
            guy1.move_right()        
        
        for event in pg.event.get():
            
            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                return
            
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                lkey_down = True

            if event.type == pg.KEYUP and event.key == pg.K_LEFT:
                lkey_down = False 

            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                rkey_down = True

            if event.type == pg.KEYUP and event.key == pg.K_RIGHT:
                rkey_down = False
        
        SCREEN.fill(BLACK)
        all_sprites_list.draw(SCREEN)
        pg.display.flip()
        clock.tick(40)
main()