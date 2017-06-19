#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Simulation de consommation de nourriture et apports alimentaires aux êtres
humains."""


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
