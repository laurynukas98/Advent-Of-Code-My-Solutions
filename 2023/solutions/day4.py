
def cleanList(str):
    rez = []
    listz = str.split(' ')
    for t in listz:
        if t.isnumeric():
            rez.append(int(t))
    return rez

def processCard(card):
    sum = 0
    whatINeed = card.split(':')[1]
    (winning,hand) = whatINeed.split('|')
    winningList = cleanList(winning)
    handList = cleanList(hand)

    streak = 0
    for number in winningList:
        if number in handList:
            if streak <= 2:
                sum += 1
            streak += 1
    if streak >= 2:
        sum = (2**(streak-1))

    return sum

def processCardPart2(card):
    sum = 0
    whatINeed = card.split(':')[1]
    (winning,hand) = whatINeed.split('|')
    winningList = cleanList(winning)
    handList = cleanList(hand)

    streak = 0
    for number in winningList:
        if number in handList:
            streak += 1

    return streak

def start():
    f = open('day4.data', 'r')
    filez = f.read().split('\n')

    suma = 0
    cardsWin = {}
    for t in range(len(filez)):
        cardsWin[str(t)] = 0

    i = 0
    for l in filez:
        win = processCardPart2(l)
        if (win > 0):
            for t in range(win):
                cardsWin[str(i+t+1)] += (cardsWin[str(i)]+1 if cardsWin[str(i)] != 0 else 1)
                #if str(i+(t+1)) in cardsWin:
                #cardsWin[str(i+t)] += 1
                #else:
                #    cardsWin[str(i+t)] = 1 
        i += 1

    for t in range(len(filez)):
        suma += cardsWin[str(t)]

    suma += len(filez)
    print(cardsWin)
    print(f'suma: {suma}')

start()