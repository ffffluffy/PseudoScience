#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure géometriques. Toutes les unités sont stockées en interne
sous l'unité du système international ou l'unité la plus courante."""

from math import pi
from . import Unit
from .general import MIN_S, H_S

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
    multiply = {'Frequency': 'AngularVelocity'}
    divide = {'Time': 'AngularVelocity'}


class AngularVelocity(Unit):
    """Décrit une vitesse angulaire. L'unité correspondante du système
    international est le radian par seconde (rad.s^-1).\n
    Utilisez un des paramètres suivants pour initialiser la classe :
    `rads` pour des radians par seconde ;
    `radmin` ou `radm` pour des radians par minute ;
    `radh` pour des radians par heure ;
    `degs` pour des degrés par seconde ;
    `rpm` pour des tours par minute."""

    fullname = "radian per second"
    pluralname = "radians per second"
    convert = {'rads': 1, 'radmin': MIN_S, 'radm': MIN_S, 'radh': H_S,
               'degs': DEG_RAD, 'rpm': MIN_S / (2 * pi)}
    multiply = {'Time': 'Angle'}
    divide = {'Frequency': 'Angle', 'Angle': 'Frequency'}
