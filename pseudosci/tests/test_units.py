#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..units import *


class TestDistance:

    def test_init(self):
        assert Distance(m=123.4).m == 123.4
        assert Distance(km=123.4).m == 123.4 * KM_M
        assert Distance(au=123.4).m == 123.4 * AU_M
        assert Distance(ly=123.4).m == 123.4 * LY_M

    def test_attributes(self):
        d = Distance(m=LY_M)
        assert d.m == LY_M
        assert d.ly == 1.0
        assert d.au == d.m / AU_M
        assert d.km == d.m / KM_M

    def test_math(self):
        assert abs(Distance(m=-4)).m == abs(Distance(m=4)).m == 4.0
        assert -Distance(m=-4).m == 4.0
        assert -Distance(m=4).m == -4.0
        assert (Distance(m=5) + Distance(m=4)).m == 9.0
        assert (Distance(m=5) - Distance(m=4)).m == 1.0
        assert (Distance(m=5) * 2.0).m == 10.0
        assert (2.0 * Distance(m=5)).m == 10.0
        assert (Distance(m=5) / 2).m == 2.5
        assert (Distance(m=5) // 2).m == 2.0
        assert (Distance(m=7.5) / Distance(m=2.5)) == 3.0
        assert (Distance(m=7.5) // Distance(m=2)) == 3.0

    def test_math_classes(self):
        d = Distance(m=9)
        assert (d / Time(s=2)).mps == 4.5
        assert (d / Velocity(mps=2)).s == 4.5
        assert (d // Time(s=2)).mps == 4
        assert (d // Velocity(mps=2)).s == 4


class TestTime:

    def test_init(self):
        assert Time(s=123.4).s == 123.4
        assert Time(m=123.4).s == 123.4 * MIN_S
        assert Time(h=123.4).s == 123.4 * H_S
        assert Time(d=123.4).s == 123.4 * D_S

    def test_attributes(self):
        t = Time(s=D_S)
        assert t.s == D_S
        assert t.d == 1.0
        assert t.h == t.s / H_S
        assert t.m == t.s / MIN_S

    def test_math(self):
        assert abs(Time(s=-5)).s == abs(Time(s=5)).s == 5.0
        assert -Time(s=-5).s == 5.0
        assert -Time(s=5).s == -5.0
        assert (Time(s=5) + Time(s=4)).s == 9.0
        assert (Time(s=5) - Time(s=4)).s == 1.0
        assert (Time(s=5) * 2).s == 10.0
        assert (2 * Time(s=5)).s == 10.0
        assert (Time(s=5) / 2).s == 2.5
        assert (Time(s=5) // 2).s == 2.0
        assert Time(s=5) / Time(s=2) == 2.5
        assert Time(s=5) // Time(s=2) == 2.0


class TestVelocity:

    def test_init(self):
        assert Velocity(mps=123.4).mps == 123.4
        assert Velocity(kph=123.4).mps == 123.4 * KPH_MPS

    def test_attributes(self):
        v = Velocity(mps=KPH_MPS)
        assert v.mps == KPH_MPS
        assert v.kph == 1.0

    def test_math(self):
        assert abs(Velocity(mps=-5)).mps == abs(Velocity(mps=5)).mps == 5.0
        assert -Velocity(mps=-5).mps == 5.0
        assert -Velocity(mps=5).mps == -5.0
        assert (Velocity(mps=5) + Velocity(mps=4)).mps == 9.0
        assert (Velocity(mps=5) - Velocity(mps=4)).mps == 1.0
        assert (Velocity(mps=5) * 2).mps == 10.0
        assert (2 * Velocity(mps=5)).mps == 10.0
        assert (Velocity(mps=5) / 2).mps == 2.5
        assert (Velocity(mps=5) // 2).mps == 2.0
        assert Velocity(mps=5) / Velocity(mps=2) == 2.5
        assert Velocity(mps=5) // Velocity(mps=2) == 2.0

    def test_math_class(self):
        assert (Velocity(mps=5) * Time(s=4)).m == 20.0
        assert (Velocity(mps=5) / Time(s=2)).mpss == 2.5


class TestAcceleration:

    def test_init(self):
        assert Acceleration(mpss=123.4).mpss == 123.4
        assert Acceleration(kphs=123.4).mpss == 123.4 * KPHS_MPSS

    def test_attributes(self):
        a = Acceleration(mpss=KPHS_MPSS)
        assert a.mpss == KPHS_MPSS
        assert a.kphs == 1.0

    def test_math(self):
        assert abs(Acceleration(mpss=-5)).mpss == 5.0
        assert abs(Acceleration(mpss=5)).mpss == 5.0
        assert -Acceleration(mpss=-5).mpss == 5.0
        assert -Acceleration(mpss=5).mpss == -5.0
        assert (Acceleration(mpss=5) + Acceleration(mpss=4)).mpss == 9.0
        assert (Acceleration(mpss=5) - Acceleration(mpss=4)).mpss == 1.0
        assert (Acceleration(mpss=5) * 2).mpss == 10.0
        assert (2 * Acceleration(mpss=5)).mpss == 10.0
        assert (Acceleration(mpss=5) / 2).mpss == 2.5
        assert (Acceleration(mpss=5) // 2).mpss == 2.0
        assert Acceleration(mpss=5) / Acceleration(mpss=2) == 2.5
        assert Acceleration(mpss=5) // Acceleration(mpss=2) == 2.0

    def test_math_class(self):
        assert (Acceleration(mpss=5) * Time(s=2)).mps == 10.0
