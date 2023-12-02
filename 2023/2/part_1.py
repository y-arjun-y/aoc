with open("2023/2/part_1_2_input.txt", "r") as fobj:
    lines = fobj.readlines()
    sum = 0

    for id in range(len(lines)):
        possible = True
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
                    if int(num) > 12:
                        possible = False
                        break

                elif "green" in count:
                    num = ""
                    for i in count:
                        if i.isnumeric():
                            num += i
                    if int(num) > 13:
                        possible = False
                        break

                elif "blue" in count:
                    num = ""
                    for i in count:
                        if i.isnumeric():
                            num += i
                    if int(num) > 14:
                        possible = False
                        break

        print(lines[id], possible)

        if possible:
            sum += id + 1

    print(sum)
