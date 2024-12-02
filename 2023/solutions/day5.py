class Map:
    def __init__(self, lines):
        (self._from,self._to) = lines[0][:-len(" map:")].split("-to-")
        self.destinationRangeStart = []
        self.sourceRangeStart = []
        self.rangeLength = []
        for line in lines[1:]:
            (x,y,z) = line.split(" ")
            self.destinationRangeStart.append(int(x))
            self.sourceRangeStart.append(int(y))
            self.rangeLength.append(int(z))
        print("whut?")

    def convert(self, number):
        value = float('inf')
        for i in range(len(self.destinationRangeStart)):
            if self.sourceRangeStart[i] <= number and self.sourceRangeStart[i]+self.rangeLength[i] >= number:
                if value > self.sourceRangeStart[i]-number+self.destinationRangeStart[i]:
                    value = number-self.sourceRangeStart[i]+self.destinationRangeStart[i]
                    break
        if value == float('inf'):
            value = number
        return (self._to, value)

def readMaps(strList):
    maps = {}

    yeah = []
    for line in strList:
        if len(line) > 0:
            yeah.append(line)
        elif len(line) == 0:
            t = Map(yeah)
            maps[t._from] = t
            yeah = []
    t = Map(yeah)
    maps[t._from] = t

    return maps


def start():
    f = open('day5.data', 'r')
    filez = f.read().split('\n')

    seeds = filez[0].split(' ')[1:]
    
    maps = readMaps(filez[2:])

    min = float('inf')
    i = 0
    for seed in range(int(len(seeds)/2)):
        for t in range(int(seeds[(seed*2)+1])):
            name = "seed"
            number = int(seeds[seed*2])+t
            fail = False
            while name != 'location':
                if name in maps.keys():
                    #print(f'    {name}: {number}')
                    (name, number) = maps[name].convert(number)
                if number == float('inf'):
                    fail = True
                    break
            #print(f'    {name}: {number}')
            if not fail:
                if min > number:
                    min = number
        i += 1

    print(f'\nMIN: {min}')

start()