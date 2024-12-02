def layer(array):
    line = []
    #print (array)
    if len(array) == 1:
        return array[0]

    for i in range(len(array)-1):
        line.append(array[i+1] - array[i])

    return array[len(array)-1] + layer(line)

def layerReverse(array, paremt = False):
    line = []
    print (array)
    if len(array) == 1:
        return array[0]

    for i in range(len(array)-1):
        line.append(array[i+1] - array[i])

    #if paremt:
    #    vaaa = layerReverse(line)
    #    print(vaaa)
    #    return vaaa
    return array[0] - layerReverse(line)

def start():
    f = open('day9.data', 'r')
    filez = f.read().split('\n')

    linesRez = []
    linesRezReversed = []
    for line in filez:
        arrayz = []
        for i in line.split(' '):
            arrayz.append(int(i))
        linesRez.append(layer(arrayz))
        linesRezReversed.append(layerReverse(arrayz,True))

    sum = 0
    sumReversed = 0
    for rez in linesRez:
        sum += rez
    for rez in linesRezReversed:
        sumReversed += rez

    print(sum)
    print(f'Reversed: {sumReversed}')

start()