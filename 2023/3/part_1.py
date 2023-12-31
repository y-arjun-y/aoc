def symbol(str):
    if str.isalnum() == False and str != ".":
        return True
    else:
        return False


with open("2023/3/part_1_input.txt", "r") as fobj:
    lines = fobj.readlines()
    all_nums = []
    part_nums = []

    for i in range(len(lines)):
        nums = [j for j in lines[i].split(".") if j != "" and j != "\n"]
        for j in range(len(nums)):
            if len(nums[j]) > 4:
                a, b = (
                    nums[j][: nums[j].index("*")],
                    nums[j][nums[j].index("*") + 1 :],
                )
                nums[j] = a
                nums.insert(j + 1, b)
        all_nums.extend(nums)

    for i in range(len(lines)):
        nums = [j for j in lines[i].split(".") if j != "" and j != "\n"]

        for j in range(len(nums)):
            if len(nums[j]) > 4:
                a, b = (
                    nums[j][: nums[j].index("*")],
                    nums[j][nums[j].index("*") + 1 :],
                )
                nums[j] = a
                nums.insert(j + 1, b)
                print(a, b)

        for num in nums:
            part = False

            if (symbol(num[-1]) or symbol(num[0])) and (
                num[:1].isnumeric() or num[1:].isnumeric()
            ):
                part_nums.append(num)
                part = True
            else:
                if i == 0:
                    if part == False and symbol(lines[i + 1][lines[i].index(num) - 1]):
                        part_nums.append(num)
                        part = True

                    if part == False:
                        for j in range(len(num)):
                            if part == False and symbol(
                                lines[i + 1][lines[i].index(num) + j]
                            ):
                                part_nums.append(num)
                                part = True

                    if part == False and symbol(
                        lines[i + 1][lines[i].index(num) + len(num)]
                    ):
                        part_nums.append(num)
                        part = True
                elif i != len(lines) - 1:
                    if part == False and symbol(lines[i - 1][lines[i].index(num) - 1]):
                        part_nums.append(num)
                        part = True

                    if part == False:
                        for j in range(len(num)):
                            if part == False and symbol(
                                lines[i - 1][lines[i].index(num) + j]
                            ):
                                part_nums.append(num)
                                part = True

                    if part == False and symbol(
                        lines[i - 1][lines[i].index(num) + len(num)]
                    ):
                        part_nums.append(num)
                        part = True

                    if part == False and symbol(lines[i + 1][lines[i].index(num) - 1]):
                        part_nums.append(num)
                        part = True

                    if part == False:
                        for j in range(len(num)):
                            if part == False and symbol(
                                lines[i + 1][lines[i].index(num) + j]
                            ):
                                part_nums.append(num)
                                part = True

                    if part == False and symbol(
                        lines[i + 1][lines[i].index(num) + len(num)]
                    ):
                        part_nums.append(num)
                        part = True
                else:
                    if part == False and symbol(lines[i - 1][lines[i].index(num) - 1]):
                        part_nums.append(num)
                        part = True

                    if part == False:
                        for j in range(len(num)):
                            if part == False and symbol(
                                lines[i - 1][lines[i].index(num) + j]
                            ):
                                part_nums.append(num)
                                part = True

                    if part == False and symbol(
                        lines[i - 1][lines[i].index(num) + len(num)]
                    ):
                        part_nums.append(num)
                        part = True

    for i in range(len(part_nums)):
        if len(part_nums[i]) <= 4:
            num = int("".join([j for j in part_nums[i] if j.isnumeric()]))
            part_nums[i] = num

    print(sum(part_nums))
