#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Tests unitaires des éléments basiques de géométrie du projet."""

from ..basic import Point
import pytest


class TestPoint:
    """Tests de la classe pseudosci.geometry.basic.Point"""

    def test_init(self):
        """Tests du constructeur de la classe."""
        p = Point(123.4, 432.1)
        assert p.x == 123.4
        assert p.y == 432.1
        assert str(p) == "Point à X=123.4 et Y=432.1"
        assert p.__repr__() == "<Point X=123.4 Y=432.1>"

    def test_math(self):
        """Tests des opérations mathématiques de la classe."""
        assert abs(Point(-3, 4)) == Point(3, 4)
        assert +Point(-3, 4) == Point(-3, 4)
        assert -Point(-3, 4) == Point(3, -4)
        assert Point(1, 2) + Point(2, 1) == Point(1, 2) + (2, 1) == Point(3, 3)
        assert Point(3, 3) - Point(2, 1) == Point(3, 3) - (2, 1) == Point(1, 2)
        assert Point(1, 2) * Point(3, 4) == Point(1, 2) * (3, 4) == Point(3, 8)
        assert Point(1, 2) * 2 == Point(2, 4)
        assert Point(5, 3) / 2 == Point(2.5, 1.5)
        assert Point(5, 3) // 2 == Point(2, 1)
        with pytest.raises(TypeError):
            Point(1, 1) + 4
            Point(1, 1) - "some object"
            Point(1, 1) * "test"
            Point(1, 1) / "testtest"
            Point(1, 1) // "pouet"

    def test_compare(self):
        """Tests des opérateurs de comparaison de la classe."""
        assert Point(1, 3) == Point(1, 3)
        assert Point(1, 3) != Point(2, 2)
