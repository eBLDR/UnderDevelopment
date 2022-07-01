from dataclasses import dataclass


@dataclass
class Weapon:
    level: int = 1
    experience: int = 0

    damage: int = 0
    range: int = 0

    broken: bool = False
    usage: int = 0
    projectiles: int = 0

    special: object = None

    @classmethod
    def from_class(cls, class_):
        attrs = dir(cls)
        return cls(
            **{
                attr: value for attr, value in class_.__dict__.items() if not attr.startswith('_') and attr in attrs
            },
        )


class Bow(Weapon):
    damage = 5
    range = 300


class LongBow(Weapon):
    damage = 5
    range = 500


class CrossBow(Weapon):
    damage = 10
    range = 250
