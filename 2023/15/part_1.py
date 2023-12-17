def HASH(st):
    cur = 0

    for i in st:
        cur += ord(i)
        cur *= 17
        cur = cur % 256

    return cur


with open("2023/15/part_1_2_input.txt") as fobj:
    line = fobj.readlines()[0]
    total = 0

    for i in line.split(","):
        print(i, HASH(i))
        total += HASH(i)

    print(total)
