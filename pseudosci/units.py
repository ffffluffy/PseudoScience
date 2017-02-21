#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure du projet. Toutes les unités sont stockées en interne sous
l'unité du système international."""

# Constantes de conversion - modifiez-les pour briser les lois de la physique
KM_M = 1e3
AU_M = 149597870.700
# modifiez surtout celle-ci - elle implique une autre vitesse de la lumière
LY_M = 9460730472580800
MIN_S = 60
H_S = 3600
D_S = 86400
KPH_MPS = 1 / 3.6
KPHS_MPSS = 1 / 3.6
UG_KG = 1e-9
MG_KG = 1e-6
G_KG = 1e-3
T_KG = 1e3
DYN_N = 1e-5
KGF_N = 9.80665
LBF_N = 4.448222
PDL_N = 0.138255
ACRE_M2 = 4046.86
ARPENT_M2 = 3418.89
HA_M2 = 1e4


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

    def __eq__(self, other):
        return type(self) is type(other) and self.value == other.value

    def __ne__(self, other):
        return type(self) is type(other) and self.value != other.value

    def __gt__(self, other):
        if (type(self) is not type(other)):
            raise TypeError("Une unité doit être comparée à une unité de même "
                            "type.")
        else:
            return self.value > other.value

    def __ge__(self, other):
        if (type(self) is not type(other)):
            raise TypeError("Une unité doit être comparée à une unité de même "
                            "type.")
        else:
            return self.value >= other.value

    def __lt__(self, other):
        if (type(self) is not type(other)):
            raise TypeError("Une unité doit être comparée à une unité de même "
                            "type.")
        else:
            return self.value < other.value

    def __le__(self, other):
        if (type(self) is not type(other)):
            raise TypeError("Une unité doit être comparée à une unité de même "
                            "type.")
        else:
            return self.value <= other.value


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
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

    def __mul__(self, other):
        if type(other) is Distance:
            return Area(m2=self.m * other.m)
        else:
            return Unit.__mul__(self, other)
    __rmul__ = __mul__

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
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

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
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

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
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

    def __mul__(self, other):
        if type(other) is Time:
            return Velocity(mps=self.mpss * other.s)
        elif type(other) is Mass:
            return Force(n=self.mpss * other.kg)
        else:
            return Unit.__mul__(self, other)

    __rmul__ = __mul__


class Mass(Unit):
    """Décrit une masse. L'unité correspondante du système international est le
    kilogramme (kg).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :
    ``ug=`` pour des microgrammes,
    ``mg=`` pour des milligrammes,
    ``g=`` pour des grammes,
    ``kg=`` pour des kilogrammes,
    ``t=`` pour des tonnes."""

    def __init__(self, ug=None, mg=None, g=None, kg=None, t=None):
        if ug is not None:
            Unit.__init__(self, float(ug) * UG_KG)
        elif mg is not None:
            Unit.__init__(self, float(mg) * MG_KG)
        elif g is not None:
            Unit.__init__(self, float(g) * G_KG)
        elif kg is not None:
            Unit.__init__(self, float(kg))
        elif t is not None:
            Unit.__init__(self, float(t) * T_KG)
        else:
            raise ValueError("Pour construire une unité de masse, "
                             "fournissez ug, mg, g, kg ou t.")

    def __getattr__(self, name):
        if name.lower() == 'ug':
            self.ug = ug = self.value / UG_KG
            return ug
        elif name.lower() == 'mg':
            self.mg = mg = self.value / MG_KG
            return mg
        elif name.lower() == 'g':
            self.g = g = self.value / G_KG
            return g
        elif name.lower() == 'kg':
            self.kg = kg = self.value
            return kg
        elif name.lower() == 't':
            self.t = t = self.value / T_KG
            return t
        else:
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

    def __mul__(self, other):
        if type(other) is Acceleration:
            return Force(n=self.kg * other.mpss)
        else:
            return Unit.__mul__(self, other)
    __rmul__ = __mul__


