"""masterpiece"""

from Helpers.coordz import Coord


DIRECTIONS = [Coord(0,-1), Coord(1,0), Coord(0,1), Coord(-1,0)]
DIRECTIONS_SYMBOLS = ['^', '>', 'v', '<']

def solve_part1(maze, start: Coord, tries: int = 0, index_direction: int = 0):
    _maze = maze.copy()
    coord = start
    exit = False
    rez = 1
    i = 0
    for_part2_points = []
    try:
        while not exit:
            c_coord = coord.transform(DIRECTIONS[index_direction])
            if c_coord.x < 0 or c_coord.y < 0:
                exit = True
            if _maze[c_coord.y][c_coord.x] == '#':
                index_direction = (index_direction + 1) % 4
            elif _maze[c_coord.y][c_coord.x] == '.':
                for_part2_points += [Coord(c_coord.x, c_coord.y)]
                _maze[c_coord.y] = _maze[c_coord.y][:c_coord.x] + '^' + _maze[c_coord.y][c_coord.x + 1:]
                rez = rez + 1
                coord = c_coord
            else:
                coord = c_coord
            if tries != 0 and i > tries:
                return 0
            i += 1
    except Exception as e:
        return rez
    return (rez, for_part2_points)

def further_check(_maze, c_coord, index_direction):
    check_point = c_coord
    check_exit = False
    dir = DIRECTIONS[(index_direction + 1) % 4]
    try:
        while not check_exit:
            check_point1 = check_point.transform(dir)
            if check_point1.x < 0 or check_point1.y < 0:
                check_exit = True
            elif _maze[check_point1.y][check_point1.x] == '#':
                if _maze[check_point.y][check_point.x] != '.':
                    return True
            check_point = check_point1
    except Exception as error:
        print(error)
    return False

def solve_part2_real(maze, start: Coord, points: list[Coord]):
    rez = 0
    for c in points:
        maze_c = maze.copy()
        maze_c[c.y] = maze_c[c.y][:c.x] + '#' + maze_c[c.y][c.x + 1:]
        if solve_part1(maze_c, start, 20000) == 0:
            rez += 1
    return rez

def part1(data) -> str:
    """starts masterpiece part 1"""
    start_coord = ''
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '^':
                start_coord = Coord(x,y)
                break
        if start_coord != '':
            break
    return solve_part1(data,start_coord)

def part2(data) -> str:
    """starts masterpiece part 2"""
    start_coord = ''
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '^':
                start_coord = Coord(x,y)
                break
        if start_coord != '':
            break
    (_, points) = solve_part1(data,start_coord)
    return solve_part2_real(data, start_coord, points)
