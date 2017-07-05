#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..human import Human
from ..food import NutrientData, Food
from ...units.general import Mass, Distance, Energy
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

    def test_eat(self):
        """Test de la consommation de nourriture."""
        data = NutrientData(protein=0.2, fat=0.1)
        ate = Human.eat(data, Mass(kg=2))
        assert ate.protein.kg == 0.4
        assert ate.fat.kg == 0.2
        nom = Food("Delicious thing", Energy(j=100), data)
        energy, ate2 = Human.eat(nom, Mass(kg=2))
        assert ate == ate2
        assert energy.j == 200
