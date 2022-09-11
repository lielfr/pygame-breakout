import pygame
from breakout_game import Const
import os.path

bricks = [
    'brick-0.png',
    'brick-1.png',
    'brick-2.png',
    'brick-3.png',
    'brick-4.png',
    'brick-5.png',
    'brick-6.png',
    'brick-7.png'
]



class Brick(pygame.sprite.Sprite):
    def __init__(self, row, col):
        super().__init__()
        self.pos_x = Const.brick_pad_h + (col * Const.brick_size[0]) + Const.brick_size[0]/2
        self.pos_y = Const.brick_pad_v + (row * Const.brick_size[1]) + Const.brick_size[1]/2
        self.image = pygame.image.load(os.path.join('assets', bricks[row]))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
