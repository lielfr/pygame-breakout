#!/usr/bin/env python
# import pygame
# import random

# from pygame.sprite import AbstractGroup
from breakout_game import Game
# SCREENRECT = pygame.Rect(0, 0, 640, 480)
# bg_image = pygame.image.load('assets/bg.jpg')

# def loop(screen, bat):
#     screen.blit(bg_image, (0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             return False
#     bat.update()
#     bat.draw(screen)
#
#     pygame.display.update()
#     return True


# class MySprite(pygame.sprite.Sprite):
#     def draw(self, surface):
#         surface.blit(self.image, self.rect)


# class Brick(MySprite):
#     NUM_BRICKS = 8
#
#     def __init__(self, *groups: AbstractGroup) -> None:
#         super().__init__(*groups)
#         image_num = random.randint(1, self.NUM_BRICKS)
#         self.image = pygame.image.load(f'brick-{image_num}.png')

# def init_stage():
#     pygame.display.set_caption('Awesome Breakout Game!')
#     screen = pygame.display.set_mode((640, 480))
#     screen.blit(bg_image, (0, 0))
#     pygame.display.flip()
#     bat = Bat()
#     return screen, bat

# def main():


    # while loop(screen, bat):
    #     pass


if __name__ == '__main__':
    game = Game()
    while True:
        game.handle_events()
        game.update()
        game.draw()
