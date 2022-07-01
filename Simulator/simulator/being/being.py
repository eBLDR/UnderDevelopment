import random


class Being:

    total_beings = 0

    # Attributes
    lifespan = 100
    age_rate = 1

    # The higher this number, the higher chance to live a long life
    resistance_to_death_factor = 3

    thirst_limit = hunger_limit = fatigue_limit = 100
    thirst_rate = 5
    hunger_rate = 3
    fatigue_rate = 2

    def __init__(self, species):
        self.species = species
        self.alive = True

        self.age = 0
        self.sick = False

        self.thirst = 0
        self.hunger = 0
        self.fatigue = 0

        self.total_beings += 1

    def die(self):
        self.alive = False
        self.total_beings -= 1

    def exist(self):
        self.age += self.age_rate
        self.thirst += self.thirst_rate
        self.hunger += self.hunger_rate
        self.fatigue += self.fatigue_rate

        # Natural death due to aging
        if self.natural_death():
            self.die()

        # Death for lack of requisites
        for attribute, limit in [
            (self.thirst, self.thirst_limit),
            (self.hunger, self.hunger_limit),
            (self.fatigue, self.fatigue_limit)
        ]:
            if attribute >= limit:
                self.die()

    def natural_death(self):
        chance_of_dying = (self.age / self.lifespan) ** self.resistance_to_death_factor
        return chance_of_dying > random.random(0, 1)

    def drink(self, amount=None):
        self.thirst = self.thirst - amount if amount else 0
        if self.thirst < 0:
            self.thirst = 0

    def eat(self, amount=None):
        self.hunger = self.hunger - amount if amount else 0
        if self.hunger < 0:
            self.hunger = 0

    def rest(self, amount=None):
        self.fatigue = self.fatigue - amount if amount else 0
        if self.fatigue < 0:
            self.fatigue = 0
