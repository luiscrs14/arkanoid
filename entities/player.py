import pygame


class Player(object):
    def __init__(self, x, y, width, height):
        self.surface = pygame.display.get_surface()
        self.color = "red"
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_player(self):
        self.player = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.player)

    def move(self, dt):
        # get current state of the keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.x > self.width - self.width:
                self.x -= 300 * dt
        if keys[pygame.K_d]:
            if self.x < self.surface.get_width() - self.width:
                self.x += 300 * dt
