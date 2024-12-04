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
