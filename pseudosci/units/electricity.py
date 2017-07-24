#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure liées à l'électricité et au magnétisme."""

from . import Unit

# Constantes de conversion - modifiez-les pour casser EDF
STATV_V = 299.792458
ABV_V = 1e-8
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
