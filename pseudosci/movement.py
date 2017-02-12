#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Simulation de mouvements rectilignes prenant en charge les accélérations
et freinages."""

from .units import Distance, Time, Velocity, Acceleration


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
        return '<Movement {0},{1},{2}>'.format(
            self.distance, self.time, self.velocity)

    def __add__(self, other):
        if type(other) is Movement:
            return Movement(distance=self.distance + other.distance,
                            time=self.time + other.time)
        else:
            raise TypeError("Un Movement ne peut être ajouté qu'à un Movement")

    def __sub__(self, other):
        if type(other) is Movement:
            return Movement(distance=self.distance - other.distance,
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

    def __div__(self, other):
        if type(other) is int or type(other) is float:
            return Movement(distance=self.distance / other,
                            time=self.time / other)
        else:
            raise TypeError("Un Movement ne peut être divisé que par un "
                            "nombre.")

    def __floordiv__(self, other):
        if type(other) is int or type(other) is float:
            return Movement(distance=self.distance // other,
                            time=self.time // other)
        else:
            raise TypeError("Un Movement ne peut être divisé que par un "
                            "nombre.")


class ComplexMovement(object):
    """Décrit un mouvement rectiligne débutant par une accélération et se
    terminant par un freinage. Au moins deux des paramètres suivants sont
    obligatoires : ``distance=``, ``velocity=``, ``time=``.
    Paramètres optionnels : ``accel=``, ``brake=``
    ``velocity=`` est la vitesse de pointe.
    Si ``brake=`` est omis, la décélération sera égale à l'accélération.
    Si ``accel=`` est omis, l'accélération sera ignorée et l'instance se
    comportera comme pseudosci.movement.Movement."""

    def __init__(self, distance=None, velocity=None, time=None, accel=None,
                 brake=None):
        if not (velocity and (distance or time)):
            raise TypeError("Des arguments obligatoires sont manquants.\n"
                            "Le paramètre ``velocity=`` est obligatoire ainsi "
                            "qu'au moins un des deux paramètres suivants : "
                            "``distance=``, ``time=``")
        if distance and type(distance) is not Distance:
            raise TypeError("Le paramètre ``distance`` doit être une instance "
                            "de pseudosci.units.Distance.")
        if velocity and type(velocity) is not Velocity:
            raise TypeError("Le paramètre ``velocity`` doit être une instance "
                            "de pseudosci.units.Velocity.")
        if time and type(time) is not Time:
            raise TypeError("Le paramètre ``time`` doit être une instance "
                            "de pseudosci.units.Time.")
        if accel and type(accel) is not Acceleration:
            raise TypeError("Le paramètre ``accel`` doit être une instance "
                            "de pseudosci.units.Acceleration.")
        if brake and type(brake) is not Acceleration:
            raise TypeError("Le paramètre ``brake`` doit être une instance "
                            "de pseudosci.units.Acceleration.")
        self.distance = distance
        self.velocity = velocity
        self.time = time
        if accel:
            self.accel = abs(accel)  # Toujours positif
        if brake:
            self.brake = -abs(brake)  # Toujours négatif
        self.compute()

    def compute(self):
        """Exécute les calculs basés sur les attributs de la classe. La méthode
        est appelée automatiquement après l'exécution du constructeur."""

        if (not self.accel and not self.brake) or \
                (self.accel == 0 and self.brake == 0):
            self.distance = Movement.distance
            self.velocity = Movement.velocity
            self.time = Movement.time
            self.acceldist, self.brakedist = Distance(m=0), Distance(m=0)
            self.acceltime, self.braketime = Time(s=0), Time(s=0)
            self.maxdist, self.maxtime = self.distance, self.time
            self.meanvelocity = self.velocity
            return
        elif not self.accel or self.accel == 0:
            self.accel = -self.brake
        elif not self.brake or self.brake == 0:
            self.brake = -self.accel

        if self.velocity:  # Vitesse de pointe connue
            self.acceltime = self.velocity / self.accel
            self.braketime = abs(self.velocity / self.brake)
        # else:  # Distance totale et temps total connus
        #    self.acceltime = \
        #        (-self.brake * self.time) / (self.accel - self.brake)
        #    self.braketime = self.time - self.acceltime
        self.acceldist = ((self.accel / 2) * self.acceltime) * self.acceltime
        self.brakedist = abs(((self.brake / 2) * self.braketime) *
                             self.braketime)
        if not self.time:  # Distance totale et vitesse de pointe connues
            self.maxdist = self.distance - self.acceldist - self.brakedist
            self.maxtime = self.maxdist / self.velocity
            self.time = self.maxtime + self.acceltime + self.braketime
        elif not self.distance:  # Temps total et vitesse de pointe connus
            self.maxtime = self.time - self.acceltime - self.braketime
            self.maxdist = self.maxtime * self.velocity
            self.distance = self.maxdist + self.acceldist + self.brakedist
        # else:  # Distance totale et temps total connus
        #     self.maxdist = Distance(m=0)
        #     self.maxtime = Time(s=0)
        #     self.velocity = self.accel * self.acceltime
        self.meanvelocity = self.distance / self.time
