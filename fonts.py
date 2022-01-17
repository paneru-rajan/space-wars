import pygame

from constants import WIDTH, HEIGHT


class Fonts:

    def __init__(self, surface, level) -> None:
        pygame.font.init()
        self.surface = surface
        self.level = level
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.lost_font = pygame.font.SysFont("comicsans", 70)

    def render(self):
        lives_label = self.main_font.render(f"Lives : {self.level.lives}", 1, (255, 255, 255))
        level_label = self.main_font.render(f"Level : {self.level.level}", 1, (255, 255, 255))
        self.surface.blit(lives_label, (10, 10))
        self.surface.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

    def display_lose_message(self):
        lost_label = self.lost_font.render("You Lost!!", 1, (255, 0, 0))
        self.surface.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, HEIGHT / 2))
