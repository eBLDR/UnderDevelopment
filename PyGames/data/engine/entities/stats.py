from dataclasses import dataclass


@dataclass
class Stats:
    alive: bool = True
    level: int = 1
    experience: int = 0

    movement_speed: int = 10
    health: int = 0
    energy: int = 0
    strength: int = 0
    range: int = 0

    @classmethod
    def from_file(cls, filename):
        stats_json = {}  # TODO: import me

        return cls(
            **{
                attr: value for attr, value in stats_json.items() if attr in dir(cls)
            },
        )
