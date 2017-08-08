#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..light import Wave, ElectromagneticWave, wavelength_to_rgb
from ..data.constants import LIGHT_VELOCITY
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

    def test_electromagneticwave(self):
        """Tests de pseudosci.light.ElectromagneticWave"""
        assert issubclass(ElectromagneticWave, Wave)
        ew = ElectromagneticWave(amplitude=42, length=Distance(m=450e-9))
        assert ew.velocity == LIGHT_VELOCITY
        # I worked it out in my head.
        assert ew.photonenergy.j == 4.41432398309724e-19
        c = ew.color
        assert c == (ew.red, ew.green, ew.blue)

    def test_wavelength_to_rgb(self):
        """Tests de pseudosci.light.wavelength_to_rgb()"""
        assert wavelength_to_rgb(379) == wavelength_to_rgb(751) == (0, 0, 0)
        assert wavelength_to_rgb(400) == (111, 0, 154)
        assert wavelength_to_rgb(450) == (0, 70, 255)
        assert wavelength_to_rgb(500) == (0, 255, 146)
        assert wavelength_to_rgb(550) == (162, 255, 0)
        assert wavelength_to_rgb(600) == (0, 190, 0)
        assert wavelength_to_rgb(700) == (176, 0, 0)
