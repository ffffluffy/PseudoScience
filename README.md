# PseudoScience [![Build Status](https://travis-ci.org/Lucidiot/PseudoScience.svg?branch=master)](https://travis-ci.org/Lucidiot/PseudoScience) [![Coverage Status](https://coveralls.io/repos/github/Lucidiot/PseudoScience/badge.svg?branch=master)](https://coveralls.io/github/Lucidiot/PseudoScience?branch=master) [![Requirements Status](https://requires.io/github/Lucidiot/PseudoScience/requirements.svg?branch=master)](https://requires.io/github/Lucidiot/PseudoScience/requirements/?branch=master) [![Code Climate](https://codeclimate.com/github/Lucidiot/PseudoScience/badges/gpa.svg)](https://codeclimate.com/github/Lucidiot/PseudoScience) [![Code Health](https://landscape.io/github/Lucidiot/PseudoScience/master/landscape.svg?style=flat)](https://landscape.io/github/Lucidiot/PseudoScience/master)

Mes études pseudo-scientfiques sur [mon site personnel](http://brainshit.fr) (catégorie [Pseudo-science](https://brainshit.fr/category/3)) concernent de nombreux domaines et tentent de répondre d'une manière au mieux approchée de la réalité (la validité des données et calculs dépendant souvent de ma motivation) à des questions que personne ne se pose. Suite à ma volonté de découvrir Python pour effectuer des calculs d'orbite dont j'avais besoin dans une de ces études, j'ai voulu créer un projet plus propre, réutilisable facilement et avec des composants qui me serviront dans beaucoup d'autres études, y compris des plus sérieuses.

Les classes du projet sont donc les implémentations répondant aux besoins spécifiques que j'ai pu avoir au cours de mes calculs, mais le projet sera progressivement étendu pour me fournir une base solide me permettant de répondre à beaucoup de questions plus rapidement, notamment en implémentant ce dont j'aurai pu avoir besoin dans des études antérieures.

## Pré-requis

Le projet nécessite `six` pour la compatibilité avec Python 2 et 3 du système d'unités.

### Scripts

* [Skyfield](http://rhodesmill.org/skyfield/) ([github](https://github.com/brandon-rhodes/python-skyfield/)), testé en version 0.9.1 ;
* [Matplotlib](http://matplotlib.org) ([github](https://github.com/matplotlib/matplotlib)), testé en version 2.0.0 (fonctionnera probablement en 1.5.x)

## Installation

``` bash
git clone https://github.com/Lucidiot/PseudoScience
cd PseudoScience
pip install -r requirements.txt
```

## Développement

### Mise en route

``` bash
git clone https://github.com/Lucidiot/PseudoScience
cd PseudoScience
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

### Tests unitaires

Dans le répertoire racine du projet :

``` bash
python -m pytest
```

Pour obtenir les données de couverture du code par les tests unitaires :

``` bash
python -m pytest --cov pseudosci --cov-report html
```

### Vérification du style

Le style de code PEP 8 est utilisé. Pour vérifier qu'un fichier corresponde au style PEP 8, saisissez `python -m pep8 [fichier]`. Pour vérifier l'intégralité du package `pseudosci` :

``` bash
python -m pep8 pseudosci/*
```
