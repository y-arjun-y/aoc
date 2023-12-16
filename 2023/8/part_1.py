with open("2023/8/part_1_2_input.txt") as fobj:
    lines = fobj.readlines()
    moves = lines[0]
    dict = {}

    for i in range(2, len(lines)):
        init, tup = lines[i].split(" = ")[0], (
            lines[i].split(" = ")[1][1:4],
            lines[i].split(" = ")[1][6:9],
        )
        dict[init] = tup

    count = 0
    cur = "AAA"
    pos = 0

    while cur != "ZZZ":
        if pos > len(moves) - 2:
            pos = 0

        if moves[pos] == "L":
            print(cur, pos, "L", count)
            cur = dict[cur][0]
            pos += 1
            count += 1
        else:
            print(cur, pos, "R", count)
            cur = dict[cur][1]
            pos += 1
            count += 1

    print(count)
