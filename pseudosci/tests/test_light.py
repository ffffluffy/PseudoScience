#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..light import Wave
from ..units.general import Time, Frequency, Distance, Velocity
from ..units.geometry import Angle, AngularVelocity
from math import pi
import pytest


class TestLight:
    """Tests du module pseudosci.light"""

    def test_wave(self):
        """Tests de pseudosci.light.Wave"""
        wl = Wave(amplitude=123.4, length=Distance(m=0.2),
                  velocity=Velocity(mps=2.0))
        wf = Wave(amplitude=123.4, frequency=Frequency(hz=10),
                  velocity=Velocity(mps=2.0))
        wp = Wave(amplitude=123.4, period=Time(s=0.1),
                  velocity=Velocity(mps=2.0))
        assert wl.amplitude == wf.amplitude == wp.amplitude == 123.4
        assert wl.velocity.mps == wf.velocity.mps == wp.velocity.mps == 2.0
        assert wl.phasevel.mps == wf.phasevel.mps == wp.phasevel.mps == 2.0
        assert wl.length.m == wf.length.m == wp.length.m == 0.2
        assert wl.wavelength.m == wf.wavelength.m == wp.wavelength.m == 0.2
        assert wl.frequency.hz == wf.frequency.hz == wp.frequency.hz == 10.0
        assert wl.period.s == wf.period.s == wp.period.s == 0.1
        assert wl.spectro_wavenumber == wl.repetency == 5.0
        assert wl.wavenumber == wl.angular_wavenumber == \
            wl.angular_repetency == 10 * pi
        assert wf.pulsatance.rads == wf.angular_frequency.rads == 20 * pi
