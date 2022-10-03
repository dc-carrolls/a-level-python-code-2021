import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First Flipbook")

game_over = False

# Sun starting position
circle_x_pos = -40
circle_y_pos = 100

# coefficient's for quadratic equation of sun movement
##a =  0.000976563
##b = -0.625
##c =  150
a=-0.000488281
b=0.3125
c=100






### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment


    circle_x_pos = circle_x_pos + 1
    if circle_x_pos > 680:
        circle_x_pos = -40
    #circle_y_pos = -1 * int(a * circle_x_pos**2 + b * circle_x_pos - c)
        circle_y_pos = -1 * int(((-1 * sun_x**2) // 2048) + ((5 * sun_x) // 16) - 100)        
        # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (circle_x_pos,circle_y_pos),40,0)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
