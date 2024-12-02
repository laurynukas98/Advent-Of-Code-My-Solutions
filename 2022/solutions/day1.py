"""Day1 solution"""

def start():
    """Day1 solution"""
    with open('day1.data', 'r', encoding="utf-8") as f:
        data = sorted([sum(list(map(int,test.split("\n")))) for test in f.read().split("\n\n")]
                      ,reverse=True)
        print('Part1: ' + str(data[0]))
        print('Part2: ' + str(sum(list(data)[:3])))

start()
