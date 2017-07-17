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
        if isinstance(other, (int, float)):
            return type(self)(self.value + other)
        elif type(self) is type(other):
            return type(self)(self.value + other.value)
        return NotImplemented
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(self.value - other)
        elif type(self) is type(other):
            return type(self)(self.value - other.value)
        return NotImplemented
    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(self.value * other)
        return NotImplemented
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(self.value / other)
        elif type(self) is type(other):
            return (self.value / other.value)
        return NotImplemented
    __div__ = __truediv__

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(self.value // other)
        elif type(self) is type(other):
            return (self.value // other.value)
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(self.value ** other)
        return NotImplemented

    def __eq__(self, other):
        if type(self) is type(other):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        return not self == other
