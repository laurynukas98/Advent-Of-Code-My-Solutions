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
    try:
        while not exit:
            c_coord = coord.transform(DIRECTIONS[index_direction])
            if c_coord.x < 0 or c_coord.y < 0:
                exit = True
            if _maze[c_coord.y][c_coord.x] == '#':
                index_direction = (index_direction + 1) % 4
            elif _maze[c_coord.y][c_coord.x] == '.':
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
    return rez

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
                #print('check:')
                #print(_maze[check_point.y][check_point.x])
                #print(_maze[check_point1.y][check_point1.x])
                #print(_maze[check_point.y][check_point.x] + ' != ' + DIRECTIONS_SYMBOLS[(index_direction + 1) % 4])
                if _maze[check_point.y][check_point.x] != '.':
                    print('TRUE')
                    return True
            #elif _maze[check_point1.y][check_point1.x] != '.':
            #    print('TRUE')
            #    return True
            check_point = check_point1
    except Exception as error:
        print(error)
    return False #2642 NOPE

def solve_part2(maze, start: Coord):
    _maze = maze.copy()
    index_direction = 0
    coord = start
    exit = False
    rez = 0
    try:
        while not exit:
            c_coord = coord.transform(DIRECTIONS[index_direction])
            if c_coord.x < 0 or c_coord.y < 0:
                exit = True
            if _maze[c_coord.y][c_coord.x] == '#':
                index_direction = (index_direction + 1) % 4
            elif _maze[c_coord.y][c_coord.x] == '.':
                #if further_check(_maze, c_coord, index_direction):
                #    rez += 1
                try:
                    t1 = c_coord.transform(DIRECTIONS[index_direction])
                    if _maze[t1.y][t1.x] == '.':
                        copy_maze = _maze.copy()
                        copy_maze[t1.y] = copy_maze[t1.y][:t1.x] + '#' + copy_maze[t1.y][t1.x + 1:]
                        cc_coord = c_coord
                        c_index = index_direction
                        if solve_part1(copy_maze, cc_coord, 100000, c_index) == 0:
                            rez +=1
                    _maze[c_coord.y] = _maze[c_coord.y][:c_coord.x] + DIRECTIONS_SYMBOLS[index_direction] + _maze[c_coord.y][c_coord.x + 1:]
                except:
                    nee = 10
                coord = c_coord
            else:
                try:
                    t1 = c_coord.transform(DIRECTIONS[index_direction])
                    if _maze[t1.y][t1.x] == '.':  
                        copy_maze = _maze.copy()
                        copy_maze[t1.y] = copy_maze[t1.y][:t1.x] + '#' + copy_maze[t1.y][t1.x + 1:]
                        cc_coord = c_coord
                        c_index = index_direction
                        if solve_part1(copy_maze, cc_coord, 100000, c_index) == 0:
                            rez +=1
                    _maze[c_coord.y] = _maze[c_coord.y][:c_coord.x] + DIRECTIONS_SYMBOLS[index_direction] + _maze[c_coord.y][c_coord.x + 1:]
                except:
                    nee = 10
                coord = c_coord
                
    except Exception as error:
        print(error)
    for line in _maze:
        print(line)
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

    #return 'Not Implemented'

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
    return solve_part2(data,start_coord)
