import pygame, bfs_maze, time
black = ( 0, 0, 0)
white = ( 255, 255, 255)
start = ( 0, 255, 0)
red = ( 255, 0, 0)
pth = (213,220,5)

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Test')
gameDisplay.fill((0,0,255))

tbox = pygame.makeTextBox(10,80,300,0,"Enter text: ")
pygame.showTextBox(tbox)

crashed = False
def drawTable():
    margin = 1
    grid = bfs_maze.Maze(10)
    grid.solveMaze()
    grid.replaceMaze(grid.path)
    colour = {'O' : start, 'X' : red, '#': black, ' ': white, '+' : pth}
    width = 10
    height = 10
    for row in range(grid.size):
        for column in range(grid.size):
            time.sleep(0.01)
            pygame.draw.rect(gameDisplay, colour[grid.replaced[column][row]],[(margin+width)*column+margin, (margin+height)*row+margin, width, height])
            pygame.display.update()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawTable()




