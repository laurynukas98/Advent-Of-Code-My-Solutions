def translate(c):
    if c == 'A':
        return '15'
    if c == 'K':
        return '14'
    if c == 'Q':
        return '13'
    if c == 'J':
        return '..'
    if c == 'T':
        return '11'
    return f'0{c}'

def countCards(deck):
    arr = {}
    wildCard = 0
    for a in deck:
        char = translate(a)
        if char == '..':
            wildCard += 1
        elif char in arr:
            arr[char] += 1
        else:
            arr[char] = 1
    if len(arr.keys()) == 0:
        arr = {'..': 5}
    else:
        beeg = ''
        valuez = 0
        for t in arr:
            if valuez < arr[t]:
                beeg = t
                valuez = arr[t]
        arr[beeg] += wildCard
    return arr

def translateDeck(deck):
    arr = []
    for i in enumerate(deck):
        arr.append(translate(deck[i[0]]))
    return ''.join(arr)

def compare(deck1,deck2):
    deck1Count = countCards(deck1)
    deck2Count = countCards(deck2)
    deck1 = translateDeck(deck1)
    deck2 = translateDeck(deck2)

    #Five of a kind
    if len(deck1Count) == 1:
        if len(deck2Count) == 1:
            return deck1 > deck2
        return True
    if len(deck2Count) == 1:
        return False
    #Four of a kind
    if len(deck1Count) == 2 and (list(deck1Count.items())[0][1] == 1 or list(deck1Count.items())[0][1] == 4):
        if len(deck2Count) == 2 and (list(deck2Count.items())[0][1] == 1 or list(deck2Count.items())[0][1] == 4):
            return deck1 > deck2
        return True
    if len(deck2Count) == 2 and (list(deck2Count.items())[0][1] == 1 or list(deck2Count.items())[0][1] == 4):
        return False
    #Full house
    if len(deck1Count) == 2:
        if len(deck2Count) == 2:
            return deck1 > deck2
        return True
    if len(deck2Count) == 2:
        return False
    #Three of a kind
    if len(deck1Count) == 3 and (list(deck1Count.items())[0][1] == 3 or list(deck1Count.items())[1][1] == 3 or list(deck1Count.items())[2][1] == 3):
        if len(deck2Count) == 3 and (list(deck2Count.items())[0][1] == 3 or list(deck2Count.items())[1][1] == 3 or list(deck2Count.items())[2][1] == 3):
            return deck1 > deck2
        return True
    if len(deck2Count) == 3 and (list(deck2Count.items())[0][1] == 3 or list(deck2Count.items())[1][1] == 3 or list(deck2Count.items())[2][1] == 3):
        return False
    #Two pair
    if len(deck1Count) == 3 :
        if len(deck2Count) == 3:
            return deck1 > deck2
        return True
    if len(deck2Count) == 3:
        return False
    #One Pair
    if len(deck1Count) == 4 :
        if len(deck2Count) == 4:
            return deck1 > deck2
        return True
    if len(deck2Count) == 4:
        return False
    #High card
    return deck1 > deck2
    

def deckOrder(decks):
    arr = []
    for deck in decks.items():
        rank = 0
        for i in enumerate(arr):
            if not compare(deck[0],arr[i[0]]):
                break
            rank += 1
        if len(arr) == 0:
            arr = [deck[0]]
        elif rank == 0:
            arr = [deck[0]] + arr
        else:
            arr = arr[:rank] + [deck[0]] + arr[rank:]
    return arr


def start():
    with open('day7.data', 'r', encoding='utf-8') as f:
        filez = f.read().split('\n')
        rez = 0
        decks = {}
        for t in filez:
            (deck,value) = t.split(' ')
            decks[deck] = value
        ranks = deckOrder(decks)

        for i in enumerate(ranks):
            rez += int(decks[ranks[i[0]]]) * (i[0]+1)
        print(f"press {rez}")

start()