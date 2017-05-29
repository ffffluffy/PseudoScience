#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Simulation de mouvements rectilignes prenant en charge les accélérations
et freinages."""

from .units import Unit, Distance, Time, Velocity, Acceleration


class Movement(object):
    """Décrit un mouvement rectiligne uniforme. Au moins deux des paramètres
    suivants sont obligatoires : ``distance=``, ``velocity=``, ``time=``."""

    def __init__(self, distance=None, velocity=None, time=None):
        if not (distance and (velocity or time)) and not (time and velocity):
            raise TypeError("Des arguments obligatoires sont manquants.\n"
                            "Utiliser au moins deux des paramètres suivants : "
                            "``distance=``, ``velocity=``, ``time=``")
        if distance and type(distance) is not Distance:
            raise TypeError("Le paramètre ``distance`` doit être une instance "
                            "de pseudosci.units.Distance.")
        if velocity and type(velocity) is not Velocity:
            raise TypeError("Le paramètre ``velocity`` doit être une instance "
                            "de pseudosci.units.Velocity.")
        if time and type(time) is not Time:
            raise TypeError("Le paramètre ``time`` doit être une instance "
                            "de pseudosci.units.Time.")
        if distance:
            self.distance = distance
        if velocity:
            self.velocity = velocity
        if time:
            self.time = time

    def __getattr__(self, name):
        if name == 'velocity':
            self.velocity = self.distance / self.time
            return self.velocity
        elif name == 'distance':
            self.distance = self.velocity * self.time
            return self.distance
        elif name == 'time':
            self.time = self.distance / self.velocity
            return self.time
        else:
            raise AttributeError("Aucun attribut nommé {0}".format(name))

    def __repr__(self):
        return '<{0} {1},{2},{3}>'.format(
            type(self).__name__, self.distance, self.time, self.velocity)

    def __add__(self, other):
        if type(self) is type(other):
            return type(self)(distance=self.distance + other.distance,
                              time=self.time + other.time)
        else:
            raise TypeError("Un Movement ne peut être ajouté qu'à un Movement")

    def __sub__(self, other):
        if type(self) is type(other):
            return type(self)(distance=self.distance - other.distance,
                              time=self.time - other.time)
        else:
            raise TypeError("Un Movement ne peut être soustrait qu'à un "
                            "Movement")

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Movement(distance=self.distance * other,
                            time=self.time * other)
        else:
            raise TypeError("Un Movement ne peut être multiplié que par un "
                            "nombre.")
    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return Movement(distance=self.distance / other,
                            time=self.time / other)
        else:
            raise TypeError("Un Movement ne peut être divisé que par un "
                            "nombre.")
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is int or type(other) is float:
            return Movement(distance=self.distance // other,
                            time=self.time // other)
        else:
            raise TypeError("Un Movement ne peut être divisé que par un "
                            "nombre.")


class AcceleratedMovement(Movement):
    """Décrit un mouvement rectiligne uniformément accéléré ou ralenti.
    Au moins trois des paramètres suivants sont obligatoires : ``accel=``,
    ``velocity=``, ``time=``, ``distance=``."""

    def __init__(self, distance=None, velocity=None, time=None, accel=None):
        Movement.__init__(self,
                          distance=distance, velocity=velocity, time=time)
        if accel:
            if type(accel) is not Acceleration:
                raise TypeError("Le paramètre ``accel`` doit être une instance"
                                " de pseudosci.units.Acceleration.")
            self.accel = accel
        elif velocity and time:
            self.accel = velocity / time
        elif time and distance:
            self.accel = 2 * distance / time / time
        elif velocity and distance:
            self.time = 2 * distance / velocity
            self.accel = velocity / self.time

    def __getattr__(self, name):
        if name == 'velocity':
            self.velocity = self.accel * self.time
            return self.velocity
        elif name == 'distance':
            self.distance = (self.accel * self.time * self.time) / 2
            return self.distance
        elif name == 'time':
            self.time = self.velocity / self.accel
            return self.time
        else:
            return Movement.__getattr__(self, name)


class ComplexMovement(object):
    """Gère un ensemble de mouvements rectilignes comme un unique mouvement."""

    def __init__(self, *args):
        self.movements = list(args)

    def __repr__(self):
        return '<{0} {1},{2},{3}>'.format(
            type(self).__name__, self.distance, self.time, self.velocity)

    def __add__(self, other):
        if type(self) is type(other):
            m = self.movements
            m.extend(other.movements)
            return type(self)(*m)
        elif isinstance(other, Movement):
            m = self.movements
            m.append(other)
            return type(self)(*m)
        else:
            raise TypeError("Un ComplexMovement doit s'additionner à un "
                            "ComplexMovement ou à un Movement")

    def __getattr__(self, name):
        if name == 'distance':
            return Distance(m=sum(self.distances))
        elif name == 'time':
            return Time(s=sum(self.times))
        elif name == 'velocity':
            if self.time == 0:
                return 0
            else:
                return self.distance / self.time
        elif name == 'distances':
            return [m.distance for m in self.movements]
        elif name == 'times':
            return [m.time for m in self.movements]
        elif name == 'velocities':
            return [m.velocity for m in self.movements]
