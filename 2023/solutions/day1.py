words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7', 
    'eight': '8',
    'nine': '9'
}

def wordToNumberProcess(str):
    strlow = str.lower()
    out = ''
    for i in range(len(strlow)):
        for key, value in words.items():
            if strlow[i:].startswith(key):
                out += value
            elif strlow[i].isnumeric:
                out += strlow[i]
    return out

def start():
    f = open('day1.data', 'r')
    input = f.read().split('\n')
    output = 0
    whattt = 0

    for x in input :
        array = []
        word = wordToNumberProcess(x)
        for y in word:
            if y.isnumeric():
                array.append(y)
        if len(array) >= 1:
            print(array[0] + array[len(array)-1])
            output += int(array[0] + array[len(array)-1])
            whattt += 1
    print(whattt)
    print(output)

start()