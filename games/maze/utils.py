import requests
from constants import *
from wall import Wall
import pygame
from pygame.locals import *

def generate_maze(n_row, n_cols):
    wall_sprites = pygame.sprite.Group()
    maze = requests.post('http://www.delorie.com/game-room/mazes/genmaze.cgi',
                          data={'cols': n_cols, 'rows': n_row, 'type': 'text'})
    y = 0
    for l in maze.text.splitlines():
          if not l.startswith('<'):
            x = 0
            for c in l:
                if c != ' ':
                        w = Wall(x, y, WALL_DX, WALL_DY)
                        wall_sprites.add(w)
                x += WALL_DX
            y +=WALL_DY
    return wall_sprites


def check_main_events(events, state):
    global running,gameon
     # for loop through the event queue
    for event in events:
    # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                state['running'] = False
            if event.key == K_1:
                state['gameon'] = True
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            state['running'] = False

