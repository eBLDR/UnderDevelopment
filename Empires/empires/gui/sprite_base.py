import os

import pygame

from empires import constants


class SpriteBase(pygame.sprite.Sprite):
    sprites_path = constants.STATIC_PATH

    def __init__(self, filename, init_position):
        super().__init__()

        self.image_path = os.path.join(
            self.sprites_path,
            '{filename}.png'.format(
                filename=filename,
            )
        )

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.position = init_position

        self.rect = self.get_rect()

    def get_rect(self):
        return self.image.get_rect(center=self.position)

    def update(self):
        self.rect = self.get_rect()

    def is_collision(self, x, y):
        if self.rect.collidepoint(x, y):
            x -= self.rect.x
            y -= self.rect.y
            return self.mask.get_at((x, y))
