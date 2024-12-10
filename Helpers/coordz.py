"""simple Coordz because yes"""
class Coord:
    x: float = 0
    y: float = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def transform(self, x: float, y: float):
        return Coord(self.x + x, self.y + y)

    def transform(self, coord):
        return Coord(self.x + coord.x, self.y + coord.y)
    
    def print(self):
        print('(' + str(self.x) + ',' + str(self.y) +')')

    def equals(self, e):
        return self.x == e.x and self.y == e.y

    def unique_coords(list):
        rez = []
        for x in list:
            add = True
            for y in rez:
                if y.equals(x):
                    add = False
                    break
            if add:
                rez.append(x)
        return rez