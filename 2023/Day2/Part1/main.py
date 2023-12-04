from CubeConundrum import GameCollection

GAME_COLLECTION = GameCollection()
GAME_COLLECTION.load_games("input.txt")


def main():
    total = 0
    for game in GAME_COLLECTION.games:
        if game.is_possible():
            total += game.game_number

    print(total)


if __name__ == '__main__':
    main()
