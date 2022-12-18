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

    def compare_me(l, r):
        res = compare_items(l, r)
        if res == True:
            return -1
        elif res == False:
            return 1
        else:
            return 0

    c = 0
    all_packets = []
    while c < len(data):
        left, right = eval(data[c]), eval(data[c+1])
        all_packets.append(left)
        all_packets.append(right)
        c+=3
    all_packets.append([[2]])
    all_packets.append([[6]])
    from functools import cmp_to_key
    # for *every* pair of lists we run the compare funciton. Thus we get the sorted list from low to high
    all_packets = sorted(all_packets, key=cmp_to_key(lambda l, r: compare_me(l, r)))
    res = 1
    for i, p in enumerate(all_packets):
        if p==[[2]] or p == [[6]]:
            res *= i+1
    print(res)