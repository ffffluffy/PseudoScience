#!/usr/bin/env python
# -*- coding:utf-8 -*

from .. import Unit
from ..general import Distance, AU_M, LY_M, IN_M, FT_M, YD_M
import pytest

class TestUnitsGeneral:
    """Tests de pseudosci.units.general"""

    def test_distance(self):
        """Tests de Distance"""
        assert issubclass(Distance, Unit)
        assert Distance(inch=42).m == 1.0668
        assert Distance(m=123).inch == 4842.5196850393704 # attention aux arrondis ?
        assert Distance(ft=123).m == 37.4904
        assert Distance(m=456).ft == 1496.0629921259842
        assert Distance(yd=123).m == 112.4712
        assert Distance(m=789).yd == 862.8608923884515
        with pytest.raises(ValueError):
            Distance()
