from sys import argv

day = argv[1] 
part = argv[2]

with open("day{}/input".format(day), "r") as f:
    data = f.read()

elvs = []
total = 0
for l in data.splitlines():
    if len(l.strip()) == 0:
        elvs.append(total)
        total = 0
        continue

    total += int(l.strip())

if part == 1:
    print("Part 1: Max {}".format(max(elvs)))
else:
    print("Part 2: {}".format(sum(sorted(elvs)[-3:])))