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

    def __init__(self, cd=None):
        if cd is not None:
            Unit.__init__(self, float(cd))
        else:
            raise ValueError("Pour construire une unité d'intensité lumineuse,"
                             " fournissez `cd`.")
        self.fullname = "candela"
        self.pluralname = "candelas"

    def __getattr__(self, name):
        if name.lower() == 'cd':
            return self.value
        else:
            return Unit.__getattr__(self, name)


class LightFlow(Unit):
    """Décrit une mesure de flux lumineux. L'unité correspondante du système
    international est le lumen (lm).
    Utilisez le paramètre `lm=` pour instancier la classe."""

    def __init__(self, lm=None):
        if lm is not None:
            Unit.__init__(self, float(lm))
        else:
            raise ValueError("Pour construire une unité de flux lumineux,"
                             " fournissez `lm`.")
        self.fullname = "lumen"
        self.pluralname = "lumens"

    def __getattr__(self, name):
        if name.lower() == 'lm':
            return self.value
        else:
            return Unit.__getattr__(self, name)

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

    def __init__(self, lx=None, phot=None, nox=None):
        if lx is not None:
            Unit.__init__(self, float(lx))
        elif phot is not None:
            Unit.__init__(self, float(phot) * PHOT_LX)
        elif nox is not None:
            Unit.__init__(self, float(nox) * NOX_LX)
        else:
            raise ValueError("Pour construire une unité d'éclairement "
                             "lumineux, fournissez `lx`, `phot` ou `nox`.")
        self.fullname = self.pluralname = "lux"

    def __getattr__(self, name):
        if name.lower() in ['lx', 'lux']:
            return self.value
        elif name.lower() == 'phot':
            return self.value / PHOT_LX
        elif name.lower() == 'nox':
            return self.value / NOX_LX
        else:
            return Unit.__getattr__(self, name)

    def __mul__(self, other):
        if isinstance(other, Area):
            return LightFlow(lm=self.lx * other.m2)
        else:
            return Unit.__mul__(self, other)
    __rmul__ = __mul__
