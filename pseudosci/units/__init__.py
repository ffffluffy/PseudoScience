#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure du projet. Toutes les unités sont stockées en interne sous
l'unité du système international."""


class Unit(object):
    """Décrit une unité de mesure."""

    def __init__(self, value):
        self.value = float(value)
        self.fullname = "unit"
        self.pluralname = "units"

    def __str__(self):
        return '{0} {1}'.format(str(self.value), self.fullname
                                if self.value == 1 else self.pluralname)

    def __repr__(self):
        return '<{0} {1}>'.format(type(self).__name__, self)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __abs__(self):
        return type(self)(abs(self.value))

    def __pos__(self):
        return type(self)(+self.value)

    def __neg__(self):
        return type(self)(-self.value)

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value + other)
        elif type(self) is type(other):
            return type(self)(self.value + other.value)
        else:
            raise TypeError("Il n'est pas possible d'additionner deux unités "
                            "différentes.")
    __radd__ = __add__

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value - other)
        elif type(self) is type(other):
            return type(self)(self.value - other.value)
        else:
            raise TypeError("Il n'est pas possible de soustraire deux unités "
                            "différentes.")
    __rsub__ = __sub__

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value * other)
        else:
            raise TypeError("Il n'est pas possible de multiplier deux unités "
                            "différentes.")
    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value / other)
        elif type(self) is type(other):
            return (self.value / other.value)
        else:
            raise TypeError("Il n'est pas possible de diviser deux unités "
                            "différentes.")
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value // other)
        elif type(self) is type(other):
            return (self.value // other.value)
        else:
            raise TypeError("Il n'est pas possible de diviser deux unités "
                            "différentes.")

    def __pow__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value ** other)
        else:
            raise TypeError("L'exposant d'une puissance d'une unité ne peut "
                            "être qu'un nombre.")

    def __eq__(self, other):
        return type(self) is type(other) and self.value == other.value

    def __ne__(self, other):
        return type(self) is type(other) and self.value != other.value

    def __gt__(self, other):
        if (type(self) is not type(other)):
            raise TypeError("Une unité doit être comparée à une unité de même "
                            "type.")
        else:
            return self.value > other.value

    def __ge__(self, other):
        if (type(self) is not type(other)):
            raise TypeError("Une unité doit être comparée à une unité de même "
                            "type.")
        else:
            return self.value >= other.value

    def __lt__(self, other):
        if (type(self) is not type(other)):
            raise TypeError("Une unité doit être comparée à une unité de même "
                            "type.")
        else:
            return self.value < other.value

    def __le__(self, other):
        if (type(self) is not type(other)):
            raise TypeError("Une unité doit être comparée à une unité de même "
                            "type.")
        else:
            return self.value <= other.value
