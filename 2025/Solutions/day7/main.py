"""masterpiece"""

def part1(data) -> str:
    """starts masterpiece part 1"""
    index = data[0].find("S")
    drops = [index]
    split = 0
    for l in data[1:]:
        new_drops = []
        for drop in drops:
            if l[drop] == "^":
                split += 1
                if (drop - 1 > -1):
                    new_drops.append(drop - 1)
                if (drop + 1 < len(data[0])):
                    new_drops.append(drop + 1)
            elif l[drop] == ".":
                new_drops.append(drop)
        drops = list(set(new_drops))
    return split

def down(data, level, point):
    rez = 0
    if (point < 0) and (point > len(data[0]) - 1):
        return 0
    for i in range(level, len(data)):
        if data[i][point] == '^':
            rez += down(data, i + 1, point - 1)
            rez += down(data, i + 1, point + 1)
            rez += 1
            return rez
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    index = data[0].find("S")
    drops = [index]
    split = 0
    print(down(data, 0, index) + 1)
    #for l in data[1:]:
    #    gee = 0
    #    new_drops = []
    #    for drop in drops:
    #        if l[drop] == "^":
    #            gee += 1
    #            if (drop - 1 > -1):
    #                new_drops.append(drop - 1)
    #            if (drop + 1 < len(data[0])):
    #                new_drops.append(drop + 1)
    #        elif l[drop] == ".":
    #            new_drops.append(drop)
    #    drops = list(set(new_drops))
    #    split += gee * 2
    print(split)
    return 'Not Implemented'
