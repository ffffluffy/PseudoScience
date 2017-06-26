#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Calculs liés à la théorie de la relativité."""

from math import sqrt
from data.constants import LIGHT_VELOCITY


def contraction_factor(vel):
    return sqrt(1 - (vel ** 2) / (LIGHT_VELOCITY ** 2))


def lorentz_factor(vel):
    return 1 / contraction_factor(vel)


def time_dilation(time, vel):
    return time / contraction_factor(vel)


def length_contraction(distance, vel):
    return distance * contraction_factor(vel)
