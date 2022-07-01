import argparse

from data import games


def get_games_list():
    return [
        name for name in dir(games) if name[0].isupper()
    ]


def list_games():
    print(f'''
Available games are:

        {(chr(0x0A) + chr(0x09)).join(get_games_list())}
''')


parser = argparse.ArgumentParser(
    description='PyGames suite - for easy fun.',
)

parser.add_argument(
    '-l',
    '--list',
    help='lists all available games',
    action='store_true',
)

parser.add_argument(
    'game',
    help='name of game to play',
    type=str,
    nargs='?',
    default='',
)

args = parser.parse_args()

if args.list:
    list_games()
    exit(0)

game_name = args.game.title()

if not game_name:
    parser.print_help()
    exit(1)

# Check game availability
if not hasattr(games, game_name):
    print(f'Game {game_name} not found in collection.')
    list_games()
    exit(2)

Game = getattr(games, game_name)
game = Game()
game.play()
