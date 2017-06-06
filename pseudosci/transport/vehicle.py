#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..units import Distance, Velocity, Acceleration, Mass
from ..movement import Movement, AcceleratedMovement, ComplexMovement


class Vehicle:
    """Décrit un moyen de locomotion standard."""

    def __init__(self, velocity=None, accel=None, brake=None, mass=None):
        self.velocity = velocity
        self.accel = accel
        self.brake = brake
        self.mass = mass
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
        if mass and type(mass) is not Mass:
            raise TypeError("Le paramètre optionnel ``mass`` doit être une "
                            "instance de pseudosci.units.Mass.")

    def move(self, distance):
        """Génère un ComplexMovement correspondant au déplacement du véhicule
        sur une distance donnée."""
        c = ComplexMovement()
        if self.accel.mpss > 0:
            c += AcceleratedMovement(
                velocity=self.velocity, accel=self.accel,
                time=self.velocity / self.accel)
        if self.brake.mpss > 0:
            c += AcceleratedMovement(
                velocity=self.velocity, accel=self.accel,
                time=self.velocity / self.accel)
        return c + Movement(
            distance=distance - c.distance, velocity=self.velocity)

    def __getattr__(self, name):
        if name == 'accelforce' or name == 'thrust':
            return self.mass * self.accel
        elif name == 'brakeforce':
            return self.mass * self.brake
