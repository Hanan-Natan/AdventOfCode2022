from sys import argv

day = int("04")
part = int(argv[1])

with open("day04/input".format(day), "r") as f:
    data = f.read()

count = 0
if part == 1:
    for l in data.splitlines():
        (ll, lr), (rl, rr) = l.split(",")[0].split("-"), l.split(",")[1].split("-")
        ll, lr, rl, rr = int(ll), int(lr), int(rl), int(rr)

        if ll <= rl and lr >= rr:
            # left contains right
            count += 1
        elif rl <= ll and rr >= lr:
            count += 1

    print("Count is {}".format(count))
else:
    lines = data.splitlines()
    count = len(lines)
    for l in lines:
        (ll, lr), (rl, rr) = l.split(",")[0].split("-"), l.split(",")[1].split("-")
        ll, lr, rl, rr = int(ll), int(lr), int(rl), int(rr)

        if lr < rl or ll > rr:
            # not overlap
            count-=1

    print("Count is {}".format(count))