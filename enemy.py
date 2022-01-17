import pygame

from loaders import RED_LASER, RED_SPACE_SHIP, GREEN_LASER, GREEN_SPACE_SHIP, BLUE_LASER, BLUE_SPACE_SHIP
from ship import Ship


class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, win, color, vel, health=100) -> None:
        super().__init__(x, y, win, health=health)

        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.vel = vel

    def move(self):
        self.y += self.vel


class EnemyBuilder():

    def __init__(self) -> None:
        pass

    def add_cords(self, x, y):
        self.x = x
        self.y = y
        return self

    def add_color(self, color):
        self.color = color
        return self

    def add_surface(self, surface):
        self.surface = surface
        return self

    def add_velocity(self, velocity):
        self.velocity = velocity
        return self

    def build(self):
        return Enemy(self.x, self.y, self.surface, self.color, self.velocity)
