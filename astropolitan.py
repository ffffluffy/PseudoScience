#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Module principal pour l'étude Astropolitain"""

from csv import writer
from array import array
from skyfield.api import load
import matplotlib.pyplot as plt
from pseudosci.units import Distance, Velocity, Time

print "Script de calcul pour la distance Alsace-Mercure"

ts = load.timescale()
data = load('de421.bsp')
earth, mercury = data['earth'], data['mercury']
days = range(300, 800)
dist, speed, time = [], [], []
metrovel = Velocity(kph=80)
traveltime = Time(s=46)

print "Calcul..."
dist = [
    Distance(au=earth.at(ts.utc(2017, 1, day)).observe(mercury).distance().au)
    for day in days]
speed = [d / traveltime for d in dist]
time = [d / metrovel for d in dist]

print "Exportation des données..."
csvarray = [dist, speed, time]
csvdata = [list(i) for i in zip(*csvarray)]
with open("metro.csv", "wb") as f:
    writer = writer(f)
    writer.writerows(csvdata)

print "Production du graphe..."
plt.figure(figsize=[10, 20])
plt.subplot(3, 1, 1)
plt.plot(days, [d.km for d in dist])
plt.title("Distance Alsace-Mercure (km)")
plt.subplot(3, 1, 2)
plt.plot(days, [v.kph for v in speed])
plt.title("Vitesse du metro (km/h)")
plt.subplot(3, 1, 3)
plt.plot(days, [t.h for t in time])
plt.title("Temps de parcours (heures)")
plt.savefig('/home/lucidiot/Prog/Python/metro.png')
plt.savefig('/home/lucidiot/Prog/Python/metro.pdf')

print "Script terminé"
