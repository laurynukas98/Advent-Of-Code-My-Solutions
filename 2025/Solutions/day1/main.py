"""masterpiece"""
import math

def part1(data) -> str:
    """starts masterpiece part 1"""
    current = 50
    min = 0
    max = 99
    rez = 0
    for x in data:
        (direction, ticks) = (x[0],int(x[1:]))
        current += ((-1 if (direction == 'L') else 1) * ticks)
        current = current % 100
        print(direction)
        print(ticks)
        print(current)
        rez += 1 if current == 0 else 0
        print("EUEEE")
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    current = 50
    min = 0
    max = 99
    rez = 0
    for x in data:
        (direction, ticks) = (x[0],int(x[1:]))
        current += ((-1 if (direction == 'L') else 1) * ticks)
        print(abs(math.trunc(-155 / 100)))
        #print("WHAT = ")
        #print( (math.trunc(current / 100) + 1))
        rez += (abs(math.trunc(current / 100)) + 1) if (current < 1 and (-1 * ticks) != current) or current > 99 else 0
        current = current % 100
        #print(direction)
        #print(ticks)
        #print(current)
    return 'Not Implemented'
