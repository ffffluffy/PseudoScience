#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..human import Human
from ...units import Mass, Distance
import pytest


class TestHuman:
    """Tests de la classe pseudosci.humanity.human.Human"""

    def test_init(self):
        """Test du constructeur de la classe."""
        w = Mass(kg=100)
        h = Distance(m=2)
        m = Human(w, h)
        assert m.weight == w
        assert m.height == h
        with pytest.raises(TypeError):
            Human(w, 4)
            Human("lol", h)

    def test_attributes(self):
        """Test des attributs de la classe."""
        w = Mass(kg=100)
        h = Distance(m=2)
        m = Human(w, h)
        assert m.bmi == 25
