#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure monétaires. Le package Python `forex-python` est requis.
Une connexion Internet est nécessaire ; les taux de conversion sont chargés à
l'importation du module."""

from . import Unit
from forex_python.converter import CurrencyRates
from collections import ChainMap


def get_rates():
        """Obtenir les derniers taux de change à partir des dollars USD."""
        return dict(ChainMap(CurrencyRates().get_rates('USD'), {'USD': 1}))


class Currency(Unit):
    """Décrit une quantité de monnaie. L'unité de référence utilisée est le
    dollar américain (USD).\n
    Exemple d'utilisation : Currency(eur=40) pour 40 euros.
    La liste complète des paramètres utilisables est disponible à l'adresse
    <http://forex-python.readthedocs.io/en/latest/currencysource.html>"""

    fullname = "dollar américain"
    pluralname = "dollars américains"
    convert = get_rates()

    def update_rates(self):
        """Forcer la mise à jour des taux de change."""
        convert = get_rates()
