"""masterpiece"""

from Helpers.coordz import Coord

DIRECTIONS = [Coord(0, 1), Coord(1, 1), Coord(1, 0), Coord(1, -1), Coord(0, -1), Coord(-1, 1), Coord(-1, 0), Coord(-1, -1)]

#-1, -1 | 0, 1  | 1, 1
#-1, 0  | 0, 0  | 1, 0
#-1, 1  | 0, -1 | 1, -1

def part1(data) -> str:
    """starts masterpiece part 1"""
    (removed, _) = filter_papers(data)
    return removed # 1376

def filter_papers(data):
    """starts masterpiece part 1"""
    max_coord = Coord(len(data), len(data[0]))
    coordz = []
    rez = 0
    for x in range(0, max_coord.x):
        for y in range(0, max_coord.y):
            coord = Coord(x, y)
            if data[coord.y][coord.x] == "@":
                count_toilet = 0
                for d_coord in DIRECTIONS:
                    t_coord = coord.transform(d_coord)
                    if t_coord.in_distance(max_coord.x, max_coord.y):
                        if (data[t_coord.y][t_coord.x] == "@"):
                            count_toilet += 1
                if count_toilet < 4:
                    coordz.append(coord)
                    rez += 1
    for t in coordz:
        tt = list(data[t.y])
        tt[t.x] = 'x'
        data[t.y] = "".join(tt)
    return (len(coordz), data) # 1376

def part2(data) -> str:
    """starts masterpiece part 2"""
    breakz = False
    rez = 0
    while not breakz:
        (removed, data) = filter_papers(data)
        if removed == 0:
            breakz = True
            break
        rez += removed
    return rez # 8587
