import os

import pygame

from empires import constants
from empires.gui import design_constants
from empires.gui.screen import Screen


class GUI:

    background_images_path = os.path.join(
        constants.STATIC_PATH,
        'backgrounds',
    )

    background_village_path = os.path.join(
        background_images_path,
        design_constants.VILLAGE_BACKGROUND_IMAGE,
        )

    def __init__(self, background_color=design_constants.COLOR_BLACK):
        # self.source_path = os.path.join(os.getcwd(), SOURCE_PATH)

        self.running = True

        self.screen = Screen(constants.SCREEN_SIZE, background_color)

        self.all_sprites = pygame.sprite.Group()

        self.fps = constants.FPS
        self.clock = pygame.time.Clock()

        self.background_image_position = (0, design_constants.TOP_MENU_HEIGHT)
        self.background_village_image = pygame.image.load(self.background_village_path)

    def add_sprite(self, sprite):
        self.all_sprites.add(sprite)
        self.all_sprites.draw(self.screen.surface)

    def draw_village_background(self):
        self.screen.draw_image(
            self.background_village_image,
            self.background_image_position
        )

    def update_frame(self):
        # Clear sprites on previous frame
        # self.all_sprites.clear(
        #     self.screen.surface,
        #     self.screen.surface_background
        # )

        # Update sprites
        # for entity in self.all_sprites:
        #     entity.update(keys)

        # Draw sprites
        # self.all_sprites.draw(self.screen.surface)

        pygame.display.update()

    # def display_static_background(self):
    #     self.screen.surface.blit(self.screen.surface_background, (0, 0))

    def main(self):

        while self.running:

            mouse_button = mouse_x = mouse_y = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == pygame.BUTTON_LEFT:
                        mouse_x, mouse_y = event.pos

                        for sprite in self.all_sprites:
                            if sprite.is_collision(mouse_x, mouse_y):
                                print(f'Clicked on: {sprite.name}')
                        # mouse_button = constants.MOUSE_LEFT

            # keys = pygame.key.get_pressed()

            # Mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            self.update_frame()

            self.clock.tick(self.fps)
