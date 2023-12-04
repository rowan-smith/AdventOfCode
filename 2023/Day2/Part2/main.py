from functools import reduce
from operator import mul

from Game import load_games

GAMES = load_games("input.txt")


def main():
    total = 0
    for game in GAMES:
        total += reduce(mul, game.max_colours().values())
    print(total)


if __name__ == '__main__':
    main()
