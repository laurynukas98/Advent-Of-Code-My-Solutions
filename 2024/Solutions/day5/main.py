"""masterpiece"""

def ordering_check_part1(rules, page):
    for i, char in enumerate(page):
        for (x, y) in rules:
            if char == x:
                for _, charr in enumerate(page[:i]):
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
        copy_start = start.copy()
        copy_start.insert(x, array_of_available_values[0])
        if ordering_check_part1(rules, copy_start):
            value = build_recursion(rules, copy_start, array_of_available_values[1:])
            if value != '':
                return value
    return ''

def ordering_check_part2(rules, page) -> str:
    if not ordering_check_part1(rules, page):
        return build_recursion(rules, [page[0]], page[1:])
    return ''

def prepare_data(data):
    switch_flag = False
    rules = []
    pages = []
    for line in data:
        if line == '':
            switch_flag = True
            continue
        if switch_flag:
            pages.append(line.split(','))
        else:
            matched = line.split('|')
            rules.append((matched[0],matched[1]))
    return (rules, pages)

def calc_rez(functionz, data):
    (rules, pages) = prepare_data(data)
    rez = 0
    for page in pages:
        value = functionz(rules, page)
        if isinstance(value, list) or value is True:
            rez += int(value[len(value)//2] if isinstance(value, list) else page[len(page)//2])
    return rez

def part1(data) -> str:
    """starts masterpiece part 1"""
    return calc_rez(ordering_check_part1, data)

def part2(data) -> str:
    """starts masterpiece part 2"""
    return calc_rez(ordering_check_part2, data)
