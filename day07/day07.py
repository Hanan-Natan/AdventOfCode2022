from sys import argv
import sys
sys.setrecursionlimit(5000)

day = int("07")
part = int(argv[1])

with open("day07/input".format(day), "r") as f:
    data = f.read().splitlines()


part1 = 0
part2 = 70000000

class Dir:

    def __init__(self, parent=None, name="") -> None:
        self.parent = parent
        self.name = name
        self.files = {}
        self.dirs = {}
        self.total_file_size = 0

    def get_file(self, name):
        if name in self.file:
            return self.file[name]
        return None

    def add_file(self, name, size: int):
        self.files[name] = size
        self.total_file_size += size

    def add_dir(self, name):
        d = Dir(self, name)
        self.dirs[name] = d

    def get_dir(self, name):
        return self.dirs[name]

    def find_total_size_dir(self, dirs , max_val = 100000):
        for d in self.dirs.values():
            if d.total_file_size < max_val:
                dirs.append(d.total_file_size)
            if len(d.dirs) > 0:
                d.find_total_size_dir(dirs, max_val)

    def get_total_size(self):
        total = sum([self.files[i] for i in self.files])
        total += sum([self.dirs[i].total_file_size for i in self.dirs])
        self.total_file_size = total

        return total

    def find_delete_candidate(self, total_size, free_space=30000000):
        global part2
        for d in self.dirs.values():
            if ((70000000 - (total_size - d.total_file_size)) > free_space ):
                    part2 = min(part2, d.total_file_size)
            if d.dirs:
                d.find_delete_candidate(total_size, free_space) 

root = None
d = {}

def parse(data, curr_dir: Dir):
    global less_than_10
    if len(data) == 0:
        return
    c = data.pop(0).split()
    if c[0] == "$":
        if c[1] == "cd":
            if c[2] == "..":
                curr_dir.parent.total_file_size += curr_dir.total_file_size
                curr_dir = curr_dir.parent
            else:
                curr_dir = curr_dir.get_dir(c[2])
    elif c[0] == "dir":
        curr_dir.add_dir(c[1])
    else:
        curr_dir.add_file(c[1], int(c[0]))

    return parse(data, curr_dir)

d = Dir(None, "/")
root = d
data.pop(0)
parse(data, curr_dir=d)
total = root.get_total_size()
if part == 1:
    total_dirs = []
    root.find_total_size_dir(total_dirs)
    print("Part 1 {}".format(sum(total_dirs)))
if part == 2:
    root.find_delete_candidate(total)
    print("Part 2 {}".format(part2))