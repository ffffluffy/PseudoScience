#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Module principal pour l'étude Astropolitain"""

from csv import writer
from array import array
from skyfield.api import load
import matplotlib.pyplot as plt
from pseudosci.units import Distance, Velocity, Time, Acceleration
from pseudosci.movement import AcceleratedMovement
from pseudosci.data.vehicles import lille_metro

print("Script de calcul pour la distance Alsace-Mercure")

ts = load.timescale()
data = load('de421.bsp')
earth, mercury = data['earth'], data['mercury']
days = range(300, 800)
dist, vel, time = [], [], []
traveltime = Time(s=46)

print("Calcul...")
dist = [
    Distance(au=earth.at(ts.utc(2017, 1, day)).observe(mercury).distance().au)
    for day in days]
mv = [AcceleratedMovement(distance=d, time=traveltime / 2) for d in dist]
vel = [m.velocity for m in mv]
accel = [m.accel for m in mv]
time = [lille_metro.move(d).time for d in dist]

print("Exportation des données...")
csvarray = [dist, vel, time]
csvdata = [list(i) for i in zip(*csvarray)]
with open("metro.csv", "wb") as f:
    writer = writer(f)
    writer.writerows(csvdata)

print("Production du graphe...")
plt.figure(figsize=[10, 20])
plt.subplot(3, 1, 1)
plt.plot(days, [d.km for d in dist])
plt.title("Distance Alsace-Mercure (km)")
plt.subplot(3, 1, 2)
plt.plot(days, [v.kph for v in vel], 'g', label="Vitesse de pointe")
plt.twinx().plot(days, [a.mpss for a in accel], 'r', label="Acceleration")
plt.legend()
plt.title("Vitesse de pointe (km/h) et acceleration (m/s2)")
plt.subplot(3, 1, 3)
plt.plot(days, [t.d for t in time])
plt.title("Temps de parcours (jours)")
plt.savefig('metro.svg')

print("Script terminé")
