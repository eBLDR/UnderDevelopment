from empires.buildings.building_base import BuildingBase


class TownHall(BuildingBase):
    filename = 'town_hall'

    stats = {
        'name': 'Town Hall',
        'position': [300, 300],
        'max_level': 30,
        'costs': {},
    }

    def __init__(self):
        super().__init__(
            self.filename,
            self.stats,
        )
