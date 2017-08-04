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
CH_W = 735.49875
HP_W = 745.699872


class Distance(Unit):
    """Décrit une mesure de distance. L'unité correspondante du système
    international est le mètre (m).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :\n
    `m=` pour des mètres ;\n
    `km=` pour des kilomètres ;\n
    `au=` pour des unités astronomiques ;\n
    `ly=` pour des années-lumière."""

    fullname = "meter"
    pluralname = "meters"
    convert = {'m': 1, 'km': KM_M, 'au': AU_M, 'ly': LY_M}
    multiply = {'Distance': 'Area', 'Area': 'Volume', 'Force': 'Energy'}
    divide = {'Time': 'Velocity', 'Velocity': 'Time'}


class Time(Unit):
    """Décrit une mesure temporelle. L'unité correspondante du système
    international est la seconde (s).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :\n
    `s=` pour des secondes ;\n
    `m=` pour des minutes ;\n
    `h=` pour des heures ;\n
    `d=` pour des jours."""

    fullname = "second"
    pluralname = "seconds"
    convert = {'s': 1, 'm': MIN_S, 'min': MIN_S, 'h': H_S, 'd': D_S}
    multiply = {'Velocity': 'Distance', 'Acceleration': 'Velocity',
                'Current': 'Charge'}
    divide = {'Resistance': 'Capacity', 'Capacity': 'Resistance'}
    inverse = 'Frequency'


class Velocity(Unit):
    """Décrit une vitesse, ou vélocité. L'unité correspondante du système
    international est le mètre par seconde (m.s^-1).\n
    Utilisez soit `mps=`, soit `kph=` pour l'initialiser."""

    fullname = "meter per second"
    pluralname = "meters per second"
    convert = {'mps': 1, 'kph': KPH_MPS}
    multiply = {'Time': 'Distance'}
    divide = {'Time': 'Acceleration', 'Acceleration': 'Time',
              'Frequency': 'Distance'}


class Acceleration(Unit):
    """Décrit une accélération. L'unité correspondante du système international
    est le mètre par seconde carrée (m.s^-2).\n
    Utilisez `mpss=`, `kphs=` ou `g=` pour l'intialiser."""

    fullname = "meter per second squared"
    pluralname = "meters per second squared"
    convert = {'mpss': 1, 'kphs': KPHS_MPSS, 'g': G_MPSS}
    multiply = {'Time': 'Velocity', 'Mass': 'Force'}
    divide = {'Frequency': 'Velocity'}


class Mass(Unit):
    """Décrit une masse. L'unité correspondante du système international est le
    kilogramme (kg).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :
    `ug=` pour des microgrammes,
    `mg=` pour des milligrammes,
    `g=` pour des grammes,
    `kg=` pour des kilogrammes,
    `t=` pour des tonnes."""

    fullname = "kilogram"
    pluralname = "kilograms"
    convert = {'t': T_KG, 'kg': 1, 'g': G_KG, 'mg': MG_KG, 'ug': UG_KG}
    multiply = {'Acceleration': 'Force'}


class Force(Unit):
    """Décrit une force. L'unité correspondante du système international est le
    newton (N).\n
    Utilisez l'un des paramètres suivants pour initialiser la classe :
    `n=` pour des newtons,
    `dyn=` pour des dynes,
    `kgf=` pour des kilogrammes-force,
    `lbf=` pour des livres-force,
    `pdl=` pour des poundals."""

    fullname = "newton"
    pluralname = "newtons"
    convert = {'n': 1, 'dyn': DYN_N, 'kgf': KGF_N, 'lbf': LBF_N, 'pdl': PDL_N}
    multiply = {'Distance': 'Energy'}
    divide = {'Acceleration': 'Mass', 'Mass': 'Acceleration',
              'Pressure': 'Area', 'Area': 'Pressure'}


