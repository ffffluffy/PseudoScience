#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Données pré-enregistrées concernant la nourriture et les apports
nutritionnels. Les noms utilisés correspondent à la nomenclature des
nutriments décrite dans la documentation du projet.
https://github.com/Lucidiot/PseudoScience/wiki/Nomenclature-des-nutriments"""

from ..units.general import Mass, Energy
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

USA_ENERGY_INTAKE = Energy(kcal=2000)

# Conséquences médicales d'un apport insuffisant ou trop élevé des nutriments.
# Pour une version en anglais, voir CONSEQUENCES_EN.
# Format : 'nutriment': ("en cas de carence", "en cas d'excès")
CONSEQUENCES_FR = {
    'total_fat': ("troubles de croissance et risque de maladies chroniques",
                  "obésité et risque de maladies cardiovasculaires, cancers "
                  "ou diabète de type 2"),
    'saturated_fat': ("troubles de croissance et risque de maladies "
                      "chroniques", "obésité et risque de maladies "
                      "cardiovasculaires, cancers ou diabète de type 2"),
    'cholesterol': ("altération des membranes cellulaires, fatigue, "
                    "dépression, tristesse, nausées, constipation, manque "
                    "d'appétit, hypotension, vertiges, fourmillements, sueurs "
                    "froides, malaises ou pertes de connaissance",
                    "maladies cardiovasculaires"),
    'sodium': ("déshydratation, hypotension, fatigue musculaire, manque "
               "d'appétit, baisse de libido, altération du système nerveux",
               "hypertension, maladies cardiovasculaires, rétention d'eau et "
               "cellulite"),
    'carbohydrates': ("malaises, pertes de connaissance, fatigue, vertiges, "
                      "sueurs, tremblements, maux de tête, palpitations et "
                      "troubles neurologiques", "obésité, caries, diabète de "
                      "type 2, maladies cardiovasculaires et constipation"),
    'dietary_fiber': ("constipation et risques de diabète", "diarrhées"),
    'sugar': ("altération des fonctions congitives et lésions organiques",
              "obésité, constipation, aigreurs d'estomac, baisse du système "
              "immunitaire, caries et cancers"),
    'protein': ("troubles de croissance",
                "calculs rénaux, ostéoporose, cancer du côlon"),
    'vitamin_A': ("troubles de la vision, maladies de peau, cheveux secs, "
                  "caries, troubles de croissance, infections respiratoires, "
                  "digestives ou urogénitales, fatigue, nervosité, diarrhée, "
                  "perte d'appétit", "nausées, vomissements, troubles de la "
                  "vision, maux de tête, perte de cheveux, déssechement de la "
                  "peau, douleurs aux articulations, fragilité osseuse, "
                  "hypertrophie du foie, anorexie"),
    'vitamin_B5': ("perte d'appétit, maladies de peau, nausées, vomissements, "
                   "troubles respiratoires, fourmillements, crampes, spasmes "
                   "musculaires, dégénérescence neuro-musculaire et du foie, "
                   "fatigue, maux de tête, stress, irritabilité, troubles du "
                   "sommeil, dépression, convulsions, troubles de croissance",
                   "diarrhée, hyperglycémie"),
    'vitamin_B6': ("perte d'appétit, anorexie, vomissements, maladies de peau,"
                   " vertiges, convulsions, irritabilité, nervosité, "
                   "confusion, dépression, anémie, maladies du foie, calculs "
                   "rénaux, troubles de croissance et baisse du système "
                   "immunitaire", "réflexes réduits, engourdissements, "
                   "difficultés à marcher, lésions du système nerveux"),
    'vitamin_B12': ("anémie, nausées, constipation, inflammation de la langue,"
                    "baisse du système immunitaire, douleurs musculaires et "
                    "allergies", "acné à long terme"),
    'vitamin_C': ("cicatrisation lente, gingivite, trouble de croissance des "
                  "os, anémie, fatigue extrême, infections, manque d'appétit, "
                  "perte de poids, maux de tête, troubles du sommeil, "
                  "palpitations, manque de concentration, irritabilité, "
                  "dépression, scorbut (caries, hémorragies, douleurs aux os "
                  "et aux articulations, dégénérescence des muscules et des "
                  "cartilages, ecchymoses, anémie, perte de poids, fièvre, "
                  "troubles digestifs, tachycardie, mort)",
                  "diarrhées, coagulation, crise de goutte et calculs rénaux "
                  "en cas de doses extrêmes"),
    'vitamin_D': ("rachitisme chez l'enfant (ramollissement de la boîte "
                  "crânienne, retard de croissance, hypotonie musculaire, "
                  "retard mental, maladies aux bronches, tétanie, etc.), "
                  "ostéomalacie chez l'adulte (douleurs osseuses, déformation "
                  "de la colonne vertébrale ou du bassin, hypotonie "
                  "musculaire, fractures spontanées)", "maux de tête, pertes "
                  "d'appétit, anorexie, amaigrissement, arrêt de croissance, "
                  "nausées, vomissements, diarrhées, excès d'urine, "
                  "soif excessive, déshydratation, hypertension, calculs "
                  "rénaux, durcissement des artères, insuffisance rénale, "
                  "troubles de l'humeur, agitation, dépression, lésions au "
                  "coeur et aux reins"),
    'vitamin_E': ("stérilité, anémie, faiblesse musculaire, troubles "
                  "neurologiques et cardio-vasculaires, baisse de la vision, "
                  "vieillissement de la peau, infections, enfants morts-nés "
                  "et retards de croissance", "cicatrisation lente, troubles "
                  "intestinaux et maux de tête"),
    'vitamin_K': ("ecchymoses, saignements, menstruations abondantes, "
                  "hémorragies internes, fractures et ostéoporose",
                  "troubles hépatiques et caillots sanguins en dose massive"),
    'calcium': ("arythmie, troubles du sommeil, nervosité, agitation, caries, "
                "tétanie, crampes, rachitisme, ostéoporose, ongles cassants "
                "et eczéma", "calculs rénaux, maux de tête, irritabilité, "
                "confusion, perte d'appétit, nausées, vomissements, douleurs "
                "musculaires"),
    'iron': ("anémie, fatigue, dépression, essouflement, palpitations, "
             "flatulences, anorexie et troubles de la thermorégulation",
             "impuissance, hypertrophie du foie, cirrhose, diabète grave, "
             "insuffisance cardiaque, troubles hormonaux, ostéoporose, "
             "douleurs abdominales et articulaires, dépressions, maladies "
             "cardiaques, vieillisement"),
    'thiamin': ("perte d'appétit, amaigrissement, fatigue extrême, "
                "irritabilité, dépression, troubles de la vision, de la "
                "concentration et de la mémoire, manque d'équilibre, troubles "
                "digestifs, palpitations, confusions, ulcères de l'estomac et "
                "des jambes, anorexie, faiblesse musculaire",
                "effet diurétique"),
    'riboflavin': ("inflammation des lèvres, de la langue, des muqueuses, "
                   "lésions aux muqueuses anales et vaginales, baisse de la "
                   "vision, conjonctivite, cataracte, entérite, hypotonie, "
                   "crampes, démangeaisons, nausées, engourdissements, "
                   "urine fluorescente"),
    'niacin': ("perte d'appétit, aphtes, engelures, apathie, tristesse, "
               "fatigue, maux de tête, vertiges, confusion, insomnies, "
               "anxiété, rougeurs, photosensibilité, troubles nerveux, "
               "inflammations des lèvres, de la langue, de la muqueuse "
               "buccale, mort", "rougeurs, diarrhées, maux de tête, "
               "hyperglycémie, hépatite, dépression"),
    'biotin': ("ongles cassants, inflammations des lèvres, de la langue, de "
               "la muqueuse buccale, de la peau, eczéma, nausées, fatigue, "
               "perte d'appétit, anorexie, dépression, hypotonie, retard "
               "psychomoteur, convulsions, douleurs musculaires",
               "effet diurétique"),
    'folate': ("anémie, trouble de croissance, perte d'appétit, insomnie, "
               "apathie, asthénie, troubles de mémoire, confusion, "
               "irritabilité, anxiété, dépression, diarrhée, nausées, "
               "inflammation de la langue, des gencives, lésions aux "
               "muqueuses et à la peau, maux de tête, palpitations, "
               "avortement", "effet diurétique et allergies rares"),
    'phosphorus': ("faiblesse, problèmes osseux, perte d'appétit et anorexie",
                   "troubles digestifs et osseux"),
    'magnesium': ("palpitations, tremblements, crampes, tétanie, fatigue, "
                  "asthénie, anxiété, hyperémotivité, dépression, insomnie, "
                  "AVC, goutte, arthrose et troubles digestifs", "rougeurs, "
                  "respiration superficielle, diarrhées, troubles nerveux"),
    'zinc': ("baisse de l'immunité, infections, fatigue, perte du goût et de "
             "l'odorat, troubles oculaires, retard de croissance, difficultés "
             "d'apprentissage, perte d'appétit, de poids, chute de cheveux, "
             "ongles cassants, sécheresse de la peau, cicatrisation lente, "
             "impuissance, stérilité masculine et diarrhée",
             "difficultés à marcher, troubles de l'élocution, tremblements, "
             "nausées et vomissements"),
    'choline': ("cirrhose, hypertension, dégénérescence du foie, durcissement "
                "et obstruction des artères, ulcères d'estomac, troubles "
                "cardiaques, blocage des voies urinaires, hémorragies aux "
                "reins", "nausées, vomissements, diarrhées"),
    'chloride': ("fatigue, crampes, agitation, tétanie et arythmie",
                 "effet diurétique, respiration rapide et profonde, faiblesse,"
                 "vomissements et destruction de la flore intestinale"),
    'iodine': ("grossissement de la thyroïde, fatigue, diminution de la "
               "mémoire, hallucinations, dépression, constipation, perte "
               "d'appétit, anorexie, crampes, myalgies, anémie, prise de "
               "poids, intolérance au froid, stérilité féminine, menstruations"
               " abondantes, diminution de la lactation, baisse de la "
               "fréquence cardiaque et hypotension, retard de croissance, "
               "nanisme, crétinisme et constipation chez le nourrisson",
               "hyperthyroïdie et intoxication chez les sujets sensibles : "
               "coryza, larmoiement, éruptions cutanées, salivation, "
               "pharyngite, acné, purpura, hémorragies, tachycardie, maux de "
               "tête, vertiges, oedèmes de la glotte ou du poumon"),
    'selenium': ("baisse du système immunitaire, infections, fatigue, peau "
                 "sèche et ridée, troubles musculaires et cardiovasculaires",
                 "nausées, vomissements, fatigue, perte de poids, ongles "
                 "cassants, chute de cheveux, irritabilité"),
    'copper': ("anémie, leucopénie, neutropénie, ostéoporose chez l'enfant",
               "vomissements, nausées, diarrhée, maux d'estomac, insuffisance "
               "rénale, troubles du comportement, de la parole, convulsions, "
               "salivation, insuffisance hépatique"),
    'potassium': ("troubles du rythme cardiaque, fatigue, crampes, soif, "
                  "courbatures, douleurs musculaires et rhumatismes, nausées, "
                  "vomissements, paralysie partielle ou totale",
                  "effet diurétique ou faiblesse musculaire, diminution des "
                  "réflexes, paralysie, palpitations, arythmie, état de choc "
                  "en cas d'insuffisance rénale"),
    'fluoride': ("anémie, pâleur, perte d'appétit, infections, caries",
                 "fluorose : problèmes osseux et d'émail"),
    'chromium': ("intolérance au glucose, hyperglycémie, hyperlipidémie, "
                 "augmentation de l'insuline", "problèmes d'estomac, "
                 "hypoglycémie, lésions au foie, aux reins et aux nerfs, "
                 "troubles du rythme cardiaque, insuffisance rénale, "
                 "vertiges, éruptions cutanées"),
    'manganese': ("retard de croissance, dermatite, cheveux mal pigmentés, "
                  "baisse du cholestérol, stérilité", "maux de tête, "
                  "somnolence"),
    'molybdenum': ("troubles urinaires, neurologiques et de la vision, "
                   "accélération brusque de la respiration, tachycardie",
                   "dysfonctionnement du foie, douleurs aux glandes et "
                   "articulations, déformations articulairs, érythème, "
                   "oedèmes, contractions musculaires et ralentissement "
                   "de la croissance osseuse")
}

