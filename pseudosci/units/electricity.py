#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Unités de mesure liées à l'électricité et au magnétisme."""

from . import Unit

# Constantes de conversion - modifiez-les pour casser EDF
STATV_V = 299.792458
ABV_V = 1e-8
MA_A = 1e-3
ABA_A = 10
STATA_A = 3.336e-10
KOHM_OHM = 1e3
ABOHM_OHM = 1e-9
STATOHM_OHM = 8.987551787e11
UF_F = 1e-6
ABF_F = 1e9
STATF_F = 1/898314833955
JAR_F = 1111e-12
GAMMA_T = 1e-9
G_T = 1e-4


class Voltage(Unit):
    """Décrit une unité de tension ou de potentiel électrique. L'unité
    correspondante du système international est le volt (V).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `v` pour des volts ;
    `statv` pour des statvolts ;
    `abv` pour des abvolts."""

    fullname = "volt"
    pluralname = "volts"
    convert = {'v': 1, 'statv': STATV_V, 'abv': ABV_V}
    multiply = {'Current': 'Power', 'Capacity': 'Charge', 'Charge': 'Energy',
                'Conductance': 'Current'}
    divide = {'Current': 'Resistance'}


class Current(Unit):
    """Décrit une unité d'intensité du courant électrique. L'unité
    correspondante du système international est l'ampère (A).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `a` pour des ampères ;
    `ma` pour des milliampères ;
    `aba` ou `bi` pour des abampères (ou biots) ;
    `stata` pour des statampères."""

    fullname = "ampere"
    pluralname = "amperes"
    convert = {'a': 1, 'ma': MA_A, 'aba': ABA_A, 'bi': ABA_A, 'stata': STATA_A}
    multiply = {'Voltage': 'Power', 'Time': 'Charge'}
    divide = {'Voltage': 'Conductance', 'Conductance': 'Voltage'}


class Capacity(Unit):
    """Décrit une unité de capacité. L'unité correspondante du système
    international est le farad (F).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `f` pour des farads ;
    `mf` pour des microfarads ;
    `abf` pour des abfarads ;
    `statf` pour des statfarads ;
    `jar` pour des jars."""

    fullname = "farad"
    pluralname = "farads"
    convert = {'f': 1, 'mf': UF_F, 'abf': ABF_F, 'statf': STATF_F,
               'jar': JAR_F}
    multiply = {'Voltage': 'Charge', 'Resistance': 'Time'}


class Resistance(Unit):
    """Décrit une unité de résistance diélectrique. L'unité correspondante du
    système international est l'ohm (Ω).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `ohm` pour des ohms ;
    `kohm` pour des kiloohms ;
    `abohm` pour des abohms ;
    `statohm` pour des statohms."""

    fullname = "ohm"
    pluralname = "ohms"
    convert = {'ohm': 1, 'kohm': KOHM_OHM, 'abohm': ABOHM_OHM,
               'statohm': STATOHM_OHM}
    multiply = {'Capacity': 'Time', 'Current': 'Voltage'}


class Conductance(Unit):
    """Décrit une unité de conductance diélectrique. L'unité correspondante du
    système international est le siemens (S).
    Utilisez le paramètre `s` pour instancier la classe."""

    fullname = pluralname = "siemens"
    convert = {'s': 1}
    multiply = {'Voltage': 'Current'}


class MagneticField(Unit):
    """Décrit un champ magnétique. L'unité correspondante du système
    international est le tesla (T).
    Utilisez l'un des attributs suivants pour initialiser la classe :
    `t` pour des teslas ;
    `gamma` pour des gammas ;
    `g` pour des gauss."""

    fullname = "tesla"
    pluralname = "teslas"
    convert = {'t': 1, 'gamma': GAMMA_T, 'g': G_T}
