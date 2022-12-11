from sys import argv
import operator

day = int("09")
part = int(argv[1])

with open("day09/input".format(day), "r") as f:
    data = f.read().splitlines()

# test_data = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20""".strip().splitlines()

op = {"R":operator.add, "L":operator.sub, "U":operator.add, "D":operator.sub}

def change_pos(tail : list, head : list):
    if abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1:
        return tail
    elif abs(head[1]-tail[1]) >= 2 and abs(head[0]-tail[0]) >= 2:
        tail = [head[0]-1 if tail[0]< head[0] else head[0]+1, head[1]-1 if tail[1]<head[1] else head[1]+1]
    elif abs(head[0]-tail[0]) >=2:
        # row diff + 2
        tail = [head[0]-1 if tail[0]<head[0] else head[0]+1, head[1]]
    elif abs(head[1]-tail[1]) >= 2:
        # col diff
        tail = [head[0], head[1]-1 if tail[1]<head[1] else head[1] +1]

    return tail

if part == 1:
    tail_steps = set([(0,0)])
    head, tail = [0,0], [0,0]
    last_head = head.copy()
    for s in data:
        DIR, STEPS = s.split()
        for _ in range(0, int(STEPS)):
            if DIR in "RL":
                head[1] = op[DIR](head[1], 1)
            else: 
                head[0] = op[DIR](head[0], 1)
            if abs(head[0]-tail[0]) ==2 or abs(head[1]-tail[1]) ==2:
                tail = last_head.copy()
                tail_steps.add((last_head[0], last_head[1]))
            last_head = head.copy()

    print(len(tail_steps))
else:
    tail_steps = set([(0,0)])
    head  = [0,0]
    tail = [[0,0] for i in range(9)]
    last_head = head.copy()
    for s in data:
        DIR, STEPS = s.split()
        for _ in range(0, int(STEPS)):
            if DIR in "RL":
                head[1] = op[DIR](head[1], 1)
            else: 
                head[0] = op[DIR](head[0], 1)

            tail[0] = change_pos(tail[0], head)
            for t in range(1, len(tail)):
                tail[t] = change_pos(tail[t], tail[t-1])

            tail_steps.add((tail[8][0], tail[8][1]))

    print(len(tail_steps))