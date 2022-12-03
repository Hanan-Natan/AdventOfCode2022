import string
from sys import argv

day = int("03")
part = int(argv[1])

with open("day03/input".format(day), "r") as f:
    data = f.read()

# data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

def get_priority(v):
    return ord(v) - ord("A") + 27 if v.isupper() else ord(v) - ord("a") + 1

priority_val = 0
if part == 1:
    for l in data.splitlines():
        mid = len(l)//2
        d = dict.fromkeys(string.ascii_lowercase + string.ascii_uppercase, 0)
        for i in range(0, mid):
            d[l[i]] += 1
        for i in range(mid, len(l)):
            if d[l[i]] > 0:
                priority_val += get_priority(l[i])
                break

    print("Priority val {}".format(priority_val)) 
else:

    data = data.splitlines()
    for l in range(0, len(data), 3):
        v = set(data[l]) & set(data[l+1]) & set(data[l+2])
        priority_val += get_priority(v.pop())

    print(priority_val)