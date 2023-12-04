from Game import load_games

GAMES = load_games("input.txt")


def main():
    total = 0
    for game in GAMES:
        if game.is_possible():
            total += game.game_number

    print(total)


if __name__ == '__main__':
    main()
