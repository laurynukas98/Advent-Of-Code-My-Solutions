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

cache = {}

def down(data, level, point):
    rez = 0
    if (point < 0) and (point > len(data[0]) - 1):
        return rez
    for i in range(level, len(data)):
        if data[i][point] == '^':
            if f"{point},{i}" not in cache:
                cache[f"{point},{i}"] = down(data, i + 1, point - 1)
                cache[f"{point},{i}"] += down(data, i + 1, point + 1)
            rez += cache[f"{point},{i}"]
            return rez
    return 1

def part2(data) -> str:
    """starts masterpiece part 2"""
    index = data[0].find("S")
    return down(data, 0, index)
