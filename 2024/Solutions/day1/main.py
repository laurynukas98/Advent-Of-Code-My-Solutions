"""masterpiece"""

def _sum(x, y) -> int:
    """starts masterpiece part 1"""
    rez = 0
    for i in range(len(x)):
        rez += abs(x[i] - y[i])
    return rez

def part1(data) -> str:
    """starts masterpiece part 1"""
    test = [(x.split()) for x in data]

    lList = [int(x[0]) for x in test]
    rList = [int(x[1]) for x in test]

    rList.sort()
    lList.sort()

    # Part 1
    return _sum(rList,lList)

# Probably this  piece of garbage needs to be reworked
def part2(data) -> str:
    """starts masterpiece part 2"""
    test = [(x.split()) for x in data]

    lList = [int(x[0]) for x in test]
    rList = [int(x[1]) for x in test]

    rList.sort()
    lList.sort()

    rListCount = dict(map(lambda x: (x, rList.count(x)), rList))
    summ = 0
    for (key, x) in rListCount.items():
        summ += x * key * lList.count(key)

    return summ
