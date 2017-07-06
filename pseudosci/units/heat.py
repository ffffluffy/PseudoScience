#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesures relatives à l'énergie thermique."""

from . import Unit

# Constantes de conversion - modifiez-les pour briser la thermodynamique
C_K = 273.15


class Temperature(Unit):
    """Décrit une mesure de température. L'unité correspondante du système
    international est le degré Kelvin (°K).\n
    Utilisez l'un des paramètres suivants pour instancier la classe :
    `k` pour des degrés Kelvin ;
    `c` pour des degrés Celsius ;
    `f` pour des degrés Fahrenheit."""

    @staticmethod
    def fahrenheit2kelvin(f):
        return Temperature.fahrenheit2celsius(f) + C_K

    @staticmethod
    def fahrenheit2celsius(f):
        return (5.0 / 9.0) * (f - 32.0)

    @staticmethod
    def kelvin2fahrenheit(k):
        return (9.0 / 5.0) * Temperature.kelvin2celsius(k) + 32.0

    @staticmethod
    def kelvin2celsius(k):
        return k - C_K

    def __init__(self, k=None, c=None, f=None):
        if k is not None:
            Unit.__init__(self, float(k))
        elif c is not None:
            Unit.__init__(self, float(c + C_K))
        elif f is not None:
            Unit.__init__(self, float(self.fahrenheit2kelvin(f)))
        else:
            raise ValueError("Pour construire une unité de température, "
                             "fournissez `c`, `k` ou `f`.")
        self.fullname = "Kelvin degree"
        self.pluralname = "Kelvin degrees"

    def __getattr__(self, name):
        if name.lower() in ['k', 'kelvin']:
            return self.value
        elif name.lower() in ['c', 'celsius']:
            return self.kelvin2celsius(self.value)
        elif name.lower() in ['f', 'fahrenheit']:
            return self.kelvin2fahrenheit(self.value)
        else:
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))
