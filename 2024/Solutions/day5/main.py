"""masterpiece"""

def ordering_check_part1(rules, page):
    for i, char in enumerate(page):
        for (x, y) in rules:
            if char == x:
                for ib, charr in enumerate(page[:i]):
                    if charr == y:
                        return False
    return True

# Build a tree recursion
def build_recursion(rules, start, array_of_available_values):
    if len(array_of_available_values) == 0:
        if ordering_check_part1(rules, start):
            return start
        else:
            return ''
    for x in range(len(start) + 1):
        testt = start.copy()
        testt.insert(x, array_of_available_values[0])
        if ordering_check_part1(rules, testt):
            if (len(array_of_available_values)) == 0:
                return testt
            value = build_recursion(rules, testt, array_of_available_values[1:])
            if value != '':
                return value
    return ''

def ordering_check_part2(rules, page) -> str:
    if not ordering_check_part1(rules, page):
        return build_recursion(rules, [page[0]], page[1:])
    return ''

def part1(data) -> str:
    """starts masterpiece part 1"""
    switch_flag = False
    rules = []
    pages = []
    for line in data:
        if line == '':
            switch_flag = True
            continue
        if switch_flag:
            pages.append(line.split(','))
        if not switch_flag:
            matched = line.split('|')
            rules.append((matched[0],matched[1]))

    rez = 0
    i = 0
    for page in pages:
        if ordering_check_part1(rules, page):
            rez += int(page[len(page)//2])
        else:
            i += 1
    print('Part 1 not working: ' + str(i))

    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    switch_flag = False
    rules = []
    pages = []
    for line in data:
        if line == '':
            switch_flag = True
            continue
        if switch_flag:
            pages.append(line.split(','))
        if not switch_flag:
            matched = line.split('|')
            rules.append((matched[0],matched[1]))

    rez = 0
    for page in pages:
        value = ordering_check_part2(rules, page)
        if value != '':
            rez += int(value[len(value)//2])
    return rez
