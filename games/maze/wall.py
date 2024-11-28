import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,dx,dy):
        super().__init__()
        image = pygame.image.load('games/images/wall.png')
        image = pygame.transform.scale(image, (dx,dy))
        self.surf = image.convert()
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.top = y
