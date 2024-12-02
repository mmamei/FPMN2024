import pygame
from pygame.locals import *
from constants import SCREEN_WIDTH

class Missile(pygame.sprite.Sprite):
    def __init__(self,x,y,direction, wall_sprites):
        super().__init__()
        self.image = pygame.image.load('games/images/missile.png')
        self.surf = pygame.transform.rotate(self.image, direction-90)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(x,y))
        self.direction = direction
        self.speed = 5
        self.wall_sprites = wall_sprites

    def update(self):
        if self.direction == 90:
            self.rect.move_ip(self.speed, 0)
        if self.direction == 180:
            self.rect.move_ip(0,-self.speed)
        if self.direction == 0:
            self.rect.move_ip(0, self.speed)
        if self.direction == 270:
            self.rect.move_ip(-self.speed,0)
        if pygame.sprite.spritecollideany(self,self.wall_sprites):
            self.kill()