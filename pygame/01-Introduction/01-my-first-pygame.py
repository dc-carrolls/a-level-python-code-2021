import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First PyGame")

# -- Screen background is BLACK
screen.fill (BLACK)

# -- Draw here
pygame.draw.rect(screen, BLUE, (220,165,200,150))
pygame.draw.circle(screen, YELLOW, (40,100),40,0)

# -- flip display to reveal new position of objects
pygame.display.flip()
