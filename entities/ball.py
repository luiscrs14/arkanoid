import pygame

from entities.brick import Brick
from entities.intersection_utils.intersection_utils import rect_intersection
from entities.player import Player


class Ball(object):
    def __init__(self, x, y, diameter=20, speed=[6, -6]):
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
        if self.ball.colliderect(player.player):
            hit_location = self._get_player_hit_location(player)
            if hit_location == "VERTICAL":
                self.speed[1] = -self.speed[1]
            elif hit_location == "HORIZONTAL":
                self.speed[0] = -self.speed[0]

    def _get_brick_hit_location(self, brick: Brick):
        intersection = rect_intersection(self.ball, brick.brick_rect)
        print(
            f"hit player. intersection rect : {intersection.x, intersection.y, intersection.width, intersection.height}"
        )

        if intersection.width >= intersection.height:
            return "VERTICAL"
        else:
            return "HORIZONTAL"

    def _get_player_hit_location(self, player: Player):
        intersection = rect_intersection(self.ball, player.player)
        print(
            f"hit player. intersection rect : {intersection.x, intersection.y, intersection.width, intersection.height}"
        )

        if intersection.width >= intersection.height:
            return "VERTICAL"
        else:
            return "HORIZONTAL"
