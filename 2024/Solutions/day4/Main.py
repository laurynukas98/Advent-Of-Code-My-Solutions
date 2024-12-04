# Not sure if there's a better way to handle this one...
import sys
sys.path.append("../../../Helpers")
from CommonShitz import matrix_check, start

# PART 1
WHAT_TO_FIND_PART1 = ['XMAS']
TRANSFORMATIONS_PART1 = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

# PART 2
WHAT_TO_FIND_PART2 = ['MAS', 'SAM']
UPPER_LEFT = (-1,1)
UPPER_LEFT_MOVE = (1,-1)
UPPER_RIGHT = (1,1)
UPPER_RIGHT_MOVE = (-1,-1)

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
                        rez += matrix_check(matrix, (x,y), transformation, word)
    return rez

def calc_part2(matrix) -> int:
    """part 2 check."""
    len_x = len(matrix[0])
    len_y = len(matrix)
    rez = 0
    for y in range(len_y):
        for x in range(len_x):
            # THE X
            found_ul = False
            found_ur = False
            for word in WHAT_TO_FIND_PART2:
                if matrix[y][x] == word[1] and matrix_check(matrix, (x + UPPER_LEFT[0], y + UPPER_LEFT[1]), UPPER_LEFT_MOVE, word):
                    found_ul = True
                if matrix[y][x] == word[1] and matrix_check(matrix, (x + UPPER_RIGHT[0], y + UPPER_RIGHT[1]), UPPER_RIGHT_MOVE, word):
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

start(part1, part2)