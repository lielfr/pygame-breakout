import pygame
from breakout_game import Const
from breakout_game.brick import Brick

class BricksManager:

    def init_bricks(self):
        current_y = Const.top_left[1] + Const.brick_pad
        current_img = 0
        current_x = 0 # TODO: Fix this

        while current_y <= self.max_y:
            while current_x <= self.max_x:
                new_brick = Brick((current_x, current_y), current_img)
                self.group.add(new_brick)
                current_x += Const.brick_pad + Const.brick_size[0]
            current_y += Const.brick_pad + Const.brick_size[1]
            current_x = Const.top_left[0] + Const.brick_pad
            current_img = (current_img + 1) % Const.num_brick_images

    def __init__(self) -> None:
        self.max_x = Const.screen_width - Const.brick_size[0] - Const.brick_pad
        self.max_y = Const.screen_height // 3 - Const.brick_size[1] - Const.brick_pad
        self.group = pygame.sprite.Group()
        self.init_bricks()