"""masterpiece"""

from Helpers.coordz import Coord


def find_unique(data):
    rez = []
    for y in data:
        for x in y:
            if x != '.' and x != '#' and x not in rez:
                rez += [x]
    return rez

def get_points_part1(map):
    rez = []
    for (y, line_y) in enumerate(map):
        for (x, char_x) in enumerate(line_y):
            if char_x != '.':
                rez += [(char_x, Coord(y, x))]
    return rez

def produce_antinode(points):
    antinodes = []
    for x, (char_x, coord_x) in enumerate(points):
        for y, (char_y, coord_y) in enumerate(points[x + 1:]):
            if char_x == char_y:
                distance = coord_y.distance(coord_x) 
                print(char_x)
                print(char_y)
                print()
                coord_x.print()
                coord_y.print()
                print('Distance:')
                distance.print()
                print()
                coord_x.distance(distance).print()
                coord_y.transform(distance).print()
                print()
                antinodes += [coord_x.distance(distance), coord_y.transform(distance)]
    return Coord.unique_coords(antinodes)

def in_borders(points, max_x, max_y):
    return [x for x in points if x.in_distance(max_x,max_y)]

def print_map(data, points):
    for y in data:
        print(y)
    print()
    for x in points:
        data[x.y] = data[x.y][:x.x] + '#' + data[x.y][x.x + 1:]
    for y in data:
        print(y)

def part1(data) -> str:
    """starts masterpiece part 1"""
    test = get_points_part1(data)
    antinodes = produce_antinode(test)
    antinodes = in_borders(antinodes, len(data[0]), len(data))
    rez = []
    for y in antinodes:
        add = True
        for (_, x) in test:
            if y.equals(x):
                add = False
                break
        if add:
            rez += [y]
    print_map(data, rez)
    return len(rez) #428 too high

def part2(data) -> str:
    """starts masterpiece part 2"""
    return 'Not Implemented'
