# Not sure if there's a better way to handle this one...
import sys
sys.path.append("../../../Helpers")
from CommonShitz import readFile

def start():
    data = readFile()
    print('Part1 rez: ' + str(part1(data)))
    print('Part2 rez: ' + str(part2(data)))

def part1(data):
    return 'Not Implemented'

def part2(data):
    return 'Not Implemented'

start()