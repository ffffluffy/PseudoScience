#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure du projet. Toutes les unités sont stockées en interne sous
l'unité du système international."""


class Unit(object):
    """Décrit une unité de mesure."""

    def __init__(self, value=0, fullname="unit", pluralname="units",
                 attributes={'unit': 1, 'u': 1, 'units': 1}):
        self.value = float(value)
        if not hasattr(self, 'fullname'):
            self.fullname = fullname
        if not hasattr(self, 'pluralname'):
            self.pluralname = pluralname
        if not hasattr(self, 'attributes'):
            self.attributes = attributes

    def __str__(self):
        return '{0} {1}'.format(str(self.value), self.fullname
                                if self.value == 1 else self.pluralname)

    def __repr__(self):
        return '<{0} {1}>'.format(type(self).__name__, self)

    def __getattr__(self, name):
        try:
            return self.convertto(name)
        except ValueError as v:
            raise AttributeError("{0} object has no attribute {1}".format(
                    self.__class__.__name__, name))

    def convertfrom(self, value, source):
        """Convertir une mesure d'une unité dans une unité source vers l'unité
        de mesure standard. `value` désigne la valeur à convertir et `source`
        est une chaîne de caractères représentant l'unité, appartenant à
        l'attribut `attributes` de l'unité."""
        if source.lower() == 'value':
            return value
        for (name, conv) in self.attributes.items():
            if source.lower() == name.lower():
                if isinstance(conv, (int, float)):
                    return value * conv
                elif type(conv) is tuple and len(conv) == 2 \
                        and callable(conv[0]):
                    return conv[0](value)
        raise ValueError("Cannot convert {0} {1} to {2}".format(
            value, source, self.pluralname))

    def convertto(self, dest):
        """Convertir l'unité de mesure standard en une autre unité.
        `value` désigne la valeur à convertir et `dest` est une chaîne de
        caractères représentant l'unité souhaitées, présent parmi les clés du
        dictionnaire `attributes` de l'instance."""
        if dest.lower() == 'value':
            return value
        for (name, conv) in self.attributes.items():
            if dest.lower() == name.lower():
                if isinstance(conv, (int, float)):
                    return self.value / conv
                elif type(conv) is tuple and len(conv) == 2 \
                        and callable(conv[1]):
                    return conv[1](self.value)
        raise ValueError("Cannot convert {0} to {1}".format(self, dest))

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __abs__(self):
        return type(self)(value=abs(self.value))

    def __pos__(self):
        return type(self)(value=+self.value)

    def __neg__(self):
        return type(self)(value=-self.value)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(value=self.value + other)
        elif type(self) is type(other):
            return type(self)(value=self.value + other.value)
        return NotImplemented
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(value=self.value - other)
        elif type(self) is type(other):
            return type(self)(value=self.value - other.value)
        return NotImplemented
    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(value=self.value * other)
        return NotImplemented
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(value=self.value / other)
        elif type(self) is type(other):
            return (self.value / other.value)
        return NotImplemented
    __div__ = __truediv__

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(value=self.value // other)
        elif type(self) is type(other):
            return (self.value // other.value)
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return type(self)(value=self.value ** other)
        return NotImplemented

    def __eq__(self, other):
        if type(self) is type(other):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        return not self == other
