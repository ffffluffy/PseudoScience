#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Module principal"""

print "Script de calcul pour la distance Alsace-Mercure"
print "Initialisation..."
from csv import writer
from skyfield.api import load
import matplotlib.pyplot as plotter

ts = load.timescale()
data = load('de421.bsp')
earth, mercure = data['earth'], data['mercury']
days = range(300, 800)
dist, speed, time = [], [], []

print "Calcul..."
for day in days:
    date = ts.utc(2017, 1, day)
    dist.append(earth.at(date).observe(mercure).distance().km)

for d in dist:
    speed.append((1500*d)/23)
    time.append(d/80)

print "Exportation des données..."
csvarray = [dist, speed, time]
csvdata = [list(i) for i in zip(*csvarray)]
with open("metro.csv", "wb") as f:
    writer = writer(f)
    writer.writerows(csvdata)

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
