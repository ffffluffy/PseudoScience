#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure géometriques. Toutes les unités sont stockées en interne
sous l'unité du système international ou l'unité la plus courante."""

from math import pi
from ..units import Unit

# Constantes de conversion - modifiez-les pour briser les mathématiques

DEG_RAD = pi / 180
GON_RAD = pi / 200


class Angle(Unit):
    """Décrit un angle. L'unité correspondante du système international est le
    radian (rad).\n
    Utilisez un des paramètres suivants pour initialiser la classe :
    ``rad`` pour des radians ;
    ``deg`` pour des degrés ;
    ``gon`` pour des grades."""

    def __init__(self, rad=None, deg=None, gon=None):
        if rad is not None:
            Unit.__init__(self, float(rad))
        elif deg is not None:
            Unit.__init__(self, float(deg * DEG_RAD))
        elif gon is not None:
            Unit.__init__(self, float(gon * GON_RAD))
        else:
            raise ValueError("Pour construire une unité d'angle, fournissez "
                             "rad, deg ou gon.")

    def __getattr__(self, name):
        if name.lower() == 'rad':
            self.rad = rad = self.value
            return rad
        elif name.lower() == 'deg':
            self.deg = deg = self.value / DEG_RAD
            return deg
        elif name.lower() == 'gon':
            self.gon = gon = self.value / GON_RAD
            return gon
        else:
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))
