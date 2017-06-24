#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Simulation de consommation de nourriture et apports alimentaires aux êtres
humains."""

from ..units import Energy


class TypedDict(dict):
    """Dictionnaire associé à un type pour le rendre plus joli
    ou compréhensible."""

    def __init__(self, *args, **kwargs):
        """Instancie un nouveau dictionnaire typé."""
        self.update(kwargs)
        for dictionary in args:
            self.update(dictionary)

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]


class NutrientData(TypedDict):
    """Données d'apports nutritionnels pour une unité de masse donnée.
    Une valeur de 0.1 équivaudra à 10% de la masse."""

    def __init__(self, *args, **kwargs):
        """Instancie un nouveau groupe d'apports nutritionnels.
        Chaque argument nommé donnera un nouvel attribut au groupe. Des
        dictionnaires peuvent être utilisés à la place des arguments nommés.
        Consultez la documentation du projet pour les noms normalisés d'apports
        nutritionnels utilisés dans le projet."""
        TypedDict.__init__(self, *args, **kwargs)


class NutrientAmount(TypedDict):
    """Apports nutritionnels réels (masses)."""

    def __init__(self, *args, **kwargs):
        """Instancie un nouveau groupe d'apports nutrtionnels réels.
        Chaque argument nommé donnera un nouvel attribut au groupe. Des
        dictionnaires peuvent être utilisés à la place des arguments nommés.
        Consultez la documentation du projet pour les noms normalisés d'apports
        nutritionnels utilisés dans le projet."""
        TypedDict.__init__(self, *args, **kwargs)


class Food(object):
    """Décrit une nourriture et ses propriétés alimentaires."""

    def __init__(self, name, energy, nutrients):
        """Instancie une nourriture avec les nom, quantité d'énergie et apports
        nutritionnels fournis. La quantité d'énergie est représentée pour un
        kilogramme de nourriture."""
        if type(energy) is not Energy:
            raise TypeError("La quantité d'énergie doit être une instance de "
                            "pseudosci.units.Energy.")
        if type(nutrients) is not NutrientData:
            raise TypeError("Les apports nutritionnels doivent être une "
                            "instance de pseudosci.humanity.food.NutrientData")
        self.name = str(name)
        self.energy = energy
        self.nutrients = nutrients
