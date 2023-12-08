def prepare_data():
    original_cards = []
    counter_dict = dict()

    for card in cards:
        winning, yours = card.split('|')
        idx, winning = winning.split(': ')
        idx = idx[len("Card "):].strip()
        counter_dict[idx] = 1
        winning = winning.split()
        yours = yours.split()

        original_cards.append([idx, winning, yours])

    return original_cards, counter_dict

def calc_duplicate_scratchcards():
    while original_cards:
        i, winning_numbers, your_numbers = original_cards.pop(0)
        winner = sum([1 if num in your_numbers else 0 for num in winning_numbers])

        for c in range(winner):
            idx_card_count = int(i) + c + 1
            counter_dict[str(idx_card_count)] += counter_dict[str(i)]

    return counter_dict


cards = open('test', 'r').read().splitlines()
original_cards, counter_dict = prepare_data()
print(sum(calc_duplicate_scratchcards().values()))
