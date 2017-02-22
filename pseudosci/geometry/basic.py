#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Éléments basiques de géométrie du projet."""


class Point(object):
    """Définit un point dans un plan à 2 dimensions."""

    def __init__(self, x, y):
        """Instancier un nouveau point.
        Point(1, 2) va créer un point de coordonnées X=1 et Y=2."""
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "Point à X={0} et Y={1}".format(self.x, self.y)

    def __repr__(self):
        return "<{0} X={1} Y={2}>".format(type(self).__name__, self.x, self.y)

    def __abs__(self):
        return type(self)(abs(self.x), abs(self.y))

    def __pos__(self):
        return type(self)(+self.x, +self.y)

    def __neg__(self):
        return type(self)(-self.x, -self.y)

    def __add__(self, other):
        if type(self) is type(other):
            return type(self)(self.x + other.x, self.y + other.y)
        elif type(other) is tuple and len(other) == 2:
            return type(self)(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("Seuls un tuple ou un point peuvent être "
                            "additionnés à un point.")
    __radd__ = __add__

    def __sub__(self, other):
        if type(self) is type(other):
            return type(self)(self.x - other.x, self.y - other.y)
        elif type(other) is tuple and len(other) == 2:
            return type(self)(self.x - other[0], self.y - other[1])
        else:
            raise TypeError("Seuls un tuple ou un point peuvent être "
                            "soustraits à un point.")
    __rsub__ = __sub__

    def __mul__(self, other):
        if type(self) is type(other):
            return type(self)(self.x * other.x, self.y * other.y)
        elif type(other) is int or type(other) is float:
            return type(self)(self.x * other, self.y * other)
        elif type(other) is tuple and len(other) == 2:
            return type(self)(self.x * other[0], self.y * other[1])
        else:
            raise TypeError("Un point n'est multipliable que par un tuple, un "
                            "point ou un nombre.")
    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.x / other, self.y / other)
        else:
            raise TypeError("Un point n'est divisible que par un nombre.")
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.x // other, self.y // other)
        else:
            raise TypeError("Un point n'est divisible que par un nombre.")

    def __eq__(self, other):
        return type(self) is type(other) and \
            self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return type(self) is not type(other) or \
            self.x != other.x or self.y != other.y
