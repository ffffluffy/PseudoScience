#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..general import Area
from ..light import LightIntensity, LightFlow, Illuminance, PHOT_LX, NOX_LX
import pytest


class TestLightIntensity:
    """Test de la classe pseudosci.units.light.LightIntensity."""

    def test_all(self):
        """Test de la classe pseudosci.units.light.LightIntensity."""
        assert issubclass(LightIntensity, Unit)
        assert LightIntensity(cd=123.4).cd == 123.4
        with pytest.raises(ValueError):
            LightIntensity()
        with pytest.raises(AttributeError):
            LightIntensity(cd=123.4).pouet


class TestLightFlow:
    """Tests de la classe pseudosci.units.light.LightFlow."""

    def test_class(self):
        """Test de la classe."""
        assert issubclass(LightFlow, Unit)
        assert LightFlow(lm=123.4).lm == 123.4
        with pytest.raises(ValueError):
            LightFlow()
        with pytest.raises(AttributeError):
            LightFlow(lm=123.4).pouet

    def test_math_class(self):
        """Test des opérations mathématiques impliquant d'autres classes."""
        assert (LightFlow(lm=10) / Area(m2=4)).lx == 2.5
        assert (LightFlow(lm=10) // Area(m2=4)).lx == 2.0
        assert (LightFlow(lm=10) / Illuminance(lx=4)).m2 == 2.5
        assert (LightFlow(lm=10) // Illuminance(lx=4)).m2 == 2.0
        with pytest.raises(TypeError):
            LightFlow(lm=1) / Unit(1)
            LightFlow(lm=1) // Unit(1)


class TestIlluminance:
    """Tests de la classe pseudosci.units.lightIlluminance."""

    def test_init(self):
        """Test du constructeur de la classe."""
        assert issubclass(Illuminance, Unit)
        assert Illuminance(phot=123.4).lx == 123.4 * PHOT_LX
        assert Illuminance(nox=123.4).lx == 123.4 * NOX_LX
        with pytest.raises(ValueError):
            Illuminance()

    def test_attributes(self):
        """Test des attributs de la classe."""
        i = Illuminance(phot=1)
        assert i.lx == PHOT_LX
        assert i.phot == 1.0
        assert i.nox == PHOT_LX / NOX_LX
        with pytest.raises(AttributeError):
            i.pouet

    def test_math_class(self):
        """Test des opérations mathématiques impliquant d'autres classes."""
        assert (Illuminance(lx=10) * Area(m2=4)).lm == 40.0
        with pytest.raises(TypeError):
            Illuminance(lx=1) / Unit(1)
            Illuminance(lx=1) // Unit(1)
        
