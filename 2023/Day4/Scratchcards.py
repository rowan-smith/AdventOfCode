class ScratchCard:
    def __init__(self, card_number: int, winning_numbers: list, numbers: list):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.numbers = numbers

    def __repr__(self):
        return f"ScratchCard(card_number={self.card_number},winning_numbers={self.winning_numbers},numbers={self.numbers})"

    def find_matches(self) -> list[int]:
        matched_numbers = []
        for winning_number in self.winning_numbers:
            if winning_number in self.numbers:
                matched_numbers.append(int(winning_number))

        return matched_numbers


class ScratchCardCollection:
    def __init__(self):
        self.cards: list[ScratchCard] = []

    def load_scratch_cards(self, file: str):
        with open(file, "r") as input_file:
            for line in input_file.read().splitlines():
                line = line.replace("Card ", "")

                card_number = int(line.split(":")[0])
                line = line.replace(f"{card_number}: ", "")

                sections = [section.split() for section in line.split("|")]

                self.cards.append(ScratchCard(card_number, sections[0], sections[1]))
