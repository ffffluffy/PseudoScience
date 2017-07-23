#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import Unit
import pytest


class UnitOne(Unit):
    """Classe utilisée comme premier type d'unité pour les tests unitaires de
    pseudosci.units.Unit."""
    fullname = "unit"
    pluralname = "units"


class UnitTwo(Unit):
    """Classe utilisée comme premier type d'unité pour les tests unitaires de
    pseudosci.units.Unit."""
    fullname = "unit"
    pluralname = "units"


class TestUnit:
    """Tests de la classe pseudosci.units.Unit"""
    def test_init(self):
        """Test du constructeur de la classe."""
        assert UnitOne(value=123.4).value == 123.4
        assert str(UnitOne(value=1)) == "1.0 unit"
        assert str(UnitOne(value=123.4)) == "123.4 units"
        assert UnitOne(value=1).__repr__() == "<UnitOne 1.0 unit>"

    def test_math(self):
        """Tests des opérations mathématiques de la classe."""
        assert abs(UnitOne(value=-4)).value == \
            abs(UnitOne(value=4)).value == 4.0
        assert -UnitOne(value=-4).value == +UnitOne(value=4).value == 4.0
        assert -UnitOne(value=4).value == -4.0
        assert (UnitOne(value=5) + UnitOne(value=4)).value == 9.0
        assert (UnitOne(value=5) - UnitOne(value=4)).value == 1.0
        assert (UnitOne(value=5) + 4).value == 9.0
        assert (UnitOne(value=5) * 2).value == \
            2 * UnitOne(value=5).value == 10.0
        assert (UnitOne(value=5) / 2).value == 2.5
        assert (UnitOne(value=5) // 2).value == 2.0
        assert (UnitOne(value=7.5) / UnitOne(value=2.5)) == 3.0
        assert (UnitOne(value=7.5) // UnitOne(value=2)) == 3.0
        assert int(UnitOne(value=23.4)) == 23
        with pytest.raises(TypeError):
            UnitTwo(value=4) + UnitOne(value=1)
        with pytest.raises(TypeError):
            UnitTwo(value=4) - UnitOne(value=1)
        with pytest.raises(TypeError):
            UnitTwo(value=4) * UnitOne(value=1)
        with pytest.raises(TypeError):
            UnitTwo(value=4) / UnitOne(value=1)
        with pytest.raises(TypeError):
            UnitTwo(value=4) // UnitOne(value=1)

    def test_compare(self):
        """Tests des opérations de comparaison de la classe."""
        assert UnitOne(value=1) == UnitOne(value=1)
        assert UnitOne(value=1) != UnitOne(value=2)
