# Not sure if there's a better way to handle this one...
import sys
sys.path.append("../../../Helpers")
from CommonShitz import readFile

def _sum(x, y):
    rez = 0
    for i in range(len(x)):
        rez += abs(x[i] - y[i])
    return rez

def _start():
    data = readFile()

    test = [(x.split()) for x in data]

    lList = [int(x[0]) for x in test]
    rList = [int(x[1]) for x in test]

    rList.sort()
    lList.sort()

    # Part 1
    print('Part 1: ' + str(_sum(rList,lList)))

    # Part 2
    rListCount = dict(map(lambda x: (x, rList.count(x)), rList))
    summ = 0
    for (key, x) in rListCount.items():
        summ += x * key * lList.count(key)
    print('Part 2: ' + str(summ))

_start()