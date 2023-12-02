with open("2023/2/part_1_2_input.txt", "r") as fobj:
    lines = fobj.readlines()

    sum = 0

    for id in range(len(lines)):
        max_red = 0
        max_green = 0
        max_blue = 0
        sets = lines[id].split(";")

        for subset in sets:
            counts = subset.split(",")

            for i in range(len(counts)):
                if ":" in counts[i]:
                    counts[i] = counts[i][counts[i].index(":") :]

            for count in counts:
                if "red" in count:
                    num = ""
                    for i in count:
                        if i.isnumeric():
                            num += i
                    if int(num) > max_red:
                        max_red = int(num)

                elif "green" in count:
                    num = ""
                    for i in count:
                        if i.isnumeric():
                            num += i
                    if int(num) > max_green:
                        max_green = int(num)

                elif "blue" in count:
                    num = ""
                    for i in count:
                        if i.isnumeric():
                            num += i
                    if int(num) > max_blue:
                        max_blue = int(num)

        print(lines[id], max_red, max_blue, max_green)
        sum += max_red * max_blue * max_green

    print(sum)
