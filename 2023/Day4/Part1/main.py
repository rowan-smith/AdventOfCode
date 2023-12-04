from Scratchcards import ScratchCardCollection

SCRATCH_CARDS = ScratchCardCollection()
SCRATCH_CARDS.load_scratch_cards("input.txt")


def main():
    total = 0
    for card in SCRATCH_CARDS.cards:
        match_count = len(card.find_matches())

        if match_count:
            card_total = 1
            for i in range(match_count - 1):
                card_total *= 2

            total += card_total

    print(total)


if __name__ == '__main__':
    main()
