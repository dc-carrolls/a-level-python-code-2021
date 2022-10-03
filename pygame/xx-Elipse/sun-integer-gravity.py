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

# scaling factor needs to be power of 2 for efficent maths
# I'm scaling up the virtual world as 640x480 does not have
# enough pixels to simulate reality
scale_factor = 16
game_over = False
circle_x_pos = -40 * scale_factor
circle_y_pos = 200 * scale_factor
y_dir = -1
x_dir = 1
x_speed = 1 * scale_factor
y_speed = 1 * scale_factor
gravity = 1  # Acceleration due to gravity


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment

    # Reset sun to beginning 
    if circle_x_pos > 680 * scale_factor:
        circle_x_pos = -40 * scale_factor
        circle_y_pos = 200 * scale_factor
        y_speed = 1 * scale_factor

    # update sun x,y position
    circle_x_pos = circle_x_pos + x_dir * x_speed
    circle_y_pos = circle_y_pos + y_dir * y_speed
    # Change y velocity based on gravity
    if circle_x_pos % (22*scale_factor) == 0:
        y_speed = y_speed - gravity

        # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (circle_x_pos//scale_factor,circle_y_pos//scale_factor),40,0)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
