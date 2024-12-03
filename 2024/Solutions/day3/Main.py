# Not sure if there's a better way to handle this one...
import sys
import re
sys.path.append("../../../Helpers")
from CommonShitz import readFile

def regex_rizz_found_part1(line) -> list[str]:
    """part 3 regex."""
    return re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", line)

def regex_rizz_found_part2(line) -> list[str]:
    """part 2 regex."""
    test = re.sub(r"(don't\(\)).*?(do\(\))","", line)
    test = re.sub(r"(don't\(\)).*","", test)
    return re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", test)

def multiplicationz(line) -> int:
    """do multiplication."""
    test = re.match(r"mul\((.*),(.*)\)", line)
    return int(test.group(1)) * int(test.group(2))

def start():
    """starts masterpiece."""
    data = readFile()
    print('Part1 rez: ' + str(part1(data)))
    print('Part2 rez: ' + str(part2(data)))

def part1(data) -> str:
    """starts masterpiece part 1"""
    found = []
    for line in data:
        found += regex_rizz_found_part1(line)
    rez = 0
    for x in found:
        rez += multiplicationz(x)
    return rez

def part2(data) -> str:
    """starts masterpiece part 2"""
    found = regex_rizz_found_part2("".join(data))
    rez = 0
    for x in found:
        rez += multiplicationz(x)
    return rez

start()