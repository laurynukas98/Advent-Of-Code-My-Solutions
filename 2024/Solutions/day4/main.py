"""masterpiece"""
from Helpers.common_shitz import matrix_check
from Helpers.coordz import Coord

# PART 1
WHAT_TO_FIND_PART1 = ['XMAS']
TRANSFORMATIONS_PART1 = [Coord(0,1),Coord(0,-1),Coord(1,0),Coord(-1,0),Coord(1,1),Coord(-1,1),Coord(1,-1),Coord(-1,-1)]

# PART 2
WHAT_TO_FIND_PART2 = ['MAS', 'SAM']
UPPER_LEFT = Coord(-1,1)
UPPER_LEFT_MOVE = Coord(1,-1)
UPPER_RIGHT = Coord(1,1)
UPPER_RIGHT_MOVE = Coord(-1,-1)

def calc_part1(matrix) -> int:
    """part 1 check."""
    len_x = len(matrix[0])
    len_y = len(matrix)
    rez = 0
    for y in range(len_y):
        for x in range(len_x):
            for word in WHAT_TO_FIND_PART1:
                for transformation in TRANSFORMATIONS_PART1:
                    if matrix[y][x] == word[0]:
                        rez += matrix_check(matrix, Coord(x,y), transformation, word)
    return rez

def calc_part2(matrix) -> int:
    """part 2 check."""
    len_x = len(matrix[0])
    len_y = len(matrix)
    rez = 0
    for y in range(len_y):
        for x in range(len_x):
            coord = Coord(x,y)
            # THE X
            found_ul = False
            found_ur = False
            for word in WHAT_TO_FIND_PART2:
                if matrix[y][x] == word[1] and matrix_check(matrix, coord.transform(UPPER_LEFT), UPPER_LEFT_MOVE, word):
                    found_ul = True
                if matrix[y][x] == word[1] and matrix_check(matrix, coord.transform(UPPER_RIGHT), UPPER_RIGHT_MOVE, word):
                    found_ur = True
            # So
            if (found_ul and found_ur):
                rez += 1
                matrix[y] = matrix[y][:x] + 'G' + matrix[y][x+1:]
    return rez

def part1(data) -> str:
    """starts masterpiece part 1"""
    return calc_part1(data)

def part2(data) -> str:
    """starts masterpiece part 2"""
    return calc_part2(data)
