#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure du projet. Toutes les unités sont stockées en interne sous
l'unité du système international."""

from six import with_metaclass


class UnitBase(type):
    """Métaclasse servant à la création d'unités."""
    units = {}

    def __new__(cls, name, bases, attrs):
        if name not in ["Unit", "NewBase"] and \
                not all(k in attrs for k in ("fullname", "pluralname")):
            raise AttributeError(
                "Required attributes are missing for this Unit")

        def _convertfrom(self, value, source):
            """Convertir une mesure d'une unité dans une unité source vers
            l'unité de mesure standard. `value` désigne la valeur à convertir
            et `source` est une chaîne de caractères représentant l'unité,
            appartenant à l'attribut `convert` de l'unité."""
            if source.lower() == 'value':
                return value
            for (name, conv) in self.convert.items():
                if source.lower() == name.lower():
                    if isinstance(conv, (int, float)):
                        return value * conv
                    elif callable(conv[0]):
                        return conv[0](value)
            raise ValueError("Cannot convert {0} {1} to {2}".format(
                    value, source, self.pluralname))

        def _convertto(self, dest):
            """Convertir l'unité de mesure standard en une autre unité.
            `value` désigne la valeur à convertir et `dest` est une chaîne de
            caractères représentant l'unité souhaitées, présent parmi les clés
            du dictionnaire `convert` de l'instance."""
            if dest.lower() == 'value':
                return self.value
            for (name, conv) in self.convert.items():
                if dest.lower() == name.lower():
                    if isinstance(conv, (int, float)):
                        return self.value / conv
                    elif type(conv) is tuple and len(conv) == 2 \
                            and callable(conv[1]):
                        return conv[1](self.value)
            raise ValueError("Cannot convert {0} to {1}".format(self, dest))

        def _init(self, **kwargs):
            (name, value), = kwargs.items()
            self.value = self.convertfrom(float(value), str(name))

        def _str(self): return '{0} {1}'.format(
            str(self.value), self.fullname
            if self.value == 1 else self.pluralname)

        def _repr(self): return '<{0} {1}>'.format(type(self).__name__, self)

        def _getattr(self, name):
            try:
                return self.convertto(name)
            except ValueError as v:
                raise AttributeError("{0} object has no attribute {1}".format(
                    self.__class__.__name__, name))

        def _setattr(self, name, value):
            try:
                object.__setattr__(self, 'value',
                                   self.convertfrom(value, name))
            except ValueError as v:
                object.__setattr__(self, name, value)

        def _int(self): return int(self.value)

        def _float(self): return float(self.value)

        def _abs(self): return type(self)(value=abs(self.value))

        def _pos(self): return type(self)(value=+self.value)

        def _neg(self): return type(self)(value=-self.value)

        def _add(self, other):
            if isinstance(other, type(self)):
                return type(self)(value=self.value + other.value)
            elif isinstance(other, (int, float)):
                return type(self)(value=self.value + other)
            return NotImplemented

        def _sub(self, other):
            if isinstance(other, type(self)):
                return type(self)(value=self.value - other.value)
            elif isinstance(other, (int, float)):
                return type(self)(value=self.value - other)
            return NotImplemented

        def _rsub(self, other):
            if isinstance(other, type(self)):
                return type(self)(value=other.value - self.value)
            elif isinstance(other, (int, float)):
                return type(self)(value=other - self.value)
            return NotImplemented

        def _mul(self, other):
            if isinstance(other, (int, float)):
                return type(self)(value=self.value * other)
            elif isinstance(other, Unit) and \
                    other.__class__.__name__ in self.multiply:
                return UnitBase.units[self.multiply[other.__class__.__name__]](
                    value=self.value * other.value)
            return NotImplemented

        def _div(self, other):
            if isinstance(other, type(self)):
                return self.value / other.value
            elif isinstance(other, (int, float)):
                return type(self)(value=self.value / other)
            elif isinstance(other, Unit) and \
                    other.__class__.__name__ in self.divide:
                return UnitBase.units[self.divide[other.__class__.__name__]](
                    value=self.value / other.value)
            return NotImplemented

        def _floordiv(self, other):
            if isinstance(other, type(self)):
                return self.value // other.value
            elif isinstance(other, (int, float)):
                return type(self)(value=self.value // other)
            elif isinstance(other, Unit) and \
                    other.__class__.__name__ in self.divide:
                return UnitBase.units[self.divide[other.__class__.__name__]](
                    value=self.value // other.value)
            return NotImplemented

        def _rdiv(self, other):
            if hasattr(self, 'inverse'):
                return UnitBase.units[self.inverse](value=other / self.value)
            return NotImplemented

        def _rfloordiv(self, other):
            if hasattr(self, 'inverse'):
                return UnitBase.units[self.inverse](value=other // self.value)
            return NotImplemented

        def _pow(self, other):
            if not isinstance(other, int):
                return NotImplemented
            if other > 1:  # [1, infinity]
                return self ** (other - 1) * self
            elif other < 0:  # [-infinity, 0]
                return (1 / self) ** abs(other)
            return 1 if other == 0 else self  # [0, 1]

        def _eq(self, other):
            if type(self) is type(other):
                return self.value == other.value
            return NotImplemented

        def _ne(self, other): return not self == other

        defaultattrs = {
            'convert': {'unit': 1, 'u': 1, 'units': 1}, 'value': 0.0,
            'convertto': _convertto, 'convertfrom': _convertfrom,
            'divide': {}, 'multiply': {},
            '__init__': _init, '__str__': _str, '__repr__': _repr,
            '__getattr__': _getattr, '__setattr__': _setattr, '__int__': _int,
            '__float__': _float, '__abs__': _abs, '__pos__': _pos,
            '__neg__': _neg, '__add__': _add, '__radd__': _add,
            '__sub__': _sub, '__rsub__': _rsub, '__mul__': _mul,
            '__rmul__': _mul, '__div__': _div, '__truediv__': _div,
            '__floordiv__': _floordiv, '__rdiv__': _rdiv,
            '__rtruediv__': _rdiv, '__rfloordiv__': _rfloordiv,
            '__pow__': _pow, '__eq__': _eq, '__ne__': _ne
        }

        for k, v in defaultattrs.items():
            if k not in attrs:
                attrs[k] = v
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        if name != "Unit":  # Subclass of Unit
            UnitBase.units[cls.__name__] = cls


class Unit(with_metaclass(UnitBase)):
    """Classe abstraite d'unité de base."""
    pass
