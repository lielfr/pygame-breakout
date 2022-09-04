import pygame


class Const:
    screen_height = 480
    screen_width = 640
    SCREENRECT = pygame.Rect(0, 0, screen_width, screen_height)
    INITIAL_LIVES = 3
    BAT_SPEED = 5
    FRAME_RATE = 120
    RIGHT = 1
    LEFT = -1
    collision_threshold = 12
    max_ball_speed = 6
    ball_size = 18
    bat_size = 128
    bat_height_from_floor = 20
    brick_hits_before_destroy = 2
    brick_size = (63, 16)
    brick_pad = 3
    top_left = (0, 0)
    num_brick_images = 8

    # calculated sizes
    half_ball_size = ball_size / 2
    half_bat_size = bat_size / 2
