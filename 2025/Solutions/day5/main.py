"""masterpiece"""

def process_data(data):
    intervals = []
    to_check = []
    next_data = False
    for l in data:
        if (l == ""):
            next_data = True
            continue
        if not next_data:
            (x, y) = l.split('-')
            intervals.append((int(x),int(y)))
        elif next_data:
            to_check.append(int(l))
    return (intervals, to_check)

def check_if_fresh(intervals, value):
    for (x, y) in intervals:
        if (value >= x and value <= y):
            return True
    return False

def part1(data) -> str:
    """starts masterpiece part 1"""
    (intervals, to_check) = process_data(data)
    rez = 0
    for x in to_check:
        rez += 1 if check_if_fresh(intervals, x) else 0
    return rez

def part2(data) -> str: # optimise this better or more readable
    """starts masterpiece part 2"""
    (intervals, _) = process_data(data)
    were_changes = True
    interval_new = []
    while were_changes:
        were_changes = False
        interval_new = [intervals[0]]
        for (x, y) in intervals[1:]:
            ate = False
            for i in range(0, len(interval_new)):
                (c_x, c_y) = interval_new[i]
                if (c_x >= x and c_y <= y):
                    interval_new[i] = (x,y)
                    ate = True
                    were_changes = True
                elif (c_x <= x and c_y >= y):
                    ate = True
                    were_changes = True
                elif (c_x <= x and x <= c_y <= y):
                    interval_new[i] = (c_x, y)
                    ate = True
                    were_changes = True
                elif (c_x >= x and c_y >= y >= c_x):
                    interval_new[i] = (x, c_y)
                    ate = True
                    were_changes = True
                elif (c_x == x and c_y == y):
                    ate = True
            if ate == False:
                interval_new.append((x, y))
        intervals = interval_new
        print(interval_new)
    rez = 0
    for (x,y) in interval_new:
        rez += y - x + 1
    return rez
