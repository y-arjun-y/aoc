# doesn't work beyond test

with open("2023/13/part_1_2_input.txt") as fobj:
  lines = fobj.read().splitlines()
  total = 0
  patterns = []

  indices = [i for i in range(len(lines)) if lines[i] == '']

  patterns.append(lines[:indices[0]])
  patterns.append(lines[indices[-1]+1:])

  if len(indices) > 1:
    for i in range(len(indices) - 1):
      patterns.append(lines[indices[i-1]:indices[i]])
      patterns.append(lines[indices[i]+1:indices[i+1]])
      
  for pattern in patterns:
    if len(pattern) > 0:
      cols = []

      for col_i in range(len(pattern[0])):
        col = []
        for row in range(len(pattern)):
          col.append(pattern[row][col_i])
        cols.append(col)
      
      if len(cols) % 2 != 0:
          for i in range(len(cols)):
            if cols[1:i] == cols[i:][::-1]:
              print(pattern)
              total += i
      else:
        for i in range(len(cols)):
            if cols[:i] == cols[i:][::-1]:
              print(pattern)
              total += i
      
      if len(pattern) % 2 != 0:
        for i in range(len(pattern)):
          if pattern[1:i] == pattern[i:][::-1]:
            print(pattern)
            total += i*100
      else:
        for i in range(len(pattern)):
          if pattern[:i] == pattern[i:][::-1]:
            print(pattern)
            total += i*100
    
  print(total)
  

