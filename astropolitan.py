#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Module principal pour l'étude Astropolitain"""

from csv import writer
from array import array
from skyfield.api import load
import matplotlib.pyplot as plotter
from pseudosci.units import *

print "Script de calcul pour la distance Alsace-Mercure"

ts = load.timescale()
data = load('de421.bsp')
earth, mercury = data['earth'], data['mercury']
days = range(300, 800)
dist, speed, time = [], [], []
metroV = Velocity(kph=80)
travelTime = Time(s=46)

print "Calcul..."
dist = [Distance(au=earth.at(ts.utc(2017, 1, day)).observe(mercury).distance().au)
        for day in days]
speed = [d / travelTime for d in dist]
time = [d / metroV for d in dist]

print "Exportation des données..."
csvarray = [dist, speed, time]
csvdata = [list(i) for i in zip(*csvarray)]
with open("metro.csv", "wb") as f:
    writer = writer(f)
    writer.writerows(csvdata)

dist = [d.km for d in dist]
speed = [v.kph for v in speed]
time = [t.h for t in time]
print "Production du graphe..."
plotter.figure(figsize=[10, 20])
plotter.subplot(3, 1, 1)
plotter.plot(days, dist)
plotter.title("Distance Alsace-Mercure (km)")
plotter.subplot(3, 1, 2)
plotter.plot(days, speed)
plotter.title("Vitesse du metro (km/h)")
plotter.subplot(3, 1, 3)
plotter.plot(days, time)
plotter.title("Temps de parcours (heures)")
plotter.savefig('/home/lucidiot/Prog/Python/metro.png')
plotter.savefig('/home/lucidiot/Prog/Python/metro.pdf')

print "Script terminé"
