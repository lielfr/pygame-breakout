import pygame
from breakout_game import Const

bricks = [
    'assets/brick-0.png',
    'assets/brick-1.png',
    'assets/brick-2.png',
    'assets/brick-3.png',
    'assets/brick-4.png',
    'assets/brick-5.png',
    'assets/brick-6.png',
    'assets/brick-7.png'
]



class Brick(pygame.sprite.Sprite):
    def __init__(self, row, col):
        super().__init__()
        self.pos_x = Const.brick_pad_h + (col * Const.brick_size[0]) + Const.brick_size[0]/2
        self.pos_y = Const.brick_pad_v + (row * Const.brick_size[1]) + Const.brick_size[1]/2
        self.image = pygame.image.load(bricks[row])
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
