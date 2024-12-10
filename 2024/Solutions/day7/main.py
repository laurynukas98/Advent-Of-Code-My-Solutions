"""masterpiece"""

def multiplication(a, b):
    return a * b

def addition(a, b):
    return a + b

def concatenation(a, b):
    return int(str(a) + str(b))

ACTIONS_PART1 = [multiplication, addition]
ACTIONS_PART2 = [multiplication, addition, concatenation]

def run_thingy(value_a, array, expectation, actions = ACTIONS_PART1):
    if len(array) == 0:
        return value_a
    value_b = array[0]
    for action in actions:
        rez = action(value_a, value_b)
        what_got = run_thingy(rez, array[1:], expectation, actions)
        if expectation == what_got:
            return what_got
    
def parse_data(line):
    ye = line.split(':')
    expectation = int(ye[0])
    numbers = [int(x) for x in ye[1].strip().split(' ')]
    return (expectation, numbers)

def part1(data) -> str:
    """starts masterpiece part 1"""
    rez = 0
    for line in data:
        (expectation, numbers) = parse_data(line)
        what_got = run_thingy(0, numbers, expectation)
        if what_got != None:
            rez += what_got
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    rez = 0
    for line in data:
        (expectation, numbers) = parse_data(line)
        what_got = run_thingy(0, numbers, expectation, ACTIONS_PART2)
        if what_got != None:
            rez += what_got
    return rez
