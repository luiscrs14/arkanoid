from enum import StrEnum


class GameState(StrEnum):
    GAME_OVER = "GAME_OVER"
    GAME_IN_PROGRESS = "GAME_IN_PROGRESS"
    GAME_WON = "GAME_WON"
