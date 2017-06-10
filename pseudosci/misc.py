#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Fonctions utilitaires généralistes."""

from .data.text import PREFIX_LIST
from .units import Unit


def movingavg(Lx, Ly, p=1):
    """Réalise une moyenne glissante sur une liste de données Ly en modifiant
    l'axe des abscisses Lx selon P : Ne prend que le P premier élément jusqu'au
    P dernier élément, puisqu'une moyenne glissante ne peut pas conserver tous
    les points. Par défaut, P vaut 1."""
    Lxout, Lyout = Lx[p: -p], []
    for i in range(p, len(Ly)-p):
        avg = sum(Ly[i-p:i+p+1]) / (2 * p + 1)
        Lyout.append(avg)
    return Lxout, Lyout


def prefix(unit, prefixes=PREFIX_LIST):
    """Effectue le préfixage d'une unité selon une liste de préfixes donnés.
    Par défaut, pseudosci.data.text.PREFIX_LIST est utilisée."""
    if not issubclass(type(unit), Unit):
        raise ValueError("Parameter `unit` must be an instance of "
                         "pseudosci.units.Unit.")
    from operator import itemgetter
    for key, value in sorted(prefixes.items(),
                             key=itemgetter(1), reverse=True):
        if unit.value // value >= 1:
            return "{0} {1}{2}".format(unit.value / value, key, unit.fullname
                                       if unit.value == 1 else unit.pluralname)
    # Oups, aucun préfixe trouvé
    return str(unit)
