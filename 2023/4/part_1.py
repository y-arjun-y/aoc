with open("2023/4/part_1_2_input.txt", "r") as fobj:
    cards = fobj.readlines()
    sum = 0

    for card in cards:
        points = 0
        card = card[card.index(":") + 2 :]
        winning = [int(i) for i in card.split("|")[0].split(" ") if i != ""]
        have = [int(i) for i in card.split("|")[1].split(" ") if i != ""]

        if len([i for i in have if i in winning]) == 1:
            points += 1
        elif len([i for i in have if i in winning]) != 0:
            points += 2 ** (len([i for i in have if i in winning]) - 1)

        print([i for i in have if i in winning], points)

        sum += points

    print(sum)
