#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Éléments basiques de géométrie du projet."""

from ..units.geometry import Angle


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
            return NotImplemented
    __radd__ = __add__

    def __sub__(self, other):
        if type(self) is type(other):
            return type(self)(self.x - other.x, self.y - other.y)
        elif type(other) is tuple and len(other) == 2:
            return type(self)(self.x - other[0], self.y - other[1])
        else:
            return NotImplemented
    __rsub__ = __sub__

    def __mul__(self, other):
        if type(self) is type(other):
            return type(self)(self.x * other.x, self.y * other.y)
        elif type(other) is int or type(other) is float:
            return type(self)(self.x * other, self.y * other)
        elif type(other) is tuple and len(other) == 2:
            return type(self)(self.x * other[0], self.y * other[1])
        else:
            return NotImplemented
    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.x / other, self.y / other)
        else:
            return NotImplemented
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.x // other, self.y // other)
        else:
            return NotImplemented

    def __eq__(self, other):
        return type(self) is type(other) and \
            self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return type(self) is not type(other) or \
            self.x != other.x or self.y != other.y


class Line(object):
    """Définit une ligne dans un plan à 2 dimensions."""

    def __init__(self, p1, p2):
        """Instancier une nouvelle ligne à partir de deux points.
        Line(Point(1,1), Point(2,2)) va créer une ligne partant de X=1 Y=1
        et arrivant à X=2 Y=2."""

        if type(p1) is not Point or type(p2) is not Point:
            raise TypeError("Les paramètres p1 et p2 doivent être des "
                            "instances de pseudosci.geometry.basic.Point.")
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "Ligne entre {0} et {1}".format(str(self.p1), str(self.p2))

    def __repr__(self):
        return "<{0} p1={1} p2={2}>".format(
            type(self).__name__, self.p1.__repr__(), self.p2.__repr__())

    def __add__(self, other):
        if type(self) is type(other):
            if self.p2 == other.p1:
                return type(self)(self.p1, other.p2)
            elif self.p1 == other.p2:
                return type(self)(self.p2, other.p1)
            elif self.p1 == other.p1:
                return type(self)(self.p2, other.p2)
            elif self.p2 == other.p2:
                return type(self)(self.p1, other.p1)
            else:
                raise ValueError("Deux lignes ne peuvent s'additionner que si "
                                 "elles ont un point en commun.")
        else:
            return NotImplemented

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Line(p1=self.p1, p2=Point(
                x=self.p1.x + (self.p2.x - self.p1.x) * other,
                y=self.p1.y + (self.p2.y - self.p1.y) * other))
        else:
            return NotImplemented
    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return self * (1 / float(other))
        else:
            return NotImplemented
    __div__ = __truediv__

    def __getattr__(self, name):
        if name in ['length', 'distance', 'size']:
            from math import sqrt
            return sqrt((self.p2.x - self.p1.x) ** 2 +
                        (self.p2.y - self.p1.y) ** 2)
        elif name in ['middle', 'midpoint']:
            return Point(x=(self.p1.x + self.p2.x) / 2,
                         y=(self.p1.y + self.p2.y) / 2)
        elif name == 'angle':
            from math import atan2
            return Angle(rad=atan2(self.p2.y - self.p1.y,
                                   self.p2.x - self.p1.x))
        else:
            raise AttributeError("Pas d'attribut nommé {0}".format(name))

    def __eq__(self, other):
        return type(self) is type(other) and \
            self.p1 == other.p1 and self.p2 == other.p2

    def __ne__(self, other):
        return type(self) is not type(other) or \
            self.p1 != other.p1 or self.p2 != other.p2
