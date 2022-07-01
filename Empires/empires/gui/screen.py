import pygame

from empires import constants
from empires.gui import design_constants


class Screen:
    def __init__(self, screen_size, background_color):
        self.size = screen_size
        self.background_color = background_color

        self.surface = pygame.display.set_mode(self.size, 0, 32)
        # self.surface_background = None

        pygame.display.set_caption(constants.TITLE)
        # icon = pygame.image.load('icon.png')
        # pygame.display.set_icon(icon)

        self.init(background_color)

    def init(self, background_color):
        self.surface.fill(background_color)

        self.draw_top_menu()

        # Set screen background
        # self.set_surface_background()

    # def set_surface_background(self):
    #     self.surface_background = self.surface.copy()

    def render_text(self, text, position):
        self.surface.blit(text, position)

    def draw_image(self, image, position):
        self.surface.blit(
            image,
            position,
        )

    def draw_top_menu(self):
        # TODO replace for image
        pygame.draw.rect(
            self.surface,
            design_constants.COLOR_WHITE,
            (0, 0, constants.SCREEN_WIDTH, design_constants.TOP_MENU_HEIGHT),
        )
