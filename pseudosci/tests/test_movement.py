#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..movement import *
import pytest


class TestMovement:
    def test_init(self):
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
        mv = Movement(distance=Distance(m=10), time=Time(s=2))
        md = Movement(velocity=Velocity(mps=5), time=Time(s=2))
        mt = Movement(distance=Distance(m=10), velocity=Velocity(mps=5))
        assert mv.velocity.mps == 5
        assert md.distance.m == 10
        assert mt.time.s == 2

    def test_math(self):
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
