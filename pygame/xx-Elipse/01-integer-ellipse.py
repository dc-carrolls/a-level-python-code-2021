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
circle_x_pos = -400
circle_y_pos = 2000
y_dir = -1
x_dir = 1
x_speed = 10
y_speed = 10
gravity = 1


class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, x_pos, y_pos):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([2, 2])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos




ellipse_grp = pygame.sprite.Group()
 



def PlotEllipse(CX, CY, XRadius, YRadius, ellipse_grp ):
    TwoASquare = 2*XRadius*XRadius
    TwoBSquare = 2*YRadius*YRadius
    X = XRadius
    Y = 0
    XChange = YRadius*YRadius*(1-2*XRadius)
    YChange = XRadius*XRadius
    EllipseError = 0
    StoppingX = TwoBSquare*XRadius
    StoppingY = 0

    while ( StoppingX >= StoppingY ): 
        Plot4EllipsePoints(CX,CY,X,Y, ellipse_grp)
        Y+=1
        StoppingY += TwoASquare
        EllipseError += YChange
        YChange +=TwoASquare
        if ((2*EllipseError + XChange) > 0 ):
            X-=1
            StoppingX -= TwoBSquare
            EllipseError += XChange
            XChange += TwoBSquare
# 1st point set is done; start the 2nd set of points }
    X = 0
    Y = YRadius
    XChange = YRadius*YRadius
    YChange = XRadius*XRadius*(1-2*YRadius)
    EllipseError = 0
    StoppingX = 0
    StoppingY = TwoASquare*YRadius
    while ( StoppingX <= StoppingY ): # 2nd set of points, y < 1
        Plot4EllipsePoints(CX, CY,X,Y, ellipse_grp) 
        X += 1;
        StoppingX += TwoBSquare
        EllipseError+= XChange
        XChange += TwoBSquare
        if ((2*EllipseError + YChange) > 0 ):
            Y-=1
            StoppingY -= TwoASquare
            EllipseError += YChange
            YChange+=TwoASquare

# end procedure PlotEllipse

def Plot4EllipsePoints(xc, yc, x,y, ellipse_grp):
    my_block = Block(RED, xc+x, yc+y)
    ellipse_grp.add(my_block)
    my_block = Block(RED, xc-x, yc+y)
    ellipse_grp.add(my_block)
    my_block = Block(RED, xc+x, yc-y)
    ellipse_grp.add(my_block)
    my_block = Block(RED, xc-x, yc-y)
    ellipse_grp.add(my_block)

# end procedure Plot4EllipsePoints

PlotEllipse(200, 200, 150, 100, ellipse_grp )

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
    if circle_x_pos > 6800:
        circle_x_pos = -400
        circle_y_pos = 2000
        y_dir = -1
        x_dir = 1
        x_speed = 10
        y_speed = 10
        gravity = 1

    circle_x_pos = circle_x_pos + x_dir * x_speed
    circle_y_pos = circle_y_pos + y_dir * y_speed
    if circle_x_pos % 400 == 0:
        print(circle_x_pos)
        y_speed = y_speed - gravity

        # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (circle_x_pos//10,circle_y_pos//10),40,0)
    ellipse_grp.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
