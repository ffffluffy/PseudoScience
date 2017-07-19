#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesures relatives à l'énergie thermique."""

from . import Unit
from .general import Area, Force

# Constantes de conversion - modifiez-les pour briser la thermodynamique
C_K = 273.15
HPA_PA = 100
BAR_PA = 1e5
ATM_PA = 101325


class Temperature(Unit):
    """Décrit une mesure de température. L'unité correspondante du système
    international est le degré Kelvin (°K).\n
    Utilisez l'un des paramètres suivants pour instancier la classe :
    `k` pour des degrés Kelvin ;
    `c` pour des degrés Celsius ;
    `f` pour des degrés Fahrenheit."""

    @staticmethod
    def fahrenheit2kelvin(f):
        """Convertir de degrés Fahrenheit en degrés Kelvin."""
        return Temperature.fahrenheit2celsius(f) + C_K

    @staticmethod
    def fahrenheit2celsius(f):
        """Convertir de degrés Fahrenheit en degrés Celsius."""
        return (5.0 / 9.0) * (f - 32.0)

    @staticmethod
    def kelvin2fahrenheit(k):
        """Convertir de degrés Kelvin en degrés Fahrenheit."""
        return (9.0 / 5.0) * Temperature.kelvin2celsius(k) + 32.0

    @staticmethod
    def kelvin2celsius(k):
        """Convertir de degrés Kelvin en degrés Celsius."""
        return k - C_K

    @staticmethod
    def celsius2kelvin(c):
        """Convertir de degrés Celsius en degrés Kelvin."""
        return c + C_K

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "Kelvin degree"
        self.pluralname = "Kelvin degrees"
        self.attributes = {'k': 1,
                           'c': (self.celsius2kelvin, self.kelvin2celsius),
                           'f': (self.fahrenheit2kelvin,
                                 self.kelvin2fahrenheit)}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

    def __getattr__(self, name):
        if name.lower() in ['k', 'kelvin']:
            return self.value
        elif name.lower() in ['c', 'celsius']:
            return self.kelvin2celsius(self.value)
        elif name.lower() in ['f', 'fahrenheit']:
            return self.kelvin2fahrenheit(self.value)
        else:
            return Unit.__getattr__(self, name)


class Pressure(Unit):
    """Décrit une mesure de pression d'un gaz. L'unité correspondante du
    système international est le pascal (Pa).\n
    Utilisez l'un des paramètres suivants pour instancier la classe :
    `pa` pour des pascals ;
    `hpa` pour des hectopascals ;
    `bar` pour des bars ;
    `atm` pour des atmosphères."""

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "pascal"
        self.pluralname = "pascals"
        self.attributes = {'pa': 1, 'hpa': HPA_PA,
                           'bar': BAR_PA, 'atm': ATM_PA}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

    def __mul__(self, other):
        if type(other) is Area:
            return Force(n=self.pa * other.m2)
        else:
            return Unit.__mul__(self, other)
    __rmul__ = __mul__
