#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..movement import Movement, AcceleratedMovement, ComplexMovement
from ..units import Unit
from ..units.general import Distance, Time, Velocity, Acceleration
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
        with pytest.raises(AttributeError):
            mv.pouet

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
        with pytest.raises(TypeError):
            msum + 42
            msub - "test"
            mmul * mrmul
            mdiv / mfdiv
            mfdiv // mdiv


class TestAcceleratedMovement:
    """Tests de la classe pseudosci.movement.AcceleratedMovement"""
    def test_init(self):
        """Tests du constructeur de la classe."""
        a = AcceleratedMovement(distance=Distance(m=50),
                                time=Time(s=10),
                                velocity=Velocity(mps=10),
                                accel=Acceleration(mpss=1))
        assert a.distance.m == 50
        assert a.time.s == 10
        assert a.velocity.mps == 10
        assert a.accel.mpss == 1
        with pytest.raises(TypeError):
            AcceleratedMovement(accel=0)

    def test_attributes(self):
        """Tests des attributs de la classe."""
        mv = AcceleratedMovement(distance=Distance(m=50), time=Time(s=10))
        mt = AcceleratedMovement(distance=Distance(m=50),
                                 velocity=Velocity(mps=10))
        md = AcceleratedMovement(time=Time(s=10), velocity=Velocity(mps=10))
        assert mv.accel.mpss == md.accel.mpss == mt.accel.mpss == 1
        assert mv.velocity.mps == 10
        assert md.distance.m == 50
        assert mt.time.s == 10
        with pytest.raises(AttributeError):
            mv.pouet


class TestComplexMovement:
    """Tests de la classe pseudosci.movement.ComplexMovement"""
    def test_init(self):
        """Tests du constructeur de la classe."""
        c = ComplexMovement(
            Movement(distance=Distance(m=4), time=Time(s=10)),
            Movement(distance=Distance(m=2), time=Time(s=5))
        )
        assert len(c.movements) == 2

    def test_attributes(self):
        """Tests des attributs de la classe."""
        c = ComplexMovement(
            Movement(distance=Distance(m=4), time=Time(s=10)),
            Movement(distance=Distance(m=2), time=Time(s=5))
        )
        assert c.distance.m == 6
        assert c.time.s == 15
        assert c.velocity.mps == 0.4
        assert c.distances == [Distance(m=4), Distance(m=2)]
        assert c.times == [Time(s=10), Time(s=5)]
        assert c.velocities == [Velocity(mps=0.4), Velocity(mps=0.4)]

    def test_math(self):
        """Tests des calculs effectués par la classe."""
        c = ComplexMovement()
        assert len(c.movements) == 0
        c += Movement(distance=Distance(m=4), time=Time(s=10))
        assert len(c.movements) == 1
        assert c.distance.m == 4
        c += c
        assert len(c.movements) == 2
        assert c.distance.m == 8
        with pytest.raises(TypeError):
            c += "pouet"
