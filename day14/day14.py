from operator import itemgetter
from sys import argv

part = int(argv[1])

with open("day14/input", "r") as f:
    data = f.read().splitlines()

# data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

col_start_val, col_max_val = float('inf'), 0
col_max_height = 0

def print_graph(data):
    c = 0
    while True:
        # if c == col_max_height+1: # for part 1 only
        if c == col_max_height+3:
            break
        l = ""
        for line in sorted(data):
            if data[line][c] == 0:
                l += "."
            elif data[line][c] == 1:
                l += "#"
            elif data[line][c] == -1:
                l += "o"
            else:
                l += "."
            # print(''.join(["." if i == 0 else "#" for i in line])[c], end='')
        print(l)
        c+=1

def parse(data):
    global col_start_val, col_max_val, col_max_height
    parsed_lines = []
    for i in data:
        v = [(int(e.split(",")[0]), int(e.split(",")[1]))  for e in i.split("->")]
        tmp_min, tmp_max = min(v, key=itemgetter(0)), max(v, key=itemgetter(0))
        tmp_max_height = max(v, key=itemgetter(1))
        col_max_height = max(col_max_height, tmp_max_height[1])
        col_start_val, col_max_val = min(col_start_val, tmp_min[0]), max(col_max_val, tmp_max[0])
        parsed_lines.append([(int(e.split(",")[0]), int(e.split(",")[1]))  for e in i.split("->")])
        
    return parsed_lines

def check_move(table, col, row):
    tmp_p = (col, row)
    while True:
        if table[col][row+1] == 0:
            # check down
            # print("check down", col, row+1)
            row += 1
            continue
        elif table[col-1][row+1] == 0:
            # check left
            # print("check left", col-1, row+1)
            col -= 1
            row += 1
            continue
        elif table[col+1][row+1] == 0:
            # print("check right", col+1, row+1)
            col += 1
            row += 1
            continue
        break
    table[col][row] = -1
    # print_graph(table)

def check_move_p2(table, col, row):
    global col_start_val, col_max_val
    while True:
        if table[col][row+1] == 0:
            row += 1
            continue
        elif table[col-1][row+1] == 0:
            col -= 1
            row += 1
            if col-1 < col_start_val:
                table.update({col-1: [0 for _ in range(col_max_height + 2)] + [1]})
                col_start_val = col-1
            continue
        elif table[col+1][row+1] == 0:
            col += 1
            row += 1
            if col+1 > col_max_val:
                table.update({col+1: [0 for _ in range(col_max_height + 2)] + [1]})
                col_max_val = col+1
            continue
        break
    table[col][row] = -1


# Part 1 took me really long time. I didn't focus on a whole simple solution and always built another little fix that comlicated the solution and made it more complicated.
if part == 1:
    data = parse(data)
    table = {}
    for i in range(col_start_val, col_max_val+1):
        # generate table with colum for each
        table[i]=[0 for _ in range(col_max_height+1)]

    # draw
    for l in data:
        for i in range(1, len(l)):
            start, end = min([l[i-1], l[i]]), max([l[i-1], l[i]])
            for j in range(start[0], end[0]+1):
                for k in range(start[1], end[1]+1):
                    table[j][k] = 1
    # print(table)
    # sand falls
    start = 500
    count = 1
    while True:
        check_move(table, start, 0)
        print("Step", count)
        count +=1
else:
    data = parse(data)
    table = {}
    for i in range(col_start_val, col_max_val+1):
        # generate table with colum for each
        table[i]=[0 for _ in range(col_max_height+2)] + [1]

    # draw
    for l in data:
        for i in range(1, len(l)):
            start, end = min([l[i-1], l[i]]), max([l[i-1], l[i]])
            for j in range(start[0], end[0]+1):
                for k in range(start[1], end[1]+1):
                    table[j][k] = 1

    start = 500
    count = 0
    while True:
        if table[start][0] == -1:
            print("Step", count)
            break
        check_move_p2(table, start, 0)
        count +=1
        # if count == 96:
        #     break
    # print_graph(table)