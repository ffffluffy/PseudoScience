#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Données pré-enregistrées concernant la nourriture et les apports
nutritionnels. Les noms utilisés correspondent à la nomenclature des
nutriments décrite dans la documentation du projet.
https://github.com/Lucidiot/PseudoScience/wiki/Nomenclature-des-nutriments"""

from ..units.general import Mass, Energy
from ..humanity.food import NutrientAmount
import json
import inspect
import os

EU_ENERGY_INTAKE = Energy(kcal=2000)
USA_ENERGY_INTAKE = Energy(kcal=2000)


def load_consequences_all(file=None):
    """Charger toutes les conséquences pour la santé de l'excès ou carence en
    nutriments."""
    with open(_parse_file_path(file, 'food_consequences.json'), 'r') as f:
        return json.loads(f.read())


def load_consequences(lang, file=None):
    """Charger les conséquences pour la santé de l'excès ou la carence en
    nutriments dans une langue donnée."""
    return load_consequences_all(file)[lang]


def load_rdi_all(file=None):
    """Charger toutes les valeurs nutritionnelles de référence."""
    with open(_parse_file_path(file, 'food_rdi.json'), 'r') as f:
        parsed_json = json.loads(f.read())
    return {k: _parse_rdi_json(parsed_json[k]) for k in parsed_json}


def load_rdi(variant, file=None):
    """Charger un ensemble de valeurs nutritionnelles de référence selon son
    code de variante."""
    with open(_parse_file_path(file, 'food_rdi.json'), 'r') as f:
        return _parse_rdi_json(json.loads(f.read())[variant])


def _parse_rdi_json(jsondict):
    """Convertir un dictionnaire importé d'un JSON, indiquant les masses en
    milligrammes, en un objet NutrientAmount."""
    return NutrientAmount({nut: Mass(mg=jsondict[nut]) for nut in jsondict})


def _parse_file_path(path, default):
    """Convertir un chemin de fichier en chemin absolu proprement."""
    if path is None:  # Use default
        return default if os.path.isabs(default) else \
            os.path.dirname(inspect.getfile(inspect.currentframe())) + '/' + \
            default
    else:
        return os.path.abspath(path)
