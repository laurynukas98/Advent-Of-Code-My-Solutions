"""masterpiece"""

def part1(data) -> str:
    """starts masterpiece part 1"""
    arrays = "".join(data).split(",")
    rez = 0
    for x in arrays:
        (min, max) = x.split("-")
        for y in list(range(int(min), int(max)+1)):
            strY = str(y)
            invalidID = True
            for c in set(strY):
                if (strY.count(c) % 2 == 1):
                    invalidID = False
                    break
            if invalidID:
                (x1, x2) = (strY[: (len(strY) // 2)] , strY[len(strY) // 2 :])
                if int(x1) != 0 and int(x2) != 0 and (int(x1) / int(x2)) == 1:
                    rez += y
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    arrays = "".join(data).split(",")
    rez = 0
    for x in arrays:
        (min, max) = x.split("-")
        for y in list(range(int(min), int(max)+1)):
            strY = str(y)
            invalidID = True
            for c in set(strY):
                if (strY.count(c) == 1):
                    invalidID = False
                    break
            if invalidID:
                    for i in range(1, (len(strY) // 2) + 1):
                        if len(strY) % i == 0 and strY.count(strY[:i]) == (len(strY) / i):
                            rez += y
                            break    
    return rez
