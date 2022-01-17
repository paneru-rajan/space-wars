import pygame

from fonts import Fonts
from helpers import is_player_dead
from level import Level
from loaders import BG
from movement import Movement
from player import Player


class GameManger:

    def __init__(self, surface, clock) -> None:
        self.surface = surface
        self.running = True
        self.clock = clock
        self.lost = False
        self.player = Player(300, 650, surface, 7, -9)
        self.movement = Movement(self.player)
        self.level = Level(0, 5, surface)
        self.fonts = Fonts(surface, self.level)
        self.lost_count = 0

    def exit_game(self):
        self.running = False

    def redraw_window(self):
        self.surface.blit(BG, (0, 0))
        self.player.draw()
        self.fonts.render()
        for enemy in self.level.enemies:
            enemy.draw()
        if self.lost:
            self.fonts.display_lose_message()

        pygame.display.update()

    def start(self):
        while self.running:
            self.clock.tick(60)
            self.redraw_window()
            if is_player_dead(self.level.lives, self.player.health):
                self.lost = True
                self.lost_count += 1

            if self.level.enemies_empty:
                self.level.spawn_enemies()

            if self.lost:
                if self.lost_count > 60 * 3:
                    self.exit_game()
                else:
                    continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.movement.detect_movement()

            self.level.move_enemies(self.player)

            self.player.move_lasers(self.level.enemies)
