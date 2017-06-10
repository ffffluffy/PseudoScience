#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..units import Distance, Time, Velocity, Acceleration, Unit, Mass, \
    Force, Area, Volume, KM_M, AU_M, LY_M, MIN_S, H_S, D_S, KPH_MPS, \
    KPHS_MPSS, UG_KG, MG_KG, G_KG, T_KG, DYN_N, KGF_N, LBF_N, PDL_N, ACRE_M2, \
    ARPENT_M2, HA_M2, L_M3
import pytest


class TestUnit:
    """Tests de la classe pseudosci.units.Unit"""
    def test_init(self):
        """Test du constructeur de la classe."""
        assert Unit(123.4).value == 123.4
        assert str(Unit(1)) == "1.0 unit"
        assert str(Unit(123.4)) == "123.4 units"
        assert Unit(1).__repr__() == "<Unit 1.0 unit>"

    def test_math(self):
        """Tests des opérations mathématiques de la classe."""
        assert abs(Unit(-4)).value == abs(Unit(4)).value == 4.0
        assert -Unit(-4).value == +Unit(4).value == 4.0
        assert -Unit(4).value == -4.0
        assert (Unit(5) + Unit(4)).value == 9.0
        assert (Unit(5) - Unit(4)).value == 1.0
        assert (Unit(5) + 4).value == 9.0
        assert (Unit(5) * 2).value == (2 * Unit(5)).value == 10.0
        assert (Unit(5) / 2).value == 2.5
        assert (Unit(5) // 2).value == 2.0
        assert (Unit(7.5) / Unit(2.5)) == 3.0
        assert (Unit(7.5) // Unit(2)) == 3.0
        assert int(Unit(value=23.4)) == 23
        with pytest.raises(TypeError):
            Distance(m=4) + Unit(1)
            Distance(m=4) - Unit(1)
            Distance(m=4) * Unit(1)
            Distance(m=4) / Unit(1)
            Distance(m=4) // Unit(1)

    def test_compare(self):
        """Tests des opérations de comparaison de la classe."""
        assert Unit(1) == Unit(1)
        assert Unit(1) != Unit(2)
        assert Unit(2) > Unit(1)
        assert Unit(2) >= Unit(1)
        assert Unit(1) >= Unit(1)
        assert Unit(1) < Unit(2)
        assert Unit(1) <= Unit(2)
        assert Unit(1) <= Unit(1)
        with pytest.raises(TypeError):
            Distance(m=4) > Unit(1)
            Distance(m=4) >= Unit(1)
            Distance(m=4) < Unit(1)
            Distance(m=4) <= Unit(1)


class TestDistance:
    """Tests de la classe pseudosci.units.Distance"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Distance, Unit)
        assert Distance(km=123.4).m == 123.4 * KM_M
        assert Distance(au=123.4).m == 123.4 * AU_M
        assert Distance(ly=123.4).m == 123.4 * LY_M
        with pytest.raises(ValueError):
            Distance()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        d = Distance(m=LY_M)
        assert d.m == LY_M
        assert d.ly == 1.0
        assert d.au == d.m / AU_M
        assert d.km == d.m / KM_M
        with pytest.raises(AttributeError):
            d.pouet

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        d = Distance(m=9)
        assert (d / Time(s=2)).mps == 4.5
        assert (d / Velocity(mps=2)).s == 4.5
        assert (d // Time(s=2)).mps == 4
        assert (d // Velocity(mps=2)).s == 4
        assert (d * d).m2 == 81
        assert (d * (d * d)).m3 == 729


class TestTime:
    """Tests de la classe pseudosci.units.Time"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Distance, Unit)
        assert Time(m=123.4).s == 123.4 * MIN_S
        assert Time(h=123.4).s == 123.4 * H_S
        assert Time(d=123.4).s == 123.4 * D_S
        with pytest.raises(ValueError):
            Time()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        t = Time(s=D_S)
        assert t.s == D_S
        assert t.d == 1.0
        assert t.h == t.s / H_S
        assert t.m == t.s / MIN_S
        with pytest.raises(AttributeError):
            t.pouet

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        t = Time(s=10)
        assert (t * Velocity(mps=10)).m == 100
        assert (t * Acceleration(mpss=10)).mps == 100


class TestVelocity:
    """Tests de la classe pseudosci.units.Velocity"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Distance, Unit)
        assert Velocity(kph=123.4).mps == 123.4 * KPH_MPS
        with pytest.raises(ValueError):
            Velocity()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        v = Velocity(mps=KPH_MPS)
        assert v.mps == KPH_MPS
        assert v.kph == 1.0
        with pytest.raises(AttributeError):
            v.pouet

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        assert (Velocity(mps=5) * Time(s=4)).m == 20.0
        assert (Velocity(mps=5) / Time(s=2)).mpss == 2.5
        assert (Velocity(mps=5) / Acceleration(mpss=2)).s == 2.5
        assert (Velocity(mps=5) // Time(s=2)).mpss == 2.0
        assert (Velocity(mps=5) // Acceleration(mpss=2)).s == 2.0
        with pytest.raises(TypeError):
            Velocity(mps=5) / Unit(2)
            Velocity(mps=5) // Unit(2)


class TestAcceleration:
    """Tests de la classe pseudosci.units.Acceleration"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Distance, Unit)
        assert Acceleration(kphs=123.4).mpss == 123.4 * KPHS_MPSS
        with pytest.raises(ValueError):
            Acceleration()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        a = Acceleration(mpss=KPHS_MPSS)
        assert a.mpss == KPHS_MPSS
        assert a.kphs == 1.0
        with pytest.raises(AttributeError):
            a.pouet

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        assert (Acceleration(mpss=5) * Time(s=2)).mps == 10.0
        assert (Acceleration(mpss=5) * Mass(kg=2)).n == 10.0
        with pytest.raises(TypeError):
            Acceleration(mpss=5) * Unit(2)


class TestMass:
    """Tests de la classe pseudosci.units.Mass"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Mass, Unit)
        assert Mass(ug=123.4).kg == 123.4 * UG_KG
        assert Mass(mg=123.4).kg == 123.4 * MG_KG
        assert Mass(g=123.4).kg == 123.4 * G_KG
        assert Mass(t=123.4).kg == 123.4 * T_KG
        with pytest.raises(ValueError):
            Mass()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        m = Mass(kg=T_KG)
        assert m.kg == T_KG
        assert m.t == 1.0
        assert m.g == m.kg / G_KG
        assert m.mg == m.kg / MG_KG
        assert m.ug == m.kg / UG_KG
        with pytest.raises(AttributeError):
            m.pouet

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        assert (Mass(kg=5) * Acceleration(mpss=2)).n == 10.0
        with pytest.raises(TypeError):
            Mass(kg=5) * Unit(2)


class TestForce:
    """Tests de la classe pseudosci.units.Force"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Force, Unit)
        assert Force(dyn=123.4).n == 123.4 * DYN_N
        assert Force(kgf=123.4).n == 123.4 * KGF_N
        assert Force(lbf=123.4).n == 123.4 * LBF_N
        assert Force(pdl=123.4).n == 123.4 * PDL_N
        with pytest.raises(ValueError):
            Force()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        f = Force(n=KGF_N)
        assert f.n == KGF_N
        assert f.kgf == 1.0
        assert f.dyn == f.n / DYN_N
        assert f.lbf == f.n / LBF_N
        assert f.pdl == f.n / PDL_N
        with pytest.raises(AttributeError):
            f.pouet

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        assert (Force(n=10) / Acceleration(mpss=4)).kg == 2.5
        assert (Force(n=10) // Acceleration(mpss=4)).kg == 2.0
        assert (Force(n=10) / Mass(kg=4)).mpss == 2.5
        assert (Force(n=10) // Mass(kg=4)).mpss == 2.0
        with pytest.raises(TypeError):
            Force(n=10) / Unit(1)
            Force(n=10) // Unit(1)


class TestArea:
    """Tests de la classe pseudosci.units.Area"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Area, Unit)
        assert Area(km2=123.4).m2 == 123.4 * (KM_M ** 2)
        assert Area(acre=123.4).m2 == 123.4 * ACRE_M2
        assert Area(arpent=123.4).m2 == 123.4 * ARPENT_M2
        assert Area(ha=123.4).m2 == 123.4 * HA_M2
        with pytest.raises(ValueError):
            Force()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        a = Area(m2=KM_M ** 2)
        assert a.m2 == KM_M ** 2
        assert a.km2 == 1.0
        assert a.acre == a.m2 / ACRE_M2
        assert a.arpent == a.m2 / ARPENT_M2
        assert a.ha == a.m2 / HA_M2
        with pytest.raises(AttributeError):
            a.pouet

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        assert (Area(m2=10) * Distance(m=4)).m3 == 40.0
        assert (Area(m2=10) / Distance(m=4)).m == 2.5
        assert (Area(m2=10) // Distance(m=4)).m == 2.0
        with pytest.raises(TypeError):
            Area(m2=12) * Unit(1)
            Area(m2=12) / Unit(1)
            Area(m2=12) // Unit(1)


class TestVolume:
    """Tests de la classe pseudosci.units.Volume"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        assert issubclass(Volume, Unit)
        assert Volume(km3=123.4).m3 == 123.4 * (KM_M ** 3)
        assert Volume(l=123.4).m3 == 123.4 * L_M3
        with pytest.raises(ValueError):
            Volume()

    def test_attributes(self):
        """Tests des attributs de la classe."""
        a = Volume(m3=KM_M ** 3)
        assert a.m3 == KM_M ** 3
        assert a.km3 == 1.0
        assert a.l == a.m3 / L_M3
        with pytest.raises(AttributeError):
            a.pouet

    def test_math_class(self):
        """Tests des opérations mathématiques impliquant d'autres classes."""
        assert (Volume(m3=10) / Distance(m=4)).m2 == 2.5
        assert (Volume(m3=10) // Distance(m=4)).m2 == 2.0
        assert (Volume(m3=10) / Area(m2=4)).m == 2.5
        assert (Volume(m3=10) // Area(m2=4)).m == 2.0
        with pytest.raises(TypeError):
            Volume(m3=1) / Unit(1)
            Volume(m3=1) // Unit(1)
