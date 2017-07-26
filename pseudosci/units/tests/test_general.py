#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
from ..general import Distance, Time, Velocity, Acceleration, Mass, \
    Force, Area, Volume, Energy, ChemicalAmount, Frequency, Power, Flow, \
    KM_M, AU_M, LY_M, MIN_S, H_S, D_S, KPH_MPS, KPHS_MPSS, G_MPSS, UG_KG, \
    MG_KG, G_KG, T_KG, DYN_N, KGF_N, LBF_N, PDL_N, ACRE_M2, ARPENT_M2, HA_M2, \
    L_M3, KWH_J, KGM_J, CAL_J, KCAL_J, EV_J, CH_W, HP_W
import pytest


class TestUnitsGeneral:
    """Tests des unités de pseudosci.units.general"""

    def test_distance(self):
        """Tests de Distance."""
        assert issubclass(Distance, Unit)
        assert Distance(km=123.4).m == 123.4 * KM_M
        assert Distance(au=123.4).m == 123.4 * AU_M
        assert Distance(ly=123.4).m == 123.4 * LY_M
        with pytest.raises(ValueError):
            Distance()

    def test_time(self):
        """Tests de Time."""
        assert issubclass(Distance, Unit)
        assert Time(m=123.4).s == 123.4 * MIN_S
        assert Time(h=123.4).s == 123.4 * H_S
        assert Time(d=123.4).s == 123.4 * D_S
        with pytest.raises(ValueError):
            Time()

    def test_velocity(self):
        """Tests de Velocity."""
        assert issubclass(Distance, Unit)
        assert Velocity(kph=123.4).mps == 123.4 * KPH_MPS
        with pytest.raises(ValueError):
            Velocity()

    def test_acceleration(self):
        """Tests de Acceleration."""
        assert issubclass(Distance, Unit)
        assert Acceleration(kphs=123.4).mpss == 123.4 * KPHS_MPSS
        assert Acceleration(g=123.4).mpss == 123.4 * G_MPSS
        with pytest.raises(ValueError):
            Acceleration()

    def test_mass(self):
        """Tests de Mass."""
        assert issubclass(Mass, Unit)
        assert Mass(ug=123.4).kg == 123.4 * UG_KG
        assert Mass(mg=123.4).kg == 123.4 * MG_KG
        assert Mass(g=123.4).kg == 123.4 * G_KG
        assert Mass(t=123.4).kg == 123.4 * T_KG
        with pytest.raises(ValueError):
            Mass()

    def test_force(self):
        """Tests de Force."""
        assert issubclass(Force, Unit)
        assert Force(dyn=123.4).n == 123.4 * DYN_N
        assert Force(kgf=123.4).n == 123.4 * KGF_N
        assert Force(lbf=123.4).n == 123.4 * LBF_N
        assert Force(pdl=123.4).n == 123.4 * PDL_N
        with pytest.raises(ValueError):
            Force()

    def test_area(self):
        """Tests de Area."""
        assert issubclass(Area, Unit)
        assert Area(km2=123.4).m2 == 123.4 * (KM_M ** 2)
        assert Area(acre=123.4).m2 == 123.4 * ACRE_M2
        assert Area(arpent=123.4).m2 == 123.4 * ARPENT_M2
        assert Area(ha=123.4).m2 == 123.4 * HA_M2
        with pytest.raises(ValueError):
            Force()

    def test_volume(self):
        """Tests de Volume."""
        assert issubclass(Volume, Unit)
        assert Volume(km3=123.4).m3 == 123.4 * (KM_M ** 3)
        assert Volume(l=123.4).m3 == 123.4 * L_M3
        with pytest.raises(ValueError):
            Volume()

    def test_energy(self):
        """Tests de Energy."""
        assert issubclass(Energy, Unit)
        assert Energy(kwh=123.4).j == 123.4 * KWH_J
        assert Energy(kgm=123.4).j == 123.4 * KGM_J
        assert Energy(cal=123.4).j == 123.4 * CAL_J
        assert Energy(kcal=123.4).j == 123.4 * KCAL_J
        assert Energy(ev=123.4).j == 123.4 * EV_J
        with pytest.raises(ValueError):
            Energy()

    def test_chemical_amount(self):
        """Tests de ChemicalAmount."""
        assert issubclass(ChemicalAmount, Unit)
        assert ChemicalAmount(mol=123.4).mol == 123.4
        with pytest.raises(ValueError):
            ChemicalAmount()

    def test_frequency(self):
        """Tests de Frequency."""
        assert issubclass(Frequency, Unit)
        assert Frequency(hz=123.4).hz == 123.4
        with pytest.raises(ValueError):
            Frequency()

    def test_power(self):
        """Tests de Power."""
        assert issubclass(Power, Unit)
        assert Power(ch=123.4).w == 123.4 * CH_W
        assert Power(hp=123.4).w == 123.4 * HP_W
        with pytest.raises(ValueError):
            Power()

    def test_flow(self):
        """Tests de Flow."""
        assert issubclass(Flow, Unit)
        assert Flow(m3m=1.5).m3s == 90.0
        assert Flow(m3min=1.5).m3s == 90.0
        assert Flow(m3h=1.5).m3s == 5400.0
        assert Flow(ls=1500).m3s == 1.5
        assert Flow(lm=1500).m3s == 90.0
        assert Flow(lmin=1500).m3s == 90.0
        assert Flow(lh=1500).m3s == 5400.0
        with pytest.raises(ValueError):
            Flow()
