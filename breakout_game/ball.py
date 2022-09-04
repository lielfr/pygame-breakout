import pygame
from random import randint
from breakout_game import Const


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.pos_x = Const.screen_width / 2
        self.pos_y = Const.screen_height / 2
        self.image = pygame.image.load('assets/ball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.velocity = [randint(2, 4), randint(-4, 4)]
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        # collision detection
        if self.pos_x <= 9 or self.pos_x >= Const.screen_width - 9:
            self.velocity[0] = -self.velocity[0]
        if self.pos_y <= 9:
            self.velocity[1] = -self.velocity[1]

        # make sure we don't get stuck in a vertical or horizontal position.
        if self.velocity[0] == 0:
            self.velocity[0] += 1
        if self.velocity[1] == 0:
            self.velocity[1] += 1

        # applying the velocity to the position.
        self.pos_x += self.velocity[0]
        self.pos_y += self.velocity[1]

        self.rect.center = (self.pos_x, self.pos_y)

    def reset(self):
        self.pos_x = Const.screen_width / 2
        self.pos_y = Const.screen_height / 2
        self.velocity = [randint(2, 4), randint(-4, 4)]
        self.rect.center = (self.pos_x, self.pos_y)

    '''
    Checks if the ball went off-screen
    '''
    def is_off_screen(self):
        if self.pos_y > Const.screen_height:
            return True
        return False

    '''
    collision detection with the bat
    :pram bat: the bat to collide with.
    '''
    def hit_bat(self, bat):
        if self.rect.colliderect(bat.rect):
            if abs(self.rect.bottom-bat.rect.top) < Const.collision_threshold and self.velocity[1] > 0:
                self.velocity[1] = -self.velocity[1]
                self.velocity[0] += bat.bat_direction

                # limiting the speed movement of the ball.
                if self.velocity[0] > abs(Const.max_ball_speed):
                    temp = self.velocity[0]
                    self.velocity[0] = Const.max_ball_speed
                    if temp < 0:
                        self.velocity[0] *= -1

            else:
                # if we don't hit the top of the bat (we are hitting the side of the bat)
                self.velocity[0] = -self.velocity[0]
