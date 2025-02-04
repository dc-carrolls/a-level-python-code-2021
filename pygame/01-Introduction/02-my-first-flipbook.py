import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
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
circle_x_pos = 400
circle_y_pos = 1000
y_dir = -1
x_dir = 1
x_speed = 10
y_speed = 10
gravity = 1


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment
    if circle_x_pos > 3200:
        y_dir = 1
        gravity = -1
    elif circle_x_pos > 6400:
        circle_x_pos = 40
        circle_y_pos = 100
        y_dir = -1

    circle_x_pos = circle_x_pos + x_dir * x_speed
    circle_y_pos = circle_y_pos + y_dir * y_speed
    if circle_x_pos % 200 == 0:
        y_speed = y_speed - gravity

        # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (circle_x_pos//10,circle_y_pos//10),40,0)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
