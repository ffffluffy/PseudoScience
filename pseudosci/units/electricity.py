#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure liées à l'électricité et au magnétisme."""

from . import Unit

# Constantes de conversion - modifiez-les pour casser EDF
GAMMA_T = 1e-9
G_T = 1e-4


class MagneticField(Unit):
    """Décrit un champ magnétique. L'unité correspondante du système
    international est le tesla (T).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `t` pour des teslas ;
    `gamma` pour des gammas ;
    `g` pour des gauss."""

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "tesla"
        self.pluralname = "teslas"
        self.attributes = {'t': 1, 'gamma': GAMMA_T, 'g': G_T}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))
