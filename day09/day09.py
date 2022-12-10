from sys import argv
import operator

day = int("09")
part = int(argv[1])

with open("day09/input".format(day), "r") as f:
    data = f.read().splitlines()

# test_data = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2""".strip().splitlines()

op = {"R":operator.add, "L":operator.sub, "U":operator.add, "D":operator.sub}

if part == 1:
    tail_steps = set([(0,0)])
    head= [0,0] # initial pos
    last_head = head.copy()
    tail= [0,0] # ''
    for s in data:
    # for s in test_data:
        DIR, STEPS = s.split()
        for _ in range(1, int(STEPS)+1):
            if DIR in "RL":
                head[1] = op[DIR](head[1], 1)
            else: 
                head[0] = op[DIR](head[0], 1)
            if abs(head[0]-tail[0]) ==2 or abs(head[1]-tail[1]) ==2:
                tail = last_head.copy()
                tail_steps.add((last_head[0], last_head[1]))
                # print("tail to {}, head at {}".format(tail, head))
            last_head = head.copy()

    print(len(tail_steps))