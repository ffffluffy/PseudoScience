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
    `f` pour des degrés Fahrenheit ;
    `b` pour des degrés Benamran."""

    fullname = "Kelvin degree"
    pluralname = "Kelvin degrees"
    convert = {'k': 1,
               'c': (lambda c: c + C_K, lambda k: k - C_K),
               'f': (lambda f: (5.0 / 9.0) * (f - 32.0) + C_K,
                     lambda k: (9.0 / 5.0) * (k - C_K) + 32.0),
               'b': (lambda b: b * (356.7 - 4.2) / 187 + 4.2 + C_K,
                     lambda k: (k - C_K - 4.2) * 187 / (356.7 - 4.2))}

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


class Pressure(Unit):
    """Décrit une mesure de pression d'un gaz. L'unité correspondante du
    système international est le pascal (Pa).\n
    Utilisez l'un des paramètres suivants pour instancier la classe :
    `pa` pour des pascals ;
    `hpa` pour des hectopascals ;
    `bar` pour des bars ;
    `atm` pour des atmosphères."""

    fullname = "pascal"
    pluralname = "pascals"
    convert = {'pa': 1, 'hpa': HPA_PA, 'bar': BAR_PA, 'atm': ATM_PA}
    multiply = {'Area': 'Force'}
