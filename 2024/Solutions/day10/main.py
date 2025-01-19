"""masterpiece"""
from Helpers.coordz import Coord

DIRECTIONS = [Coord(0,-1), Coord(1,0), Coord(0,1), Coord(-1,0)]

_data:list[list[str]] = []

def move(coord: Coord, direction_from: Coord):
    current_value = _data[coord.y][coord.x]
    if current_value == '#':
        return 0
    if int(current_value) == 9:
        _data[coord.y] = _data[coord.y][:coord.x] + '#' + _data[coord.y][coord.x+1:]
        return 1
    rez = 0
    max_x = len(_data)
    max_y = len(_data[0])
    directions = [x for x in DIRECTIONS if not x.equals(direction_from) and coord.transform(x).in_distance(max_x,max_y)]
    _data[coord.y] = _data[coord.y][:coord.x] + '#' + _data[coord.y][coord.x+1:]
    for x in directions:
        next_move = coord.transform(x)
        if _data[next_move.y][next_move.x] != '#' and int(_data[next_move.y][next_move.x]) == (int(current_value) + 1):
            rez += move(next_move, x.negation())
    return rez

def move_part2(coord: Coord, direction_from: Coord):
    current_value = _data[coord.y][coord.x]
    if int(current_value) == 9:
        return 1
    rez = 0
    max_x = len(_data)
    max_y = len(_data[0])
    directions = [x for x in DIRECTIONS if not x.equals(direction_from) and coord.transform(x).in_distance(max_x,max_y)]
    for x in directions:
        next_move = coord.transform(x)
        if int(_data[next_move.y][next_move.x]) == (int(current_value) + 1):
            rez += move_part2(next_move, x.negation())
    return rez

def part1(data) -> str:
    """starts masterpiece part 1"""
    global _data
    rez = 0
    for (y, line_y) in enumerate(data):
        for (x, char_x) in enumerate(line_y):
            if char_x == '0':
                _data = data.copy()
                t = move(Coord(x,y), Coord(0,0))
                rez += t
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    global _data
    rez = 0
    for (y, line_y) in enumerate(data):
        for (x, char_x) in enumerate(line_y):
            if char_x == '0':
                _data = data.copy()
                t = move_part2(Coord(x,y), Coord(0,0))
                rez += t
    return rez
