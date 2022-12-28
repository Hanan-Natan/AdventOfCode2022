from sys import argv
import re

part = int(argv[1])

with open("day15/input", "r") as f:
    data = f.read().splitlines()

data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()

def parse(data):
    graph = []
    beacons, sensors = [], []
    leftmost_idx, rightmost_idx, max_y  = 0,0,0
    for l in data:
        xs = [int(i) for i in re.findall(r'(?:[, ])x=(-?\d+)', l)]
        ys = [int(i) for i in re.findall(r'(?:[, ])y=(-?\d+)', l)]
        leftmost_idx = min(leftmost_idx, xs[0],xs[1])
        rightmost_idx = max(rightmost_idx, xs[0], xs[1])
        max_y = max(max_y, ys[0], ys[1])
        sensors.append((xs[0],ys[0]))
        beacons.append((xs[1], ys[1]))

    # TODO: how to represent the data and which Data structure to use


# way to solution
# 1. calculate the distance from S to B (|x1-x2| + |y1-y2|)
# 2. distance from S to every corner shouldn't contain more Bs
if part == 1:
    parse(data)
else:
    pass
