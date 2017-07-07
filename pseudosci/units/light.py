#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure relatives à la lumière."""

from . import Unit


class LightIntensity(Unit):
    """Décrit une intensité lumineuse. L'unité correspondante du système
    international est la candela (cd).
    Utilisez le paramètre `cd=` pour instancier la classe."""

    def __init__(self, cd=None):
        if cd is not None:
            Unit.__init__(self, float(cd))
        else:
            raise ValueError("Pour construire une unité d'intensité lumineuse,"
                             " fournissez `cd`.")
        self.fullname = "candela"
        self.pluralname = "candelas"

    def __getattr__(self, name):
        if name.lower() == 'cd':
            return self.value
        else:
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))
