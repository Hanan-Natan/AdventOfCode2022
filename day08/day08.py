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


test_data = """30373
25512
65332
33549
35390"""

if part == 1:
    g = parse(data)
    visible = (len(g) * 2) + (len(g[0])*2) - 4
    # print("Vis", visible)
    vis = True
    # col = [-1, 1, 0, 0] # left, right
    # row = [0, 0, -1, 1] # up, down
    for r in range(1, len(g)-1):
        # walk rows
        for c in range(1, len(g[r])-1):

            # visible += 1
            # if r == 1 and c == 1:
            #     print("checking left", g[r][c], g[r][:c]) # left
            if all(l < g[r][c] for l in g[r][:c]):
                # print(r, c, g[r][c], "vis")
                visible += 1
                # print("checking right", g[r][c], g[r][c+1:]) # right
                # if r == 3 and c == 3:
                #     print(g[r][c+1:])
            elif all(l < g[r][c] for l in g[r][c+1:]):
                # print(r, c, g[r][c], "vis")
                visible += 1
                # print("checking up", g[r][c], g[r][c+1:]) # right
            elif all(g[l][c] < g[r][c] for l in range(r-1, -1, -1)):
                # print(r, c, g[r][c], "vis")
                visible += 1
                # print("checking down", g[r][c], g[r][c+1:]) # right
            elif all(g[l][c] < g[r][c] for l in range(r+1, len(g))):
                # print(r, c, g[r][c], "vis")
                visible += 1

    print(visible)

if part == 2:
    pass
