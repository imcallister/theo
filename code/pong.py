import pygame as pg



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

        self.hitting_ball = False

        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.center = (start_x, start_y)

        self.speed_x = 10
        self.speed_y = -10

        

    def move(self):
        current_x = self.rect.x
        current_y = self.rect.y

        # if a bit of code is greyed out like hit_b_wall then its a hint
        # from Visual Studio that the variable is not being used
        # check if you can delete some code
        hit_l_wall = hit_r_wall = hit_t_wall = hit_b_wall = False

        # the code below is much more verbose than it needs to be
        # see if you can combine the two sections of setting all the hit_walls
        # and checking if the hit_walls are True into less lines of code
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
    
    SCREEN = pg.display.set_mode((0,0), pg.FULLSCREEN)
    screen_boundary = SCREEN.get_rect()
    screen_width = screen_boundary.width
    screen_height = screen_boundary.height
    
    ball_start_x = round(screen_width * .5, -1)
    ball_start_y = round(screen_height * .5, -1)

    ball_width = 15
    ball_height = 15

    paddle_width = 110
    paddle_height = 15

    paddle_start_x = round(screen_width * .5, -1)
    paddle_start_y = screen_height - 2.5 * paddle_height

    score = 0

    lkey_down = False
    rkey_down = False

    ball_alive = True

    paddle1 = Paddle(WHITE, paddle_width, paddle_height, paddle_start_x, paddle_start_y)    
    ball1 = Ball(WHITE, ball_width, ball_height, ball_start_x, ball_start_y)

    clock = pg.time.Clock()

    all_sprites_list = pg.sprite.Group()  
    all_sprites_list.add(paddle1)    
    all_sprites_list.add(ball1)

    while ball_alive:
 
        # check for collision of ball with paddle
        ball_x = ball1.rect.centerx
        ball_right = ball1.rect.right
        ball_left = ball1.rect.left
        ball_y = ball1.rect.y
        paddle_x = paddle1.rect.centerx
        paddle_left = paddle1.rect.left
        paddle_right = paddle1.rect.right
        
        # the gap between 850 and 900 seems quite large
        # it might result in the ball bouncing when its too high above paddle
        # or below the paddle.
        # Can you narrow down the range a bit? Or decide it doesn't matter
        print('Ball:', ball_x, ball_y, 'Hitting', ball1.hitting_ball, 'Paddle x', paddle_x, 'Paddle center', paddle1.rect.center)

        if ball_y >=paddle_start_y - paddle_height * .5 and ball_y <= paddle_start_y + paddle_height * .5:
            # check if its hitting paddle
            if ball_right >= paddle_left and ball_left <= paddle_right:

                if ball1.hitting_ball == False:
                # ball has hit the paddle
                    score += 1
                    ball1.speed_y = -ball1.speed_y
                    ball1.hitting_ball = True

        if ball_x >= screen_width:
            ball1.hitting_ball = False

        if ball_x <= 0:
            ball1.hitting_ball = False

        if ball_y <= 0:
            ball1.hitting_ball = False
        
        if ball_y >= screen_height:
            ball_alive = False

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