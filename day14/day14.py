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
        if c == 10:
            break
        l = ""
        for idx, line in data.items():
            if line[c] == 0:
                l += "."
            elif line[c] == 1:
                l += "#"
            elif line[c] == -1:
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

# def move(table,point):
#     start = 500
#     DIR = [(0, 0), (0,-1), (0, 1)] # down, left, right
#     moved = False
#     move_to = (0,0)
#     while True:
#         # check down
#         down = point+DIR[0][1]
#         if down != 10:
#             print("Testing down", start, down, table[start][down])
#             if table[start][down] == 0:
#                 start, point = start, down
#                 move_to= (start, down)
#                 moved = True
#                 continue
#         if move_to[0] == 497:
#             print("Show me next", move_to)
#             print_graph(table)
#         left, down = start+DIR[1][1], point+DIR[1][0]
#         if down != 10:
#             print("Testing left", left, down, table[left][down])
#             if left < col_start_val:
#                 print(f"left OOB at {d}")
#                 print(left, col_start_val)
#                 print_graph(table)
#                 exit(0)
#             if table[left][down] == 0:
#                 DIR[0] = (0,1) # we set it here so taht first time we check only 0
#                 start, point = left, down+1
#                 move_to= (left, down)
#                 moved = True
#                 continue
#         # try right
#         right, down = start+DIR[2][1], point+DIR[2][0] 
#         if down != 10:
#             print("Testing right", right, down, table[right][down])
#             if right > col_max_val:
#                 print(f"right OOB at {d}")
#                 print_graph(table)
#                 print(right, col_start_val)
#                 exit(0)
#             if table[right][down] == 0:
#                 DIR[0] = (0,1) # we set it here so taht first time we check only 0
#                 move_to= (right, down)
#                 start, point = right, down+1
#                 moved = True
#                 continue
#         break
#     if moved:
#         # print("Settle at",move_to)
#         table[move_to[0]][move_to[1]] = -1

#     return moved

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
                # print(j)
                for k in range(start[1], end[1]+1):
                    # print(k)
                    print(j, k)
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
    pass
