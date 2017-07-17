#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
import pytest


class SubUnit(Unit):
    """Classe utilisée comme deuxième type d'unité pour les tests unitaires de
    pseudosci.units.Unit."""
    pass


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
            SubUnit(4) + Unit(1)
            SubUnit(4) - Unit(1)
            SubUnit(4) * Unit(1)
            SubUnit(4) / Unit(1)
            SubUnit(4) // Unit(1)

    def test_compare(self):
        """Tests des opérations de comparaison de la classe."""
        assert Unit(1) == Unit(1)
        assert Unit(1) != Unit(2)
