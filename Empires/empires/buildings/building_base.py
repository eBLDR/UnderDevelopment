import os

from empires.gui.sprite_base import SpriteBase
from empires.resources.resources import Resources


class BuildingBase(SpriteBase):
    buildings_image_path = 'buildings'

    def __init__(self, filename, stats):
        filename = os.path.join(self.buildings_image_path, filename)
        super().__init__(filename, stats['position'])

        # Stats
        self.name = stats['name']
        self.level = 1
        self.max_level = stats['max_level']
        self.costs_mapper = stats['costs']

    def get_resource_cost(self):
        pass
        # return Resources()

    def can_level_up(self):
        return self.level < self.max_level

    def level_up(self, resources):
        if not self.can_level_up():
            return False

        self.level += 1
