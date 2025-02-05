"""masterpiece"""
from Helpers.coordz import Coord
import re

def read_data(data):
    rez = []
    reading = True
    pattern = r"X=?([+-]?\d+),\s*Y=?([+-]?\d+)"
    while reading:
        if len(data) is 0:
            reading = False
        elif data[0] == '':
            data = data[1:]
        else:
            match1 = re.search(pattern, data[0])
            match2 = re.search(pattern, data[1])
            match3 = re.search(pattern, data[2])
            rez.append({
                'A': Coord(int(match1.group(1)),int(match1.group(2))),
                'B': Coord(int(match2.group(1)),int(match2.group(2))),
                'Prize': Coord(int(match3.group(1)),int(match3.group(2))),
            })
            data = data[3:]
    return rez

#Cramer method
# aN+bM=X
# cN+dM=Y
# X and Y is prize
# N and M is A and B button pressed
# a and b movement to X
# c and d movement to Y
def find_shit(test, correction = 0):
    X = test['Prize'].x + correction
    Y = test['Prize'].y + correction
    a = test['A'].x
    b = test['B'].x
    c = test['A'].y
    d = test['B'].y
    N = (X * d - b * Y) / (a * d - b * c)
    M = (a * Y - X * c) / (a * d - b * c)
    if N.is_integer() and M.is_integer():
        return (N,M)
    return None

def run(data, correction = 0):
    test = read_data(data)
    rez = 0
    for x in test:
        solution = find_shit(x, correction)
        if solution is not None:
            rez += (solution[0] * 3 + solution[1])
    return int(rez)

def part1(data) -> str:
    """starts masterpiece part 1"""
    return run(data)

def part2(data) -> str:
    """starts masterpiece part 2"""
    return run(data, 10000000000000)
