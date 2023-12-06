with open("2023/6/part_1_2_input.txt") as fobj:
    lines = fobj.readlines()
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    possiblities = 0

    for i in range(1, time):
        if (time - i) * i > distance:
            possiblities += 1

    print(possiblities)
