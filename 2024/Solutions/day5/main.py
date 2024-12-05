"""masterpiece"""
import re

def ordering_check_part1(rules, page):
    for i, char in enumerate(page):
        for (x, y) in rules:
            if char == x:
                for ib, charr in enumerate(page[:i]):
                    if charr == y:
                        return False
    return True

def ordering_check_part2(rules, page):
    for i, char in reversed(list(enumerate(page))):
        for (x, y) in rules:
            if char == x:
                for ib, charr in enumerate(page[i:]):
                    if charr == y:
                        for (xx,yy) in rules:
                            test = page.copy()
                            # continue laterz
                        return False
    return True

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
    for page in pages:
        if ordering_check_part1(rules, page):
            #print(page)
            rez += int(page[len(page)//2])

    
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    return 'Not Implemented'
