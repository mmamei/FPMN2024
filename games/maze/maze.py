import requests
import pygame
from pygame.locals import *
import random
from pygame import font
from player import Player
from wall import Wall
from constants import *
from utils import generate_maze, check_main_events

# Variable to keep our main loop running

state = {
    'maze':False,
    'running':True,
    'gameon':False
}

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Our main loop!
while state['running']:
    check_main_events(state)
    screen.fill([0, 0, 0])
    if not state['gameon']:
        surf = font.Font(None,36).render('Premi 1 per iniziare...', True, [255,255,255])
        screen.blit(surf, (SCREEN_WIDTH/2-surf.get_width()/2, SCREEN_HEIGHT/2))
        if state['maze'] == False:
            state['maze'] = True
            wall_sprites = generate_maze(N_ROWS,N_COLS)
            player = Player(PLAYER_DX/2+1, WALL_DY + PLAYER_DY/2+1, wall_sprites)
    if state['gameon']:
        player.update(pygame.key.get_pressed())
        screen.blit(player.surf,player.rect)
        for s in wall_sprites:
            screen.blit(s.surf, s.rect)
    pygame.display.flip()
    clock.tick(200)



