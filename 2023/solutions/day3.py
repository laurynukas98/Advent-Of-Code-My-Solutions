engineSchematic = ['']
suma = 0
powerRez = 0
coords = [
    (-1,-1),
    (0,-1),
    (1,-1),
    (-1,0),
    (1,0),
    (-1,1),
    (0,1),
    (1,1)
]

def findNumber(coord):
    #let's go to the left
    endedL = coord['x']
    endedR = coord['x']
    while endedL != -1 and engineSchematic[coord['y']][endedL].isnumeric():
        endedL -= 1
    #then go to the right
    while endedR < len(engineSchematic[coord['y']]) and engineSchematic[coord['y']][endedR].isnumeric():
        endedR += 1

    endedL += 1
    daNumber = int(engineSchematic[coord['y']][endedL:endedR])
    global suma
    suma += daNumber
    engineSchematic[coord['y']] = engineSchematic[coord['y']][:endedL] + ('.' * len(engineSchematic[coord['y']][endedL:endedR])) + engineSchematic[coord['y']][endedR:]
    return daNumber
    

def findNearNumbers(coord):
    numberCount = 0
    power = 1
    for (x, y) in coords:
        if coord['x'] + x >= 0 and coord['x'] + x < len(engineSchematic[coord['y']]) and coord['y'] + y >= 0 and coord['y'] + y < len(engineSchematic):
            if engineSchematic[coord['y'] + y][coord['x'] + x].isnumeric():
                power = power * findNumber({'x': coord['x'] + x, 'y': coord['y'] + y})
                numberCount += 1
    if numberCount == 2:
        global powerRez
        powerRez += power

def arrow():
    for y in range(len(engineSchematic)):
        for x in range(len(engineSchematic[y])):
            if engineSchematic[y][x] != '.' and not engineSchematic[y][x].isnumeric():
                findNearNumbers({'x': x, 'y': y})

def start():
    f = open('day3.data', 'r')
    global engineSchematic
    engineSchematic = f.read().split('\n')

    arrow()

    print(f'suma: {suma}')
    print(f'power Sum: {powerRez}')

start()