import pygame
from random import randint
from breakout_game import Const


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.pox_x = Const.screen_width / 2
        self.pos_y = Const.screen_height / 2
        self.image = pygame.image.load('assets/ball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.velocity = [randint(2, 4), randint(-4, 4)]
        self.rect.center = (self.pox_x, self.pos_y)


