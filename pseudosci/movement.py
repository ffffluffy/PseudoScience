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
        if distance and type(distance) is not Distance:
            raise TypeError("Le paramètre ``distance`` doit être une instance "
                            "de pseudosci.units.Distance.")
        if velocity and type(velocity) is not Velocity:
            raise TypeError("Le paramètre ``velocity`` doit être une instance "
                            "de pseudosci.units.Velocity.")
        if time and type(time) is not Time:
            raise TypeError("Le paramètre ``time`` doit être une instance "
                            "de pseudosci.units.Time.")
        if distance:
            self.distance = distance
        if velocity:
            self.velocity = velocity
        if time:
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

    def __repr__(self):
        return '<Movement {0},{1},{2}>'.format(
            self.distance, self.time, self.velocity)

    def __add__(self, other):
        if type(other) is Movement:
            return Movement(distance=self.distance + other.distance,
                            time=self.time + other.time)
        else:
            raise TypeError("Un Movement ne peut être ajouté qu'à un Movement")

    def __sub__(self, other):
        if type(other) is Movement:
            return Movement(distance=self.distance - other.distance,
                            time=self.time - other.time)
        else:
            raise TypeError("Un Movement ne peut être soustrait qu'à un "
                            "Movement")

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Movement(distance=self.distance * other,
                            time=self.time * other)
        else:
            raise TypeError("Un Movement ne peut être multiplié que par un "
                            "nombre.")
    __rmul__ = __mul__

    def __div__(self, other):
        if type(other) is int or type(other) is float:
            return Movement(distance=self.distance / other,
                            time=self.time / other)
        else:
            raise TypeError("Un Movement ne peut être divisé que par un "
                            "nombre.")

    def __floordiv__(self, other):
        if type(other) is int or type(other) is float:
            return Movement(distance=self.distance // other,
                            time=self.time // other)
        else:
            raise TypeError("Un Movement ne peut être divisé que par un "
                            "nombre.")
