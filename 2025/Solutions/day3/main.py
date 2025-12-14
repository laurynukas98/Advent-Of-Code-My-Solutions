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
        print(maxJolt)
        rez += maxJolt
    return rez

def idr_how_this_is_called(line, size, val, max):
    test = max
    if (size == 0):
        if (test < int(val)):
            return int(val)
        return test
    if len(line) > 0 and len(line) >= size:
        for x in range(0, len(line)):
            test = idr_how_this_is_called(line[x + 1:], size - 1, val + line[x], test)
    return test

def part2_stupid_solution(data) -> str:
    """starts masterpiece part 2"""
    rez = 0
    for line in data:
        valuez = idr_how_this_is_called(line, 12, "", 0)
        print("-------")
        print(valuez)
        print("-------")
        rez += valuez
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    rez = 0
    for line in data:
        rezValue = ""
        size = 12
        set_chars = {key:(line.count(key)) for key in sorted(set(line), reverse=True)}
        toFind = {}
        for key,value in set_chars.items():
            if (size - value > 0):
                toFind[key] = value
                size -= value
            else:
                toFind[key] = size
                break
        for c in line: # Nope, this doesn't work
            if toFind[c] > 0:
                rezValue += c
                toFind[c] -= 1
        print(rezValue)
        rez += int(rezValue)
    return 'Not Implemented'
