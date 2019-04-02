# -*-coding:utf8;-*-
# qpy:pygame
# qpy:qpyapp
# (these were added by the app I used to write it on my mobile phone, QPython)

import pygame
import config
import utils
import random
from collections import deque
import time
import sys


def main():
    pygame.init()
    # Resolution is ignored on Android
    screen = pygame.display.set_mode(config.SCREEN_SIZE)
    # Only one built in font is available on Android
    sans = pygame.font.SysFont(config.FONT, config.FONT_SIZE)
    big_sans = pygame.font.SysFont(config.FONT, config.FONT_SIZE * 3, bold=True)

    screen.fill(config.BLACK)
    clock = pygame.time.Clock()
    pygame.display.flip()

    # movement directions
    # 0 -> right
    # 1 -> up
    # 2 -> left
    # 3 -> down
    direction = 0
    last_direction = direction

    head_pos = [config.COLUMNS / 2, config.ROWS / 2]
    body_pos = deque()
    body_pos.append(tuple(head_pos))
    score = 0

    wall_spotss = utils.generate_walls(config.WALLS)

    food_pos = (random.randrange(config.COLUMNS), random.randrange(config.ROWS))
    food_type = 0
    while True:
        if food_pos in wall_spotss or food_pos in body_pos or food_pos == tuple(head_pos):
            food_pos = (random.randrange(config.COLUMNS), random.randrange(config.ROWS))
        else:
            break
    food_spot = utils.spot(food_pos)

    fps = config.BASE_FPS
    end = 0

    # 0 - continue
    # 1 - game oer
    # 2 - quit

    def game_over():
        utils.draw(screen, config.RED, food_spot, config.FOOD_COLOURS[food_type], body_spots,
                   utils.spot(head_pos), wall_spots, score, big_sans)
        pygame.display.flip()
        time.sleep(2)
        main()

    while not end:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = 2
            if "win" in sys.platform:
                if event.type == pygame.KEYDOWN:
                    if event.key in (100, 275) and last_direction != config.LEFT:
                        direction = config.RIGHT
                    elif event.key in (119, 273) and last_direction != config.DOWN:
                        direction = config.UP
                    elif event.key in (97, 276) and last_direction != config.RIGHT:
                        direction = config.LEFT
                    elif event.key in (115, 274) and last_direction != config.UP:
                        direction = config.DOWN
                    elif event.key == 27:
                        end = 2

            else:
                if event.type == pygame.MOUSEMOTION:
                    x_rel, y_rel = event.rel
                    if abs(x_rel) > abs(y_rel):  # horizontal
                        if x_rel >= 0:  # right
                            if last_direction != config.LEFT:
                                direction = config.RIGHT
                        else:  # left
                            if last_direction != config.RIGHT:
                                direction = config.LEFT
                    else:  # vertical
                        if y_rel <= 0:  # up
                            if last_direction != config.DOWN:
                                direction = config.UP
                        else:  # down
                            if last_direction != config.UP:
                                direction = config.DOWN

        # logic
        if direction == config.RIGHT:
            head_pos[0] += 1
        elif direction == config.UP:
            head_pos[1] -= 1
        elif direction == config.LEFT:
            head_pos[0] -= 1
        elif direction == config.DOWN:
            head_pos[1] += 1
        last_direction = direction

        head_pos[0], head_pos[1] = head_pos[0] % config.COLUMNS, head_pos[1] % config.ROWS

        for part in body_pos:
            if head_pos == list(part):
                end = 1

        for part in wall_spotss:
            if head_pos == list(part):
                end = 1

        body_spots = [utils.spot(pos) for pos in body_pos]
        wall_spots = [utils.spot(pos) for pos in wall_spotss]

        # eating
        if head_pos == list(food_pos):
            food_pos = (random.randrange(config.COLUMNS), random.randrange(config.ROWS))
            while True:
                if food_pos in wall_spotss or food_pos in body_pos or head_pos == list(food_pos):
                    food_pos = (random.randrange(config.COLUMNS), random.randrange(config.ROWS))
                else:
                    break
            food_spot = utils.spot(food_pos)
            body_pos.append(tuple(head_pos))
            score += 1
            if fps < config.MAX_FPS and food_type != config.SLOW:  # speed up the snake
                fps = min(fps * 1.15, fps + 1, config.MAX_FPS)

            if food_type == config.SHORT:  # shorten the snake
                for i in range((len(body_pos) / 2) - 1):
                    body_pos.popleft()

            if food_type == config.SLOW:  # slow down the snake
                fps = max([fps / 2 + 2, config.BASE_FPS])

            r = random.randrange(100)  # determine type food type
            if r > 94:
                food_type = config.SHORT
            elif r > 89:
                food_type = config.SLOW
            else:
                food_type = config.NORMAL

        else:
            body_pos.append(tuple(head_pos))  # move the snake forward
            body_pos.popleft()  # remove the last bit of the snake

        # graphics
        utils.draw(screen, config.BLACK, food_spot, config.FOOD_COLOURS[food_type], body_spots,
                   utils.spot(head_pos), wall_spots, score, sans)

        pygame.display.flip()
        clock.tick(fps)

    if end == 1:  # lost, not exited
        game_over()
    pygame.quit()


if __name__ == "__main__":
    main()
