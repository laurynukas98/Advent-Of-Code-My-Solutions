
def read_file():
    f = open('input.data', 'r')
    return f.read().split('\n')

def matrix_check(data, coord, transform, word_check) -> bool:
    """check if IDK."""
    if len(word_check) == 0:
        return True
    if coord[0] < 0 or coord[1] < 0 or coord[0] > (len(data[0])-1) or coord[1] > (len(data)-1):
        return False
    if data[coord[1]][coord[0]] == word_check[0]:
        test = (int(coord[0]) + int(transform[0]), int(coord[1]) + int(transform[1]))
        return matrix_check(data, test, transform, word_check[1:])
    return False

def start(part1, part2):
    """starts masterpiece."""
    data = read_file()
    print('Part1 rez: ' + str(part1(data.copy())))
    print('Part2 rez: ' + str(part2(data.copy())))