import pygame as pg
walk_right = [pg.image.load('./code/stuff/R1.png'), pg.image.load('./code/stuff/R2.png'), pg.image.load('./code/stuff/R3.png'), pg.image.load('./code/stuff/R4.png'), pg.image.load('./code/stuff/R5.png'), pg.image.load('./code/stuff/R6.png'), pg.image.load('./code/stuff/R7.png'), pg.image.load('./code/stuff/R8.png'), pg.image.load('./code/stuff/R9.png')]
walk_left = [pg.image.load('./code/stuff/L1.png'), pg.image.load('./code/stuff/L2.png'), pg.image.load('./code/stuff/L3.png'), pg.image.load('./code/stuff/L4.png'), pg.image.load('./code/stuff/L5.png'), pg.image.load('./code/stuff/L6.png'), pg.image.load('./code/stuff/L7.png'), pg.image.load('./code/stuff/L8.png'), pg.image.load('./code/stuff/L9.png')]
bg = pg.image.load('./code/stuff/bg.jpg')
char = pg.image.load('./code/stuff/standing.png')
bg = pg.transform.scale(bg, (1440, 960))
BLACK = (  0,  0,  0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,  0)
BLUE = (  0,  0, 255)

SCREEN = pg.display.set_mode((0,0), pg.FULLSCREEN)
screen_boundary = SCREEN.get_rect()

all_sprites_list = pg.sprite.Group()

clock = pg.time.Clock()

class Guy(pg.sprite.Sprite):


    speed = 0
    
    def __init__(self, color, width, height, start_x, start_y):

        pg.sprite.Sprite.__init__(self)
        
        self.left = False
        self.right = False
        self.walk_count = 0

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

def draw_window():
    SCREEN.fill(BLACK)
    SCREEN.blit(bg, (0,0))
    all_sprites_list.draw(SCREEN)
    if walk_count + 1 >= 40:
        walk_count = 0
    pg.display.flip()
    

def main():
    pg.init()

    guy_start_x = 1300
    guy_start_y = 500

    lkey_down = False
    rkey_down = False

    guy1 = Guy(RED, 64, 64, guy_start_x, guy_start_y)


    guy_alive = True

    clock.tick(40)
    
    all_sprites_list.add(guy1)

    while guy_alive:
        if lkey_down == True:
            guy1.move_left()
            left = True
            right = False
        elif rkey_down == True:
            guy1.move_right()        
            right = True
            Left = False
        else:
            right = False
            left = False
            walk_count = 0
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
draw_window   
main()