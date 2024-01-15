import os
main_dir = os.path.split(os.path.abspath(__file__))[0]

# import basic pygame modules
import pygame as pg

SCREENRECT = pg.Rect(0, 0, 1280, 960)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 255, 0)

def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file).convert_alpha()
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    return surface.convert()


class BouncingBall(pg.sprite.Sprite):

    speed = 0

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = load_image("circle_dad.png")
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.rect.center = (640,480)

    def move(self):
        self.rect.move_ip(self.speed, 10)
        self.rect = self.rect.clamp(SCREENRECT)
        

def main():
    # Initialize pygame
    pg.init()
    
    clock = pg.time.Clock()
    
    # Set the display mode
    screen = pg.display.set_mode(SCREENRECT.size, pg.RESIZABLE)
    
    alive = True
    ball = BouncingBall()

    # This is a list of every sprite.
    # All blocks and the player block as well.
    all_sprites_list = pg.sprite.Group()
    all_sprites_list.add(ball)

    background = WHITE

    # -------- Main Program Loop -----------
    while alive:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                return
        

        # Clear the screen
        #screen.fill(GREEN)

        # Draw all the spites
        all_sprites_list.draw(screen)
        # Go ahead and update the screen with what we've drawn.
        pg.display.flip()
        
        ball.move()
        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        clock.tick(40)


# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()