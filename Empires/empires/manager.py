from empires.buildings.timber_camp import TimberCamp
from empires.buildings.town_hall import TownHall
from empires.gui.gui import GUI


class Manager:

    def __init__(self):
        self.gui = GUI()

    def main(self):
        self.gui.main()

    def test(self):
        self.gui.draw_village_background()
        town_hall = TownHall()
        timber_camp = TimberCamp()
        self.gui.add_sprite(town_hall)
        self.gui.add_sprite(timber_camp)
