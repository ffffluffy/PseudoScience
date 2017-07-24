#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..electricity import Voltage, STATV_V, ABV_V, \
    MagneticField, GAMMA_T, G_T
import pytest


class TestVoltage:
    """Tests de la classe pseudosci.units.electricity.Voltage"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Voltage, Unit)
        assert Voltage(statv=123.4).v == 123.4 * STATV_V
        assert Voltage(abv=1e8).v == 1.0
        with pytest.raises(ValueError):
            Voltage()

    def test_attributes(self):
        """Test des attributs de la classe."""
        u = Voltage(v=299.792458)
        assert u.v == 299.792458
        assert u.statv == 1.0
        assert u.abv == 29979245800.0


class TestMagneticField:
    """Tests de la classe pseudosci.units.electricity.MagneticField"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(MagneticField, Unit)
        assert MagneticField(g=123.4).t == 123.4 * G_T
        assert MagneticField(gamma=123.4).t == 123.4 * GAMMA_T
        with pytest.raises(ValueError):
            MagneticField()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        a = MagneticField(t=1)
        assert a.t == 1.0
        assert a.g == 1 / G_T
        assert a.gamma == 1 / GAMMA_T
        with pytest.raises(AttributeError):
            MagneticField.pouet
