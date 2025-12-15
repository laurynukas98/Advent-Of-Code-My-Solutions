"""masterpiece"""

def part1(data) -> str:
    """starts masterpiece part 1"""
    rez = 0
    for line in data:
        maxJolt = 0
        for x in range(0, len(line)):
            for y in range(x + 1, len(line)):
                calc = int(line[x] + line[y])
                if calc > maxJolt:
                    maxJolt = calc
        rez += maxJolt
    return rez

def idr_how_this_is_called(line, size, val, max): # Optimise because too sloowww
    test = max
    if (size == 0):
        if (test < int(val)):
            return int(val)
        return test
    if (val != '' and test > int(val) * (10**size)):
        return test
    if len(line) > 0 and len(line) >= size:
        for x in range(0, len(line)):
            test = idr_how_this_is_called(line[x + 1:], size - 1, val + line[x], test)
    return test

def part2(data) -> str:
    """starts masterpiece part 2"""
    rez = 0
    for line in data:
        valuez = idr_how_this_is_called(line, 12, "", 0)
        rez += valuez
    return rez
