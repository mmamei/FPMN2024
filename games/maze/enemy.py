import pygame
from constants import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, all_sprites, missiles_sprites, wall_sprites):
        super().__init__()
        self.direction = 270

        self.image = pygame.image.load('games/images/tank2.png')
        self.image = pygame.transform.scale(self.image, (40,40))
        self.surf = pygame.transform.rotate(self.image, self.direction)
        
        self.rect = self.surf.get_rect()
        self.rect.center = [start_x, start_y]
        self.v = 3
        self.all_sprites = all_sprites
        self.missiles_sprites = missiles_sprites
        self.wall_sprites = wall_sprites
    def update(self):

        if random.randint(0,100) > 97:
            self.direction = (self.direction + 90 ) % 360

        dx = 0
        dy = 0
        if self.direction == 180:
            dy = -self.v
        if self.direction == 0:
            dy = self.v
            
        if self.direction == 270:
            dx  = -self.v
            
        if self.direction == 90:
            dx = self.v
        self.rect.move_ip(dx,dy)
        self.surf = pygame.transform.rotate(self.image, self.direction)
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = (self.direction + 90 ) % 360
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.direction = (self.direction + 90 ) % 360
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction = (self.direction + 90 ) % 360
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.direction = (self.direction + 90 ) % 360

        if pygame.sprite.spritecollideany(self,self.wall_sprites):
            self.rect.move_ip(-dx,-dy)
            self.direction = (self.direction + 90 ) % 360

        