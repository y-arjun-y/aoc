def replace(st):
    mappings = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    digits = []

    for i in range(len(st)):
        for j in range(len(st)):
            if st[i:j+1] in mappings:
                digits.append(mappings[st[i:j+1]])
            elif st[i:j+1].isdigit():
                digits.append(st[i:j+1])
    
    return "".join(digits)

with open("part_1_2_input.txt", "r") as fobj:
    lines = fobj.readlines()
    sum = 0

    for line in lines:
        line = replace(line)
        print(line)
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        if len(digits) >= 2:
            sum += int(digits[0] + digits[-1])
        else:
            sum += int(digits[0] * 2)
        
        print(sum)