# Health consequences on under- or over- nutritional intakes.
# For a French version, see CONSEQUENCES_FR.
# Format : 'nutrient': ("in case of lack", "in case of excess")
CONSEQUENCES_EN = {
    'total_fat': ("growth disorders and chronic disease risks", "obesity and "
                  "heart disease, cancer or type II diabetes risks"),
    'saturated_fat': ("growth disorders and chronic disease risks", "obesity "
                      "and heart disease, cancer or type II diabetes risks"),
    'cholesterol': ("cell membranes alteration, fatigue, depression, sadness, "
                    "nausea, constipation, lack of appetite, hypotension, "
                    "dizziness, tingling, cold sweat, loss of consciousness",
                    "heart diseases"),
    'sodium': ("dehydration, hypotension, muscle fatigue, lack of appetite, "
               "lowered libido, nervous system alteration", "hypertension, "
               "heart diseases, water retention and cellulite"),
    'carbohydrates': ("loss of consciousness, fatigue, dizziness, sweating, "
                      "shakiness, headache, heart palpitations and "
                      "neurological disorders", "obesity, caries, type II "
                      "diabetes, heart diseases and constipation"),
    'dietary_fiber': ("constipation and diabetes risk", "diarrhea"),
    'sugar': ("cognitive functions alteration and organ damage",
              "obesity, constipation, heartburn, lowered immune system, "
              "caries and cancers"),
    'protein': ("growth disorders", "kidney stones, osteoporosis, "
                "colon cancer"),
    'vitamin_A': ("impaired vision, skin diseases, dry hair, caries, growth "
                  "disorders, respiratory, digestive or urogenital infection, "
                  "fatigue, nervousness, diarrhea, loss of appetite",
                  "nausea, vomiting, impaired vision, headache, hair loss, "
                  "dry skin, joint pain, fragile bones, liver hypertrophy, "
                  "anorexia"),
    'vitamin_B5': ("loss of appetite, skin diseases, nausea, vomiting, "
                   "respiratory disorders, tingling, cramps, muscle spasms, "
                   "neuromuscular and liver degeneration, fatigue, headache, "
                   "stress, irritability, sleep disorders, depression, "
                   "seizures, growth disorders", "diarrhea, hyperglycemia"),
    'vitamin_B6': ("loss of appetite, anorexia, vomiting, skin diseases, "
                   "dizziness, seizures, irritability, nervousness, confusion,"
                   " depression, anemia, liver diseases, kidney stones, growth"
                   " disorders and lowered immune system",
                   "lowered reflexes, numbness, difficult walking, nervous "
                   "system injuries"),
    'vitamin_B12': ("anemia, nausea, constipation, tongue inflammation, "
                    "lowered immune system, muscle aches and allergies",
                    "acne on long term"),
    'vitamin_C': ("slow cicatrisation, gingivitis, bone growth disorders, "
                  "anemia, extreme fatigue, infections, lack of appetite, "
                  "weight loss, headache, sleep disorders, heart palpitations,"
                  " lack of focus, irritability, depression, scurvy (caries, "
                  "bleeding, bone and joint aches, cartilage and muscle "
                  "degeneration, bruising, anemia, weight loss, fever, "
                  "digestive disorders, tachycardia, death)", "diarrhea, "
                  "coagulation, gout and kidney stones on extreme doses"),
    'vitamin_D': ("rachitis on children (brain cavity softening, growth "
                  "retardation, muscle hypotonia, mental retardation, "
                  "bronchial diseases, tetany, etc.), osteomalacia on adults "
                  "(bone aches, spine and pelvis deformation, muscle "
                  "hypotonia, spontaneous fractures)", "headache, loss of "
                  "appetite, anorexia, slimming, growth interruption, nausea, "
                  "vomiting, diarrhea, excessive urination and thirst, "
                  "dehydration, hypertension, kidney stones, artery hardening,"
                  " renal failure, mood swings, agitation, depression, heart "
                  "and kidney injuries"),
    'vitamin_E': ("sterility, anemia, muscular weakness, neural and "
                  "cardiovascular disorders, lowered vision, skin aging, "
                  "infections, stillborn babies and growth retardation",
                  "slow cicatrisation, intestinal disorders and headache"),
    'vitamin_K': ("bruising, bleeding, heavy periods, internal bleeding, "
                  "fractures and osteoporosis",
                  "liver disorders and blood clots on massive doses"),
    'calcium': ("arythmia, sleep disorders, nervousness, agitation, caries, "
                "tetany, cramps, rachitis, osteoporosis, brittle nails and "
                "eczema", "kidney stones, headache, irritability, confusion, "
                "loss of appetite, nausea, vomiting, muscle aches"),
    'iron': ("anemia, fatigue, depression, panting, heart palpitations, "
             "flatulency, anorexia and thermoregulation disorders",
             "impotency, liver hypertrophy, cirrhosis, serious diabetes, "
             "heart failure, hormonal disorders, osteoporosis, abdomen and "
             "joint aches, depressions, heart diseases, aging"),
    'thiamin': ("loss of appetite, slimming, extreme fatigue, irritability, "
                "depression, impaired vision, focus and memory, lack of "
                "equilibrium, digestive disorders, heart palpitations, "
                "confusion, stomach and legs ulcers, anorexia, muscular "
                "weakness", "diuretic effect"),
    'riboflavin': ("sore lips, tongue, moucous, injuries to anal and vaginal "
                   "mucous, lowered vision, conjunctivitis, cataract, "
                   "enteritis, hypotonia, cramps", "itching, nausea, numbness,"
                   " fluorescent urine"),
    'niacin': ("loss of appetite, mouth ulcers, frostbite, apathy, sadness, "
               "fatigue, headache, dizziness, confusion, insomnia, anxiety, "
               "depression, redness, photosensitivity, nervous disorders, "
               "sore lips, tongue, mouth mucous and death", "redness, "
               "diarrhea, headache, hyperglycemia, hepatitis, depression"),
    'biotin': ("brittle nails, sore lips, tongue, mouth mucous and skin, "
               "eczema, nausea, fatigue, loss of appetite, anorexia, "
               "depression, hypotonie, psychomotor retardation, seizures, "
               "muscle aches", "diuretic effect"),
    'folate': ("anemia, growth disorders, loss of appetite, insomnie, apathy, "
               "asthenia, memory disorders, confusion, irritability, anxiety, "
               "depression, diarrhea, nausea, sore tongue and gums, skin and "
               "mucous injuries, headache, heart palpitations, abortions",
               "diuretic effect and rare allergies"),
    'phosphorus': ("weakness, bone disorders, loss of appetite and anorexia",
                   "digestive and bony disorders"),
    'magnesium': ("heart palpitations, shakiness, cramps, tetany, fatigue, "
                  "asthenia, anxiety, hyperemotivity, depression, insomnie, "
                  "strokes, gout, osteoarthritis and digestive disorders",
                  "redness, superficial respiration, diarrhea, nervous "
                  "disorders"),
    'zinc': ("lowered immune system, infections, fatigue, loss of senses of "
             "smell and taste, vision disorders, growth retardation, difficult"
             " learning, loss of appetite and weight, hair loss, brittle "
             "nails, dry skin, slow cicatrisation, impotency, male sterility "
             "and diarrhea", "difficult walking and speaking, shakiness, "
             "nausea and vomiting"),
    'choline': ("cirrhosis, hypertension, liver degeneration, hardened and "
                "clogged arteries, stomach ulcers, heart diseases, urinary "
                "tract obstruction, kidney bleeding",
                "nausea, vomiting, diarrhea"),
    'chloride': ("fatigue, cramps, agitation, tetany and arythmia",
                 "diuretic effect, fast and deep breathing, weakness, "
                 "vomiting and intestinal flora destruction"),
    'iodine': ("thyroid hypertrophy, fatigue, lowered memory, hallucinations, "
               "depression, constipation, loss of appetite, anorexia, cramps, "
               "myalgies, anemia, weight gain, cold intolerance, female "
               "sterility, heavy periods, lowered lactation, lowered "
               "heartbeat and hypotension, growth retardation, dwarfism, "
               "cretinism and constipation on babies", "thyroid hypertrophy "
               "and intoxication on sensitive patients : coryza, snivel, "
               "rashes, salivation, pharyngitis, acne, purpura, bleeding, "
               "tachycardia, headache, dizziness, glottis or lung edema"),
    'selenium': ("lowered immune system, infections, fatigue, dry and wrinkly "
                 "skin, muscle and heart disorders",
                 "nausea, vomiting, fatigue, weight loss, brittle nails, "
                 "hair loss, irritability"),
    'copper': ("anemia, leukopenia, neutropenia, osteoporosis on children",
               "vomiting, nausea, diarrhea, stomachache, renal failure, "
               "behavior and speech disorders, seizures, salivation, "
               "hepatic failure"),
    'potassium': ("heartbeat disorders, fatigue, cramps, thirstness, "
                  "muscle aches and rheumatism, nausea, vomiting, partial or "
                  "total paralysis", "diuretic effect or muscular weakness, "
                  "lowered reflexes, paralysis, heart palpitations, arythmia, "
                  "state of shock in case of renal failure"),
    'fluoride': ("anemia, paleness, loss of appetite, infections, caries",
                 "fluorosis : bone and enamel disorders"),
    'chromium': ("glucose intolerance, hyperglycemia, hyperlipidemia, higher "
                 "insuline amount", "stomach and heartbeat disorders, "
                 "hypoglycemia, liver, kidney and nerve injuries, kidney "
                 "failure, dizziness, rashes"),
    'manganese': ("growth retardation, dermatitis, bad hair pigmentation, "
                  "lowered cholesterol, sterility", "headache, drowsiness"),
    'molybdenum': ("urine, neural and vision disorders, quick breathing "
                   "acceleration, tachycardia", "liver failure, gland and "
                   "joint aches, joint deformations, erythema, edema, muscle "
                   "contractions and slower bone growth")
}
