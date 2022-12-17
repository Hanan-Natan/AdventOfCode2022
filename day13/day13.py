from sys import argv
from typing import List

part = int(argv[1])

with open("day13/input", "r") as f:
    data = f.read().splitlines()

tdata = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".splitlines()


def compare_lists(left,lidx, right, ridx):
    print(f"Comparing lists: {left}:{lidx},{right}:{ridx}")
    if len(left) == len(right) == 0:
        return None
    if len(left) == 0 or left[lidx] < right[ridx]:
        print(f"{left},{right} IN order")
        return lidx
    elif len(right) == 0 or left[lidx] > right[ridx]:
        print(f"{left},{right} NOT IN order")
        return ridx
    else:
        return compare_lists(left,lidx+1, right, ridx+1)

# I had hard time coming up with the right algo for the different comparisions.
# I tried doing recursive on the case of both lists and It faild.
# At the end I compied the idea from: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/13.py
def compare_items(left,  right):
    if type(left) == type(right) == int:
        if left == right:
            return None
        else:
            return True if left < right else False
    elif type(left) == type(right) == list:
        low = len(left) if len(left) < len(right) else len(right)
        for i in range(low):
            res = compare_items(left[i], right[i])
            if res == True:
                return True
            elif res == False:
                return False
        if len(left) == len(right):
            return None
        else:
            return True if low < len(right) else False
    elif type(left) == list and type(right) == int:
        return compare_items(left, [right])
    else:
        return compare_items([left], right)


if part == 1:
    c = 0
    pair = 1
    total = 0
    while c < len(data):
        left, right = eval(data[c]), eval(data[c+1])
        res = compare_items(left, right)
        # res = new_compare(left, right,)
        # print(f"Pair {pair} is {res}")
        if res == True:
            total += pair
            # print(f"total is {total}")
        c += 3
        pair +=1

    print(f"Result {total}")
else:
    pass
