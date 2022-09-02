#!/usr/bin/env python
# import pygame
# import random

from breakout_game import Game
if __name__ == '__main__':
    game = Game()

    while True:
        game.handle_events()
        game.draw()
        game.update()
