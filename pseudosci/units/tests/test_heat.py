#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..heat import Temperature, C_K
import pytest


class TestTemperature:
    """Tests de la classe pseudosci.units.heat.Temperature"""

    def test_init(self):
        """Test du constructeur de la classe."""
        assert issubclass(Temperature, Unit)
        assert Temperature(c=123.4).k == 123.4 + C_K
        assert Temperature(f=123.4).k == Temperature.fahrenheit2kelvin(123.4)
        with pytest.raises(ValueError):
            Temperature()

    def test_conversion(self):
        """Test des méthodes statiques de conversion de la classe."""
        assert Temperature.fahrenheit2celsius(32.0) == 0.0
        assert Temperature.fahrenheit2kelvin(32.0) == 273.15
        assert round(Temperature.fahrenheit2kelvin(-459.67), 5) == 0.0
        assert Temperature.kelvin2celsius(273.15) == 0.0
        assert Temperature.kelvin2celsius(0.0) == -273.15
        assert round(Temperature.kelvin2fahrenheit(0.0), 5) == -459.67

    def test_attributes(self):
        """Test des attributs de la classe."""
        t = Temperature(k=0)
        assert t.k == 0.0
        assert t.c == -273.15
        assert round(t.f, 5) == -459.67
