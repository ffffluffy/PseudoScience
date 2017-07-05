#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..geometry import Angle, DEG_RAD, GON_RAD
from math import pi
import pytest


class TestAngle:
    """Tests de la classe pseudosci.geometry.units.Angle"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Angle, Unit)
        assert Angle(deg=180).rad == 180 * DEG_RAD
        assert Angle(gon=200).rad == 200 * GON_RAD
        with pytest.raises(ValueError):
            Angle()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        a = Angle(rad=pi)
        assert a.rad == pi
        assert a.deg == pi / DEG_RAD
        assert a.gon == pi / GON_RAD
        with pytest.raises(AttributeError):
            Angle.pouet
