from Scratchcards import ScratchCardCollection

SCRATCH_CARDS = ScratchCardCollection()
SCRATCH_CARDS.load_scratch_cards("input.txt")


def main():
    cards = [1] * len(SCRATCH_CARDS.cards)

    for card_num, card in enumerate(SCRATCH_CARDS.cards):
        match_count = len(card.find_matches())

        for match_range in range(match_count):
            cards[card_num + match_range + 1] += cards[card_num]

    print(sum(cards))


if __name__ == '__main__':
    main()
