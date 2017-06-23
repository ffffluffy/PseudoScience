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
L_M3 = 1e-3
KWH_J = 3.6e6
KGM_J = 9.80665
# Se base sur la définition du Comité International des Poids et Mesures
CAL_J = 4.1868
KCAL_J = 4.1868e3
EV_J = 1.602176565e-19


class Unit(object):
    """Décrit une unité de mesure."""

    def __init__(self, value):
        self.value = float(value)
        self.fullname = "unit"
        self.pluralname = "units"

    def __str__(self):
        return '{0} {1}'.format(str(self.value), self.fullname
                                if self.value == 1 else self.pluralname)

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
    `m=` pour des mètres ;\n
    `km=` pour des kilomètres ;\n
    `au=` pour des unités astronomiques ;\n
    `ly=` pour des années-lumière."""

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
        self.fullname = "meter"
        self.pluralname = "meters"

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
        elif type(other) is Area:
            return Volume(m3=self.m * other.m2)
        elif type(other) is Force:
            return Energy(j=self.m * other.n)
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
    `s=` pour des secondes ;\n
    `m=` pour des minutes ;\n
    `h=` pour des heures ;\n
    `d=` pour des jours."""

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
        self.fullname = "second"
        self.pluralname = "seconds"

    def __getattr__(self, name):
        if name.lower() == 's':
            self.s = s = self.value
            return s
        elif name.lower() in ['min', 'm']:
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
    Utilisez soit `mps=`, soit `kph=` pour l'initialiser."""

    def __init__(self, mps=None, kph=None):
        if mps is not None:
            Unit.__init__(self, float(mps))
        elif kph is not None:
            Unit.__init__(self, float(kph) * KPH_MPS)
        else:
            raise ValueError(
                "Pour construire une unité de vitesse, fournissez mps ou kph.")
        self.fullname = "meter per second"
        self.pluralname = "meters per second"

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
        if type(other) is Time:
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
    Utilisez soit un paramètre `mpss=`, soit un paramètre `kphs=` pour
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
        self.fullname = "meter per second squared"
        self.pluralname = "meters per second squared"

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
    `ug=` pour des microgrammes,
    `mg=` pour des milligrammes,
    `g=` pour des grammes,
    `kg=` pour des kilogrammes,
    `t=` pour des tonnes."""

    def __init__(self, kg=None, ug=None, mg=None, g=None, t=None):
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
        self.fullname = "kilogram"
        self.pluralname = "kilograms"

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
    `n=` pour des newtons,
    `dyn=` pour des dynes,
    `kgf=` pour des kilogrammes-force,
    `lbf=` pour des livres-force,
    `pdl=` pour des poundals."""

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
        self.fullname = "newton"
        self.pluralname = "newtons"

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

    def __mul__(self, other):
        if type(other) is Distance:
            return Energy(j=self.n * other.m)
        else:
            return Unit.__mul__(self, other)
    __rmul__ = __mul__

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
    `m2=` pour des mètres carrés,
    `km2=` pour des kilomètres carrés,
    `acre=` pour des acres,
    `arpent=` pour des arpents,
    `ha=` pour des hectares."""

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
        self.fullname = "square meter"
        self.pluralname = "square meters"

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

    def __mul__(self, other):
        if type(other) is Distance:
            return Volume(m3=self.m2 * other.m)
        else:
            return Unit.__mul__(self, other)
    __rmul__ = __mul__

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


class Volume(Unit):
    """Décrit un volume. L'unité correspondante du système international est
    le mètre cube (m^3).\n
    Utilisez un des paramètres suivants pour initialiser la classe :
    `m3=` pour des mètres cube,
    `km3=` pour des kilomètres cube,
    `l=` pour des litres."""

    def __init__(self, m3=None, km3=None, l=None):
        if m3 is not None:
            Unit.__init__(self, float(m3))
        elif km3 is not None:
            Unit.__init__(self, float(km3) * (KM_M ** 3))
        elif l is not None:
            Unit.__init__(self, float(l) * L_M3)
        else:
            raise ValueError("Pour construire une unité de volume, fournissez "
                             "m3, km3 ou l.")
        self.fullname = "cubic meter"
        self.pluralname = "cubic meters"

    def __getattr__(self, name):
        if name.lower() == 'm3':
            self.m3 = m3 = self.value
            return m3
        elif name.lower() == 'km3':
            self.km3 = km3 = self.value / (KM_M ** 3)
            return km3
        elif name.lower() == 'l':
            self.l = l = self.value / L_M3
            return l
        else:
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

    def __truediv__(self, other):
        if type(other) is Distance:
            return Area(m2=self.m3 / other.m)
        elif type(other) is Area:
            return Distance(m=self.m3 / other.m2)
        else:
            return Unit.__truediv__(self, other)
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is Distance:
            return Area(m2=self.m3 // other.m)
        elif type(other) is Area:
            return Distance(m=self.m3 // other.m2)
        else:
            return Unit.__floordiv__(self, other)


class Energy(Unit):
    """Décrit une quantité d'énergie. L'unité correpsondante du système
    international est le joule (J).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :
    `j=` pour des joules ;
    `kwh=` pour des kilowatts-heure ;
    `kgm=` pour des kilogrammes-mètre ;
    `cal=` pour des calories ;
    `kcal=` pour des kilocalories ;
    `ev=` pour des électrons-volts."""

    def __init__(self, j=None, kwh=None, kgm=None,
                 cal=None, kcal=None, ev=None):
        if j is not None:
            Unit.__init__(self, float(j))
        elif kwh is not None:
            Unit.__init__(self, float(kwh * KWH_J))
        elif kgm is not None:
            Unit.__init__(self, float(kgm * KGM_J))
        elif cal is not None:
            Unit.__init__(self, float(cal * CAL_J))
        elif kcal is not None:
            Unit.__init__(self, float(kcal * KCAL_J))
        elif ev is not None:
            Unit.__init__(self, float(ev * EV_J))
        else:
            raise ValueError("Pour construire une unité d'énergie, fournissez"
                             "j, kwh, kgm, cal, kcal ou ev.")
        self.fullname = "joule"
        self.pluralname = "joules"

    def __getattr__(self, name):
        if name == 'j':
            self.j = j = self.value
            return j
        elif name == 'kwh':
            self.kwh = kwh = self.value / KWH_J
            return kwh
        elif name == 'kgm':
            self.kgm = kgm = self.value / KGM_J
            return kgm
        elif name == 'cal':
            self.cal = cal = self.value / CAL_J
            return cal
        elif name == 'kcal':
            self.kcal = kcal = self.value / KCAL_J
            return kcal
        elif name == 'ev':
            self.ev = ev = self.value / EV_J
            return ev
        else:
            raise AttributeError("No attribute named {0!r}"
                                 .format(name.lower()))

    def __truediv__(self, other):
        if type(other) is Distance:
            return Force(n=self.j / other.m)
        elif type(other) is Force:
            return Distance(m=self.j / other.n)
        else:
            return Unit.__truediv__(self, other)
    __div__ = __truediv__

    def __floordiv__(self, other):
        if type(other) is Distance:
            return Force(n=self.j // other.m)
        elif type(other) is Force:
            return Distance(m=self.j // other.n)
        else:
            return Unit.__floordiv__(self, other)
