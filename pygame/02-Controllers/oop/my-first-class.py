import pygame
# -- Global Constants



# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
# -- My Classes

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        keys = pygame.key.get_pressed()
    ## - the up key or down key has been pressed
        if keys[pygame.K_UP]:
            self.y = self.y - 1
        elif keys[pygame.K_DOWN]:
            self.y = self.y + 1
        #End if

    def draw(self):
    # Make the mouse pointer appear in the middle of the square...
        pygame.draw.rect(screen, RED, (self.x, self.y, 25, 25))

        



        


# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First Flipbook")

blocks = []
game_over = False
blocks.append(Ball(size[0]//2,size[1]//2))
blocks.append(Ball(50,50))


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event

            
            
    # -- Game logic goes after this comment
    for block in blocks:
        block.move()
        
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    for block in blocks:
        block.draw()


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
