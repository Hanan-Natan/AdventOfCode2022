from sys import argv
from requests import get

day = argv[1]
url = argv[2]

cookie = open("cookie.txt", 'r').read().strip()


data = get(url.format(day), cookies={"session":cookie})
with open("./day{}/input".format(day), "wb") as file:
    file.write(data.content)

print("Done!")