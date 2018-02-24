#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..money import get_rates, Currency
import pytest


class TestUnitsMoney:
    """Tests des unités de pseudosci.units.money."""

    def test_get_rates(self):
        """Tests de la méthode get_rates"""
        assert get_rates().get('USD') == 1

    def test_currency(self):
        """Tests de Currency."""
        assert issubclass(Currency, Unit)
        c = Currency(usd=4)
        assert c.usd == 4.0
        c.update_rates()
        assert c.convert == get_rates()
        with pytest.raises(ValueError):
            Currency()
        with pytest.raises(AttributeError):
            c.pouet
