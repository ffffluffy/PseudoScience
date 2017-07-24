#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure liées à l'électricité et au magnétisme."""

from . import Unit

# Constantes de conversion - modifiez-les pour casser EDF
STATV_V = 299.792458
ABV_V = 1e-8
MA_A = 1e-3
ABA_A = 10
STATA_A = 3.336e-10
GAMMA_T = 1e-9
G_T = 1e-4


class Voltage(Unit):
    """Décrit une unité de tension ou de potentiel électrique. L'unité
    correspondante du système international est le volt (V).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `v` pour des volts ;
    `statv` pour des statvolts ;
    `abv` pour des abvolts."""

    fullname = "volt"
    pluralname = "volts"
    convert = {'v': 1, 'statv': STATV_V, 'abv': ABV_V}
    multiply = {'Current': 'Power', 'Capacity': 'Charge', 'Charge': 'Energy',
                'Conductance': 'Current'}
    divide = {'Current': 'Resistance'}


class Current(Unit):
    """Décrit une unité d'intensité du courant électrique. L'unité
    correspondante du système international est l'ampère (A).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `a` pour des ampères ;
    `ma` pour des milliampères ;
    `aba` ou `bi` pour des abampères (ou biots) ;
    `stata` pour des statampères."""

    fullname = "ampere"
    pluralname = "amperes"
    convert = {'a': 1, 'ma': MA_A, 'aba': ABA_A, 'bi': ABA_A, 'stata': STATA_A}
    multiply = {'Voltage': 'Power', 'Time': 'Charge'}
    divide = {'Voltage': 'Conductance', 'Conductance': 'Voltage'}


class MagneticField(Unit):
    """Décrit un champ magnétique. L'unité correspondante du système
    international est le tesla (T).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `t` pour des teslas ;
    `gamma` pour des gammas ;
    `g` pour des gauss."""

    fullname = "tesla"
    pluralname = "teslas"
    convert = {'t': 1, 'gamma': GAMMA_T, 'g': G_T}
