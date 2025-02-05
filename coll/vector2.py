import random
class Vector2:
    def __init__(self, x=0, y=0, randoms=False, ranges = (0, 100) ):
        self.x = x
        self.y = y
        if randoms:
            self.x = random.randint(*ranges)
            self.y = random.randint(*ranges)
    def __str__(self):
        return f"Vector2({self.x}, {self.y})"
    def __add__(self, other):
        if type(other) == list or type(other) == tuple:
            return [self.x + other[0], self.y + other[1]]
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)
    def get(self):
        return [self.x, self.y]
    def get_js(self):
        return {
            "x" : self.x,
            "y" : self.y
        }
    def dot(self, other):
        return self.x * other.x + self.y * other.y