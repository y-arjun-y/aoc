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
    pos = 0
    curs = [i for i in dict if i[-1] == "A"][1:5]

    print(curs)

    while False in [cur[-1] == "Z" for cur in curs]:
        for i in range(len(curs)):
            if pos > len(moves) - 2:
                pos = 0

            if moves[pos] == "L":
                curs[i] = dict[curs[i]][0]
            else:
                curs[i] = dict[curs[i]][1]

        count += 1
        pos += 1

        print(curs, len([i for i in curs if i[-1] == "Z"]))

    print(count)
