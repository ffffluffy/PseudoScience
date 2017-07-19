#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Tests relatifs à la consommation de nourriture humaine."""

from ...units.general import Mass
from ..food import TypedDict, NutrientData, NutrientAmount
import pytest


class TestTypedDict:
    """Tests de la classe pseudosci.humanity.food.TypedDict"""

    def test_dict(self):
        """Test du constructeur de la classe."""
        d = TypedDict({'test': 'pouet'}, age=3)
        assert d.test == 'pouet'
        assert d.age == 3


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
