from collections import defaultdict
from pprint import pprint
from queue import PriorityQueue
from sys import argv
import sys
from typing import List

sys.setrecursionlimit(5000)
part = int(argv[1])

with open("day12/input", "r") as f:
    data = f.read().splitlines()


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.parent = {}
        self.end = -1
        self.start = -1
        self.all_a = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def parse(self, data: List[str]):
        DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS = len(data)
        COL = len(data[0])

        for r in range(ROWS):
            # print(data[r])
            if "S" in data[r]:
                self.start = data[r].find("S") + (COL * r)
                # print(f"start at {self.start}")
                data[r] = data[r].replace("S", "a")
            if "E" in data[r]:
                self.end = data[r].find("E") + (COL * r)
                # print(f"End at {self.end}")
                data[r] = data[r].replace("E", "z")

            for c in range(COL):
                if data[r][c] == "a":
                    self.all_a.append(r*COL + c)
                for (dr, dc) in DIR:
                    if not (0 <= r + dr < ROWS and 0 <= c+dc < COL):
                        continue
                    if (data[r][c] >= data[r+dr][c+dc]) or (ord(data[r+dr][c+dc]) - ord(data[r][c]) == 1):
                    # if (data[r][c] == data[r+dr][c+dc]) or (ord(data[r+dr][c+dc]) - ord(data[r][c]) == 1 or (ord(data[r][c]) - ord(data[r+dr][c+dc]) > 0)):
                        self.add_edge(r*COL + c, (r+dr)*COL + (c+dc))

    def BFS(self, s):
        visited = [False] * (max(self.graph)+1)
        queue = []
        queue.append(s)
        visited[s] = True
        self.parent = [-1 for _ in range(max(self.graph)+1)]
        while queue:
            s = queue.pop(0)
            # print(s, end=' ')
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    self.parent[i] = s
                    # print(f"Parent of {i} is {s}")

    def count_short_path(self, start, end, parents):
        if (start == end) or (end == -1):
            return 0

        return 1 + self.count_short_path(start, parents[end], parents)

# data = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi""".splitlines()


g = Graph()
g.parse(data)

# Part 1 and part 2 are buggy as hell
# I've bugs in the BFS and shortest paath algorithem
# I need to study this topic more...
# I manged to answer right but that's not in a manner that I like to...

if part == 1:
    g.BFS(g.start)
    s = g.count_short_path(g.start, g.end, g.parent)
    print("Shortest {}".format(s))
else:
    m = []
    for s in g.all_a:
        g.BFS(s)
        m.append((g.count_short_path(s, g.end, g.parent), s))

    print("Shortest {}".format(m))
