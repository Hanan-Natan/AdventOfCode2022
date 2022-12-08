from functools import reduce
from sys import argv

day = int("08")
part = int(argv[1])

with open("day08/input".format(day), "r") as f:
    data = f.read().strip().splitlines()


def parse(data):
    g = [[]*len(data[0])]*len(data)
    for i, l in enumerate(data):
        g[i] = list(l)

    return g


# test_data = """30373
# 25512
# 65332
# 33549
# 35390"""

g = parse(data)
# g = parse(test_data.strip().splitlines())
if part == 1:
    visible = (len(g) * 2) + (len(g[0])*2) - 4
    for r in range(1, len(g)-1):
        # walk rows
        for c in range(1, len(g[r])-1):
            if all(l < g[r][c] for l in g[r][:c]):
                visible += 1
            elif all(l < g[r][c] for l in g[r][c+1:]):
                visible += 1
            elif all(g[l][c] < g[r][c] for l in range(r-1, -1, -1)):
                visible += 1
            elif all(g[l][c] < g[r][c] for l in range(r+1, len(g))):
                visible += 1

    print(visible)

elif part == 2:
    highest = 0
    row = [0,0,-1,1]
    col = [-1,1, 0, 0]
    for r in range(1, len(g)-1):
        # walk rows. Another method for walking the graph. This one is IMHO better than the one i originaly used to solve.
        for c in range(1, len(g[r])-1):
            mul = []
            for i in range(len(row)):
                count = 1
                c_row = r+row[i]
                c_col = c+col[i]
                while True:
                    if not (0<=c_row<len(g) and 0<=c_col<len(g[0])):
                        count -= 1
                        break
                    if g[c_row][c_col] >= g[r][c] :
                        break
                    count +=1
                    c_row += row[i]
                    c_col += col[i]
                mul.append(count)
            highest =  max(reduce(lambda x,y: x * y, mul), highest)
    print(highest)

                

            # loop = [list(reversed(g[r][:c])), g[r][c+1:]]  # left and right
            # mul = []
            # for l in loop:
            #     count = 0
            #     for x in l:
            #         if x >= g[r][c]:
            #             count += 1
            #             break
            #         else:
            #             count += 1
            #     mul.append(count)

            # loop = [range(r-1, -1, -1), range(r+1, len(g))]  # up and down
            # for l in loop:
            #     count = 0
            #     for x in l:
            #         if g[x][c] >= g[r][c]:
            #             count += 1
            #             break
            #         else:
            #             count += 1
            #     mul.append(count)

            # highest =  max(reduce(lambda x,y: x * y, mul), highest)
    # print(highest)
            # if r == 1 and c == 2:
            #     print(r, c, g[r][c], mul)
            #     exit(0)
