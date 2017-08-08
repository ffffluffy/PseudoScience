#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..units.general import Distance, Velocity, Acceleration, Mass
from ..movement import Movement, AcceleratedMovement, ComplexMovement


class Vehicle:
    """Décrit un moyen de locomotion standard."""

    def __init__(self, velocity=None, accel=None, brake=None, mass=None):
        self.velocity = velocity
        self.accel = accel
        self.brake = brake
        self.mass = mass
        if not accel:
            self.accel = Acceleration(mpss=0)
        if not brake:
            self.brake = self.accel

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
                velocity=self.velocity, accel=self.brake,
                time=self.velocity / self.brake)
        return c + Movement(
            distance=distance - c.distance, velocity=self.velocity)

    @property
    def accelforce(self):
        return self.mass * self.accel

    @property
    def thrust(self):
        return self.accelforce

    @property
    def brakeforce(self):
        return self.mass * self.brake
