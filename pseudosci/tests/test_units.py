#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..units import Distance, Time, Velocity, Acceleration, Unit, \
    KM_M, AU_M, LY_M, MIN_S, H_S, D_S, KPH_MPS, KPHS_MPSS


class TestUnit:
    """Tests de la classe pseudosci.units.Unit"""
    def test_init(self):
        """Test du constructeur de la classe."""
        assert Unit(123.4).value == 123.4

    def test_math(self):
        assert abs(Unit(-4)).value == abs(Unit(4)).value == 4.0
        assert -Unit(-4).value == +Unit(4).value == 4.0
        assert -Unit(4).value == -4.0
        assert (Unit(5) + Unit(4)).value == 9.0
        assert (Unit(5) - Unit(4)).value == 1.0
        assert (Unit(5) * 2).value == (2 * Unit(5)).value == 10.0
        assert (Unit(5) / 2).value == 2.5
        assert (Unit(5) // 2).value == 2.0
        assert (Unit(7.5) / Unit(2.5)) == 3.0
        assert (Unit(7.5) // Unit(2)) == 3.0


class TestDistance:
    """Tests de la classe pseudosci.units.Distance"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Distance, Unit)
        assert Distance(km=123.4).m == 123.4 * KM_M
        assert Distance(au=123.4).m == 123.4 * AU_M
        assert Distance(ly=123.4).m == 123.4 * LY_M

    def test_attributes(self):
        """Tests des attributs de la classe."""
        d = Distance(m=LY_M)
        assert d.m == LY_M
        assert d.ly == 1.0
        assert d.au == d.m / AU_M
        assert d.km == d.m / KM_M

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        d = Distance(m=9)
        assert (d / Time(s=2)).mps == 4.5
        assert (d / Velocity(mps=2)).s == 4.5
        assert (d // Time(s=2)).mps == 4
        assert (d // Velocity(mps=2)).s == 4


class TestTime:
    """Tests de la classe pseudosci.units.Time"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Distance, Unit)
        assert Time(m=123.4).s == 123.4 * MIN_S
        assert Time(h=123.4).s == 123.4 * H_S
        assert Time(d=123.4).s == 123.4 * D_S

    def test_attributes(self):
        """Tests des attributs de la classe."""
        t = Time(s=D_S)
        assert t.s == D_S
        assert t.d == 1.0
        assert t.h == t.s / H_S
        assert t.m == t.s / MIN_S


class TestVelocity:
    """Tests de la classe pseudosci.units.Velocity"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Distance, Unit)
        assert Velocity(kph=123.4).mps == 123.4 * KPH_MPS

    def test_attributes(self):
        """Tests des attributs de la classe."""
        v = Velocity(mps=KPH_MPS)
        assert v.mps == KPH_MPS
        assert v.kph == 1.0

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        assert (Velocity(mps=5) * Time(s=4)).m == 20.0
        assert (Velocity(mps=5) / Time(s=2)).mpss == 2.5


class TestAcceleration:
    """Tests de la classe pseudosci.units.Acceleration"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Distance, Unit)
        assert Acceleration(kphs=123.4).mpss == 123.4 * KPHS_MPSS

    def test_attributes(self):
        """Tests des attributs de la classe."""
        a = Acceleration(mpss=KPHS_MPSS)
        assert a.mpss == KPHS_MPSS
        assert a.kphs == 1.0

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        assert (Acceleration(mpss=5) * Time(s=2)).mps == 10.0
