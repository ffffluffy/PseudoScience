#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Être humain et calculs pseudo-scientifiques s'y rattachant."""

from ..units.general import Mass, Distance, Energy
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
            raise AttributeError("{0} object has no attribute {1}".format(
                    self.__class__.__name__, name))

    @staticmethod
    def eat(stuff, mass):
        """Consommation de nourriture dans une quantité donnée."""
        if type(stuff) is Food:
            return (Energy(j=stuff.energy.j * mass.kg),
                    NutrientAmount({k: v * mass
                                    for (k, v) in stuff.nutrients.items()}))
        else:
            return NutrientAmount({k: v * mass for (k, v) in stuff.items()})

    @staticmethod
    def consequences(stuff, rdi, data, lower=0.8, upper=1.3):
        """Conséquences d'apports nutritionnels donnés.
        Prend en paramètre un NutrientAmount pour les apports à comparer,
        un NutrientAmount représentant les apports recommandés et un
        dictionnaire de texte représentant les conséquences d'un apport
        insuffisant ou en excès, sous la forme :
        nutriment: ('si carence', 'si excès')"""
        # Take nutrients present in both arguments
        for nutrient in set(stuff).intersection(set(rdi)):
            pct = stuff[nutrient] / rdi[nutrient]
            if pct <= lower:
                print("{0} ({1} {2})".format(
                    data[nutrient][0], nutrient, stuff[nutrient]))
            elif pct >= upper:
                print("{0} ({1} {2})".format(
                    data[nutrient][1], nutrient, stuff[nutrient]))
