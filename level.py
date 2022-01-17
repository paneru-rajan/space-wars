import random

from constants import HEIGHT
from enemy import EnemyBuilder
from helpers import generate_random_enemy, collide


class Level:

    def __init__(self, level, wavelength, surface) -> None:

        self.level = level
        self.lives = 5
        self.surface = surface
        self.wavelength = wavelength
        self.enemies = []

    @property
    def enemies_empty(self):
        return len(self.enemies) == 0

    def spawn_enemies(self):
        self.level += 1
        self.wavelength += 5
        for i in range(self.wavelength):
            # enemy = Enemy(random.randrange(50,WIDTH-100), random.randrange(-1700,-100),self.surface,random.choice(["red","blue","green"]),random.randrange(2,6))
            rand_x, rand_y, rand_color, rand_velocity = generate_random_enemy()
            print(rand_y)
            enemy = EnemyBuilder().add_cords(rand_x, rand_y) \
                .add_surface(self.surface) \
                .add_color(rand_color) \
                .add_velocity(rand_velocity).build()
            self.enemies.append(enemy)

    def move_enemies(self, player):
        for enemy in self.enemies[:]:
            enemy.move()
            enemy.move_lasers(4, player)

            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()

            if enemy.y + enemy.get_height > HEIGHT:
                self.lives -= 1
                self.enemies.remove(enemy)

            if collide(enemy, player):
                player.health -= 10
                self.enemies.remove(enemy)
