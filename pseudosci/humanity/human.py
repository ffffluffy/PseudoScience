#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Être humain et calculs pseudo-scientifiques s'y rattachant."""

from ..units import Mass, Distance, Energy
from .food import NutrientData, NutrientAmount, Food


class Human(object):
    """Définit un être humain."""

    def __init__(self, weight, height):
        """Instancier un nouvel humain."""
        if type(weight) is not Mass:
            raise TypeError("Le poids doit être une instance de Mass.")
        if type(height) is not Distance:
            raise TypeError("La hauteur doit être une instance de Distance.")
        self.weight = weight
        self.height = height

    def __getattr__(self, name):
        if name == 'bmi':
            return self.weight.kg / (self.height.m ** 2)
        else:
            raise AttributeError("Pas d'attribut nommé {0}".format(name))

    @staticmethod
    def eat(stuff, mass):
        """Consommation de nourriture dans une quantité donnée."""
        if type(stuff) is Food:
            return (Energy(j=stuff.energy.j * mass.kg),
                    NutrientAmount({k: v * mass
                                    for (k, v) in stuff.nutrients.items()}))
        else:
            return NutrientAmount({k: v * mass for (k, v) in stuff.items()})
