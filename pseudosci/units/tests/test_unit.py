#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import UnitBase, Unit
import pytest


class UnitOne(Unit):
    """Classe utilisée comme premier type d'unité pour les tests unitaires de
    pseudosci.units.Unit."""
    fullname = "unit"
    pluralname = "units"
    convert = {'tupletest': (lambda v: 100 * v, lambda v: v / 100)}


class UnitTwo(Unit):
    """Classe utilisée comme second type d'unité pour les tests unitaires de
    pseudosci.units.Unit."""
    fullname = "unit"
    pluralname = "units"
    inverse = "UnitOne"


class TestUnitBase:
    """Tests de la classe pseudosci.units.UnitBase"""

    def test_required_attributes(self):
        with pytest.raises(AttributeError):
            UnitBase.__new__(Unit, 'AttributeTest', (), {})


class TestUnit:
    """Tests de la classe pseudosci.units.Unit"""

    def test_init(self):
        """Test du constructeur de la classe."""
        assert UnitOne(value=123.4).value == 123.4
        assert str(UnitOne(value=1)) == "1.0 unit"
        assert str(UnitOne(value=123.4)) == "123.4 units"
        assert UnitOne(value=1).__repr__() == "<UnitOne 1.0 unit>"
        assert UnitOne(value=1).convertto('value') == 1
        assert UnitOne(value=100).tupletest == 1
        assert UnitOne(tupletest=1).value == 100

    def test_setattr(self):
        """Test de modification des attributs de la classe."""
        u = UnitOne(value=123.4)
        assert u.value == 123.4
        u.convert["dozens"] = 10.0
        assert u.dozens == 12.34
        u.dozens = 133.7
        assert u.dozens == 133.7
        assert u.value == 1337.0
        u.value = 12.0
        assert u.value == 12.0
        u.dummyattribute = "you dummy"
        assert u.dummyattribute == "you dummy"

    def test_math(self):
        """Tests des opérations mathématiques de la classe."""
        assert abs(UnitOne(value=-4)).value == \
            abs(UnitOne(value=4)).value == 4.0
        assert -UnitOne(value=-4).value == +UnitOne(value=4).value == 4.0
        assert -UnitOne(value=4).value == -4.0
        assert (UnitOne(value=5) + UnitOne(value=4)).value == 9.0
        assert (UnitOne(value=5) - UnitOne(value=4)).value == 1.0
        assert UnitOne(value=4).__rsub__(UnitOne(value=5)).value == 1.0
        assert (5 - UnitOne(value=1)).value == 4.0
        assert (UnitOne(value=5) - 4).value == 1.0
        assert (UnitOne(value=5) + 4).value == 9.0
        assert (UnitOne(value=5) * 2).value == \
            2 * UnitOne(value=5).value == 10.0
        assert (UnitOne(value=5) / 2).value == 2.5
        assert (UnitOne(value=5) // 2).value == 2.0
        assert (UnitOne(value=7.5) / UnitOne(value=2.5)) == 3.0
        assert (UnitOne(value=7.5) // UnitOne(value=2)) == 3.0
        assert (1 / UnitTwo(value=2)).value == 0.5
        assert (1 // UnitTwo(value=2)).value == 0
        assert int(UnitOne(value=23.4)) == 23
        u = UnitOne(value=4)
        u.divide = {'UnitTwo': 'UnitOne'}
        assert (u // UnitTwo(value=2)).value == 2

    def test_math_errors(self):
        """Tests des erreurs dans les opérations mathématiques de la classe."""
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
        assert UnitOne(value=1).__pow__(UnitTwo(value=1)) == NotImplemented

    def test_compare(self):
        """Tests des opérations de comparaison de la classe."""
        assert UnitOne(value=1) == UnitOne(value=1)
        assert UnitOne(value=1) != UnitOne(value=2)
        assert UnitOne(value=1).__eq__(UnitTwo(value=1)) == NotImplemented
