import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,dx,dy):
        super().__init__()
        self.surf = pygame.Surface((dx,dy))
        self.surf.fill([255,0,0])
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.top = y
