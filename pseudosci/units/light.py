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

    fullname = "candela"
    pluralname = "candelas"
    convert = {'cd': 1}


class LightFlow(Unit):
    """Décrit une mesure de flux lumineux. L'unité correspondante du système
    international est le lumen (lm).
    Utilisez le paramètre `lm=` pour instancier la classe."""

    fullname = "lumen"
    pluralname = "lumens"
    convert = {'lm': 1}
    divide = {'Illuminance': 'Area', 'Area': 'Illuminance'}


class Illuminance(Unit):
    """Décrit une mesure d'éclairement lumineux. L'unité correspondante du
    système international est le lux (lx).\n
    Utilisez l'un des paramètres suivants pour instancier la classe :
    `lx=` pour des lux ;
    `phot=` pour des phots ;
    `nox=` pour des nox."""

    fullname = pluralname = "lux"
    convert = {'lx': 1, 'lux': 1, 'phot': PHOT_LX, 'nox': NOX_LX}
    multiply = {'Area': 'LightFlow'}
