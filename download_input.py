from sys import argv
from pathlib import Path
from requests import get

day = int(argv[1])
url = f"https://adventofcode.com/2022/day/{day:02d}/input"

template = f"""from sys import argv

part = int(argv[1])

with open("day{day:02d}/input", "r") as f:
    data = f.read()

if part == 1:
    pass
else:
    pass
"""

cookie = open("cookie.txt", 'r').read().strip()

# create file template
template_file = Path(f"./day{day:02d}/day{day:02d}.py")
template_file.parent.mkdir(exist_ok=True, parents=True)
template_file.write_text(template)

# download input
data = get(url, cookies={"session":cookie})

# write input file
input_file = Path(f"./day{day:02d}/input")
input_file.parent.mkdir(exist_ok=True, parents=True)
input_file.write_text(data.content.decode())

print("Done!")