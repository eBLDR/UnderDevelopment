"""
Player class.
"""


class Player:
    def __init__(self, number, color, is_AI=False):
        self.is_AI = is_AI
        self.number = number
        self.color = color
        self.name = 'AI' if is_AI else self.set_name()
        self.pieces = {}
    
    @staticmethod
    def set_name():
        return 'Me'
