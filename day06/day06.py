from sys import argv

day = int("06")
part = int(argv[1])

with open("day06/input".format(day), "r") as f:
    data = f.read().strip()

if part == 1:
    for l in range(len(data)):
        if len(set(data[l:l+4])) == len(data[l:l+4]):
            print(l+4)
            break
else:
    for l in range(len(data)):
        if len(set(data[l:l+14])) == len(data[l:l+14]):
            print(l+14)
            break