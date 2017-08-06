#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Calculs liés à la lumière et aux ondes électromagnétiques."""

from .data.constants import LIGHT_VELOCITY
from .units.geometry import Angle
from math import pi


class Wave(object):
    """Décrit une onde oscillatoire de tout type.
    Préférer utiliser une classe héritant de Wave plutôt que Wave
    lorsque c'est possible."""

    def __init__(self, amplitude=None, length=None, frequency=None,
                 period=None, velocity=None):
        self._amplitude = amplitude
        self._velocity = velocity
        if length:
            self._length = length
            self._period = length / velocity
            self._frequency = 1 / self._period
        elif frequency:
            self._frequency = frequency
            self._period = 1 / frequency
            self._length = self._period * velocity
        elif period:
            self._period = period
            self._frequency = 1 / period
            self._length = period * velocity

    @property
    def amplitude(self):
        return self._amplitude

    @property
    def velocity(self):
        return self._velocity

    @property
    def phasevel(self):
        return self.velocity

    @property
    def wavelength(self):
        return self._length

    @property
    def length(self):
        return self.wavelength

    @property
    def frequency(self):
        return self._frequency

    @property
    def period(self):
        return self._period

    @property
    def wavenumber(self):
        return self.angular_repetency

    @property
    def angular_wavenumber(self):
        return self.angular_repetency

    @property
    def angular_repetency(self):
        return 2 * pi / self._length.m

    @property
    def spectro_wavenumber(self):
        return self.repetency

    @property
    def repetency(self):
        return 1 / self._length.m

    @property
    def pulsatance(self):
        return self.angular_frequency

    @property
    def angular_frequency(self):
        return Angle(rad=2 * pi) * self.frequency
