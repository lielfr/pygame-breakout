import pygame
import sys
import os.path


from breakout_game.const import Const
from breakout_game.Bat import Bat
from breakout_game.ball import Ball
from breakout_game.bricks_manager import BricksManager


class Game:

    def init_sprites(self):
        self.bat = Bat()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bat, self.ball)

        self.bricks_manager = BricksManager(self.all_sprites)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Awesome Breakout Game!')
        self.screen = pygame.display.set_mode((Const.screen_width, Const.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("black")
        self.text_color = pygame.Color("orange")
        self.game_over = False

        # linux/macOS: assets/PublicPixel.ttf
        # windows: assets\PublicPixel.ttf
        self.font_title = pygame.font.Font(
            os.path.join('assets', 'PublicPixel.ttf'),
            Const.font_size_title
        )

        self.font_text = pygame.font.Font(
            os.path.join('assets', 'PublicPixel.ttf'),
            Const.font_size_text
        )

        self.font_score_bar = pygame.font.Font(
            os.path.join('assets', 'PublicPixel.ttf'),
            Const.font_size_score
        )

        self.init_sprites()

    def handle_events(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.bat.pos_x - Const.half_bat_size - Const.BAT_SPEED >= 0:
            self.bat.move(Const.LEFT)
        if pressed_keys[pygame.K_RIGHT] and self.bat.pos_x + Const.half_bat_size + Const.BAT_SPEED <= Const.screen_width:
            self.bat.move(Const.RIGHT)
        if pressed_keys[pygame.K_r]:
            self.reset()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        # if the ball is off-screen you lose life, ahd the ball resets to the middle of the filed.
        if self.ball.is_off_screen():
            self.bat.die()
            self.ball.reset()
            if self.bat.live_number <= 0:
                self.game_over = True

        # Hitting the bat
        self.ball.hit_bat(self.bat)
        self.bricks_manager.check_collisions(self.ball)

        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(Const.FRAME_RATE)
    
    def draw_game_over(self):
        title_text = self.font_title.render('GAME OVER', True, self.text_color)
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (Const.screen_width // 2, Const.screen_height // 2 - 20)
        self.screen.blit(title_text, title_text_rect)

        secondary_text = self.font_text.render('Press R to continue', True, self.text_color)
        secondary_text_rect = secondary_text.get_rect()
        secondary_text_rect.center = (Const.screen_width // 2, Const.screen_height // 2 + 30)
        self.screen.blit(secondary_text, secondary_text_rect)
    
    def reset(self):
        self.all_sprites.empty()
        self.init_sprites()
        self.game_over = False


    def draw(self):
        self.screen.fill(self.bg_color)

        if self.game_over:
            self.draw_game_over()
        else:
            self.all_sprites.draw(self.screen)
