def arrowCheck(x,y):
    symbol = mapsas[y][x]
    gone = []

    #North | L J S
    if symbol in ['|', 'L', 'J', 'S']:
        if y-1 >= 0 and mapsas[y-1][x] in ['|', '7', 'F', 'S']:
            gone.append((x,y-1))
    #South | 7 F S
    if symbol in ['|', '7', 'F', 'S']:
        if y+1 < len(mapsas) and mapsas[y+1][x] in ['|', 'L', 'J', 'S']:
            gone.append((x,y+1))
    #East - L F S
    if symbol in ['-', 'L', 'F', 'S']:
        if x+1 < len(mapsas[y]) and mapsas[y][x+1] in ['-', 'J', '7', 'S']:
            gone.append((x+1,y))
    #West - J 7 S
    if symbol in ['-', 'J', '7', 'S']:
        if x-1 >= 0 and mapsas[y][x-1] in ['-', 'L', 'F', 'S']:
            gone.append((x-1,y))
    
    mapsas[y] = mapsas[y][:x] + 'X' + mapsas[y][x+1:]

    return gone

def go(sx,sy):
    arrows = [(sx,sy)]

    iteration = 0
    while len(arrows) != 0:
        arrowsT = []
        for arrow in arrows:
            arrowsT += arrowCheck(arrow[0],arrow[1])
        if len(arrowsT) == 0:
            break
        else:
            iteration += 1
        arrows = arrowsT
    
    return iteration

def start():
    f = open('day10.data', 'r')
    filez = f.read().split('\n')

    global mapsas
    mapsas = filez
    
    startX = 0
    startY = 0
    for y in range(len(mapsas)):
        t = mapsas[y].find('S')
        if t >= 0:
            startX = mapsas[y].find('S')
            startY = y
            break

    print(go(startX,startY))

    for item in mapsas:
        print(item)

start()