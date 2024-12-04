"""masterpiece"""
import re

def regex_rizz_found_part1(line: str) -> list[str]:
    """part 3 regex."""
    return re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", line)

def regex_rizz_found_part2(line: str) -> list[str]:
    """part 2 regex."""
    test = re.sub(r"(don't\(\)).*?(do\(\))","", line)
    test = re.sub(r"(don't\(\)).*","", test)
    return regex_rizz_found_part1(test)

def multiplicationz(line: str) -> int:
    """do multiplication."""
    test = re.match(r"mul\((.*),(.*)\)", line)
    return int(test.group(1)) * int(test.group(2))

def calc_sum(found: list[str]) -> int:
    """calc sum of all multiplications."""
    rez = 0
    for x in found:
        rez += multiplicationz(x)
    return rez

def part1(data: list[str]) -> str:
    """starts masterpiece part 1"""
    found = regex_rizz_found_part1("".join(data))
    return calc_sum(found)

def part2(data: list[str]) -> str:
    """starts masterpiece part 2"""
    found = regex_rizz_found_part2("".join(data))
    return calc_sum(found)
