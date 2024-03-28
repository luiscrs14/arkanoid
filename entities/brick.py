import pygame
import random

BRICK_WIDTH: int = 50
BRICK_HEIGHT: int = 20
ROW_GAP_SIZE: int = 10


class Brick:
    def __init__(self, x, y, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.width = BRICK_WIDTH
        self.height = BRICK_HEIGHT
        self.color = color
        self.is_visible = True

    def render(self, screen):
        if self.is_visible:
            pygame.draw.rect(
                screen, self.color, (self.x, self.y, self.width, self.height)
            )

    def hit(self):
        self.is_visible = False


def build_bricks(screen: pygame.Surface, rows: int):
    """
    Fills n rows of bricks on the screen
    uses brick width to calculate brick positions
    """
    bricks = []
    for row in range(rows):
        for i in range(screen.get_width() // BRICK_WIDTH):
            brick = Brick(i * 50, row * (20 + ROW_GAP_SIZE), _random_color())
            bricks.append(brick)

    return bricks


def _random_color():
    return (random.random() * 255, random.random() * 255, random.random() * 255)
