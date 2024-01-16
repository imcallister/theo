"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""

# import basic pygame modules
import pygame as pg
import random
 
SCREENRECT = pg.Rect(0, 0, 700, 400)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

class Block(pg.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        pg.sprite.Sprite.__init__(self)
 
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 

def main():
    # Initialize Pygame
    pg.init()

    clock = pg.time.Clock()
    
    # Set the display mode
    screen = pg.display.set_mode(SCREENRECT.size)
    
    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    block_list = pg.sprite.Group()
    
    # This is a list of every sprite. 
    # All blocks and the player block as well.
    all_sprites_list = pg.sprite.Group()
    
    for i in range(50):
        # This represents a block
        block = Block(GREEN, 10, 7.5)
    
        # Set a random location for the block
        block.rect.x = random.randrange(SCREENRECT.size[0])
        block.rect.y = random.randrange(SCREENRECT.size[1])
    
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
    
    # Create a RED player block
    player = Block(RED, 20, 15)
    all_sprites_list.add(player)
    
    alive = True
    score = 0
    
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
        screen.fill(WHITE)
    
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pg.mouse.get_pos()
    
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        player.rect.x = pos[0]
        player.rect.y = pos[1]
    
        # See if the player block has collided with anything.
        blocks_hit_list = pg.sprite.spritecollide(player, block_list, True)
    
        # Check the list of collisions.
        for block in blocks_hit_list:
            score += 1
            print(f'Score is: {score}')
    
        # Draw all the spites
        all_sprites_list.draw(screen)
        # Go ahead and update the screen with what we've drawn.
        pg.display.flip()
        
        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        clock.tick(40)
    
# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()

