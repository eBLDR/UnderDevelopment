from empires.buildings.building_base import BuildingBase


class TimberCamp(BuildingBase):
    filename = 'timber_camp'

    stats = {
        'name': 'Timber Camp',
        'position': [800, 500],
        'max_level': 30,
        'costs': {},
    }

    def __init__(self):
        super().__init__(
            self.filename,
            self.stats,
        )
