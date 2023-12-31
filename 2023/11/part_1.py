# TBD

with open("2023/11/part_1_2_input.txt") as fobj:
    fwobj = open("2023/11/test.txt", "w")
    lines = fobj.readlines()

    # Expansion

    # Rows
    new_lines = []

    for i in range(len(lines)):
        no_galaxy_rows = True

        if "#" in lines[i]:
            no_galaxy_rows = False

        if no_galaxy_rows:
            if lines[i][-1] == "\n":
                new_lines.append(lines[i])
                new_lines.append("." * (len(lines[i]) - 1) + "\n")
            else:
                new_lines.append(lines[i] + "\n")
                new_lines.append("." * len(lines[i]))
        else:
            new_lines.append(lines[i])

    lines = new_lines

    # Columns
    galaxy_cols = []

    for col in range(len(lines[0]) - 1):
        no_galaxy_cols = True

        for row in range(len(lines)):
            if lines[row][col] == "#":
                galaxy_cols.append(col)
                break

    offset = 0

    for j in range(len(lines[0]) - 1):
        if j not in galaxy_cols:
            for i in range(len(lines)):
                print(j, "column")
                print(lines[i], offset)
                print(lines[i][: j + offset] + "." + lines[i][j + offset :])
                lines[i] = lines[i][: j + offset] + "." + lines[i][j + offset :]
                

            offset += 1
    
    # Distance
            
    points = []
    total = 0

    for y in range(len(lines)):
        for x in range(len(lines[0]) - 1):
            if lines[y][x] == '#':
                points.append((x, y))
    
    for i in points:
        for j in points:
            total += abs(j[0] - i[0]) + abs(j[1] - i[1])

    print(total // 2)

    
