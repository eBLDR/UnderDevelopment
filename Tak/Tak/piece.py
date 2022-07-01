"""
Piece class.
"""


class Piece:
    def __init__(self, color):
        self.color = color
    

class Basic(Piece):
    def __init__(self, is_wall=False):
        self.is_flat = not is_wall
        self.is_wall = is_wall
    
    def flatten(self):
        self.is_flat = True
        self.is_wall = False


class CapStone(Piece):
    def __init__(self):
        self.is_flat = True
        self.is_wall = True
