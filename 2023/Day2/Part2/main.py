from functools import reduce
from operator import mul

from CubeConundrum import GameCollection

GAME_COLLECTION = GameCollection()
GAME_COLLECTION.load_games("input.txt")


def main():
    total = 0
    for game in GAME_COLLECTION.games:
        total += reduce(mul, game.max_colours().values())
    print(total)


if __name__ == '__main__':
    main()
