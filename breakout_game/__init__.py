import pygame
import sys
from breakout_game.const import Const
from breakout_game.Bat import Bat


class Game:

    def __int__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Const.screen_width, Const.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("black")
        self.bat = Bat()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bat)

    def handle_events(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.bat.move_left()
        elif key[pygame.K_RIGHT]:
            self.bat.move_right()

        for event in pygame.event.get():
            if event.type == pygame.quit():
                pygame.quit()
                sys.exit()

    def update(self):
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(Const.FRAME_RATE)

    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)
