#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Données pré-enregistrées concernant la nourriture et les apports
nutritionnels. Les noms utilisés correspondent à la nomenclature des
nutriments décrite dans la documentation du projet.
https://github.com/Lucidiot/PseudoScience/wiki/Nomenclature-des-nutriments"""

from ..units import Mass  # , Energy
from ..humanity.food import NutrientAmount

# Valeurs nutritionnelles de référence pour l'Union Européenne, rég. 1169/2011
# Source : https://fr.wikipedia.org/wiki/Apports_journaliers_recommandés
EU_RDI = NutrientAmount(vitamin_A=Mass(ug=800), thiamin=Mass(mg=1.1),
                        riboflavin=Mass(mg=1.4), niacin=Mass(mg=16),
                        vitamin_B5=Mass(mg=6), vitamin_B6=Mass(mg=1.4),
                        biotin=Mass(ug=50), folate=Mass(ug=200),
                        vitamin_B12=Mass(ug=2.5), vitamin_C=Mass(mg=80),
                        vitamin_D=Mass(ug=5), vitamin_E=Mass(mg=12),
                        vitamin_K=Mass(ug=75), calcium=Mass(mg=800),
                        iron=Mass(mg=14), iodine=Mass(ug=150),
                        magnesium=Mass(mg=375), phosphorus=Mass(mg=700),
                        selenium=Mass(ug=55), zinc=Mass(mg=10),
                        potassium=Mass(g=2), chloride=Mass(mg=800),
                        copper=Mass(mg=1), manganese=Mass(mg=2),
                        fluoride=Mass(mg=3.5), chromium=Mass(ug=40),
                        molybdenum=Mass(ug=50), total_fat=Mass(g=70),
                        saturated_fat=Mass(g=20), carbohydrates=Mass(g=260),
                        sugar=Mass(g=90), protein=Mass(g=50), sodium=Mass(g=6))

# EU_ENERGY_INTAKE = Energy(kcal=2000)

# Anciens apports journaliers de référence pour les États-Unis
# Rendus obsolètes en 2016, ne seront plus utilisés le 28 juillet 2018
# Source : https://en.wikipedia.org/wiki/Reference_Daily_Intake
USA_OLD_RDI = NutrientAmount(vitamin_A=Mass(ug=900), vitamin_C=Mass(mg=60),
                             calcium=Mass(g=1), iron=Mass(mg=18),
                             vitamin_D=Mass(ug=10), vitamin_E=Mass(mg=13.6),
                             vitamin_K=Mass(ug=80), thiamin=Mass(mg=1.5),
                             riboflavin=Mass(mg=1.7), niacin=Mass(mg=20),
                             vitamin_B6=Mass(mg=2), folate=Mass(mg=400),
                             vitamin_B12=Mass(ug=6), biotin=Mass(ug=300),
                             vitamin_B5=Mass(mg=10), phosphorus=Mass(g=1),
                             iodine=Mass(ug=150), magnesium=Mass(mg=400),
                             zinc=Mass(mg=15), cholesterol=Mass(mg=300),
                             copper=Mass(mg=2), manganese=Mass(mg=2),
                             chromium=Mass(ug=120), molybdenum=Mass(ug=75),
                             chloride=Mass(g=3.4), total_fat=Mass(g=65),
                             saturated_fat=Mass(g=20), selenium=Mass(ug=70),
                             sodium=Mass(g=2.4), potassium=Mass(g=3.5),
                             carbohydrates=Mass(g=300), protein=Mass(g=50),
                             dietary_fiber=Mass(g=25))

# Actuels apports journaliers de référence pour les États-Unis
# Source : https://en.wikipedia.org/wiki/Reference_Daily_Intake
USA_NEW_RDI = NutrientAmount(vitamin_A=Mass(ug=900), vitamin_C=Mass(mg=90),
                             calcium=Mass(g=1.3), iron=Mass(mg=18),
                             vitamin_D=Mass(ug=20), vitamin_E=Mass(mg=15),
                             vitamin_K=Mass(ug=120), thiamin=Mass(mg=1.2),
                             riboflavin=Mass(mg=1.3), niacin=Mass(mg=16),
                             vitamin_B6=Mass(mg=1.7), folate=Mass(mg=400),
                             vitamin_B12=Mass(ug=2.4), biotin=Mass(ug=30),
                             vitamin_B5=Mass(mg=5), phosphorus=Mass(g=1.25),
                             iodine=Mass(ug=150), magnesium=Mass(mg=420),
                             zinc=Mass(mg=11), cholesterol=Mass(mg=300),
                             copper=Mass(ug=900), manganese=Mass(mg=2.3),
                             chromium=Mass(ug=35), molybdenum=Mass(ug=45),
                             chloride=Mass(g=2.3), total_fat=Mass(g=78),
                             saturated_fat=Mass(g=20), selenium=Mass(ug=70),
                             sodium=Mass(g=2.3), potassium=Mass(g=4.7),
                             carbohydrates=Mass(g=275), protein=Mass(g=50),
                             dietary_fiber=Mass(g=28), sugar=Mass(g=50),
                             choline=Mass(mg=550))

# USA_ENERGY_INTAKE = Energy(kcal=2000)
