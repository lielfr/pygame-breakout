#!/usr/bin/env python
import pygame
import random

SCREENRECT = pygame.Rect(0, 0, 640, 480)
bg_image = pygame.image.load('bg.jpg')

def loop(screen, bat):
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    bat.update()
    bat.draw(screen)

    pygame.display.update()
    return True

class MySprite(pygame.sprite.Sprite):
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Bat(MySprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('bat.png')
        pos_x, pos_y = SCREENRECT.midbottom
        pos_y -= 10
        self.rect = self.image.get_rect(midbottom=(pos_x, pos_y))
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        self.rect.clamp_ip(SCREENRECT)

class Brick(MySprite):
    NUM_BRICKS = 8
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        image_num = random.randint(1, self.NUM_BRICKS)
        self.image = pygame.image.load(f'brick-{image_num}.png')

def initStage():
    pygame.display.set_caption('Awesome Breakout Game!')
    screen = pygame.display.set_mode((640, 480))
    screen.blit(bg_image, (0, 0))
    pygame.display.flip()
    bat = Bat()
    return screen, bat

def main():
    pygame.init()
    screen, bat = initStage()
    while loop(screen, bat):
        pass

if __name__ == '__main__':
    main()