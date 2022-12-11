from sys import argv

part = int(argv[1])

with open("day11/input", "r") as f:
    data = f.read().splitlines()

operations = {0: lambda x: x * 11,
              1: lambda x: x + 1,
              2: lambda x: x * 7,
              3: lambda x: x + 3,
              4: lambda x: x + 6,
              5: lambda x: x + 5,
              6: lambda x: x * x,
              7: lambda x: x + 7}

test_op = {0: lambda x: x * 19,
           1: lambda x: x + 6,
           2: lambda x: x * x,
           3: lambda x: x + 3}


def parse(data):
    monkies = {}
    i = 0
    while i < len(data):
        if len(data[i]) == 0:
            i += 1
        m = int(data[i].split()[-1][0])
        items = [int(i) for i in data[i+1].split(": ")[1:][0].split(",")]
        op = operations[m]
        # op = test_op[m]
        test = int(data[i+3].split()[-1])
        throw = (int(data[i+4].split()[-1]), int(data[i+5].split()[-1]))
        monkies[m] = {"items": items, "op": op, "test": test, "throw": throw}
        i += 6

    return monkies

if part == 1:
    m = parse(data)
    counter = [0 for _ in range(len(m))]
    for _ in range(20):
        for round in range(len(m)):
            while m[round]["items"]:
                item = m[round]["items"].pop(0)
                counter[round] += 1
                op_res = m[round]["op"](item)//3
                if op_res % m[round]["test"] == 0:
                    m[m[round]["throw"][0]]["items"].append(op_res)
                else:
                    m[m[round]["throw"][1]]["items"].append(op_res)
    res = sorted(counter)
    print(res[-1] * res[-2])
else:

    m = parse(data)

    # This lcm value i copied from: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/11.py
    lcm = 1
    for i in m:
        lcm = (lcm*m[i]["test"])#//math.gcd(lcm,x)
    #
    counter = [0 for _ in range(len(m))]
    for _ in range(10000):
        for round in range(len(m)):
            for item in m[round]["items"]:
                counter[round] += 1
                op_res = m[round]["op"](item)
                op_res %= lcm
                if op_res % m[round]["test"] == 0:
                    m[m[round]["throw"][0]]["items"].append(op_res)
                else:
                    m[m[round]["throw"][1]]["items"].append(op_res)
            m[round]["items"] = []
    res = sorted(counter)
    print(res[-1] * res[-2])
