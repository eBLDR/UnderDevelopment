import os

import pygame

from data import constants


class GameBase:
    static_path = constants.STATIC_PATH

    def __init__(
            self,
            screen_size=constants.DEFAULT_SCREEN_SIZE,
            fps=constants.DEFAULT_FPS,
            caption=constants.DEFAULT_CAPTION,
            bg_solid_color=constants.DEFAULT_BG_SCREEN_COLOR,
    ):
        self.running = True

        # Screen
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(caption)

        self.background_solid_color = bg_solid_color
        self.background_image = None

        # Clock
        self.clock = pygame.time.Clock()
        self.fps = fps

        # Entities
        self.main_player = None
        self.all_entities = pygame.sprite.Group()

    def play(self):
        while self.running:

            # FPS clock
            self.clock.tick(self.fps)

            # Events
            for event in pygame.event.get():

                # Exit game
                if event.type == pygame.QUIT:
                    self.running = False

                # Mouse click
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_click(event.button, event.pos)

            # Keyboard's keys
            key_state = pygame.key.get_pressed()

            # Display
            self.update_frame(key_state)

    def update_frame(self, key_state):
        # Image
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))

        # Solid color
        else:
            self.screen.fill(self.background_solid_color)

        # Update sprites
        self.all_entities.update(
            key_state=key_state,
            area_size=self.screen.get_size(),
            screen=self.screen,
        )

        # Display all sprites
        self.all_entities.draw(self.screen)

        pygame.display.update()

    def set_background_image(self, filename):
        file_path = os.path.join(
            self.static_path,
            'backgrounds',
            f'{filename}.jpg',
        )
        self.background_image = pygame.image.load(file_path)

    def set_main_player(self, main_player):
        self.main_player = main_player
        self.all_entities.add(main_player)

    def mouse_click(self, button, position):
        pass
