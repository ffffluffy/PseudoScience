#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ...units import Distance, Velocity, Acceleration
from ...movement import Movement, ComplexMovement
from ..vehicle import Vehicle
import pytest


class TestVehicle:
    """Tests unitaires de pseudosci.transport.Vehicle"""

    def test_init(self):
        """Tests du constructeur et des attributs simples de la classe."""
        v = Vehicle(velocity=Velocity(kph=50),
                    accel=Acceleration(kphs=20),
                    brake=Acceleration(kphs=30))
        assert v.velocity.kph == 50
        assert v.accel.kphs == 20
        assert v.brake.kphs == 30
        v = Vehicle(velocity=Velocity(kph=50), accel=Acceleration(kphs=20))
        assert v.accel.mpss == v.brake.mpss
        v = Vehicle(velocity=Velocity(kph=50))
        assert v.accel.mpss == 0
        assert v.brake.mpss == 0
        with pytest.raises(TypeError):
            Vehicle()
            Vehicle(velocity=1)
            Vehicle(velocity=Velocity(kph=50), accel=1)
            Vehicle(velocity=Velocity(kph=50),
                    accel=Acceleration(kphs=20),
                    brake=1)
        with pytest.raises(ValueError):
            Vehicle(velocity=Velocity(mps=0))
            Vehicle(velocity=Velocity(mps=-1))
            Vehicle(velocity=Velocity(mps=1), accel=Acceleration(mpss=-1))
            Vehicle(velocity=Velocity(mps=1),
                    accel=Acceleration(mpss=0),
                    brake=Acceleration(mpss=-1))

    def test_move(self):
        """Test de la méthode `move(distance)`"""
        cm = Vehicle(velocity=Velocity(kph=50),
                     accel=Acceleration(kphs=20),
                     brake=Acceleration(kphs=30)).move(Distance(km=5))
        m = Vehicle(velocity=Velocity(kph=50)).move(Distance(km=5))
        assert type(cm) is ComplexMovement
        assert type(m) is Movement
        assert m.distance.km == 5
        assert m.velocity.kph == 50
        assert cm.distance.km == 5
        assert cm.velocity.kph == 50
        assert cm.accel.kphs == 20
        assert cm.brake.kphs == -30
