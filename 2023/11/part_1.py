# TBD

with open("2023/11/part_1_test_input.txt") as fobj:
    fwobj = open("2023/11/test.txt", "w")
    lines = fobj.readlines()

    # Expansions

    # Rows
    new_lines = []

    for i in range(len(lines)):
        no_galaxy_rows = True

        if "#" in lines[i]:
            no_galaxy_rows = False

        if no_galaxy_rows:
            new_lines.append("." * len(lines[i]) + "\n")
        else:
            new_lines.append(lines[i])

    lines = new_lines

    # Columns - TBD
    cols = []

    for col in range(len(lines[0]) - 1):
        no_galaxy_cols = True

        for row in range(len(lines)):
            if lines[row][col] == "#":
                cols.append(col)
                break
    offset = 0
    for j in range(len(lines[0]) - 1):
        if j not in cols:
            for i in range(len(lines)):
                lines[i] = lines[i][: j + offset] + "." + lines[i][j + offset :]
                offset += 1

    fwobj.writelines(lines)
