#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..human import Human
from ..food import NutrientData, NutrientAmount, Food
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
        with pytest.raises(TypeError):
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

    def test_consequences(self, capsys):
        """Test de conséquences de consommation de nourriture."""
        rdi = NutrientAmount(TEST1=Mass(kg=1),
                             TEST2=Mass(kg=10),
                             TEST3=Mass(kg=100),
                             TEST4A=Mass(ug=1))
        amount = NutrientAmount(TEST1=Mass(kg=1.1),
                                TEST2=Mass(kg=20),
                                TEST3=Mass(kg=10),
                                TEST4B=Mass(g=1))
        conseq = {
            'TEST1': ('Not enough TEST1', 'Too much TEST1'),
            'TEST2': ('Not enough TEST2', 'Too much TEST2'),
            'TEST3': ('Not enough TEST3', 'Too much TEST3'),
            'TEST4A': ('Not enough TEST4A', 'Too much TEST4A'),
            'TEST4B': ('Not enough TEST4B', 'Too much TEST4B')
        }
        Human.consequences(amount, rdi, conseq, lower=0.2, upper=2.0)
        out, err = capsys.readouterr()
        lines = filter(None, out.split('\n'))
        assert len(lines) == 2
        assert lines.count('Too much TEST2 ( TEST2 20.0 kilograms )') == 1
        assert lines.count('Not enough TEST3 ( TEST3 10.0 kilograms )') == 1
