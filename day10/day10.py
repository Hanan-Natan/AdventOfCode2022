from sys import argv

part = int(argv[1])

with open("day10/input", "r") as f:
    data = f.read().splitlines()

if part == 1:
    OPS = {"addx":2, "noop":1}
    total_cycles = 0
    reg_X = 1
    signal_strength = 0
    signal_calc = 60
    for i in data:
        op = i.split()
        operand = int(op[1]) if len(op) > 1 else None
        for c in range(OPS[op[0]]):
            total_cycles += 1
            if total_cycles == 20:
                signal_strength = reg_X * total_cycles
            elif total_cycles == signal_calc:
                signal_strength += (reg_X * total_cycles)
                signal_calc += 40
        if operand: 
            reg_X += operand
    print(signal_strength)
else:
    OPS = {"addx":2, "noop":1}
    total_cycles = 0
    reg_X = 1
    crt_screen = [["." for _ in range(40)] for _ in range(6)]
    print(len(data))
    signal_strength = 0
    signal_calc = 60
    for i in data:
        op = i.split()
        for c in range(OPS[op[0]]):
            if ((total_cycles-(40*(total_cycles//40)))-1 <= reg_X <= (total_cycles-(40*(total_cycles//40)))+1):
                crt_screen[total_cycles//40][(total_cycles-(40*(total_cycles//40)))] = "#"
            total_cycles += 1
        reg_X += int(op[1]) if len(op) > 1 else 0
    for l in crt_screen:
        print(''.join(l))