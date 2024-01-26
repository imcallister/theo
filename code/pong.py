import pygame as pg

SCREEN = pg.display.set_mode((1280, 960), pg.FULLSCREEN)

screen_boundary = SCREEN.get_rect()

class Paddle(pg.sprite.Sprite):

    speed = 0

    def __init__(self, color, width, height):

        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

               

class Ball(pg.sprite.Sprite):

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

    lkey_down = False

    rkey_down = False

    paddle1 = Paddle(WHITE, 110, 15)    

    clock = pg.time.Clock()

    all_sprites_list = pg.sprite.Group()  
    all_sprites_list.add(paddle1)


    paddle1.rect.x = 763
    paddle1.rect.y = 1025

    ball1 = Ball(WHITE, 15, 15)

    ball1.rect.x = 800
    ball1.rect.y = 550

    all_sprites_list.add(ball1)
    
    screen_boundary = SCREEN.get_rect()
    screen_boundary.clamp(paddle1)

    while game_on:
        if lkey_down == True:
            move_left()
        if rkey_down == True:
            move_right()

        def move_left():
            current_x = paddle1.rect.x
        
            paddle1.rect.x = current_x - 10
        
            SCREEN.fill(BLACK)

            all_sprites_list.draw(SCREEN)

        def move_right():
            current_x = paddle1.rect.x
                
            paddle1.rect.x = current_x + 10
                
            SCREEN.fill(BLACK)

            all_sprites_list.draw(SCREEN)     
        
       
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
   
    
        all_sprites_list.draw(SCREEN)
        pg.display.flip()
        clock.tick(40)

main()