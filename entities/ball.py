import pygame


class Ball(object):
    def __init__(self, x, y, width, height, speed):
        self.surface = pygame.display.get_surface()
        self.color = "blue"
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.ball_center = pygame.Vector2(self.x, self.y)
        self.ball = pygame.draw.circle(
            self.surface, self.color, self.ball_center, self.width // 2
        )

    def draw(self):
        self.ball_center = pygame.Vector2(self.x, self.y)
        pygame.draw.circle(self.surface, self.color, self.ball.center, self.width // 2)

    def move(self):
        self.ball = self.ball.move(self.speed)

        if self.ball.left < 0 or self.ball.right > self.surface.get_width():
            self.speed[0] = -self.speed[0]
        if self.ball.top < 0 or self.ball.bottom > self.surface.get_height():
            self.speed[1] = -self.speed[1]
