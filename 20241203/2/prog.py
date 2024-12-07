import math
import sys


def interpret_assembly(text):
    variables = {}
    metkas = {}
    commands = []
    output = []

    opers = {
        'add': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'div': lambda x, y: x / y if y != 0 else math.inf,
    }
    comprs = {
        'ifeq': lambda x, y: x == y,
        'ifne': lambda x, y: x != y,
        'ifgt': lambda x, y: x > y,
        'ifge': lambda x, y: x >= y,
        'iflt': lambda x, y: x < y,
        'ifle': lambda x, y: x <= y,
    }

    for ind, line in enumerate(text.splitlines()):
        line = line.strip()
        if not line:
            continue

        if ":" in line:
            m, *hvost = line.split(":", maxsplit=1)
            metkas[m.strip()] = len(commands)
            line = hvost[0].strip() if hvost else ""

        if line:
            commands.append(line.split())

    for cmd in commands:
        if cmd[0] in comprs and cmd[3] not in metkas:
            return

    counter = 0
    while counter < len(commands):
        cmd = commands[counter]
        op = cmd[0]

        if op == "stop":
            break

        elif op == "store":
            try:
                value = float(cmd[1])
            except ValueError:
                value = 0.0
            variables[cmd[2]] = value

        elif op in opers:
            src = variables.get(cmd[1], 0)
            operand = variables.get(cmd[2], 0)
            variables[cmd[3]] = opers[op](src, operand)

        elif op in comprs:
            src = variables.get(cmd[1], 0)
            operand = variables.get(cmd[2], 0)
            if comprs[op](src, operand):
                counter = metkas[cmd[3]]
                continue

        elif op == "out":
            output.append(variables.get(cmd[1], 0))

        counter += 1
    if output:
        print(output[-1])

s = sys.stdin.read()
interpret_assembly(s)

