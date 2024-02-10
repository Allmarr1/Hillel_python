class Vector:
    def __init__(self, components):
        self.components = components
        # print (self.components)

    def __str__(self):
        return f"Vector{self.components}"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.components == other.components

    def __add__(self, other):
        return Vector([x + y for x, y in zip(self.components, other.components)])

    def __sub__(self, other):
        return Vector([x - y for x, y in zip(self.components, other.components)])

    def dot_product(self, other):
        return sum(x * y for x, y in zip(self.components, other.components))

    def vector_addition(vectors):
        return Vector([sum(components) for components in zip(*[vector.components for vector in vectors])])

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([7, 8, 9])

assert v1 + v2 == Vector([5, 7, 9])
assert v1 - v2 == Vector([-3, -3, -3])
assert v1.dot_product(v2) == 32
assert Vector.vector_addition([v1, v2, v3]) == Vector([12, 15, 18])
