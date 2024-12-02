theBag = {
    "blue" : 14,
    "green" : 13,
    "red" : 12
}

theBagEmpty = {
    "blue" : 0,
    "green" : 0,
    "red" : 0
}

def isItPossible(str):
    whatINeed = str.split(':')[1]
    gameSets = whatINeed.split(';')

    for sett in gameSets:
        thisBag = theBag.copy()
        pull = sett.split(',')
        for pu in pull:
            g = pu.split(' ')
            value = 0
            color = ''
            for t in g:
                if t.isnumeric():
                    value = int(t)
                elif len(t) > 0:
                    color = t
                if value != 0 and color != '':
                    if color in thisBag.keys():
                        thisBag[color] -= value
                    else:
                        break
        for color, value in thisBag.items():
            if value < 0:
                return False

    return True

def findMinInTheBag(str):
    whatINeed = str.split(':')[1]
    gameSets = whatINeed.split(';')

    minBag = theBagEmpty.copy()

    for sett in gameSets:
        thisBag = theBagEmpty.copy()
        pull = sett.split(',')
        for pu in pull:
            g = pu.split(' ')
            value = 0
            color = ''
            for t in g:
                if t.isnumeric():
                    value = int(t)
                elif len(t) > 0:
                    color = t
                if value != 0 and color != '':
                    if color in thisBag.keys():
                        thisBag[color] += value
                    else:
                        break
                    
        for color, value in minBag.items():
            if thisBag[color] > value:
                minBag[color] = thisBag[color]

    power = 1
    for color, value in minBag.items():
        power = power * value

    return power

def start():
    f = open('day2.data', 'r')
    input = f.read().split('\n')
    output = 0
    i = 0

    #for x in input:
    #    i += 1
    #    if isItPossible(x):
    #        output += i
    for x in input:
        output += findMinInTheBag(x)

    print(f'Min {output}')

start()