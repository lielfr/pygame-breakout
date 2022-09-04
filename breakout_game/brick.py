import pygame
from breakout_game import Const

class Brick(pygame.sprite.Sprite):
    def __init__(self, initial_position, img_idx):
        super().__init__()
        self.image = pygame.image.load(f'assets/brick-{img_idx}.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position