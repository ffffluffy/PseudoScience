#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure géometriques. Toutes les unités sont stockées en interne
sous l'unité du système international ou l'unité la plus courante."""

from math import pi
from . import Unit

# Constantes de conversion - modifiez-les pour briser les mathématiques

DEG_RAD = pi / 180
GON_RAD = pi / 200


class Angle(Unit):
    """Décrit un angle. L'unité correspondante du système international est le
    radian (rad).\n
    Utilisez un des paramètres suivants pour initialiser la classe :
    `rad` pour des radians ;
    `deg` pour des degrés ;
    `gon` pour des grades."""

    fullname = "radian"
    pluralname = "radians"
    convert = {'rad': 1, 'deg': DEG_RAD, 'gon': GON_RAD}
