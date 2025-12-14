"""masterpiece"""

def part1(data) -> str:
    """starts masterpiece part 1"""
    current = 50
    rez = 0
    for x in data:
        (direction, ticks) = (x[0],int(x[1:]))
        current += ((-1 if (direction == 'L') else 1) * ticks)
        current = current % 100
        rez += 1 if current == 0 else 0
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    current = 50
    rez = 0
    for x in data:
        (direction, ticks) = (x[0],int(x[1:]))
        b_current = current
        current += ((-1 if (direction == 'L') else 1) * ticks)
        rez += (abs(current) // 100) + (1 if b_current != 0 and current <= 0 else 0)
        current = current % 100
    return rez
