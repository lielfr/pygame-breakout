import pygame
from breakout_game import Const
from breakout_game.brick import Brick


class BricksManager:

    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()

        for row in range(Const.brick_rows):
            for col in range(Const.brick_cols):
                brick = Brick(row, col)
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)


    def check_collisions(self, ball):
        collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in collision_list:
            ball.bounce_of_brick()
            brick.kill()
