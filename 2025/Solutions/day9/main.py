"""masterpiece"""

from Helpers.coordz import Coord


def part1(data) -> str:
    """starts masterpiece part 1"""
    beeg = 0
    for index, point in enumerate(data):
        for point2 in data[index+1:]:
            x,y = list(map(int, point.split(",")))
            x2,y2 = list(map(int, point2.split(",")))
            value = (abs(x - x2) + 1) * (abs(y - y2) + 1)
            beeg = value if beeg < value else beeg
    return beeg

# 2@@@4
# @ | @
# @ | @
# 3@@@1

def check_crossing(data, check_point1, check_point2):
    #point1 = (max([check_point1.x, check_point2.x]), max([check_point1.y, check_point2.y])) 
    #point2 = (min([check_point1.x, check_point2.x]), min([check_point1.y, check_point2.y]))
    #point3 = (min([check_point1.x, check_point2.x]), max([check_point1.y, check_point2.y]))
    #point4 = (max([check_point1.x, check_point2.x]), min([check_point1.y, check_point2.y]))
    minx = min([check_point1.x, check_point2.x])
    maxx = max([check_point1.x, check_point2.x])
    miny = min([check_point1.y, check_point2.y])
    maxy = max([check_point1.y, check_point2.y])
    for index, pointt in enumerate(data[:-1]):
        (pointgX, pointgY) = list(map(int,pointt.split(",")))
        (pointg2X, pointg2Y) = list(map(int,data[index+1].split(",")))
        if int(pointgX) == int(pointg2X): #vertic
            mingy = min([pointgY, pointg2Y])
            maxgy = max([pointgY, pointg2Y])
            if minx <= pointgX <= maxx and (miny < mingy < maxy or miny < maxgy < maxy or mingy < miny < maxgy or mingy < maxy < maxgy):
                return True
        else: # horizon
            mingx = min([pointgX, pointg2X])
            maxgx = max([pointgX, pointg2X])
            if miny <= pointgY <= maxy and (minx < mingx < maxx or minx < maxgx < maxx or mingx < minx < maxgx or mingx < maxx < maxgx):
                return True
    return False

def part2(data) -> str:
    """starts masterpiece part 2"""
    beeg = 0
    points = []
    for index, point in enumerate(data[::-1]):
        for point2 in data[index+1:]:
            x,y = list(map(int, point.split(",")))
            x2,y2 = list(map(int, point2.split(",")))
            value = (abs(x - x2) + 1) * (abs(y - y2) + 1)
            if (beeg < value) and not check_crossing(data, Coord(x,y), Coord(x2,y2)):
                points = [Coord(x,y), Coord(x2,y2)]
                beeg = value if beeg < value else beeg
    points[0].print()
    points[1].print()
    #return beeg
    return 'Not Implemented'
