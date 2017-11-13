#!/usr/bin/env python3
from pseudosci.humanity.human import Human
from pseudosci.humanity.food import Food, NutrientData
from pseudosci.units.general import Energy, Mass
from pseudosci.data.food import load_rdi, load_consequences

# L'énergie est indiquée pour un kilogramme.
# Les informations nutritionelles sont indiquées en pourcentage de la masse.
coffee = Food("Beverages, coffee, instant, regular, prepared with tap water",
              Energy(kcal=20),
              NutrientData(protein=.001, total_fat=0, carbohydrate=.0034,
                           dietary_fiber=0, sugar=0, calcium=.04, iron=.0004,
                           magnesium=.04, phosphorus=.03, potassium=.3,
                           sodium=.4, zinc=.0001, vitamin_C=0, thiamin=0,
                           riboflavin=.00001, niacin=.00236, vitamin_B6=0,
                           folate=0, vitamin_B12=0, vitamin_A=0, vitamin_E=0,
                           vitamin_K=0, saturated_fat=0.00002))

# 'eu' correspond au jeu d'apports recommandés de l'Union Européenne.
Human.consequences(Human.eat(coffee, Mass(g=1575))[1],
                   load_rdi("eu"), load_consequences('fr'))
