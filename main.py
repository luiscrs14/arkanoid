# Example file showing a circle moving on screen
import pygame

from entities.ball import Ball
from entities.brick import build_bricks
from entities.player import Player
from overlays import render_game_over_overlay

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()
running = True
run_ended = False
dt = 0
player_radius = 40
speed = [3, -3]


def start_game_objects():
    player = Player(
        screen.get_width() / 2 - 40, screen.get_height() - player_radius - 10
    )
    ball = Ball(
        screen.get_width() / 2,
        screen.get_height() - player_radius * 3,
    )
    bricks = None
    return player, ball, bricks


player, ball, bricks = start_game_objects()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")
    if run_ended:
        render_game_over_overlay(screen)
        if pygame.key.get_pressed()[pygame.K_q]:
            running = False
        if pygame.key.get_pressed()[pygame.K_r]:
            player, ball, bricks = start_game_objects()
            run_ended = False
    else:
        player.draw_player()
        ball.draw()

        if not bricks:
            bricks = build_bricks(screen, 3)
        for brick in bricks:
            brick.render(screen)

        ball.move()

        ball.manage_brick_collisions(bricks)
        ball.manage_player_collisions(player)
        player.move(dt)

        if ball.ball.bottom > screen.get_height():
            run_ended = True

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
