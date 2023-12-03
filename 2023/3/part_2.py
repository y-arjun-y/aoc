# TBD
import math

with open("2023/3/part_1_2_input.txt", "r") as fobj:
    lines = fobj.readlines()
    pairs = []

    for i in range(len(lines)):
        nums = [j for j in lines[i].split(".") if j != "" and j != "\n"]

        for num in nums:
            for j in range(len(nums)):
                if len(nums[j]) > 4:
                    a, b = (
                        nums[j][: nums[j].index("*")],
                        nums[j][nums[j].index("*") + 1 :],
                    )
                    nums[j] = a
                    nums.insert(j + 1, b)
                    print(a, b)

            found = False

            if num[-1] == "*" and num[:-1].isnumeric():
                pairs.append((num, (i, len(num) - 1)))
            elif num[0] == "*" and num[1:].isnumeric():
                pairs.append((num, (i, 0)))
            else:
                if i == 0:
                    if found == False and lines[i + 1][lines[i].index(num) - 1] == "*":
                        pairs.append((num, (i + 1, lines[i].index(num) - 1)))
                        found = True

                    if found == False:
                        for j in range(len(num)):
                            if (
                                found == False
                                and lines[i + 1][lines[i].index(num) + j] == "*"
                            ):
                                pairs.append(num, (i + 1, lines[i].index(num) + j))
                                found = True

                    if (
                        found == False
                        and lines[i + 1][lines[i].index(num) + len(num)] == "*"
                    ):
                        pairs.append((num, (i + 1, lines[i].index(num) + len(num))))
                        found = True
                elif i == len(lines) - 1:
                    if found == False and lines[i - 1][lines[i].index(num) - 1] == "*":
                        pairs.append((num, (i - 1, lines[i].index(num) - 1)))
                        found = True

                    if found == False:
                        for j in range(len(num)):
                            if (
                                found == False
                                and lines[i - 1][lines[i].index(num) + j] == "*"
                            ):
                                pairs.append((num, (i - 1, lines[i].index(num) + j)))
                                found = True

                    if (
                        found == False
                        and lines[i - 1][lines[i].index(num) + len(num)] == "*"
                    ):
                        pairs.append((num, (i - 1, lines[i].index(num) + len(num))))
                        found = True
                else:
                    if found == False and lines[i + 1][lines[i].index(num) - 1] == "*":
                        pairs.append((num, (i + 1, lines[i].index(num) - 1)))
                        found = True

                    if found == False:
                        for j in range(len(num)):
                            if (
                                found == False
                                and lines[i + 1][lines[i].index(num) + j] == "*"
                            ):
                                pairs.append((num, (i + 1, lines[i].index(num) + j)))
                                found = True

                    if (
                        found == False
                        and lines[i + 1][lines[i].index(num) + len(num) - 1] == "*"
                    ):
                        pairs.append((num, (i + 1, lines[i].index(num) + len(num))))
                        found = True

                    if found == False and lines[i - 1][lines[i].index(num) - 1] == "*":
                        pairs.append((num, (i - 1, lines[i].index(num) - 1)))
                        found = True

                    if found == False:
                        for j in range(len(num)):
                            if (
                                found == False
                                and lines[i - 1][lines[i].index(num) + j] == "*"
                            ):
                                pairs.append((num, (i - 1, lines[i].index(num) + j)))
                                found = True

                    if (
                        found == False
                        and lines[i - 1][lines[i].index(num) + len(num) - 1] == "*"
                    ):
                        pairs.append((num, (i - 1, lines[i].index(num) + len(num))))
                        found = True

    dict = {}
    sum = 0

    for i in pairs:
        if i[1] in dict:
            dict[i[1]].append(int("".join([j for j in i[0] if j.isnumeric()])))
        else:
            dict[i[1]] = [int("".join([j for j in i[0] if j.isnumeric()]))]

    for i in dict:
        prod = 1

        if len(dict[i]) > 1:
            for j in dict[i]:
                print(j, prod, sum)
                prod *= j

            sum += prod

    print(sum)
