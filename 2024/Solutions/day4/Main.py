# Not sure if there's a better way to handle this one...
import sys
sys.path.append("../../../Helpers")
from CommonShitz import readFile

# PART 1
WHAT_TO_FIND_PART1 = ['XMAS']
TRANSFORMATIONS_PART1 = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

# PART 2
WHAT_TO_FIND_PART2 = ['MAS', 'SAM']
UPPER_LEFT = (-1,1)
UPPER_LEFT_MOVE = (1,-1)
UPPER_RIGHT = (1,1)
UPPER_RIGHT_MOVE = (-1,-1)

def check(data, coord, transform, word_check) -> bool:
    """check if IDK."""
    if (len(word_check) == 0):
        return True
    elif coord[0] < 0 or coord[1] < 0 or coord[0] > (len(data[0])-1) or coord[1] > (len(data)-1):
        return False
    elif data[coord[1]][coord[0]] == word_check[0]:
        test = (int(coord[0]) + int(transform[0]), int(coord[1]) + int(transform[1]))
        return check(data, test, transform, word_check[1:])
    else:
        return False

def calc_part1(matrix):
    """part 1 check."""
    len_x = len(matrix[0])
    len_y = len(matrix)
    rez = 0
    for y in range(len_y):
        for x in range(len_x):
            for word in WHAT_TO_FIND_PART1:
                for transformation in TRANSFORMATIONS_PART1:
                    if (matrix[y][x] == word[0]):
                        rez += check(matrix, (x,y), transformation, word)
    return rez

def calc_part2(matrix):
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
                if (check(matrix, (x + UPPER_LEFT[0], y + UPPER_LEFT[1]), UPPER_LEFT_MOVE, word)):
                    found_ul = True
                if (check(matrix, (x + UPPER_RIGHT[0], y + UPPER_RIGHT[1]), UPPER_RIGHT_MOVE, word)):
                    found_ur = True            
            # So
            if (found_ul and found_ur):
                rez += 1
                matrix[y] = matrix[y][:x] + 'G' + matrix[y][x+1:]
    return rez

def start():
    """starts masterpiece."""
    data = readFile()
    print('Part1 rez: ' + str(part1(data)))
    print('Part2 rez: ' + str(part2(data)))

def part1(data):
    """starts masterpiece part 1"""
    return calc_part1(data)

def part2(data):
    """starts masterpiece part 2"""
    return calc_part2(data)

start()