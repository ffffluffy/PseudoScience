#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure relatives à la lumière."""

from . import Unit
from .general import Area

# Constantes de conversion - modifiez-les pour briser votre vision
PHOT_LX = 1e4
NOX_LX = 1e-3


class LightIntensity(Unit):
    """Décrit une intensité lumineuse. L'unité correspondante du système
    international est la candela (cd).
    Utilisez le paramètre `cd=` pour instancier la classe."""

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "candela"
        self.pluralname = "candelas"
        self.attributes = {'cd': 1}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))


class LightFlow(Unit):
    """Décrit une mesure de flux lumineux. L'unité correspondante du système
    international est le lumen (lm).
    Utilisez le paramètre `lm=` pour instancier la classe."""

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "lumen"
        self.pluralname = "lumens"
        self.attributes = {'lm': 1}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

    def __truediv__(self, other):
        if isinstance(other, Illuminance):
            return Area(m2=self.lm / other.lx)
        elif isinstance(other, Area):
            return Illuminance(lx=self.lm / other.m2)
        else:
            return Unit.__truediv__(self, other)
    __div__ = __truediv__

    def __floordiv__(self, other):
        if isinstance(other, Illuminance):
            return Area(m2=self.lm // other.lx)
        elif isinstance(other, Area):
            return Illuminance(lx=self.lm // other.m2)
        else:
            return Unit.__floordiv__(self, other)


class Illuminance(Unit):
    """Décrit une mesure d'éclairement lumineux. L'unité correspondante du
    système international est le lux (lx).\n
    Utilisez l'un des paramètres suivants pour instancier la classe :
    `lx=` pour des lux ;
    `phot=` pour des phots ;
    `nox=` pour des nox."""

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = self.pluralname = "lux"
        self.attributes = {'lx': 1, 'lux': 1, 'phot': PHOT_LX, 'nox': NOX_LX}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

    def __mul__(self, other):
        if isinstance(other, Area):
            return LightFlow(lm=self.lx * other.m2)
        else:
            return Unit.__mul__(self, other)
    __rmul__ = __mul__
