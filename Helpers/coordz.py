"""simple Coordz because yes"""
class Coord:
    x: int = 0
    y: int = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def transform(self, x: int, y: int):
        return Coord(self.x + x, self.y + y)

    def transform(self, coord):
        return Coord(self.x + coord.x, self.y + coord.y)
    
    def negation(self):
        return Coord(self.x * -1, self.y * -1)

    def print(self):
        print('(' + str(self.x) + ',' + str(self.y) +')')

    def equals(self, coord):
        return self.x == coord.x and self.y == coord.y
    
    def distance(self, coord, _abs: bool = False):
        x = self.x - coord.x
        y = self.y - coord.y
        return Coord(abs(x) if _abs else x , abs(y) if _abs else y)
    
    def in_distance(self, max_x, max_y):
        return True if self.x < max_x and self.y < max_y and self.x > -1 and self.y > -1 else False

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