#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure de base du projet."""

from . import Unit

# Constantes de conversion - modifiez-les pour briser les lois de la physique
KM_M = 1e3
AU_M = 149597870700
# modifiez surtout celle-ci - elle implique une autre vitesse de la lumière
LY_M = 9460730472580800
MIN_S = 60
H_S = 3600
D_S = 86400
KPH_MPS = 1 / 3.6
KPHS_MPSS = 1 / 3.6
G_MPSS = 9.80665
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
            return self.value
        if name.lower() == 'km':
            return self.m / KM_M
        elif name.lower() == 'au':
            return self.m / AU_M
        elif name.lower() == 'ly':
            return self.m / LY_M
        else:
            return Unit.__getattr__(self, name)

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
            return self.value
        elif name.lower() in ['min', 'm']:
            return self.s / MIN_S
        elif name.lower() == 'h':
            return self.s / H_S
        elif name.lower() == 'd':
            return self.s / D_S
        else:
            return Unit.__getattr__(self, name)

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
            return self.value
        elif name.lower() == 'kph':
            return self.value / KPH_MPS
        else:
            return Unit.__getattr__(self, name)

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
    Utilisez `mpss=`, `kphs=` ou `g=` pour l'intialiser."""

    def __init__(self, mpss=None, kphs=None, g=None):
        if mpss is not None:
            Unit.__init__(self, float(mpss))
        elif kphs is not None:
            Unit.__init__(self, float(kphs) * KPHS_MPSS)
        elif g is not None:
            Unit.__init__(self, float(g) * G_MPSS)
        else:
            raise ValueError(
                "Pour construire une unité d'accélération, fournissez mpss ou "
                "kphs.")
        self.fullname = "meter per second squared"
        self.pluralname = "meters per second squared"

    def __getattr__(self, name):
        if name.lower() == 'mpss':
            return self.value
        elif name.lower() == 'kphs':
            return self.value / KPHS_MPSS
        elif name.lower() == 'g':
            return self.value / G_MPSS
        else:
            return Unit.__getattr__(self, name)

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
            return self.value / UG_KG
        elif name.lower() == 'mg':
            return self.value / MG_KG
        elif name.lower() == 'g':
            return self.value / G_KG
        elif name.lower() == 'kg':
            return self.value
        elif name.lower() == 't':
            return self.value / T_KG
        else:
            return Unit.__getattr__(self, name)

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
            return self.value
        elif name.lower() == 'dyn':
            return self.value / DYN_N
        elif name.lower() == 'kgf':
            return self.value / KGF_N
        elif name.lower() == 'lbf':
            return self.value / LBF_N
        elif name.lower() == 'pdl':
            return self.value / PDL_N
        else:
            return Unit.__getattr__(self, name)

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
            return self.value
        elif name.lower() == 'km2':
            return self.value / (KM_M ** 2)
        elif name.lower() == 'acre':
            return self.value / ACRE_M2
        elif name.lower() == 'arpent':
            return self.value / ARPENT_M2
        elif name.lower() == 'ha':
            return self.value / HA_M2
        else:
            return Unit.__getattr__(self, name)

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
            return self.value
        elif name.lower() == 'km3':
            return self.value / (KM_M ** 3)
        elif name.lower() == 'l':
            return self.value / L_M3
        else:
            return Unit.__getattr__(self, name)

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
            return self.value
        elif name == 'kwh':
            return self.value / KWH_J
        elif name == 'kgm':
            return self.value / KGM_J
        elif name == 'cal':
            return self.value / CAL_J
        elif name == 'kcal':
            return self.value / KCAL_J
        elif name == 'ev':
            return self.value / EV_J
        else:
            return Unit.__getattr__(self, name)

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


class ChemicalAmount(Unit):
    """Décrit une quantité de matière. L'unité correspondante du système
    international est la mole (mol).\n
    Utilisez le paramètre `mol=` pour instancier en moles."""

    def __init__(self, mol=None):
        if mol is not None:
            Unit.__init__(self, float(mol))
        else:
            raise ValueError("Pour construire une unité de quantité de "
                             "matière, fournissez `mol`.")
        self.fullname = "mole"
        self.pluralname = "moles"

    def __getattr__(self, name):
        if name.lower() == 'mol':
            return self.value
        else:
            return Unit.__getattr__(self, name)
