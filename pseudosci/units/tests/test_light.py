#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..light import LightIntensity, LightFlow, Illuminance, PHOT_LX, NOX_LX
import pytest


class TestUnitsLight:
    """Tests des unités de pseudosci.units.light."""

    def test_light_intensity(self):
        """Tests de LightIntensity."""
        assert issubclass(LightIntensity, Unit)
        assert LightIntensity(cd=123.4).cd == 123.4
        with pytest.raises(ValueError):
            LightIntensity()
        with pytest.raises(AttributeError):
            LightIntensity(cd=123.4).pouet

    def test_light_flow(self):
        """Tests de LightFlow."""
        assert issubclass(LightFlow, Unit)
        assert LightFlow(lm=123.4).lm == 123.4
        with pytest.raises(ValueError):
            LightFlow()
        with pytest.raises(AttributeError):
            LightFlow(lm=123.4).pouet

    def test_illuminance(self):
        """Tests de Illuminance."""
        assert issubclass(Illuminance, Unit)
        assert Illuminance(phot=123.4).lx == 123.4 * PHOT_LX
        assert Illuminance(nox=123.4).lx == 123.4 * NOX_LX
        with pytest.raises(ValueError):
            Illuminance()
