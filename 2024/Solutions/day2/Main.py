# Not sure if there's a better way to handle this one...
import sys
sys.path.append("../../../Helpers")
from CommonShitz import start

MAXDIFF = 3

def maxdiff_rule(a, b) -> bool:
    """checks maxdiff condition."""
    return abs(a-b) > MAXDIFF

#rules:
def increasing_or_decreasing_and_no_maxdiff(line) -> bool:
    """check line for all conditions."""
    order = '0'
    for x in range(len(line)-1):
        determ = '-' if line[x] > line[x+1] else ('+' if line[x] < line[x+1] else '0')
        diff_rule = maxdiff_rule(line[x],line[x+1])
        if determ == '0' or order not in ('0', determ) or diff_rule:
            return False
        order = determ
    return True

def part1(data) -> str:
    """starts masterpiece part 1"""
    count = 0
    for x in data:
        count += increasing_or_decreasing_and_no_maxdiff([int(x) for x in x.split()])
    return count

def part2(data) -> str:
    """starts masterpiece part 2"""
    count = 0
    for x in data:
        line = [int(x) for x in x.split()]
        for y in range(len(line)):
            if increasing_or_decreasing_and_no_maxdiff(line[:y]+line[y+1:]):
                count += 1
                break
    return count

start(part1, part2)
