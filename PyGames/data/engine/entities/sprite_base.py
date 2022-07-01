import os

import pygame

from data import constants

# RGB colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class SpriteBase(pygame.sprite.Sprite):
    sprites_path = os.path.join(
        constants.STATIC_PATH,
        'sprites',
    )

    def __init__(
            self,
            size=(25, 25),
            filename=None,
            init_position=(0, 0),
            solid_color=BLACK,
            aux_color=BLACK,
    ):
        super().__init__()

        # Display
        image_path = os.path.join(
            self.sprites_path,
            f'{filename}.png'
        ) if filename else None

        self.image = pygame.image.load(image_path) if image_path else pygame.Surface(size)
        self.mask = pygame.mask.from_surface(self.image)

        self.solid_color = solid_color
        self.aux_color = aux_color

        if not filename:
            self.image.fill(self.solid_color)

        x, y = init_position
        self.rect = self.image.get_rect(
            center=(int(x), int(y))
        )

    @property
    def position(self):
        return self.rect.center

    def update(self, *args, **kwargs):
        pass

    def _move(self, x=0, y=0):
        self.rect.move_ip(x, y)

    def mouse_collision(self, position):
        x, y = position
        if self.rect.collidepoint(x, y):
            x -= self.rect.x
            y -= self.rect.y
            return self.mask.get_at((x, y))

    def surface_collision(self, rect):
        # TODO: implement mask collision
        return self.rect.colliderect(rect)

    def render_range(self, radius, screen):
        pygame.draw.circle(
            screen,
            self.aux_color,
            self.position,
            radius,
            1,
        )
