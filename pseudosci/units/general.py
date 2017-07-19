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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "meter"
        self.pluralname = "meters"
        self.attributes = {'m': 1, 'km': KM_M, 'au': AU_M, 'ly': LY_M}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "second"
        self.pluralname = "seconds"
        self.attributes = {'s': 1, 'm': MIN_S, 'min': MIN_S,
                           'h': H_S, 'd': D_S}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "meter per second"
        self.pluralname = "meters per second"
        self.attributes = {'mps': 1, 'kph': KPH_MPS}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "meter per second squared"
        self.pluralname = "meters per second squared"
        self.attributes = {'mpss': 1, 'kphs': KPHS_MPSS, 'g': G_MPSS}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "kilogram"
        self.pluralname = "kilograms"
        self.attributes = {'t': T_KG, 'kg': 1, 'g': G_KG,
                           'mg': MG_KG, 'ug': UG_KG}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "newton"
        self.pluralname = "newtons"
        self.attributes = {'n': 1, 'dyn': DYN_N, 'kgf': KGF_N,
                           'lbf': LBF_N, 'pdl': PDL_N}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "square meter"
        self.pluralname = "square meters"
        self.attributes = {'m2': 1, 'km2': KM_M ** 2, 'acre': ACRE_M2,
                           'arpent': ARPENT_M2, 'ha': HA_M2}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "cubic meter"
        self.pluralname = "cubic meters"
        self.attributes = {'m3': 1, 'km3': KM_M ** 3, 'l': L_M3}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "joule"
        self.pluralname = "joules"
        self.attributes = {'j': 1, 'kwh': KWH_J, 'kgm': KGM_J, 'cal': CAL_J,
                           'kcal': KCAL_J, 'ev': EV_J}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))

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

    def __init__(self, **kwargs):
        (name, value), = kwargs.items()
        self.fullname = "mole"
        self.pluralname = "moles"
        self.attributes = {'mol': 1}
        Unit.__init__(self, self.convertfrom(float(value), str(name)))
