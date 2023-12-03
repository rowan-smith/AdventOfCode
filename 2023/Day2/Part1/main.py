from Game import Game, GameSet

games: list[Game] = []


def main():
    with open("input.txt", "r") as input_file:
        for line in input_file.read().splitlines():
            line = line.replace("Game ", "")
            game_number = int(line.split(":")[0])

            line = line.replace(f"{game_number}: ", "")

            game_set = [i for i in line.split(";")]

            game_set_list = []
            for num, game_colors in enumerate(game_set):
                colours_list = game_colors.strip().split(", ")
                game_set_list.append(GameSet(num, {i.split(" ")[1]: int(i.split(" ")[0]) for i in colours_list}))

            games.append(Game(game_number, game_set_list))

    total = 0
    for game in games:
        if game.is_possible():
            total += game.game_number

    print(total)


if __name__ == '__main__':
    main()
