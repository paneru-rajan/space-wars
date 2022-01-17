import pygame


class Movement:

    def __init__(self, player) -> None:

        self.player = player

    def detect_movement(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.player.inbound():
            self.player.move_xcord(-1)
        if keys[pygame.K_d] and self.player.inleftbound():
            self.player.move_xcord(1)
        if keys[pygame.K_w] and self.player.in_y_bounds():
            self.player.move_ycord(-1)
        if keys[pygame.K_s] and self.player.in_height_bounds():
            self.player.move_ycord(1)

        if keys[pygame.K_UP]:
            self.player.shoot()
