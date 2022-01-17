import pygame

from components.game import GameManger
from constants import WIDTH, HEIGHT, CAPTIONS


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTIONS)
    clock = pygame.time.Clock()
    game = GameManger(window, clock)
    game.start()


main()