class Force(Unit):
    """Décrit une force. L'unité correspondante du système international est le
    newton (N).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :
    ``n=`` pour des newtons,
    ``dyn=`` pour des dynes,
    ``kgf=`` pour des kilogrammes-force,
    ``lbf=`` pour des livres-force,
    ``pdl=`` pour des poundals."""

    def __init__(self, n=None, dyn=None, kgf=None, lbf=None, pdl=None):
        if n is not None:
            Unit.__init__(self, float(n))
        elif dyn is not None:
            Unit.__init__(self, float(dyn) * DYN_N)
        elif kgf is not None:
            Unit.__init__(self, float(kgf) * KGF_N)
        elif lbf is not None:
            Unit.__init__(self, float(lbf) * LBF_N)
        elif pdl is not None:
            Unit.__init__(self, float(pdl) * PDL_N)
        else:
            raise ValueError("Pour construire une unité de force, "
                             "fournissez n, dyn, kgf, lbf ou pdl.")

    def __getattr__(self, name):
        if name.lower() == 'n':
            self.n = n = self.value
            return n
        elif name.lower() == 'dyn':
            self.dyn = dyn = self.value / DYN_N
            return dyn
        elif name.lower() == 'kgf':
            self.kgf = kgf = self.value / KGF_N
            return kgf
        elif name.lower() == 'lbf':
            self.lbf = lbf = self.value / LBF_N
            return lbf
        elif name.lower() == 'pdl':
            self.pdl = pdl = self.value / PDL_N
            return pdl
        else:
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

    def __truediv__(self, other):
        if type(other) is Acceleration:
            return Mass(kg=self.n / other.mpss)
        elif type(other) is Mass:
            return Acceleration(mpss=self.n / other.kg)
        else:
            return Unit.__truediv__(self, other)
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is Acceleration:
            return Mass(kg=self.n // other.mpss)
        elif type(other) is Mass:
            return Acceleration(mpss=self.n // other.kg)
        else:
            return Unit.__floordiv__(self, other)


class Area(Unit):
    """Décrit une surface. L'unité correspondante du système international est
    le mètre carré (m^2).\n
    Utilisez un des paramètres suivants pour initialiser la classe :
    ``m2=`` pour des mètres carrés,
    ``km2=`` pour des kilomètres carrés,
    ``acre=`` pour des acres,
    ``arpent=`` pour des arpents,
    ``ha=`` pour des hectares."""

    def __init__(self, m2=None, km2=None, acre=None, arpent=None, ha=None):
        if m2 is not None:
            Unit.__init__(self, float(m2))
        elif km2 is not None:
            Unit.__init__(self, float(km2) * (KM_M ** 2))
        elif acre is not None:
            Unit.__init__(self, float(acre) * ACRE_M2)
        elif arpent is not None:
            Unit.__init__(self, float(arpent) * ARPENT_M2)
        elif ha is not None:
            Unit.__init__(self, float(ha) * HA_M2)
        else:
            raise ValueError("Pour construire une unité de surface, "
                             "fournissez m2, km2, acre, arpent ou ha.")

    def __getattr__(self, name):
        if name.lower() == 'm2':
            self.m2 = m2 = self.value
            return m2
        elif name.lower() == 'km2':
            self.km2 = km2 = self.value / (KM_M ** 2)
            return km2
        elif name.lower() == 'acre':
            self.acre = acre = self.value / ACRE_M2
            return acre
        elif name.lower() == 'arpent':
            self.arpent = arpent = self.value / ARPENT_M2
            return arpent
        elif name.lower() == 'ha':
            self.ha = ha = self.value / HA_M2
            return ha
        else:
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

    def __truediv__(self, other):
        if type(other) is Distance:
            return Distance(m=self.m2 / other.m)
        else:
            return Unit.__truediv__(self, other)
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is Distance:
            return Distance(m=self.m2 // other.m)
        else:
            return Unit.__floordiv__(self, other)
