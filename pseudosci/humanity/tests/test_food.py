#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Tests relatifs à la consommation de nourriture humaine."""

from ...units.general import Mass, Energy
from ..food import TypedDict, NutrientData, NutrientAmount, Food
import pytest


class TestTypedDict:
    """Tests de la classe pseudosci.humanity.food.TypedDict"""

    def test_typed_dict(self):
        """Tests de TypedDict."""
        d = TypedDict({'test': 'pouet'}, age=3)
        assert d.test == 'pouet'
        assert d.age == 3
        d.test = 'toot'
        assert d.test == 'toot'
        del d.age
        assert 'age' not in d


class TestNutrientData:
    """Tests de la classe pseudosci.humanity.food.NutrientData"""

    def test_dict(self):
        """Test du constructeur de la classe."""
        d = NutrientData({'protein': 0.2}, fat=0.1)
        assert d.protein == 0.2
        assert d.fat == 0.1


class TestNutrientAmount:
    """Tests de la classe pseudosci.humanity.food.NutrientAmount"""

    def test_dict(self):
        """Test du constructeur de la classe."""
        d = NutrientAmount({'protein': Mass(kg=0.2)}, fat=Mass(kg=0.1))
        assert d.protein.kg == 0.2
        assert d.fat.kg == 0.1


class TestFood:
    """Tests de la classe pseudosci.humanity.food.Food"""

    def test_types(self):
        e = Energy(j=1)
        d = NutrientData({'protein': 0.2}, fat=0.1)
        with pytest.raises(TypeError):
            Food('Test', Mass(kg=4), d)
        with pytest.raises(TypeError):
            Food('Test', e, Mass(kg=4))
