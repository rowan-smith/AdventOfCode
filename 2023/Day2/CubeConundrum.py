COLOUR_LIMIT = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


class CubeSet:
    def __init__(self, number: int, colour_map: dict):
        self.set_number = number
        self.colour_map = colour_map

    def __repr__(self):
        return f"Set(set_number={self.set_number}, colour_map={self.colour_map})"

    def is_possible(self) -> bool:
        for colour in self.colour_map:

            if self.colour_map[colour] > COLOUR_LIMIT[colour]:
                return False

        return True


class CubeConundrumGame:
    def __init__(self, game: int, game_sets: list[CubeSet]):
        self.game_number = game
        self.game_sets = game_sets

    def __repr__(self):
        return f"Game(game_number={self.game_number},game_sets={self.game_sets})"

    def is_possible(self) -> bool:
        for game_set in self.game_sets:

            if not game_set.is_possible():
                return False

        return True

    def max_colours(self):
        game_sets = [i.colour_map for i in self.game_sets]

        max_values = {}
        for d in game_sets:
            for key, value in d.items():
                if key not in max_values or value > max_values[key]:
                    max_values[key] = value

        return max_values


class GameCollection:
    def __init__(self):
        self.games: list[CubeConundrumGame] = []

    def load_games(self, file: str):
        with open(file, "r") as input_file:
            for line in input_file.read().splitlines():
                line = line.replace("Game ", "")
                game_number = int(line.split(":")[0])

                line = line.replace(f"{game_number}: ", "")

                game_set = [i for i in line.split(";")]

                game_set_list = []
                for num, game_colors in enumerate(game_set):
                    colours_list = game_colors.strip().split(", ")
                    game_set_list.append(CubeSet(num, {i.split(" ")[1]: int(i.split(" ")[0]) for i in colours_list}))

                self.games.append(CubeConundrumGame(game_number, game_set_list))
