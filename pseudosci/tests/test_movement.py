#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..movement import Movement, ComplexMovement
import pytest


class TestMovement:
    """Tests de la classe pseudosci.movement.Movement"""
    def test_init(self):
        """Tests du constructeur de la classe."""
        m = Movement(distance=Distance(m=10),
                     time=Time(s=2),
                     velocity=Velocity(mps=5))
        assert m.distance.m == 10
        assert m.time.s == 2
        assert m.velocity.mps == 5
        with pytest.raises(TypeError):
            Movement()
            Movement(distance=Distance(m=10))
            Movement(time=Time(s=2))
            Movement(velocity=Velocity(mps=5))
            Movement(distance=10, time=2)
            Movement(distance=10, velocity=5)
            Movement(velocity=5, time=2)

    def test_attributes(self):
        """Tests des attributs de la classe."""
        mv = Movement(distance=Distance(m=10), time=Time(s=2))
        md = Movement(velocity=Velocity(mps=5), time=Time(s=2))
        mt = Movement(distance=Distance(m=10), velocity=Velocity(mps=5))
        assert mv.velocity.mps == 5
        assert md.distance.m == 10
        assert mt.time.s == 2

    def test_math(self):
        """Tests des calculs effectués par la classe."""
        msum = Movement(distance=Distance(m=4), time=Time(s=2)) + \
            Movement(distance=Distance(m=6), velocity=Velocity(mps=3))
        assert msum.distance.m == 10
        assert msum.time.s == 4
        assert msum.velocity.mps == 2.5
        msub = Movement(distance=Distance(m=6), velocity=Velocity(mps=2)) - \
            Movement(distance=Distance(m=4), time=Time(s=2))
        assert msub.distance.m == 2
        assert msub.time.s == 1
        assert msub.velocity.mps == 2
        mmul = Movement(distance=Distance(m=4), time=Time(s=2)) * 2
        mrmul = 2 * Movement(distance=Distance(m=4), time=Time(s=2))
        assert mmul.distance.m == 8
        assert mmul.time.s == 4
        assert mmul.velocity.mps == 2
        assert mrmul.distance.m == 8
        assert mrmul.time.s == 4
        assert mrmul.velocity.mps == 2
        mdiv = Movement(distance=Distance(m=5), time=Time(s=2)) / 2
        mfdiv = Movement(distance=Distance(m=5), time=Time(s=2)) // 2
        assert mdiv.distance.m == 2.5
        assert mdiv.time.s == 1
        assert mdiv.velocity.mps == 2.5
        assert mfdiv.distance.m == 2
        assert mdiv.time.s == 1
        assert mdiv.velocity.mps == 2.5


class TestComplexMovement:
    """Tests de la classe pseudosci.movement.ComplexMovement"""
    def test_init(self):
        """Tests du constructeur de la classe."""
        c = ComplexMovement(distance=Distance(km=1),
                            velocity=Velocity(mps=10),
                            accel=Acceleration(mpss=-2),
                            brake=Acceleration(mpss=4))
        assert c.distance.km == 1
        assert c.velocity.mps == 10
        assert c.accel.mpss == 2
        assert c.brake.mpss == -4

    def test_compute(self):
        """Tests des calculs effectués par la classe."""
        ct = ComplexMovement(distance=Distance(km=1),
                             velocity=Velocity(mps=10),
                             accel=Acceleration(mpss=2),
                             brake=Acceleration(mpss=4))
        cd = ComplexMovement(time=Time(s=103.75),
                             velocity=Velocity(mps=10),
                             accel=Acceleration(mpss=2),
                             brake=Acceleration(mpss=4))
        # cv = ComplexMovement(distance=Distance(km=1),
        #                      time=Time(s=103.75),
        #                      accel=Acceleration(mpss=2),
        #                      brake=Acceleration(mpss=4))
        assert ct.time.s == 103.75
        assert cd.distance.km == 1.0
        # assert cv.velocity.mps == 138.33333333333334
        assert ct.acceltime.s == cd.acceltime.s == 5.0
        assert ct.braketime.s == cd.braketime.s == 2.5
        assert ct.maxtime.s == cd.maxtime.s == 96.25
        assert ct.acceldist.m == cd.acceldist.m == 25.0
        assert ct.brakedist.m == cd.brakedist.m == 12.5
        assert ct.maxdist.m == cd.maxdist.m == 962.5
        # assert cv.maxdist.m == cv.maxtime.m == 0.0
        assert ct.meanvelocity.mps == cd.meanvelocity.mps
        # == cv.meanvelocity.mps
