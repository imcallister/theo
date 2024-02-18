import pygame as pg

BLACK = (  0,  0,  0)
WHITE = (255, 255, 255)

class Paddle(pg.sprite.Sprite):

    def __init__(self, color, width, height, screen):

        pg.sprite.Sprite.__init__(self)

        self.height = height
        self.width = width
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        start_x = round(screen.width * .5, -1)
        start_y = screen.height - 2.5 * height
    
        self.rect.x = start_x
        self.rect.y = start_y

        self.width_of_screen = screen.width

    def move(self, left, right):
        if left:
            self.move_left()
        if right:
            self.move_right()

    def move_left(self):
        current_x = self.rect.x

        if self.rect.left > 0:
            self.rect.x = current_x - 20
        

    def move_right(self):
        current_x = self.rect.x
                
        if self.rect.right < self.width_of_screen:
            self.rect.x = current_x + 20
       

class Ball(pg.sprite.Sprite):

    def __init__(self, color, width, height, screen):

        pg.sprite.Sprite.__init__(self)

        self.hitting_ball = False

        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        start_x = round(screen.width * .5, -1)
        start_y = round(screen.height * .5, -1)
        self.rect.center = (start_x, start_y)

        self.speed_x = 10
        self.speed_y = -10

        self.width_of_screen = screen.width
        self.length_of_screen = screen.height
        

    def move(self):
        current_x = self.rect.x
        current_y = self.rect.y

        if current_x <= 0 or current_x >= self.width_of_screen: 
            self.speed_x = -self.speed_x
            self.hitting_ball = False
            
        if current_y <= 0:
            self.speed_y = -self.speed_y
            self.hitting_ball = False
                    
        self.rect.y = current_y + self.speed_y
        self.rect.x = current_x + self.speed_x

    def check_alive(self):
        return self.rect.centery < self.length_of_screen
    
    def bounce_off_paddle(self):
        self.speed_y = -self.speed_y
        self.hitting_ball = True

class GameScreen:

    def __init__(self, clock, tick):
        self.screen_object = pg.display.set_mode((0,0), pg.FULLSCREEN)
        screen_boundary = self.screen_object.get_rect()
        self.width = screen_boundary.width
        self.height = screen_boundary.height
        self.sprites_list = pg.sprite.Group()
        self.tick = tick
        self.clock = clock

    def add_sprite(self, sprite):
        self.sprites_list.add(sprite)

    def update(self, score):
        self.screen_object.fill(BLACK)
        self.sprites_list.draw(self.screen_object)
        score_font = pg.font.SysFont("Times New Roman", 30)
        label1 = score_font.render("Score "+str(score), 1, (255,255,0))
        self.screen_object.blit(label1, (720,450))
        pg.display.flip()
        self.clock.tick(self.tick)

        
        

def check_collision(ball, paddle):
    # check for collision of ball with paddle
    ball_x = ball.rect.centerx
    ball_right = ball.rect.right
    ball_left = ball.rect.left
    ball_y = ball.rect.y
    paddle_x = paddle.rect.centerx
    paddle_y = paddle.rect.centery
    paddle_left = paddle.rect.left
    paddle_right = paddle.rect.right
    
    print('Ball:', ball_x, ball_y, 'Hitting', ball.hitting_ball, 'Paddle x', paddle_x, 'Paddle center', paddle.rect.center)

    if ball_y >= paddle_y - paddle.height * .5 and ball_y <= paddle_y + paddle.height * .5:
        # ball is at height of paddle so check if hitting paddle
        if ball_right >= paddle_left and ball_left <= paddle_right:
            return True    
    return False

def check_game_quit(event):
    if event.type == pg.KEYDOWN and event.key == pg.K_q:
        return True
    return False

def handle_key_events(event, lkey_down, rkey_down):
    if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
        lkey_down = True

    if event.type == pg.KEYUP and event.key == pg.K_LEFT:
        lkey_down = False 

    if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
        rkey_down = True

    if event.type == pg.KEYUP and event.key == pg.K_RIGHT:
        rkey_down = False
    return lkey_down, rkey_down


def main():
    pg.init()
    clock = pg.time.Clock()
    screen = GameScreen(clock, 40)
    
    ball_width = 15
    ball_height = 15
    ball1 = Ball(WHITE, ball_width, ball_height, screen)

    paddle_width = 110
    paddle_height = 15
    paddle1 = Paddle(WHITE, paddle_width, paddle_height, screen)    
    
    score = 0
    lkey_down = False
    rkey_down = False
    ball_alive = True
    
    screen.add_sprite(paddle1)
    screen.add_sprite(ball1)
    
    while ball_alive:
 
        ball_alive = ball1.check_alive()
        if ball_alive == False:
            print('Game over')
            return
        
        for event in pg.event.get():
            if check_game_quit(event):
                return
            
            lkey_down, rkey_down = handle_key_events(event, lkey_down, rkey_down)

        if check_collision(ball1, paddle1) == True:
            score += 1
            ball1.bounce_off_paddle()
            
        ball1.move()
        paddle1.move(lkey_down, rkey_down)
        screen.update(score)
        
main()