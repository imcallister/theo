import pygame as pg

SCREEN = pg.display.set_mode((0,0), pg.FULLSCREEN)

screen_boundary = SCREEN.get_rect()

class Paddle(pg.sprite.Sprite):

    speed = 0

    def __init__(self, color, width, height, start_x, start_y):

        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def move_left(self):
        current_x = self.rect.x

        if self.rect.left > 0:

            self.rect.x = current_x - 10
        

    def move_right(self):
        current_x = self.rect.x
                
        if self.rect.right < 1440:

                self.rect.x = current_x + 10

           

class Ball(pg.sprite.Sprite):

    
    speed = 0

    def __init__(self, color, width, height):

        pg.sprite.Sprite.__init__(self)

        self.moving1 = True

        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    
    def move(self):
        current_x = self.rect.x

        if self.rect.left >= 0 and self.rect.left <= 1440 and self.moving1 == True:

            self.rect.x = current_x - 10

        
        if self.rect.left == 0:
            self.moving1 = False

        if self.rect.left == 1440:
            self.moving1 = True
        
        if self.rect.left >= 0 and self.rect.left <= 1440 and self.moving1 == False:

            self.rect.x = current_x + 10


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

    ball_alive = True

    paddle1 = Paddle(WHITE, 110, 15, 670, 870)    

    clock = pg.time.Clock()

    all_sprites_list = pg.sprite.Group()  
    all_sprites_list.add(paddle1)

    ball1 = Ball(WHITE, 15, 15)

    ball1.rect.x = 720
    ball1.rect.y = 450

    all_sprites_list.add(ball1)

    while game_on:

        if ball_alive == True:
            ball1.move()
        
        if lkey_down == True:
            paddle1.move_left()
        if rkey_down == True:
            paddle1.move_right()
       
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