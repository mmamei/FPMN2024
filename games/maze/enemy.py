import pygame

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
        