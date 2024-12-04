"""masterpiece"""
import os
from Helpers.coordz import Coord

def read_file(input_file):
    if not os.path.isfile(input_file):
        raise Exception('No Input File Found!')
    f = open(input_file, 'r')
    return f.read().split('\n')

def matrix_check(data, coord: Coord, transform: Coord, word_check) -> bool:
    """check if IDK."""
    if len(word_check) == 0:
        return True
    if coord.x < 0 or coord.y < 0 or coord.x > (len(data[0])-1) or coord.y > (len(data)-1):
        return False
    if data[coord.y][coord.x] == word_check[0]:
        test = coord.transform(transform)
        return matrix_check(data, test, transform, word_check[1:])
    return False

def start(part1, part2, input_file, starting_message = ''):
    """starts masterpiece."""
    print(starting_message)
    data = read_file(input_file)
    print('Part1 rez: ' + str(part1(data.copy())))
    print('Part2 rez: ' + str(part2(data.copy())))