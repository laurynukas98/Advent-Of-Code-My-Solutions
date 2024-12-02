class Neuronz:
    def __init__(self,string):
        (self.left, self.right) = string.split(' = ')[1].replace('(','').replace(')','').split(', ')
        self.name = string.split(' = ')[0]

    def getLocation(self,direction):
        return self.left if direction == 'L' else self.right

class NeuronzSmrt:
    def __init__(self,string):
        (left, right) = string.split(' = ')[1].replace('(','').replace(')','').split(', ')
        self.left = [left]
        self.right = [right]

        self.name = string.split(' = ')[0]

    def add(self,string):
        (left, right) = string.split(' = ')[1].replace('(','').replace(')','').split(', ')
        self.left.append(left)
        self.right.append(right)
        #self.name = string.split(' = ')[0]

    def getLocation(self,direction):
        return self.left if direction == 'L' else self.right

def goNow(instruction, networkz):
    index = 0
    steps = 0
    node = 'AAA'
    while node != 'ZZZ':
        node = networkz[node].getLocation(instruction[index])
        index += 1
        steps += 1
        if index == len(instruction):
            index = 0
    return steps

def goNow2(instruction, networkz):
    index = 0
    steps = 0
    nodes = []
    for key in networkz.keys():
        if key[2] == 'A':
            nodes.append(key)

    while True:
        flagz = True
        for node in nodes:
            if node[2] != 'Z':
                flagz = False
                break
        if not flagz:
            nodesT = []
            for node in nodes:
                nodeT = networkz[node].getLocation(instruction[index])
                nodesT.append(nodeT)
            nodes = nodesT
            index += 1
            steps += 1
            if index == len(instruction):
                index = 0
        else:
            break
    return steps

def goNow20(instruction, networkz):
    index = 0
    steps = 0
    nodes = ['A']
    while len(nodes) != 0:
        nodesT = []
        for node in nodes:
            if len(node) == 1 or node[2] != 'Z':
                what = networkz[node if len(node) == 1 else node[2]].getLocation(instruction[index])
                nodesT = nodesT + what
        if len(nodesT) == 0:
            break
        nodes = nodesT
        index += 1
        steps += 1
        if index == len(instruction):
            index = 0
    return steps

def start():
    f = open('day8.data', 'r')
    filez = f.read().split('\n')

    instruction = filez[0]
    neuronzNetworkz = {}

    ##PART 1
    #for line in filez[2:]:
    #    neuronzNetworkz[line.split(' = ')[0]] = Neuronz(line)

    ##PART 2
    for line in filez[2:]:
        neuronzNetworkz[line.split(' = ')[0]] = Neuronz(line)

    #for line in filez[2:]:
    #    if line.split(' = ')[0][2] not in neuronzNetworkz.keys():
    #        neuronzNetworkz[line.split(' = ')[0][2]] = NeuronzSmrt(line)
    #    else:
    #        neuronzNetworkz[line.split(' = ')[0][2]].add(line)

    print(goNow2(instruction,neuronzNetworkz))

start()