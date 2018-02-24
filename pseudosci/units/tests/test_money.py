#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..money import get_rates, Currency
import pytest


class TestUnitsMoney:
    """Tests des unités de pseudosci.units.money."""

    def test_get_rates(self):
        """Tests de la méthode get_rates"""
        rates = get_rates()
        assert rates.get('USD') == 1
        assert 'BTC' in rates

    def test_currency(self):
        """Tests de Currency."""
        assert issubclass(Currency, Unit)
        c = Currency(usd=4)
        assert c.usd == 4.0
        c.update_rates()
        # Vérifier tous les éléments sauf BTC (trop souvent mis à jour)
        assert sum(True for (k, v) in get_rates().items()
                   if k != 'BTC' and c.convert[k] != v) == 0
        with pytest.raises(ValueError):
            Currency()
        with pytest.raises(AttributeError):
            c.pouet
