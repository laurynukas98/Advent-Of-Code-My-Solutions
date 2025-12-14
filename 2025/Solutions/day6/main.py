"""masterpiece"""

import re

def do_actionz(arr, action):
    rez = 0
    match action:
        case "+":
            rez = sum(arr)
        case "-":
            for i in arr:
                rez -= i
        case "*":
            rez = 1
            for i in arr:
                rez *= i
        case "/":
            rez = 1
            for i in arr:
                rez /= i
    return rez

def part1(data) -> str:
    """starts masterpiece part 1"""
    rez = 0
    values = []
    for l in data[:-1]: 
        values.append(list(map(int, re.findall("[0-9]+",l))))
    actions = re.findall("[*+-/]",data[-1])
    for x in range(0, len(values[0])):
        action = actions[x]
        arrayz = []
        for y in range(0, len(values)):
            arrayz.append(values[y][x])
        rez += do_actionz(arrayz, action)
    return rez

def part2(data) -> str:
    dataReversed = [x[::-1] for x in data]
    skip = False
    values = [[] for _ in range(0, len(dataReversed))]
    rez = 0
    action = ""
    brk = 0
    for x in range(0, len(dataReversed[0]) + 1):
        for y in range(0, len(dataReversed)):
            if skip:
                value = do_actionz([int("".join(x)) for x in values if x], action)
                rez += value
                values = [[] for _ in range(0, len(dataReversed))]
                skip = False
                brk = x
                break
            else:
                if dataReversed[y][x] in ["+", "-", "*"]:
                    action = dataReversed[y][x]
                    skip = True
                elif dataReversed[y][x] != ' ':
                    values[x - brk].append(dataReversed[y][x])
    return rez