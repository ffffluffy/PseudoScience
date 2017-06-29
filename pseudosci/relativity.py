#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Calculs liés à la théorie de la relativité."""

from math import sqrt
from data.constants import LIGHT_VELOCITY
from movement import Movement


def contraction_factor(vel):
    return sqrt(1 - (vel ** 2) / (LIGHT_VELOCITY ** 2))


def lorentz_factor(vel):
    return 1 / contraction_factor(vel)


def time_dilation(time, vel):
    return time / contraction_factor(vel)


def length_contraction(distance, vel):
    return distance * contraction_factor(vel)


class RelativistMovement(Movement):
    """Convertit un mouvement quelconque en un mouvement soumis à la dilatation
    du temps et à la contraction des longueurs. Prend en paramètre le mouvement
    à convertir.
    `distance` et `time` deviennent `properdistance` et `propertime`, et les
    attributs `distance` et `time` représentent ceux mesurés."""

    def __init__(self, movement):
        self.movement = movement

    def __getattr__(self, name):
        if name == 'properdistance':
            return self.movement.distance
        elif name == 'propertime':
            return self.movement.time
        elif name == 'velocity':
            return self.movement.velocity
        elif name in ['lorentz', 'lorentz_factor']:
            return lorentz_factor(self.velocity)
        elif name in ['contraction', 'contraction_factor']:
            return contraction_factor(self.velocity)
        elif name == 'distance':
            return length_contraction(self.properdistance, self.velocity)
        elif name == 'time':
            return time_dilation(self.propertime, self.velocity)
