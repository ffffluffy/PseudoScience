#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Calculs liés à la lumière et aux ondes électromagnétiques."""

from .data.constants import LIGHT_VELOCITY, PLANCK_CONSTANT
from .units.geometry import Angle
from .units.general import Energy
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


class ElectromagneticWave(Wave):
    """Décrit une onde électromagnétique."""

    def __init__(self, amplitude=None, length=None, frequency=None,
                 period=None):
        Wave.__init__(self, amplitude=amplitude, length=length,
                      frequency=frequency, period=period,
                      velocity=LIGHT_VELOCITY)

    @property
    def photonenergy(self):
        return Energy(j=PLANCK_CONSTANT * self._frequency.hz)

    @property
    def color(self):
        return wavelength_to_rgb(self.wavelength.m * 1e-9)

    @property
    def red(self):
        return self.color[0]

    @property
    def green(self):
        return self.color[1]

    @property
    def blue(self):
        return self.color[2]


def wavelength_to_rgb(wavelength, gamma=0.8):
    """Conversion d'une longueur d'onde électromagnétique en une couleur RGB
    approximative. La longueur d'onde est un nombre en nanomètres entre 380 et
    750 nanomètres.

    Basé sur du code volé sans scrupules d'un wiki
    http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
    Lui-même basé sur du code de Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html"""

    wavelength = float(wavelength)
    R, G, B = 0.0, 0.0, 0.0
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        G, B = ((wavelength - 440) / (490 - 440)) ** gamma, 1.0
    elif wavelength >= 490 and wavelength <= 510:
        G, B = 1.0, (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R, G = ((wavelength - 510) / (580 - 510)) ** gamma, 1.0
    elif wavelength >= 580 and wavelength <= 645:
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
    return (int(R * 255), int(G * 255), int(B * 255))
