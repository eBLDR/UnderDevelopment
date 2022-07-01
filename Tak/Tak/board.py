"""
Board class.
"""


class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
    
    def init_board(self):
        self.board = [[Box() for x in range(self.size)] for y in range(self.size)]


class Box:
    def __init__(self):
        self.pieces = []
    
    def is_free(self):
        return bool(self.pieces)
    
    def put_pieces(self, new_pieces):
        self.pieces.extend(new_pieces)
    
    def take_pieces(self, number_of_pieces):
        pieces_to_be_moved = self.pieces[len(self.pieces) - number_of_pieces:]
        self.pieces = self.pieces[:-number_of_pieces]
        return pieces_to_be_moved
