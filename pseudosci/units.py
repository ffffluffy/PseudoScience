#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure du projet. Toutes les unités sont stockées en interne sous
l'unité du système international."""

# Constantes de conversion - modifiez-les pour briser les lois de la physique
KM_M = 1000
AU_M = 149597870.700
# modifiez surtout celle-ci - elle implique une autre vitesse de la lumière
LY_M = 9460730472580800
MIN_S = 60
H_S = 3600
D_S = 86400
KPH_MPS = 1 / 3.6
KPHS_MPSS = 1 / 3.6


class Unit(object):
    """Décrit une unité de mesure."""

    def __init__(self, value):
        self.value = float(value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return '<{0} {1}>'.format(type(self).__name__, self)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __abs__(self):
        return type(self)(abs(self.value))

    def __pos__(self):
        return type(self)(+self.value)

    def __neg__(self):
        return type(self)(-self.value)

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value + other)
        elif type(self) is type(other):
            return type(self)(self.value + other.value)
        else:
            raise TypeError("Il n'est pas possible d'additionner deux unités "
                            "différentes.")
    __radd__ = __add__

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value - other)
        elif type(self) is type(other):
            return type(self)(self.value - other.value)
        else:
            raise TypeError("Il n'est pas possible de soustraire deux unités "
                            "différentes.")
    __rsub__ = __sub__

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value * other)
        else:
            raise TypeError("Il n'est pas possible de multiplier deux unités "
                            "différentes.")
    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value / other)
        elif type(self) is type(other):
            return (self.value / other.value)
        else:
            raise TypeError("Il n'est pas possible de diviser deux unités "
                            "différentes.")
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is int or type(other) is float:
            return type(self)(self.value // other)
        elif type(self) is type(other):
            return (self.value // other.value)
        else:
            raise TypeError("Il n'est pas possible de diviser deux unités "
                            "différentes.")


class Distance(Unit):
    """Décrit une mesure de distance. L'unité correspondante du système
    international est le mètre (m).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :\n
    ``m=`` pour des mètres ;\n
    ``km=`` pour des kilomètres ;\n
    ``au=`` pour des unités astronomiques ;\n
    ``ly=`` pour des années-lumière."""

    def __init__(self, m=None, km=None, au=None, ly=None):
        if m is not None:
            Unit.__init__(self, float(m))
        elif km is not None:
            Unit.__init__(self, float(km) * KM_M)
        elif au is not None:
            Unit.__init__(self, float(au) * AU_M)
        elif ly is not None:
            Unit.__init__(self, float(ly) * LY_M)
        else:
            raise ValueError(
                "Pour construire une unité de distance, fournissez m, km, au "
                "ou ly.")

    def __getattr__(self, name):
        if name.lower() == 'm':
            self.m = m = self.value
            return m
        if name.lower() == 'km':
            self.km = km = self.m / KM_M
            return km
        elif name.lower() == 'au':
            self.au = au = self.m / AU_M
            return au
        elif name.lower() == 'ly':
            self.ly = ly = self.m / LY_M
            return ly
        else:
            raise AttributeError("No attribute named %r" % (name.lower(),))

    def __truediv__(self, other):
        if type(other) is Time:
            return Velocity(mps=self.m / other.s)
        elif type(other) is Velocity:
            return Time(s=self.m / other.mps)
        else:
            return Unit.__div__(self, other)
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is Time:
            return Velocity(mps=self.m // other.s)
        elif type(other) is Velocity:
            return Time(s=self.m // other.mps)
        else:
            return Unit.__floordiv__(self, other)


class Time(Unit):
    """Décrit une mesure temporelle. L'unité correspondante du système
    international est la seconde (s).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :\n
    ``s=`` pour des secondes ;\n
    ``min=`` pour des minutes ;\n
    ``h=`` pour des heures ;\n
    ``d=`` pour des jours."""

    def __init__(self, s=None, m=None, h=None, d=None):
        if s is not None:
            Unit.__init__(self, float(s))
        elif m is not None:
            Unit.__init__(self, float(m) * MIN_S)
        elif h is not None:
            Unit.__init__(self, float(h) * H_S)
        elif d is not None:
            Unit.__init__(self, float(d) * D_S)
        else:
            raise ValueError(
                "Pour construire une unité de temps, fournissez s, m, h ou d.")

    def __getattr__(self, name):
        if name.lower() == 's':
            self.s = s = self.value
            return s
        elif name.lower() == 'm' or name.lower() == 'min':
            self.min = self.m = m = self.s / MIN_S
            return m
        elif name.lower() == 'h':
            self.h = h = self.s / H_S
            return h
        elif name.lower() == 'd':
            self.d = d = self.s / D_S
            return d
        else:
            raise AttributeError("No attribute named %r" % (name.lower(),))

    def __mul__(self, other):
        if type(other) is Velocity:
            return Distance(m=self.s * other.mps)
        elif type(other) is Acceleration:
            return Velocity(mps=self.s * other.mpss)
        else:
            return Unit.__mul__(self, other)

    __rmul__ = __mul__


class Velocity(Unit):
    """Décrit une vitesse, ou vélocité. L'unité correspondante du système
    international est le mètre par seconde (m.s^-1).\n
    Utilisez soit ``mps=``, soit ``kph=`` pour l'initialiser."""

    def __init__(self, mps=None, kph=None):
        if mps is not None:
            Unit.__init__(self, float(mps))
        elif kph is not None:
            Unit.__init__(self, float(kph) * KPH_MPS)
        else:
            raise ValueError(
                "Pour construire une unité de vitesse, fournissez mps ou kph.")

    def __getattr__(self, name):
        if name.lower() == 'mps':
            self.mps = mps = self.value
            return mps
        elif name.lower() == 'kph':
            self.kph = kph = self.mps / KPH_MPS
            return kph
        else:
            raise AttributeError("No attribute named %r" % (name.lower(),))

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Velocity(mps=self.mps * other)
        elif type(other) is Time:
            return Distance(m=self.mps * other.s)
        else:
            return Unit.__mul__(self, other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) is Time:
            return Acceleration(mpss=self.mps / other.s)
        elif type(other) is Acceleration:
            return Time(s=self.mps / other.mpss)
        else:
            return Unit.__div__(self, other)
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is Time:
            return Acceleration(mpss=self.mps // other.s)
        elif type(other) is Acceleration:
            return Time(s=self.mps // other.mpss)
        else:
            return Unit.__floordiv__(self, other)


class Acceleration(Unit):
    """Décrit une accélération. L'unité correspondante du système international
    est le mètre par seconde carrée (m.s^-2).\n
    Utilisez soit un paramètre ``mpss=``, soit un paramètre ``kphs=`` pour
    l'intialiser."""

    def __init__(self, mpss=None, kphs=None):
        if mpss is not None:
            Unit.__init__(self, float(mpss))
        elif kphs is not None:
            Unit.__init__(self, float(kphs) * KPHS_MPSS)
        else:
            raise ValueError(
                "Pour construire une unité d'accélération, fournissez mpss ou "
                "kphs.")

    def __getattr__(self, name):
        if name.lower() == 'mpss':
            self.mpss = mpss = self.value
            return mpss
        elif name.lower() == 'kphs':
            self.kphs = kphs = self.mpss / KPHS_MPSS
            return kphs
        else:
            raise AttributeError("No attribute named %r" % (name.lower(),))

    def __mul__(self, other):
        if type(other) is Time:
            return Velocity(mps=self.mpss * other.s)
        else:
            return Unit.__mul__(self, other)

    __rmul__ = __mul__
