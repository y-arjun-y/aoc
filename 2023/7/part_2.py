from functools import cmp_to_key

conversion = {
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
    "J": 1,
}


def get_type(card):
    if "J" not in card:
        if len(dict.fromkeys(card)) == 1:
            return 6  # "Five of a Kind"
        elif len(dict.fromkeys(card)) == 2:
            if 4 in {i: card.count(i) for i in dict.fromkeys(card)}.values():
                return 5  # "Four of a Kind"
            else:
                return 4  # "Full house"
        elif len(dict.fromkeys(card)) == 3:
            if 3 in {i: card.count(i) for i in dict.fromkeys(card)}.values():
                return 3  # "Three of a Kind"
            else:
                return 2  # "Two pair"
        elif len(dict.fromkeys(card)) == 4:
            return 1  # "One pair"
        elif len(dict.fromkeys(card)) == len(card):
            return 0  # "High card"
    else:
        if (
            len(dict.fromkeys(card)) == 1 or len(dict.fromkeys(card)) == 2
        ):  # JJJJJ, TJJJJ
            return 6  # "Five of a Kind"
        elif len(dict.fromkeys(card)) == 3:  # JTJ8T, J8T8T
            # print(card)
            card = "".join([i for i in card if i != "J"])
            count = {i: card.count(i) for i in dict.fromkeys(card)}
            # print(card, count)
            if 1 not in count.values():
                return 4  # Full house
            else:
                return 5  # Four of a Kind
        elif len(dict.fromkeys(card)) == 4:  # TKJAJ
            card = "".join([i for i in card if i != "J"])
            count = {i: card.count(i) for i in dict.fromkeys(card)}
            if 1 not in count.values():
                return 2  # Two pair
            else:
                return 3  # Three of a Kind
        elif len(dict.fromkeys(card)) == 5:  # TKBAJ
            return 1  # "One pair"


def stronger(card1, card2):
    for i in range(5):
        if card1[0][i] != card2[0][i]:
            if conversion[card1[0][i]] > conversion[card2[0][i]]:
                return 1
            else:
                return -1


with open("2023/7/part_1_2_input.txt") as fobj:
    lines = fobj.readlines()
    cards = [(i.split()[0], i.split()[1]) for i in lines]

    cards = sorted(cards, key=cmp_to_key(stronger))
    rank = 1
    sum = 0

    for i in sorted(cards, key=lambda x: get_type(x[0])):
        sum += int(i[1]) * rank
        rank += 1

    print(sum)
