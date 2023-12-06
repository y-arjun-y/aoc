with open("2023/6/part_1_2_input.txt") as fobj:
    lines = fobj.readlines()
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))

    result = 1

    for i in range(len(times)):
        possiblities = 0
        for j in range(1, times[i]):
            if (times[i] - j) * j > distances[i]:
                possiblities += 1

        result *= possiblities

    print(result)
