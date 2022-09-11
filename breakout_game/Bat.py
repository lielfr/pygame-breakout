import pygame
from breakout_game.const import Const
import os.path


class Bat(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(os.path.join('assets', 'bat.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos_y = Const.screen_height
        self.pos_y -= Const.bat_height_from_floor    # lift the bat 20 pixels up the window/
        self.pos_x = Const.screen_width / 2     # locating the bat at the middle of the window
        self.rect.center = (self.pos_x, self.pos_y)
        self.bat_direction = 0
        self.live_number = Const.INITIAL_LIVES

    def update(self):
        self.rect.center = (self.pos_x, self.pos_y)

    def reset(self):
        self.live_number = Const.INITIAL_LIVES

    """
    If you get a strike you loose 1 live
    """
    def die(self):
        self.live_number -= 1

    """
    The function that moves the bat
    :param direction: The wanted direction for the bat.
    """
    def move(self, direction):
        self.bat_direction = direction
        self.pos_x = self.pos_x + Const.BAT_SPEED * self.bat_direction
