import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, SCREEN_WIDTH, SCREEN_HEIGHT, wall_sprites):
        super().__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill([255,255,255])
        self.rect = self.surf.get_rect()
        self.rect.center = [start_x, start_y]
        self.v = 3
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.wall_sprites = wall_sprites

    def update(self, pressed_keys):

        dx = 0
        dy = 0

        if pressed_keys[K_UP]:
            dy = -self.v
        if pressed_keys[K_DOWN]:
            dy = self.v
        if pressed_keys[K_LEFT]:
            dx  = -self.v
        if pressed_keys[K_RIGHT]:
            dx = self.v
        self.rect.move_ip(dx,dy)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT

        if pygame.sprite.spritecollideany(self,self.wall_sprites):
            self.rect.move_ip(-dx,-dy)

        if self.rect.right > 910 and self.rect.top > 560:
            global gameon
            gameon = False
            global maze
            maze = None
            self.kill()

        print(self.rect.right,self.rect.top)
