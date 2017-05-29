#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Fonctions utilitaires généralistes."""


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
