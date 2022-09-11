import pygame
import sys


from breakout_game.const import Const
from breakout_game.Bat import Bat
from breakout_game.ball import Ball
from breakout_game.bricks_manager import BricksManager


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Awesome Breakout Game!')
        self.screen = pygame.display.set_mode((Const.screen_width, Const.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("black")
        self.bat = Bat()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bat, self.ball)

        self.bricks_manager = BricksManager(self.all_sprites)

    def handle_events(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.bat.pos_x - Const.half_bat_size - Const.BAT_SPEED >= 0:
            self.bat.move(Const.LEFT)
        if pressed_keys[pygame.K_RIGHT] and self.bat.pos_x + Const.half_bat_size + Const.BAT_SPEED <= Const.screen_width:
            self.bat.move(Const.RIGHT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        # if the ball is off-screen you lose life, ahd the ball resets to the middle of the filed.
        if self.ball.is_off_screen():
            self.bat.die()
            self.ball.reset()

        # Hitting the bat
        self.ball.hit_bat(self.bat)

        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(Const.FRAME_RATE)

    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)
