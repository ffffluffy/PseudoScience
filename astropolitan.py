#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Module principal pour l'étude Astropolitain"""

from csv import writer
from array import array
from skyfield.api import load
import matplotlib.pyplot as plt
from pseudosci.units import Distance, Velocity, Time
from pseudosci.data.vehicles import lille_metro

print "Script de calcul pour la distance Alsace-Mercure"

ts = load.timescale()
data = load('de421.bsp')
earth, mercury = data['earth'], data['mercury']
days = range(300, 800)
dist, vel, time = [], [], []
traveltime = Time(s=46)

print "Calcul..."
dist = [
    Distance(au=earth.at(ts.utc(2017, 1, day)).observe(mercury).distance().au)
    for day in days]
vel = [d / traveltime for d in dist]
time = [lille_metro.move(d).time for d in dist]

print "Exportation des données..."
csvarray = [dist, vel, time]
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
plt.plot(days, [v.kph for v in vel])
plt.title("Vitesse moyenne du metro (km/h)")
plt.subplot(3, 1, 3)
plt.plot(days, [t.d for t in time])
plt.title("Temps de parcours (jours)")
plt.savefig('/home/lucidiot/Prog/Python/metro2.png')
plt.savefig('/home/lucidiot/Prog/Python/metro2.pdf')

print "Script terminé"
