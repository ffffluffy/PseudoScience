#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..misc import movingavg
import pytest


class TestMisc:
    """Tests des fonctions utilitaires généralistes."""

    def test_movingavg(self):
        """Test de la moyenne glissante."""
        lx = list(range(10))
        ly = [2, 4, 6, 8, 6, 5, 4, 5, 6, 8]
        resx, resy = movingavg(lx, ly)
        assert resx == [1, 2, 3, 4, 5, 6, 7, 8]
        assert resy == [4, 6, 6, 6, 5, 4, 5, 6]
