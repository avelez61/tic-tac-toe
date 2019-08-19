# PYTHON VERSION: 3.7.0
# PROGRAMMER:     Alex Velez
# STARTED:        8/15/2019
# LAST MODIFIED:  8/16/2019

import pygame
from grid import Grid
pygame.init()

# Window Setup
WINDOW_SIZE = (192, 192)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('TIC TAC TOE')
running = True

# Texture Setup
grid_texture = pygame.image.load('grid.png')
x_texture = pygame.image.load('char_x.png')
o_texture = pygame.image.load('char_o.png')

# Grid Setup
grid = Grid()

# GAME FUNCTION(S)
# SIZE DEPENDANT FUNCTION
def draw():
    window.blit(grid_texture, (0, 0))
    for i in range(3):
        for j in range(3):
            if grid.grid[i][j] == grid.CHAR_X:
                window.blit(x_texture, (j * 64, i * 64))
            elif grid.grid[i][j] == grid.CHAR_O:
                window.blit(o_texture, (j * 64, i * 64))
    pygame.display.update()

# GAME LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      
        # Keep in mind when the mouse is held down it triggers below            
        if pygame.mouse.get_pressed()[0] and grid.playing:
            move = grid.get_move(pygame.mouse.get_pos())
            if grid.space_empty(move):
                grid.make_move(move)
                #Don't know if it's better to set grid.playing within
                grid.playing = not grid.check_end(move[0], move[1])
                grid.change_turn()  

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        grid.reset()

    draw()

pygame.quit()
