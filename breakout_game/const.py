import pygame


class Const:
    screen_height = 520
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
    brick_pad_h = 68 #3
    brick_pad_v = 40
    game_top = 40
    top_left = (0, 0)
    num_brick_images = 8
    font_size_title = 32
    font_size_text = 18
    font_size_score = 10
    score_pad = 5
    score_per_hit = 10


    brick_rows = 7
    brick_cols = 8

    # calculated sizes
    half_ball_size = ball_size / 2
    half_bat_size = bat_size / 2
    max_score = score_per_hit * brick_rows * brick_cols