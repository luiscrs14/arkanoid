import pygame

from entities.brick import Brick
from entities.player import Player

# Collision may not be evaluated immediately, so give some leeway
COLLISION_COMPENSATION = 10


class Ball(object):
    def __init__(self, x, y, diameter=20, speed=[4, -4]):
        self.surface = pygame.display.get_surface()
        self.color = "blue"
        self.x = x
        self.y = y
        self.speed = speed
        self.diameter = diameter
        self.ball_center = pygame.Vector2(self.x, self.y)
        self.ball = pygame.draw.circle(
            self.surface, self.color, self.ball_center, self.diameter // 2
        )

    def draw(self):
        self.ball_center = pygame.Vector2(self.x, self.y)
        pygame.draw.circle(
            self.surface, self.color, self.ball.center, self.diameter // 2
        )

    def move(self):
        self.ball = self.ball.move(self.speed)

        if self.ball.left < 0 or self.ball.right > self.surface.get_width():
            self.speed[0] = -self.speed[0]
        if self.ball.top < 0 or self.ball.bottom > self.surface.get_height():
            self.speed[1] = -self.speed[1]

    def manage_brick_collisions(self, bricks: list[Brick]):
        hit = self.ball.collidelist([brick.brick_rect for brick in bricks])
        if hit != -1:
            hit_location = self._get_brick_hit_location(bricks[hit])
            if hit_location == "VERTICAL":
                self.speed[1] = -self.speed[1]
            elif hit_location == "HORIZONTAL":
                self.speed[0] = -self.speed[0]
            bricks.pop(hit)

    def manage_player_collisions(self, player: Player):
        # TODO differentiate location of hit
        if self.ball.colliderect(player.player):
            hit_location = self._get_player_hit_location(player)
            if hit_location == "VERTICAL":
                self.speed[1] = -self.speed[1]
            elif hit_location == "HORIZONTAL":
                self.speed[0] = -self.speed[0]

    def _get_brick_hit_location(self, brick: Brick):
        print(f"ball coords {self.ball.x, self.ball.y}")
        print(f"hit {brick} brick. Coords: {brick.x, brick.y}")
        if self.ball.x + self.diameter < brick.x + COLLISION_COMPENSATION:
            print("LEFT")
            return "HORIZONTAL"
        if self.ball.x > brick.x + brick.width - COLLISION_COMPENSATION:
            print("RIGHT")
            return "HORIZONTAL"
        if self.ball.y + self.diameter < brick.y + COLLISION_COMPENSATION:
            print("UP")
            return "VERTICAL"
        if self.ball.y >= brick.y + brick.height - COLLISION_COMPENSATION:
            print("DOWN")
            return "VERTICAL"
        raise ValueError("No hit location found")

    def _get_player_hit_location(self, player: Player):
        print(f"ball coords {self.ball.x, self.ball.y}")
        print(f"hit player. Coords: {player.x, player.y}")
        if self.ball.x + self.diameter < player.x + COLLISION_COMPENSATION:
            print("LEFT")
            return "HORIZONTAL"
        if self.ball.x > player.x + player.width - COLLISION_COMPENSATION:
            print("RIGHT")
            return "HORIZONTAL"
        if self.ball.y + self.diameter < player.y + COLLISION_COMPENSATION:
            print("UP")
            return "VERTICAL"
        if self.ball.y >= player.y + player.height - COLLISION_COMPENSATION:
            raise ValueError("Hits should never happen downwards!")
        raise ValueError("No hit location found")
