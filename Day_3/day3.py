from functools import reduce

def solve():
    valid_numbers = {}
    p1 = 0
    p2 = 0
    lines = []
    f = open('data.txt', 'r')
    for line in f.readlines():
        lines.append(list(line.strip('\n')+"."))
    for row, line in enumerate(lines):
        indexes = []
        current_number = ""
        for index,c in enumerate(line):
            if c.isdigit() or index == len(line)+1:
                indexes.append(index)
                current_number += c
            elif indexes:
                if indexes:
                    start_col = indexes[0]-1
                    end_col = indexes[-1]+1
                    start_row = row-1
                    end_row = row+2
                    if indexes[0]-1 < 0:
                        start_col = 0
                    if indexes[-1]+1 > len(line):
                        end_col = indexes[-1]
                    if start_row < 0:
                        start_row = 0
                    if end_row > len(lines):
                        end_row = row+1
                    for j in range(start_col, end_col+1):
                        for i in range(start_row, end_row):
                            if not lines[i][j].isdigit() and lines[i][j] != ".":
                                p1+=int(current_number)
                                if lines[i][j] == "*":
                                    if (i,j) in valid_numbers:
                                        valid_numbers[i,j].append(int(current_number))
                                    else:
                                        valid_numbers[i,j] = [int(current_number)]  
                indexes = []
                current_number = ""
    for key,value in valid_numbers.items():
        if len(value) == 2:
            p2 += reduce((lambda x, y: x * y), value)
    print(p1)
    print(p2)

solve()