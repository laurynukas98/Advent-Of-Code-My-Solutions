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
    print(values)
    actions = re.findall("[*+-/]",data[-1])
    print(actions)
    for x in range(0, len(values[0])):
        action = actions[x]
        arrayz = []
        for y in range(0, len(values)):
            arrayz.append(values[y][x])
        rez += do_actionz(arrayz, action)
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    actions = re.findall("[*+]\s*",data[-1])
    actions_s = re.findall("[*+-/]",data[-1])
    values = []
    for l in data[:-1]: 
        values.append(re.findall("\s*\d+\s*",l))
    rez = 0
    reversed_shit = []
    for x in range(0, len(values[0])):
        action = actions[x]
        arrayz = []
        for y in range(0, len(values)):
            arrayz.append(values[y][x])
        size_test = len(action) - 1
        another_one = []
        for i in arrayz:
            yes = []
            for c in i[:-1][::-1] if i[-1] == " " else i[::-1]:
                yes.append(c)
            another_one.append(yes)
        reversed_shit.append(another_one)
    #print(reversed_shit)
    #print(["".join(x) for x in reversed_shit])
    print([list(("".join(y)) for y in x) for x in reversed_shit])
    print(values)
    return 'Not Implemented'
