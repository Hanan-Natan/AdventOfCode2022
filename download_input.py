from sys import argv
from pathlib import Path
from requests import get

day = argv[1]
url = argv[2]

template = f"""from sys import argv

day = int("{day}")
part = int(argv[1])

with open("day{{}}/input".format(day), "r") as f:
    data = f.read()
"""

cookie = open("cookie.txt", 'r').read().strip()

# create file template
template_file = Path("./day{}/day{}.py".format(day, day))
template_file.parent.mkdir(exist_ok=True, parents=True)
template_file.write_text(template.format(day))

# download input
data = get(url.format(day), cookies={"session":cookie})

# write input file
input_file = Path("./day{}/input".format(day))
input_file.parent.mkdir(exist_ok=True, parents=True)
input_file.write_text(data.content.decode())

print("Done!")