#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Simulation de mouvements rectilignes prenant en charge les accélérations
et freinages."""

from units import *


class Movement(object):
    """Décrit un mouvement rectiligne uniforme. Au moins deux des paramètres
    suivants sont obligatoires : ``distance=``, ``velocity=``, ``time=``."""

    def __init__(self, distance=None, velocity=None, time=None):
        if not (distance and (velocity or time)) and not (time and velocity):
            raise TypeError("Des arguments obligatoires sont manquants.\n"
                            "Movement doit être initialisé avec au moins deux "
                            "des paramètres suivants : ``distance=``, "
                            "``velocity=``, ``time=``")
        if type(distance) is not Distance:
            raise TypeError("Le paramètre ``distance`` doit être une instance "
                            "de pseudosci.units.Distance.")
        if type(velocity) is not Velocity:
            raise TypeError("Le paramètre ``velocity`` doit être une instance "
                            "de pseudosci.units.Velocity.")
        if type(time) is not Time:
            raise TypeError("Le paramètre ``time`` doit être une instance "
                            "de pseudosci.units.Time.")
        self.distance = distance
        self.velocity = velocity
        self.time = time

    def __getattr__(self, name):
        if name == 'velocity':
            self.velocity = self.distance / self.time
            return self.velocity
        elif name == 'distance':
            self.distance = self.velocity * self.time
            return self.distance
        elif name == 'time':
            self.time = self.distance / self.velocity
            return self.time
        else:
            raise AttributeError("Aucun attribut nommé {0}".format(name))
