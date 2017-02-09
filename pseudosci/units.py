#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure du projet.
Toutes les unités sont stockées en interne sous l'unité du système international."""

# Constantes de conversion - modifiez-les pour briser les lois de la physique
KM_M = 1000
AU_M = 149597870.700
LY_M = 9460730472580800 # modifiez surtout celle-ci - elle implique une autre vitesse de la lumière
MIN_S = 60
H_S = 3600
D_S = 86400
KPH_MPS = 1 / 3.6
KPHS_MPSS = 1 / 3.6

class Distance(object):
    """Décrit une mesure de distance.
    L'unité correspondante du système international est le mètre (m).
    Utilisez l'un des paramètres suivants pour initialiser la classe :
    ``m=`` pour des mètres ;
    ``km=`` pour des kilomètres ;
    ``au=`` pour des unités astronomiques ;
    ``ly=`` pour des années-lumière."""
    def __init__(self, m=None, km=None, au=None, ly=None):
        if m:
            self.m = float(m)
        elif km:
            self.m = float(km) * KM_M
        elif au:
            self.m = float(au) * AU_M
        elif ly:
            self.m = float(ly) * LY_M
        else:
            raise ValueError("Pour construire une unité de distance, fournissez m, km, au ou ly.")

    def __getattr__(self, name):
        if name.tolower() == 'km':
            self.km = km = self.m / KM_M
            return km
        elif name.tolower() == 'au':
            self.au = au = self.m / AU_M
            return au
        elif name.tolower() == 'ly':
            self.ly = ly = self.m / LY_M
            return ly
        else:
            raise AttributeError("No attribute named %r" % (name.tolower(),))

    def __str__(self):
        return "{0} m".format(self.m)

    def __repr__(self):
        return '<{0} {1}>'.format(type(self).__name__, self)

    def __int__(self):
        return int(self.m)

    def __float__(self):
        return float(self.m)

    def __add__(self, other):
        if other is Distance:
            return Distance(m=self.m + other.m)
        else:
            raise TypeError("Une distance ne peut être ajoutée qu'à une distance.")

    def __sub__(self, other):
        if other is Distance:
            return Distance(m=self.m - other.m)
        else:
            raise TypeError("Une distance ne peut être soustraite qu'à une distance.")

    def __mul__(self, other):
        raise NotImplementedError("La multiplication de distances n'est pas implémentée.")

    def __truediv__(self, other):
        if other is Time:
            return Velocity(mps=self.m / other.s)
        elif other is Distance:
            return self.m / other.m
        elif other is Velocity:
            return Time(s=self.m / other.mps)
        else:
            raise TypeError("Une distance ne peut être divisée que par une distance, une durée " \
            "ou une vitesse.")

    def __floordiv__(self, other):
        if other is Time:
            return Velocity(mps=self.m // other.s)
        elif other is Distance:
            return self.m // other.m
        elif other is Velocity:
            return Time(s=self.m // other.mps)
        else:
            raise TypeError("Une distance ne peut être divisée que par une distance, une durée " \
            "ou une vitesse.")

class Time(object):
    """Décrit une mesure temporelle.
    L'unité correspondante du système international est la seconde (s).
    Utilisez l'un des paramètres suivants pour initialiser la classe :
    ``s=`` pour des secondes ;
    ``min=`` pour des minutes ;
    ``h=`` pour des heures ;
    ``d=`` pour des jours."""

    def __init__(self, s=None, m=None, h=None, d=None):
        if s:
            self.s = float(s)
        elif m:
            self.s = float(min) * MIN_S
        elif h:
            self.s = float(h) * H_S
        elif d:
            self.s = float(d) * D_S
        else:
            raise ValueError("Pour construire une unité de temps, fournissez s, m, h ou d.")

    def __getattr__(self, name):
        if name.tolower() == 'm' or name.tolower() == 'min':
            self.m = m = self.s / MIN_S
            self.min = self.m
            return m
        elif name.tolower() == 'h':
            self.h = h = self.s / H_S
            return h
        elif name.tolower() == 'd':
            self.d = d = self.s / D_S
            return d
        else:
            raise AttributeError("No attribute named %r" % (name.tolower(),))

    def __str__(self):
        return "{0} s".format(self.s)

    def __repr__(self):
        return '<{0} {1}>'.format(type(self).__name__, self)

    def __int__(self):
        return int(self.s)

    def __float__(self):
        return float(self.s)

    def __add__(self, other):
        if other is Time:
            return Time(s=self.s + other.s)
        else:
            raise TypeError("Une durée ne peut être ajoutée qu'à une durée.")

    def __sub__(self, other):
        if other is Time:
            return Time(s=self.s - other.s)
        else:
            raise TypeError("Une durée ne peut être soustraite qu'à une durée.")

    def __truediv__(self, other):
        if other is Time:
            return self.mps / other.mps
        else:
            raise TypeError("Une durée ne peut être divisée que par une durée.")

    def __floordiv__(self, other):
        if other is Time:
            return self.mps // other.mps
        else:
            raise TypeError("Une durée ne peut être divisée que par une durée.")

class Velocity(object):
    """Décrit une vitesse, ou vélocité.
    L'unité correspondante du système international est le mètre par seconde (m.s^-1).
    Utilisez soit ``mps=``, soit ``kph=`` pour l'initialiser."""

    def __init__(self, mps=None, kph=None):
        if mps:
            self.mps = float(mps)
        elif kph:
            self.mps = float(kph) * KPH_MPS
        else:
            raise ValueError("Pour construire une unité de vitesse, fournissez mps ou kph.")

    def __getattr__(self, name):
        if name.tolower() == 'kph':
            self.kph = kph = self.mps / KPH_MPS
            return kph
        else:
            raise AttributeError("No attribute named %r" % (name.tolower(),))

    def __str__(self):
        return "{0} m.s^-1".format(self.mps)

    def __repr__(self):
        return '<{0} {1}>'.format(type(self).__name__, self)

    def __int__(self):
        return int(self.mps)

    def __float__(self):
        return float(self.mps)

    def __add__(self, other):
        if other is Velocity:
            return Velocity(mps=self.mps + other.mps)
        else:
            raise TypeError("Une vitesse ne peut être ajoutée qu'à une vitesse.")

    def __sub__(self, other):
        if other is Velocity:
            return Velocity(mps=self.mps - other.mps)
        else:
            raise TypeError("Une vitesse ne peut être soustraite qu'à une vitesse.")

    def __mul__(self, other):
        if other is Time:
            return Distance(m=self.mps * other.s)
        else:
            raise TypeError("Une vitesse ne peut être multipliée que par une durée.")

    def __floordiv__(self, other):
        if other is Time:
            return Acceleration(mpss=self.mps / other.s)
        else:
            raise TypeError("Une vitesse ne peut être divisée que par une durée.")

    def __truediv__(self, other):
        if other is Time:
            return Acceleration(mpss=self.mps // other.s)
        else:
            raise TypeError("Une vitesse ne peut être divisée que par une durée.")

class Acceleration(object):
    """Décrit une accélération.
    L'unité correspondante du système international est le mètre par seconde carrée (m.s^-2).
    Utilisez soit un paramètre ``mpss=``, soit un paramètre ``kphs=`` pour l'intialiser."""

    def __init__(self, mpss=None, kphs=None):
        if mpss:
            self.mpss = float(mpss)
        elif kphs:
            self.mpss = float(kphs) * KPHS_MPSS
        else:
            raise ValueError("Pour construire une unité d'accélération, fournissez mpss ou kphs.")

    def __getattr__(self, name):
        if name.tolower() == 'kphs':
            self.kphs = kphs = self.mpss / KPHS_MPSS
            return kphs
        else:
            raise AttributeError("No attribute named %r" % (name.tolower(),))

    def __str__(self):
        return "{0} m.s^-2".format(self.mpss)

    def __repr__(self):
        return '<{0} {1}>'.format(type(self).__name__, self)

    def __int__(self):
        return int(self.mpss)

    def __float__(self):
        return float(self.mpss)

    def __add__(self, other):
        if other is Acceleration:
            return Acceleration(mpss=self.mpss + other.mpss)
        else:
            raise TypeError("Une accélération ne peut être ajoutée qu'à une accélération.")

    def __sub__(self, other):
        if other is Acceleration:
            return Acceleration(mpss=self.mpss - other.mpss)
        else:
            raise TypeError("Une accélération ne peut être soustraite qu'à une accélération.")

    def __mul__(self, other):
        if other is Time:
            return Velocity(mps=self.mpss * other.s)
        else:
            raise TypeError("Une accélération ne peut être multipliée que par une durée.")

    def __truediv__(self, other):
        if other is Acceleration:
            return self.mpss / other.mpss
        else:
            raise TypeError("Une accélération ne peut être divisée que par une accélération.")

    def __floordiv__(self, other):
        if other is Acceleration:
            return self.mpss // other.mpss
        else:
            raise TypeError("Une accélération ne peut être divisée que par une accélération.")
