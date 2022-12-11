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
    pass
