"""masterpiece"""
from Helpers.coordz import Coord

_data = []

def get_points(data: list[list[str]]):
    rez = []
    for (y, line_y) in enumerate(data):
        for (x, char_x) in enumerate(line_y):
            if char_x != '.':
                rez += [(char_x, Coord(x, y))]
    return rez

def antinodes(coord1, coord2):
    distance = coord1.distance(coord2)
    antinode1 = coord1.transform(distance)
    antinode2 = coord2.transform(distance.negation())
    return [antinode1, antinode2]

def antinodes_part2(coord1: Coord, coord2: Coord):
    rez = []
    max_x = len(_data[0])
    max_y = len(_data)
    distance = coord1.distance(coord2)
    point1 = coord1
    while point1.in_distance(max_x,max_y):
        rez.append(point1)
        point1 = point1.transform(distance)
    point2 = coord2
    while point2.in_distance(max_x,max_y):
        rez.append(point2)
        point2 = point2.transform(distance.negation())
    return rez

def produce_antinodes(points: list[Coord], func = antinodes):
    _antinodes = []
    for x, (char_x, coord_x) in enumerate(points):
        for _, (char_y, coord_y) in enumerate(points[x + 1:]):
            if char_x == char_y:
                _antinodes += func(coord_x, coord_y)
    return unique_antinodes(_antinodes)

def unique_antinodes(_antinodes: list[Coord]):
    uniquelist:list[Coord] = []
    for antinode in _antinodes:
        add = True
        for unique_antinode in uniquelist:
            if unique_antinode.equals(antinode):
                add = False
                break
        if add:
            uniquelist.append(antinode)
    return uniquelist

def in_borders(points: list[Coord], max_x: int, max_y: int):
    return [x for x in points if x.in_distance(max_x,max_y)]

def part1(data) -> str:
    """starts masterpiece part 1"""
    test = get_points(data)
    _antinodes = produce_antinodes(test)
    _antinodes = in_borders(_antinodes, len(data[0]), len(data))
    rez = _antinodes
    return len(rez) #341 rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    global _data
    _data = data
    test = get_points(data)
    _antinodes = produce_antinodes(test, antinodes_part2)
    _antinodes = in_borders(_antinodes, len(data[0]), len(data))
    rez = _antinodes
    return len(rez) #1134 rez

# Optional stuff
def print_map(data, points: list[Coord]):
    for y in data:
        print(y)
    print()
    for x in points:
        data[x.y] = data[x.y][:x.x] + '#' + data[x.y][x.x + 1:]
    for y in data:
        print(y)
