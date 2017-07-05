#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Module principal pour l'étude Astropolitain"""

from csv import writer
from array import array
from skyfield.api import load
import matplotlib.pyplot as plt
from pseudosci.units.general import Distance, Velocity, Time, Acceleration
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
csvarray = [days, dist, vel, accel, time]
csvdata = [list(i) for i in zip(*csvarray)]
with open("metro.csv", "wb") as f:
    writer = writer(f)
    writer.writerows(csvdata)

print("Production du graphe...")
plt.figure(figsize=[10, 7])
plt.plot(days, [d.km for d in dist])
plt.title("Distance Alsace-Mercure (km)")
plt.savefig('metrodistance.svg')
plt.figure(figsize=[10, 7])
plt.plot(days, [v.kph for v in vel], 'g')
plt.title("Vitesse de pointe (km/h)")
plt.savefig('metrovelocity.svg')
plt.figure(figsize=[10, 7])
plt.plot(days, [t.d for t in time], 'r')
plt.title("Temps de parcours (jours)")
plt.savefig('metrotime.svg')

print("Script terminé")
