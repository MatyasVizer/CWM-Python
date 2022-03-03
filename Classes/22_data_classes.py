from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(1, 2)

print(p1 == p2)

#  it will give false because python compares memory locations, but if we used nametuples...
# ... it will magically work!

print(p1.x)  # but we can't edit attribute it after initialization
print(id(p1))
print(id(p2))
