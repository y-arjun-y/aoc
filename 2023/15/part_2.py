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
    boxes = {}

    for i in line.split(","):
        if '=' in i:
            n_id, id = i[:-2], HASH(i[:-2])
            
            if id not in boxes:
                boxes[id] = [(n_id, i[-1])]
                print(boxes)
            else:
                for j in range(len(boxes[id])):
                    if boxes[id][j][0] == n_id:
                        boxes[id] = boxes[id][:j] + [(n_id, i[-1])] + boxes[id][j+1:] 
                        break
                else:
                    boxes[id] = boxes[id] + [(n_id, i[-1])]

        else:
            n_id, id = i[:-1], HASH(i[:-1])
            
            if id in boxes:
                for j in range(len(boxes[id])):
                    if boxes[id][j][0] == n_id:
                        boxes[id] = boxes[id][:j] + boxes[id][j+1:] 
                        break
    
    total = 0

    for i in boxes:
        for j in range(len(boxes[i])):
            total += ((i+1)*(j+1)*(int(boxes[i][j][1])))
            
    print(total)