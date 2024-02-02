import pygame as pg

SCREEN = pg.display.set_mode((0,0), pg.FULLSCREEN)

screen_boundary = SCREEN.get_rect()

score = 0

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

            self.rect.x = current_x - 20
        

    def move_right(self):
        current_x = self.rect.x
                
        if self.rect.right < 1440:

                self.rect.x = current_x + 20

           

class Ball(pg.sprite.Sprite):

    def __init__(self, color, width, height, start_x, start_y):

        pg.sprite.Sprite.__init__(self)

        
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = start_x
        self.rect.y = start_y

        self.speed_x = 10
        self.speed_y = 10


    def move(self):
        current_x = self.rect.x
        current_y = self.rect.y

        hit_l_wall = hit_r_wall = hit_t_wall = hit_b_wall = False

        if current_x == 0: 
            hit_l_wall = True
            
        if current_x == 1440: 
            hit_r_wall = True
            
        if current_y == 0: 
            hit_t_wall = True
            
        if current_y == 900: 
            hit_b_wall = True


        if hit_t_wall == True:
            self.speed_y = -self.speed_y 


        if hit_b_wall == True:
            self.speed_y = -self.speed_y

        if hit_r_wall == True:
            self.speed_x = -self.speed_x
        
        if hit_l_wall == True:
            self.speed_x = -self.speed_x

                    
        self.rect.y = current_y + self.speed_y
        self.rect.x = current_x + self.speed_x


BLACK = (  0,  0,  0)

WHITE = (255, 255, 255)

RED = (255,   0,   0)

GREEN = (  0, 255,  0)

BLUE = (255, 255, 255)

game_on = True



def main():
    pg.init()
    
    score = 0

    lkey_down = False

    rkey_down = False

    ball_alive = True

    paddle1 = Paddle(WHITE, 110, 15, 670, 870)    

    clock = pg.time.Clock()

    all_sprites_list = pg.sprite.Group()  
    all_sprites_list.add(paddle1)

    ball1 = Ball(WHITE, 15, 15, 720, 450)

    
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
        score_font = pg.font.SysFont("Times New Roman", 30)
        label1 = score_font.render("Score "+str(score), 1, (255,255,0))
        SCREEN.blit(label1, (720,450))
        pg.display.flip()
        clock.tick(40)

main()