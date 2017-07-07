#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..light import LightIntensity, LightFlow
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

    def test_all(self):
        """Test de la classe pseudosci.units.light.LightFlow."""
        assert issubclass(LightFlow, Unit)
        assert LightFlow(lm=123.4).lm == 123.4
        with pytest.raises(ValueError):
            LightFlow()
        with pytest.raises(AttributeError):
            LightFlow(lm=123.4).pouet
