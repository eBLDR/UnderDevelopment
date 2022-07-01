from data.engine import utils_math
from data.engine.entities.sprite_base import SpriteBase
from data.engine.entities.stats import Stats
from data.engine.key_mapper import KeyMapper


class EntityBase(SpriteBase):

    def __init__(
            self,
            size=(25, 25),
            filename=None,
            init_position=(0, 0),
            solid_color=(255, 0, 0),
            key_mapper=None,
    ):
        super().__init__(
            size=size,
            filename=filename,
            init_position=init_position,
            solid_color=solid_color,
        )

        # In game attributes
        self.key_mapper: KeyMapper = key_mapper or KeyMapper()

        self.direction = None
        self.auto_move: bool = not bool(key_mapper)
        self.static_destination: (tuple, None) = None
        self.dynamic_destination: (EntityBase, None) = None

        self.range_display: bool = False
        self.active_range: (int, None) = None

        self.stats: Stats = Stats.from_file(filename)
        self.weapon = None

    def update(self, key_state=None, area_size=None, screen=None, *args, **kwargs):
        self._auto_move() if self.auto_move else self._manual_move(
            key_state,
            area_size,
        )

        if self.range_display:
            self.render_range(self.active_range, screen)

    def _auto_move(self):
        if not self.static_destination and not self.dynamic_destination:
            return

        # Dynamic destination has priority over static destination
        destination = self.dynamic_destination.position or self.static_destination

        d_x, d_y = utils_math.reduced_vector_between_two_points(
            self.position,
            destination,
            self.stats.movement_speed,
        )
        self._move(x=d_x, y=d_y)

        if self.position == self.static_destination:
            self.static_destination = None

    def _manual_move(self, key_state, area_size):
        area_width, area_height = area_size
        x, y = self.position
        d_x = d_y = 0

        if key_state[self.key_mapper.move_right]:
            d_x += self.stats.movement_speed if x + self.stats.movement_speed <= area_width else area_width - x

        if key_state[self.key_mapper.move_left]:
            d_x -= self.stats.movement_speed if x - self.stats.movement_speed >= 0 else x

        if key_state[self.key_mapper.move_down]:
            d_y += self.stats.movement_speed if y + self.stats.movement_speed <= area_height else area_height - y

        if key_state[self.key_mapper.move_up]:
            d_y -= self.stats.movement_speed if y - self.stats.movement_speed >= 0 else y

        # Calculate reduced vector
        if d_x and d_y:
            d_x, d_y = utils_math.reduce_vector((d_x, d_y), self.stats.movement_speed)

        if d_x or d_y:
            self._move(x=d_x, y=d_y)

    def enable_range(self, range_):
        self.range_display = True
        self.active_range = range_

    def disable_range(self):
        self.range_display = False
        self.active_range = None

    def set_static_destination(self, destination):
        self.static_destination = destination

    def clear_static_destination(self):
        self.static_destination = None

    def set_dynamic_destination(self, destination_entity):
        assert isinstance(destination_entity, EntityBase)
        self.dynamic_destination = destination_entity

    def clear_dynamic_destination(self):
        self.dynamic_destination = None
