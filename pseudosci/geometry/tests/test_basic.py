#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Tests unitaires des éléments basiques de géométrie du projet."""

from ..basic import Point, Line
from math import sqrt
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
        with pytest.raises(TypeError):
            Point(1, 1) - "some object"
        with pytest.raises(TypeError):
            Point(1, 1) * "test"
        with pytest.raises(TypeError):
            Point(1, 1) / "testtest"
        with pytest.raises(TypeError):
            Point(1, 1) // "pouet"

    def test_compare(self):
        """Tests des opérateurs de comparaison de la classe."""
        assert Point(1, 3) == Point(1, 3)
        assert Point(1, 3) != Point(2, 2)


class TestLine:
    """Tests de la classe psedosci.geometry.basic.Line"""

    def test_init(self):
        """Test du constructeur de la classe."""
        p1 = Point(x=1, y=-1)
        p2 = Point(x=-1, y=1)
        l = Line(p1=p1, p2=p2)
        assert l.p1 == p1
        assert l.p2 == p2
        assert str(l) == "Ligne entre {0} et {1}".format(str(p1), str(p2))
        assert l.__repr__() == "<Line p1={0} p2={1}>".format(
            p1.__repr__(), p2.__repr__())
        with pytest.raises(TypeError):
            Line(p1, 1)
        with pytest.raises(TypeError):
            Line(1, p2)

    def test_attributes(self):
        """Test des attributs de la classe."""
        p1 = Point(x=1, y=-1)
        p2 = Point(x=-1, y=1)
        l = Line(p1=p1, p2=p2)
        assert l.distance == l.size == l.length == 2 * sqrt(2)
        assert l.middle == l.midpoint == Point(0, 0)
        assert int(l.angle.deg) == 135
        with pytest.raises(AttributeError):
            l.pouet

    def test_math(self):
        """Test des opérations mathématiques de la classe."""
        p1 = Point(x=1, y=-1)
        p2 = Point(x=-1, y=1)
        p3 = Point(x=2, y=4)
        assert Line(p1, p2) + Line(p2, p3) == Line(p1, p3)
        assert Line(p1, p2) + Line(p3, p2) == Line(p1, p3)
        assert (Line(p1, p2) * 2).length == 4 * sqrt(2)
        assert (Line(p1, p2) / 2).length == sqrt(2)
        with pytest.raises(ValueError):
            Line(p1, p2) + Line(p3, Point(3, 3))
        with pytest.raises(TypeError):
            Line(p1, p2) * "something"
        with pytest.raises(TypeError):
            Line(p1, p2) + "something"
        with pytest.raises(TypeError):
            Line(p1, p2) / "something"

    def test_compare(self):
        """Test des opérations de comparaison de la classe."""
        p1 = Point(1, -1)
        p2 = Point(-1, 1)
        assert Line(p1, p2) == Line(p1, p2)
        assert Line(p1, p2) != Line(p2, p1)
