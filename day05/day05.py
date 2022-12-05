from sys import argv

day = int("05")
part = int(argv[1])

with open("day05/input".format(day), "r") as f:
    data = f.read()

def build_stacks(stacks):
    c = [[] for x in range(int(stacks.pop()[-1]))]
    for i in range(len(stacks)-1,-1, -1):
        for j in range(len(c)):
            v = stacks[i][j][1]
            if v.isupper():
                c[j].append(v)

    return c

# data = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

moves = False
stacks = []
for l in data.splitlines():
    if len(l) == 0:
        moves = True
        # parse stacks
        stacks = build_stacks(stacks)
        # stacks[1].append("D") # TODO: remove
    elif moves:
        i = l.split()
        n, f, t = [int(x) for x in [i[1], i[3], i[5]]]
        if part == 1:
            for i in range(0, n):
                stacks[t-1].append(stacks[f-1].pop())
        elif part == 2:
            stacks[t-1].extend(stacks[f-1][-n:])
            del stacks[f-1][-n:]
    else:
        stacks.append(l.replace("    ", " -- ").split())

for c in stacks:
    print(c.pop(), end='')
print()