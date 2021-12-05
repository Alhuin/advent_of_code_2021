class Point:
    def __init__(self, data):
        self.x, self.y = data
        self.occur = 1

    def __add__(self, other: 'Point'):
        return Point([self.x + other.x, self.y + other.y])

    def __mul__(self, other: int):
        return Point([self.x * other, self.y * other])

    def __sub__(self, other: 'Point'):
        return Point([self.x - other.x, self.y - other.y])

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return abs(self.x if self.x else self.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
