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

moves = False
stacks = []
for l in data.splitlines():
    if len(l) == 0:
        moves = True
        stacks = build_stacks(stacks)
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