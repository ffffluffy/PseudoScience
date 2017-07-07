#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..light import LightIntensity
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
