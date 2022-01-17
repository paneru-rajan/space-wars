import random

from constants import WIDTH


def collide(obj1, obj2):
    OffsetX = obj2.x - obj1.x
    offsetY = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (OffsetX, offsetY)) != None


def generate_random_enemy():
    rand_x = random.randrange(50, WIDTH - 100)
    rand_y = random.randrange(-2700, -600)
    rand_color = random.choice(["red", "blue", "green"])
    rand_velocity = random.randrange(2, 4)

    return rand_x, rand_y, rand_color, rand_velocity


def is_player_dead(lives, health):
    return lives <= 0 or health <= 0
