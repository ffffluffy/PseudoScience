#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..misc import movingavg, prefix
from ..units import Unit
import pytest


class TestMisc:
    """Tests des fonctions utilitaires généralistes."""

    def test_movingavg(self):
        """Test de la moyenne glissante."""
        lx = list(range(10))
        ly = [2, 4, 6, 8, 6, 5, 4, 5, 6, 8]
        resx, resy = movingavg(lx, ly)
        assert list(map(round, resx)) == [1, 2, 3, 4, 5, 6, 7, 8]
        assert list(map(round, resy)) == [4, 6, 7, 6, 5, 5, 5, 6]

    def test_prefix(self):
        """Test du préfixage des unités."""

        class DummyUnit(Unit):
            """Unité de test."""
            fullname = "unit"
            pluralname = "units"

        assert prefix(DummyUnit(value=1)) == "1.0 unit"
        assert prefix(DummyUnit(value=1000)) == "1.0 kilounit"
        assert prefix(DummyUnit(value=2000),
                      {"big ": 100, "small ": 10}) == "20.0 big units"
        assert prefix(DummyUnit(value=1000), {}) == "1000.0 units"
        with pytest.raises(ValueError):
            prefix(200)
