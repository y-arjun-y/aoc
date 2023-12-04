# 8839386 -> too low


def get_winning(ind, has_ran):
    if not has_ran:
        cards[ind] = cards[ind][cards[ind].index(":") + 2 :]
    winning = [int(i) for i in cards[ind].split("|")[0].split(" ") if i != ""]
    have = [int(i) for i in cards[ind].split("|")[1].split(" ") if i != ""]
    return len([i for i in have if i in winning])


with open("2023/4/part_1_2_input.txt", "r") as fobj:
    cards = fobj.readlines()
    count = {id: 1 for id in range(1, len(cards) + 1)}
    total = 0

    for id in range(1, len(cards)):
        for i in range(1, get_winning(id - 1, False) + 1):
            count[id + i] = count[id] + count[id + i]

    print(count)

    for k, v in count.items():
        total += v

    print(total)
