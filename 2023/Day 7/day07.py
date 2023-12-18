card_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1
}

hand_types = {"Five of a kind": [],      # example: 55555
                "Four of a kind": [],    # example: 5555A
                "Full house": [],        # example: 555AA
                "Three of a kind": [],   # example: 555AK
                "Two pair": [],          # example: 55AAK
                "One pair": [],          # example: 55AKQ
                "High card": []}         # example: 5AKQJ

def prepare_data():
    data = open('input', 'r').read().splitlines()
    hands = {}
    for x in data:
        hand, bid = x.split(' ')
        hands[hand] = int(bid)

    return hands

def determine_hand(hands):
    char_count = {}
    for hand in hands:
        for char in hand:
            char_count[char] = char_count.get(char, 0) + 1

        if any(count == 5 for count in char_count.values()):
            hand_types["Five of a kind"].append(hand)
        elif any(count == 4 for count in char_count.values()):
            hand_types["Four of a kind"].append(hand)
        elif any(count == 3 for count in char_count.values()) and any(count == 2 for count in char_count.values()):
            hand_types["Full house"].append(hand)
        elif any(count == 3 for count in char_count.values()):
            hand_types["Three of a kind"].append(hand)
        elif sum(count == 2 for count in char_count.values()) == 2:
            hand_types["Two pair"].append(hand)
        elif any(count == 2 for count in char_count.values()):
            hand_types["One pair"].append(hand)
        elif not any(count > 1 for count in char_count.values()):
            hand_types["High card"].append(hand)
        else:
            print("This shouldnt be happening: ", hand)

        char_count = {}


def rank_hand():
    for hand_type in hand_types:
        hand_type_hands = hand_types[hand_type]
        hand_types[hand_type] = sorted(
            hand_type_hands,
            key=lambda hand: [card_rank[card] for card in hand],
            reverse=True
        )

def concat_to_list():
    result = []
    for hand in hand_types:
        result += hand_types[hand]
    return result

def get_score(result):
    return sum([(i+1)*hands[hand] for i,hand in enumerate(result[::-1])])



hands = prepare_data()
determine_hand(hands)
rank_hand()
result = concat_to_list()
print(get_score(result))
