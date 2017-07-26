#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..heat import Temperature, Pressure, C_K, HPA_PA, BAR_PA, ATM_PA
import pytest


class TestUnitsHeat:
    """Tests des unités de pseudosci.units.heat."""

    def test_temperature(self):
        """Tests de Temperature."""
        assert issubclass(Temperature, Unit)
        assert Temperature(c=123.4).k == 123.4 + C_K
        assert Temperature(f=123.4).k == Temperature.fahrenheit2kelvin(123.4)
        with pytest.raises(ValueError):
            Temperature()

    def test_temperature_conversion(self):
        """Tests des méthodes statiques de conversion de Temperature."""
        assert Temperature.fahrenheit2celsius(32.0) == 0.0
        assert Temperature.fahrenheit2kelvin(32.0) == 273.15
        assert round(Temperature.fahrenheit2kelvin(-459.67), 5) == 0.0
        assert Temperature.kelvin2celsius(273.15) == 0.0
        assert Temperature.kelvin2celsius(0.0) == -273.15
        assert Temperature.celsius2kelvin(0.0) == 273.15
        assert Temperature.celsius2kelvin(-273.15) == 0.0
        assert round(Temperature.kelvin2fahrenheit(0.0), 5) == -459.67

    def test_pressure(self):
        """Tests de Pression."""
        assert issubclass(Pressure, Unit)
        assert Pressure(hpa=123.4).pa == 123.4 * HPA_PA
        assert Pressure(bar=123.4).pa == 123.4 * BAR_PA
        assert Pressure(atm=123.4).pa == 123.4 * ATM_PA
        with pytest.raises(ValueError):
            Pressure()
