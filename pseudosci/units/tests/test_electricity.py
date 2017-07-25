#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..electricity import Voltage, STATV_V, ABV_V, Current, MA_A, ABA_A, \
    STATA_A, Capacity, UF_F, ABF_F, STATF_F, JAR_F, Resistance, KOHM_OHM, \
    ABOHM_OHM, STATOHM_OHM, Charge, ABC_C, STATC_C, AH_C, MAH_C, Conductance, \
    MagneticField, GAMMA_T, G_T
import pytest


class TestUnitsElectricity:
    """Tests des unités de pseudosci.units.electricity."""

    def test_voltage(self):
        """Tests de Voltage."""
        assert issubclass(Voltage, Unit)
        assert Voltage(statv=123.4).v == 123.4 * STATV_V
        assert Voltage(abv=1e8).v == 1.0
        with pytest.raises(ValueError):
            Voltage()

    def test_current(self):
        """Tests de Current."""
        assert issubclass(Current, Unit)
        assert Current(stata=123.4).a == 123.4 * STATA_A
        assert Current(aba=0.1).a == 1.0
        assert Current(ma=1000).a == 1.0
        with pytest.raises(ValueError):
            Current()

    def test_capacity(self):
        """Tests de Capacity."""
        assert issubclass(Capacity, Unit)
        assert Capacity(f=123.4).f == 123.4
        assert round(Capacity(mf=123.4e6).f, 1) == 123.4
        assert Capacity(abf=123.4e-9).f == 123.4
        assert Capacity(statf=123.4).f == 123.4 * STATF_F
        assert Capacity(jar=1e11).f == 111.1
        with pytest.raises(ValueError):
            Capacity()

    def test_resistance(self):
        """Tests de Resistance."""
        assert issubclass(Resistance, Unit)
        assert Resistance(ohm=123.4).ohm == 123.4
        assert Resistance(kohm=123.4).ohm == 123400.0
        assert Resistance(abohm=1e9).ohm == 1.0
        assert Resistance(statohm=123.4).ohm == 123.4 * STATOHM_OHM
        with pytest.raises(ValueError):
            Resistance()

    def test_charge(self):
        """Tests de Charge."""
        assert issubclass(Charge, Unit)
        assert Charge(c=123.4).c == 123.4
        assert Charge(abc=12.34).c == 123.4
        assert Charge(statc=123.4).c == 123.4 * STATC_C
        assert Charge(ah=1.5).c == 5400.0
        assert Charge(mah=1.5e3).c == 5400.0
        with pytest.raises(ValueError):
            Charge()

    def test_conductance(self):
        """Tests de Conductance."""
        assert issubclass(Conductance, Unit)
        assert Conductance(s=123.4).s == 123.4

    def test_magnetic_field(self):
        """Tests de MagneticField."""
        assert issubclass(MagneticField, Unit)
        assert MagneticField(g=123.4).t == 123.4 * G_T
        assert MagneticField(gamma=123.4).t == 123.4 * GAMMA_T
        with pytest.raises(ValueError):
            MagneticField()
