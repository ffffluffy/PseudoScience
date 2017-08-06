#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..geometry import Angle, AngularVelocity, DEG_RAD, GON_RAD
from math import pi
import pytest


class TestUnitsGeometry:
    """Tests des unités de pseudosci.units.geometry."""

    def test_angle(self):
        """Tests de Angle."""
        assert issubclass(Angle, Unit)
        assert Angle(deg=180).rad == 180 * DEG_RAD
        assert Angle(gon=200).rad == 200 * GON_RAD
        with pytest.raises(ValueError):
            Angle()

    def test_angularvelocity(self):
        """Tests de AngularVelocity."""
        assert issubclass(AngularVelocity, Unit)
        assert AngularVelocity(radmin=1.0).rads == 60.0
        assert AngularVelocity(radh=1.0).rads == 3600.0
        assert AngularVelocity(degs=180).rads == 180 * DEG_RAD
        assert AngularVelocity(rpm=2 * pi).rads == 60.0
