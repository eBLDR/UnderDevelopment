import random

from data.engine.entities.entity_base import EntityBase
from data.engine.game_base import GameBase
from data.engine.key_mapper import KeyMapper

# General constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
CAPTION = 'Dodge'


class PlayerEntity(EntityBase):
    filename = 'wisp20x20red'
    init_position = (int(SCREEN_WIDTH / 2), int(SCREEN_WIDTH / 2))

    def __init__(self):
        super().__init__(
            init_position=self.init_position,
            key_mapper=KeyMapper.from_set_1(),
            filename=self.filename,
        )


class EnemyEntity(EntityBase):
    filename = 'ghost32x32'
    spawn_margin = 50

    @classmethod
    def from_random_side(cls):
        init_position = [
            random.choice([
                -cls.spawn_margin,
                var + cls.spawn_margin,
            ]) for var in [SCREEN_WIDTH, SCREEN_HEIGHT]
        ]

        return cls(
            init_position=init_position,
            filename=cls.filename,
        )


class Dodge(GameBase):

    def __init__(self):
        super().__init__(
            screen_size=SCREEN_SIZE,
            caption=CAPTION,
        )

        self.set_main_player(PlayerEntity())

        a = EnemyEntity.from_random_side()
        a.set_dynamic_destination(self.main_player)
        self.all_entities.add(a)
