#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Constantes physiques exprimées dans les unités de mesure disponibles dans
le projet. Toutes les constantes sont définies directement à partir des
unités du système international.
Source : https://fr.wikipedia.org/wiki/Constante_physique"""

from ..units import Velocity, Acceleration, Mass, Distance, Force, Time

LIGHT_VELOCITY = Velocity(mps=299792458)
EARTH_GRAVITY = Acceleration(mpss=9.80665)
ATOMIC_MASS = Mass(kg=1.66063904e-27)
BOHR_RADIUS = Distance(m=5.2917721067e-11)
ELECTRON_RADIUS = Distance(m=2.817940325e-15)
ELECTRON_MASS = Mass(kg=9.10938356e-31)
PROTON_MASS = Mass(kg=1.672621898e-27)
NEUTRON_MASS = Mass(kg=1.674927471e-27)
MUON_MASS = Mass(kg=1.883531594e-28)
TAUON_MASS = Mass(kg=3.16747e-27)
W_BOSON_MASS = Mass(kg=1.4334e-25)
Z_BOSON_MASS = Mass(kg=1.62556e-25)
PLANCK_MASS = Mass(kg=2.176470e-8)
PLANCK_TIME = Time(s=5.39106e-44)
PLANCK_LENGTH = Distance(m=1.616229e-35)
PLANCK_AREA = PLANCK_LENGTH ** 2
PLANCK_FORCE = Force(N=1.210e44)
