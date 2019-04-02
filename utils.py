import config
import pygame


def spot(coords):
    x, y = coords
    x, y = x % config.COLUMNS, y % config.ROWS
    return x * config.DOT_SIZE, y * config.DOT_SIZE


def generate_walls(mode):
    wall_spots = []
    if mode == 0:
        pass
    if mode == 1:
        for i in range(config.ROWS):
            if abs(i - (config.ROWS + 1) / 2) > 3:
                wall_spots.append((0, i))
                wall_spots.append((config.COLUMNS - 1, i))
        for i in range(config.COLUMNS):
            if abs(i - (config.COLUMNS + 1) / 2) >= 3:
                wall_spots.append((i, 0))
                wall_spots.append((i, config.ROWS - 1))
    if mode == 2:
        for i in range(config.ROWS):
            wall_spots.append((0, i))
            wall_spots.append((config.COLUMNS - 1, i))
        for i in range(config.COLUMNS):
            wall_spots.append((i, 0))
            wall_spots.append((i, config.ROWS - 1))
    return wall_spots


def draw_food(screen, food_spot, food_colour):
    pygame.draw.rect(screen, food_colour, [food_spot[0], food_spot[1], config.DOT_SIZE, config.DOT_SIZE])


def draw_snake(screen, body_spots, head_spot):
    for x, y in body_spots:
        pygame.draw.rect(screen, config.LGREEN, [x, y, config.DOT_SIZE, config.DOT_SIZE])
    pygame.draw.rect(screen, config.DGREEN, [head_spot[0], head_spot[1], config.DOT_SIZE, config.DOT_SIZE])


def draw_walls(screen, wall_spots):
    for x, y in wall_spots:
        pygame.draw.rect(screen, config.CYAN, [x, y, config.DOT_SIZE, config.DOT_SIZE])


def draw_score(screen, score, font):
    scoreboard = font.render(str(score), True, config.PURPLE)
    screen.blit(scoreboard, (config.DOT_SIZE, config.DOT_SIZE))


def draw(screen, background, food_spot, food_colour, body_spots, head_spot, wall_spots, score, font):
    screen.fill(background)
    draw_food(screen, food_spot, food_colour)
    draw_snake(screen, body_spots, head_spot)
    draw_walls(screen, wall_spots)
    draw_score(screen, score, font)
