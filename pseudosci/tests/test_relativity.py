#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..units import Velocity, Time, Distance
from ..data.constants import LIGHT_VELOCITY
from ..movement import Movement
from ..relativity import contraction_factor, lorentz_factor, time_dilation, \
    length_contraction, RelativistMovement


class TestRelativity:
    """Tests du module pseudosci.relativity"""

    def test_contraction_factor(self):
        """Test de contraction_factor(vel)"""
        assert contraction_factor(Velocity(mps=0)) == 1.0
        assert round(contraction_factor(LIGHT_VELOCITY / 10), 3) == 0.995
        assert round(contraction_factor(LIGHT_VELOCITY / 2), 3) == 0.866

    def test_lorentz_factor(self):
        """Test de lorentz_factor(vel)"""
        assert lorentz_factor(Velocity(mps=0)) == 1.0
        assert round(lorentz_factor(LIGHT_VELOCITY / 10), 3) == 1.005
        assert round(lorentz_factor(LIGHT_VELOCITY / 2), 3) == 1.155

    def test_time_dilation(self):
        """Test de time_dilation(time, vel)"""
        t = Time(s=1)
        assert time_dilation(t, Velocity(mps=0)).s == 1.0
        assert round(time_dilation(t, LIGHT_VELOCITY / 10).s, 3) == 1.005
        assert round(time_dilation(t, LIGHT_VELOCITY / 2).s, 3) == 1.155

    def test_length_contraction(self):
        """Test de length_contraction(distance, vel)"""
        d = Distance(m=1)
        assert length_contraction(d, Velocity(mps=0)).m == 1.0
        assert round(length_contraction(d, LIGHT_VELOCITY / 10).m, 3) == 0.995
        assert round(length_contraction(d, LIGHT_VELOCITY / 2).m, 3) == 0.866

    def test_relativist_movement(self):
        """Test de la classe RelativistMovement"""
        assert issubclass(RelativistMovement, Movement)
        m = Movement(distance=Distance(m=1), velocity=LIGHT_VELOCITY / 2)
        rm = RelativistMovement(m)
        assert rm.movement == m
        assert rm.properdistance == m.distance
        assert rm.propertime == m.time
        assert rm.velocity == m.velocity
        assert round(rm.contraction_factor, 3) == 0.866
        assert round(rm.lorentz_factor, 3) == 1.155
        assert round(rm.time, 9) == round(rm.propertime * rm.lorentz, 9)
        assert round(rm.distance, 9) == \
            round(rm.properdistance * rm.contraction, 9)
