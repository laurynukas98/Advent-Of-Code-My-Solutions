"""masterpiece"""
from Helpers.coordz import Coord

DIRECTIONS = [Coord(0,-1), Coord(1,0), Coord(0,1), Coord(-1,0)]

_data:list[list[str]] = []
_data2:list[list[str]] = []

"""Steal and reworked logic from day 10"""
def move(coord: Coord, direction_from: Coord):
    global _data
    te = 0
    sides = 0
    current_value = _data[coord.y][coord.x]
    (max_x, max_y) = (len(_data), len(_data[0]))
    directions = [x for x in DIRECTIONS if not x.equals(direction_from)]
    _data[coord.y] = _data[coord.y][:coord.x] + '#' + _data[coord.y][coord.x+1:]
    for x in directions:
        next_move = coord.transform(x)
        if next_move.in_distance(max_x, max_y) and _data[next_move.y][next_move.x] == current_value:
            (_sides, _te) = move(next_move, x.negation())
            sides += _sides
            te += _te
        elif (not next_move.in_distance(max_x, max_y) or _data2[next_move.y][next_move.x] != current_value):
            sides += 1
    te += 1
    return (sides, te)

def just_go(data):
    global _data
    global _data2
    _data = data.copy()
    _data2 = data.copy()
    rez = 0
    for y in range(len(_data)):
        for x in range(len(_data[y])):
            if _data[y][x] != '#':
                (sides, te) = move(Coord(x,y), Coord(0,0))
                rez += sides * te
    return rez

def part1(data) -> str:
    """starts masterpiece part 1"""
    return just_go(data)

def part2(data) -> str:
    """starts masterpiece part 2"""
    return 'Not Implemented'

#Optional
def printz(dataz):
    for y in dataz:
        print(y)