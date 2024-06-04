import pygame


def render_game_over_overlay(screen):
    game_over_text = pygame.font.SysFont("Comic Sans MS", 30).render(
        "Game Over", True, "red"
    )
    restart_text = pygame.font.SysFont("Comic Sans MS", 30).render(
        "'R' to Restart", True, "red"
    )
    quit_text = pygame.font.SysFont("Comic Sans MS", 30).render(
        "'Q' to Quit", True, "red"
    )
    screen.blit(game_over_text, (20, 0))
    screen.blit(restart_text, (20, 40))
    screen.blit(quit_text, (20, 80))
