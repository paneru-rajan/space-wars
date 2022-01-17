import pygame

from constants import WIDTH, HEIGHT
from components.loaders import YELLOW_LASER, YELLOW_SPACE_SHIP
from components.ship import Ship


class Player(Ship):

    def __init__(self, x, y, win, vel, laser_vel, health=100) -> None:
        super().__init__(x, y, win, health=health)

        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.vel = vel
        self.laser_vel = laser_vel

    def inbound(self):
        return self.x + self.vel > 0

    def inleftbound(self):
        return self.x + self.vel + self.get_width < WIDTH

    def in_y_bounds(self):
        return self.y - self.vel > 0

    def in_height_bounds(self):
        return self.y + self.get_height + self.vel < HEIGHT

    def move_xcord(self, dir):
        self.x += self.vel * dir

    def move_ycord(self, dir):
        self.y += self.vel * dir

    def move_lasers(self, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(self.laser_vel)
            if laser.off_screen(750):
                self.lasers.remove(laser)

            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def draw(self):
        super().draw()
        self.healthbar()
