import pygame
from breakout_game.const import Const


class Bat(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('assets/bat.png').convert_alpha()
        self.pos_x, self.pos_y = Const.SCREENRECT.midbottom
        self.pos_y -= 20
        self.rect.center = (self.pos_x, self.pos_y)
        self.bat_direction = 0
        self.live_number = Const.live_num

    def update(self):
        # pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[pygame.K_LEFT]:
        #     self.rect.move_ip(-1, 0)
        # if pressed_keys[pygame.K_RIGHT]:
        #     self.rect.move_ip(1, 0)
        # self.rect.clamp_ip(Const.SCREENRECT)
        if self.pos_x < 64:
            self.pos_x = 64
        if self.pos_x > Const.screen_width - 64:
            self.pos_x = Const.screen_width - 64
        self.rect.center = (self.pos_x, self.pos_y)
