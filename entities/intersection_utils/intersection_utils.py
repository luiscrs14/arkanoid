import pygame


def rect_intersection(rect1, rect2):
    """Given two pygame.Rect intersecting rectangles, calculate the rectangle of intersection"""
    left = max(rect1.left, rect2.left)
    width = min(rect1.right, rect2.right) - left
    top = max(rect1.top, rect2.top)
    height = min(rect1.bottom, rect2.bottom) - top

    return pygame.Rect(left, top, width, height)
