def do_magic(time, distance):
    (time, distance) = [int(time),int(distance)]
    ways = 0
    first_positive = False
    for tiem in range(time):
        if (time-tiem)*tiem > distance:
            first_positive = True
            ways += 1
        elif (time-tiem)*tiem <= distance and first_positive:
            break

    return ways

def clean(value):
    arrayz = []
    for t in value:
        if len(t) > 0:
            arrayz.append(t)
    return arrayz

def start():
    with open('day6.data', 'r', encoding='utf-8') as f:
        filez = f.read().split('\n')
        
        time = clean(filez[0][len('Time:      '):].split('  '))
        distance = clean(filez[1][len('Time:      '):].split(' '))

        rez = 0
        for i in enumerate(time):
            _ = do_magic(time[i[0]],distance[i[0]])
            rez = rez * _ if rez != 0 else _

        print(rez)

start()
