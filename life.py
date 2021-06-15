import pygame
import numpy
 
# DEFINE CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (75,0,130)
CELLWIDTH = CELLHEIGHT = 5
MARGIN = 0
SCREENWIDTH = 1440 + MARGIN
SCREENHEIGHT = 900 + MARGIN
nXcells = int(SCREENWIDTH / (CELLWIDTH + MARGIN))
nYcells = int(SCREENHEIGHT / (CELLHEIGHT + MARGIN))

# CREATE 2D GRIDS FOR OUTPUT AND STATE
nextState = [[0 for x in range(nXcells)] for y in range(nYcells)]
currentState = [[0 for x in range(nXcells)] for y in range(nYcells)]

#Randomly POPULATE
for i, row in enumerate(currentState):
   currentState[i] = numpy.random.choice([0,1], size=len(row), p=[.9,.1])

#Pygame initialization
pygame.init()
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")

#Loop condition
done = False

# Get value of a cell - toroidal
def checkCell(x , y):
    x = x % nXcells
    y = y % nYcells
    return currentState[y][x]

def getNeighbors(x, y):
    return  checkCell(x - 1 , y - 1) + checkCell(x , y - 1) + checkCell(x + 1 , y - 1) \
            +checkCell(x - 1 , y)      +           0          + checkCell(x + 1 , y) \
            +checkCell(x - 1 , y + 1)  + checkCell(x , y + 1)  + checkCell(x + 1 , y + 1)


clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y, row in enumerate(currentState):
        for x, col in enumerate(row):
            color = PURPLE
            value = checkCell(x , y)
            nNeighbors = getNeighbors(x , y)
            if value == 1:
                color = GREEN
                if nNeighbors == 2 or nNeighbors == 3:
                    nextState[y][x] = 1
                else: #underpopulation and overpopulation here
                    nextState[y][x] = 0
            else:
                if nNeighbors == 3:
                    nextState[y][x] = 1
            pygame.draw.rect(screen, color, [(MARGIN + CELLWIDTH) * x + MARGIN, 
                                            (MARGIN + CELLHEIGHT) * y + MARGIN,
                                            CELLWIDTH, CELLHEIGHT])
    
    currentState = nextState
    nextState = [[0 for x in range(nXcells)] for y in range(nYcells)]

    clock.tick(144) # fps cap
    pygame.display.flip()


pygame.quit()