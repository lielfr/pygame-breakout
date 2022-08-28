import pygame
import sys
from breakout_game.const import Const


class Game:

    def __int__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Const.screen_width, Const.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_image = pygame.image.load('assets/bg.jpg')

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.quit():
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_image)
