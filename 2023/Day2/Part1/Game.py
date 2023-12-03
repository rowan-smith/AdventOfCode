COLOUR_LIMIT = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


class GameSet:

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


class Game:
    def __init__(self, game: int, game_sets: list[GameSet]):
        self.game_number = game
        self.game_sets = game_sets

    def __repr__(self):
        return f"Game(game_number={self.game_number},game_sets={self.game_sets})"

    def is_possible(self) -> bool:
        for game_set in self.game_sets:

            if not game_set.is_possible():
                return False

        return True
