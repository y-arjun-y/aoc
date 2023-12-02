with open("2023/1/part_1_2_input.txt", "r") as fobj:
    lines = fobj.readlines()
    sum = 0

    for line in lines:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)

        if len(digits) >= 2:
            sum += int(digits[0] + digits[-1])
        else:
            sum += int(digits[0] * 2)

    print(sum)
