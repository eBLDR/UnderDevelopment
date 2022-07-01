"""
Game supervisor class.
"""
from Tak import config
from Tak import player
from Tak import board
from Tak import piece


class Game:
    def __init__(self, number_of_human_players):
        self.board_size = 5
        self.number_of_human_players = number_of_human_players
        self.AI_players = 2 - number_of_human_players
        self.colors = {
            1: 'Black',
            2: 'Red'
        }
        self.players = []
        self.board = None
    
    def run(self):
        self.init()
    
    def init(self):
        # Init players
        for n in [1, 2]:
            is_AI = True if n > self.number_of_human_players else False
            self.players.append(player.Player(n, self.colors[n], is_AI=is_AI))
        
        # Init board
        self.board = board.Board(self.board_size)

        # Give pieces
        self.give_pieces()
    
    def give_pieces(self):
        for player in self.players:
            player.pieces = config.PIECES_BY_SIZE[self.board_size]
