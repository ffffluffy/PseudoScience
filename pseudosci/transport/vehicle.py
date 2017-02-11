#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..units import Distance, Velocity, Acceleration
from ..movement import Movement, ComplexMovement


class Vehicle:
    """Décrit un moyen de locomotion standard."""

    def __init__(self, velocity=None, accel=None, brake=None):
        self.velocity = velocity
        self.accel = accel
        self.brake = brake
        if not velocity or type(velocity) is not Velocity:
            raise TypeError("Le paramètre obligatoire ``velocity`` doit être "
                            "une instance de pseudosci.units.Velocity.")
        if velocity.mps <= 0:
            raise ValueError("La vélocité du véhicule doit être strictement "
                             "positive.")
        if not accel:
            self.accel = Acceleration(mpss=0)
        elif type(accel) is not Acceleration:
            raise TypeError("Le paramètre optionnel ``accel`` doit être une "
                            "instance de pseudosci.units.Acceleration.")
        elif accel.mpss < 0:
            raise ValueError("L'accélération du véhicule doit être positive "
                             "ou nulle.")
        if accel and not brake:
            self.brake = accel
        elif not accel and not brake:
            self.brake = Acceleration(mpss=0)
        elif type(brake) is not Acceleration:
            raise TypeError("Le paramètre optionnel ``brake`` doit être une "
                            "instance de pseudosci.units.Acceleration.")
        elif brake.mpss <= 0:
            raise ValueError("La décélération du véhicule doit être "
                             "strictement positive.")

    def move(self, distance):
        if self.accel.mpss <= 0:
            return Movement(distance=distance, velocity=self.velocity)
        else:
            return ComplexMovement(distance=distance, velocity=self.velocity,
                                   accel=self.accel, brake=self.brake)
