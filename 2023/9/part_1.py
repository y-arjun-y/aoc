with open("2023/9/part_1_2_input.txt") as fobj:
    sequences = fobj.readlines()
    res = 0

    for sequence in sequences:
        total = None
        line = list(map(int, sequence.split()))
        sequence_breakdown = [line]

        while total != 0:
            lst = []

            for i in range(1, len(line)):
                lst.append(line[i] - line[i - 1])

            line = lst
            sequence_breakdown.append(line)
            total = sum(lst)

        sequence_breakdown = sequence_breakdown[::-1][1:]
        sequence_breakdown[0] = sequence_breakdown[0] + [sequence_breakdown[0][0]]

        for i in range(1, len(sequence_breakdown)):
            sequence_breakdown[i] = sequence_breakdown[i] + [
                sequence_breakdown[i][-1] + sequence_breakdown[i - 1][-1]
            ]

        print(sequence_breakdown)
        res += sequence_breakdown[-1][-1]

    print(res)
