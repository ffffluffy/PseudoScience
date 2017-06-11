#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Véhicules aux propriétés connues et déjà utilisés dans des études
précédentes. Bien vérifier l'exactitude des informations en fonction du
contexte du calcul à effectuer."""

from ..transport.vehicle import Vehicle
from ..units import Velocity, Acceleration

# Métro lillois (VAL 206) - https://fr.wikipedia.org/wiki/VAL_206
lille_metro = Vehicle(velocity=Velocity(kph=80),
                      accel=Acceleration(mpss=1.4),
                      brake=Acceleration(mpss=1.3),
                      mass=Mass(t=30.5))
