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


def render_game_won_overlay(screen):
    game_win_text = pygame.font.SysFont("Comic Sans MS", 30).render(
        "You won!", True, "red"
    )
    restart_text = pygame.font.SysFont("Comic Sans MS", 30).render(
        "'R' to Restart", True, "red"
    )
    quit_text = pygame.font.SysFont("Comic Sans MS", 30).render(
        "'Q' to Quit", True, "red"
    )
    screen.blit(game_win_text, (20, 0))
    screen.blit(restart_text, (20, 40))
    screen.blit(quit_text, (20, 80))


def render_fps_overlay(clock, screen):
    fps_text = pygame.font.SysFont("Comic Sans MS", 20).render(
        str(int(clock.get_fps())), True, "blue"
    )
    screen.blit(fps_text, (0, 0))
