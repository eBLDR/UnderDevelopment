# Run game
from Tak.game import Game

game = Game(2)

game.run()

for p in game.players:
    print(p.pieces)
