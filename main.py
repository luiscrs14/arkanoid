# Example file showing a circle moving on screen
import pygame

from entities.ball import Ball
from entities.brick import build_bricks
from entities.player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()
running = True
dt = 0

player_radius = 40
speed = [2, -2]

player = Player(
    screen.get_width() / 2 - 40, screen.get_height() - player_radius - 10, 80, 40
)
ball = Ball(
    screen.get_width() / 2, screen.get_height() - player_radius * 3, 20, 20, speed
)
# ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - player_radius * 3)
bricks = None
# ballrect = pygame.draw.circle(screen, "blue", ball_pos, 20)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")

    player.draw_player()
    ball.draw()

    if not bricks:
        bricks = build_bricks(screen, 3)
    for brick in bricks:
        brick.render(screen)

    # ballrect = ballrect.move(speed)
    # ballrect = pygame.draw.circle(screen, "blue", ballrect.center, 20)
    # if ballrect.left < 0 or ballrect.right > screen.get_width():
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > screen.get_height():
    #     speed[1] = -speed[1]

    ball.move()
    player.move(dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
