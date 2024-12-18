"""masterpiece"""

def generate_shit(line):
    rez = []
    block = False
    i = 0
    for x in line:
        if not block:
            rez += [ i for t in range(int(x))]
            i += 1
        if block:
            rez += '.' * int(x)
        block = not block
    return rez

def combine_part2(line):
    exit = False
    while not exit:
        found = line.index('.') if '.' in line else -1
        if found >= 0:
            line[found] = line[len(line)-1]
            line.pop(len(line)-1)
        else:
            exit = True
    return line

def combine_part1(line):
    exit = False
    while not exit:
        found = line.index('.') if '.' in line else -1
        if found >= 0:
            line[found] = line[len(line)-1]
            line.pop(len(line)-1)
        else:
            exit = True
    return line

def check_sum(arr):
    rez = 0
    for i, char in enumerate(arr):
        if char != '-1':
            rez += int(char) * i
    return rez

def part1(data) -> str:
    """starts masterpiece part 1"""
    arrayz = generate_shit(data[0])
    arr = combine_part1(arrayz)
    print(str(arr))
    #with open('output.part1.data', 'w') as f:
    #    print(arr, file=f)
    return check_sum(arr)

def part2(data) -> str:
    """starts masterpiece part 2"""
    
    return 'Not Implemented'