class Area(Unit):
    """Décrit une surface. L'unité correspondante du système international est
    le mètre carré (m^2).\n
    Utilisez un des paramètres suivants pour initialiser la classe :
    `m2=` pour des mètres carrés,
    `km2=` pour des kilomètres carrés,
    `acre=` pour des acres,
    `arpent=` pour des arpents,
    `ha=` pour des hectares."""

    fullname = "square meter"
    pluralname = "square meters"
    convert = {'m2': 1, 'km2': KM_M ** 2, 'acre': ACRE_M2, 'arpent': ARPENT_M2,
               'ha': HA_M2}
    multiply = {'Distance': 'Volume', 'Pressure': 'Force',
                'Illuminance': 'LightFlow'}
    divide = {'Distance': 'Distance'}


class Volume(Unit):
    """Décrit un volume. L'unité correspondante du système international est
    le mètre cube (m^3).\n
    Utilisez un des paramètres suivants pour initialiser la classe :
    `m3=` pour des mètres cube,
    `km3=` pour des kilomètres cube,
    `l=` pour des litres."""

    fullname = "cubic meter"
    pluralname = "cubic meters"
    convert = {'m3': 1, 'km3': KM_M ** 3, 'l': L_M3}
    divide = {'Distance': 'Area', 'Area': 'Distance'}


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

    fullname = "joule"
    pluralname = "joules"
    convert = {'j': 1, 'kwh': KWH_J, 'kgm': KGM_J, 'cal': CAL_J,
               'kcal': KCAL_J, 'ev': EV_J}
    divide = {'Distance': 'Force', 'Force': 'Distance',
              'Voltage': 'Charge', 'Charge': 'Voltage'}


class ChemicalAmount(Unit):
    """Décrit une quantité de matière. L'unité correspondante du système
    international est la mole (mol).\n
    Utilisez le paramètre `mol=` pour instancier en moles."""

    fullname = "mole"
    pluralname = "moles"
    convert = {'mol': 1}


class Frequency(Unit):
    """Décrit une fréquence. L'unité correspondante du système international
    est le hertz (Hz).
    Utilisez le paramètres `hz` pour initialiser la classe."""

    fullname = pluralname = "hertz"
    convert = {'hz': 1}
    multiply = {'Distance': 'Velocity', 'Velocity': 'Acceleration',
                'Energy': 'Power'}
    inverse = 'Time'


class Power(Unit):
    """Décrit une puissance. L'unité correspondante du système international
    est le watt (W).
    Utilisez l'un des paramètres suivants pour instancier la classe :
    `w=` pour des watts ;
    `ch=` pour des chevaux-vapeur français ;
    `hp=` pour des chevaux-vapeur anglais."""

    fullname = "watt"
    pluralname = "watts"
    convert = {'w': 1, 'ch': CH_W, 'hp': HP_W}
    multiply = {'Time': 'Energy'}
    divide = {'Frequency': 'Energy',
              'Voltage': 'Current', 'Current': 'Voltage'}


class Flow(Unit):
    """Décrit un débit massique. L'unité correspondante du système
    international est le mètre cube par seconde (m^3.s^-1).
    Utilisez l'un des paramètres suivants pour instancier la classe :
    `m3s` pour des mètres cube par seconde ;
    `m3m` ou `m3min` pour des mètres cube par minute ;
    `m3h` pour des mètres cube par heure ;
    `ls` pour des litres par seconde ;
    `lm` ou `lmin` pour des litres par minute ;
    `lh` pour des litres par heure."""

    fullname = "cubic meter per second"
    pluralname = "cubic meters per second"
    convert = {'m3s': 1, 'm3m': MIN_S, 'm3min': MIN_S, 'm3h': H_S,
               'ls': L_M3, 'lm': MIN_S * L_M3, 'lmin': MIN_S * L_M3,
               'lh': H_S * L_M3}
    multiply = {'Time': 'Volume'}
    divide = {'Frequency': 'Volume', 'Volume': 'Frequency',
              'Area': 'Velocity', 'Velocity': 'Area'}
