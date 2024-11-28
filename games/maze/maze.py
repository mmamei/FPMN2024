import requests
import pygame
from pygame.locals import *
import random
from pygame import font
from player import Player
from wall import Wall

PLAYER_DX = 40
PLAYER_DY = 40
WALL_DX = 50
WALL_DY = 50
SCREEN_WIDTH = (3*10 + 1)*WALL_DX
SCREEN_HEIGHT = (2*10 + 1)*WALL_DY


num_enemy_killed = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep our main loop running
maze = None
running = True
gameon = False



# Our main loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_1:
                gameon = True
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
    screen.fill([0, 0, 0])
    if not gameon:
        surf = font.Font(None,36).render('Premi 1 per iniziare...', True, [255,255,255])
        screen.blit(surf, (SCREEN_WIDTH/2-surf.get_width()/2, SCREEN_HEIGHT/2))
        if maze == None:
            wall_sprites = pygame.sprite.Group()
            player = Player(PLAYER_DX/2+1, WALL_DY + PLAYER_DY/2+1, SCREEN_WIDTH, SCREEN_HEIGHT, wall_sprites)

            maze = requests.post('http://www.delorie.com/game-room/mazes/genmaze.cgi',
                          data={'cols': '10', 'rows': '10', 'type': 'text'})


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




    if gameon:
        player.update(pygame.key.get_pressed())
        screen.blit(player.surf,player.rect)
        for s in wall_sprites:
            screen.blit(s.surf, s.rect)

        #surf = pygame.Surface((20, 20))
        #surf.fill([0, 255, 0])
        #rect = surf.get_rect()
        #rect.center = [910,580]
        #screen.blit(surf, rect)


    pygame.display.flip()
    clock.tick(200)



