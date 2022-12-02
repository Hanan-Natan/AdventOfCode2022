from sys import argv

day = int("02")
part = argv[1]

with open("day02/input".format(day), "r") as f:
    data = f.read()

total = 0
score_table = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
res_table = {("A", "Z"):0, ("A", "X"): 3, ("A", "Y"):6, ("B", "X"):0, ("B", "Y"): 3, ("B", "Z"):6,
            ("C", "X"): 6, ("C", "Z"): 3, ("C", "Y"): 0}

for l in data.splitlines():
    a, b = l.split()
    total += res_table[(a, b)]
    total += score_table[b]

print("Total score {}".format(total))
