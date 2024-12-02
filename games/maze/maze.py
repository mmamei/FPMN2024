import requests
import pygame
from pygame.locals import *
import random
from pygame import font
from player import Player
from enemy import Enemy
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
pygame.time.set_timer(ADDENEMY, 5000)
# Our main loop!
while state['running']:
    
    events  = pygame.event.get()
    check_main_events(events, state)

    for event in events:
        if event.type == KEYDOWN and event.key == K_SPACE:
            player.fire()
        if state['gameon'] and event.type == ADDENEMY:
            new_enemy = Enemy(ENEMY_DX,ENEMY_DY, all_sprites, missiles_sprites, wall_sprites)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    

    screen.fill([0, 0, 0])
    if not state['gameon']:
        surf = font.Font(None,36).render('Premi 1 per iniziare...', True, [255,255,255])
        screen.blit(surf, (SCREEN_WIDTH/2-surf.get_width()/2, SCREEN_HEIGHT/2))
        if state['maze'] == False:
            state['maze'] = True
            enemies = pygame.sprite.Group()
            all_sprites = pygame.sprite.Group()
            missiles_sprites = pygame.sprite.Group()
            wall_sprites = generate_maze(N_ROWS,N_COLS)
            player = Player(PLAYER_DX/2+1, WALL_DY + PLAYER_DY/2+1, all_sprites, missiles_sprites, wall_sprites)
            all_sprites.add(wall_sprites,player)
    if state['gameon']:
        player.update(pygame.key.get_pressed())
        for m in missiles_sprites:
            m.update()
        for e in enemies:
            e.update()
        for x in all_sprites:
            screen.blit(x.surf, x.rect)
    pygame.display.flip()
    clock.tick(200)



