# TP5 – Jeux Olympiques

## Table des matières

- [1. Introduction](#1-introduction)  
- [2. Module CSV](#2-module-csv)  
  - [Exercice 1 : Déduplication](#exercice-1--déduplication)  
  - [Exercice 2 : Normalisation de la colonne « Sex »](#exercice-2--normalisation-de-la-colonne-sex)  
  - [Exercice 3 : Filtrage des médaillés](#exercice-3--filtrage-des-médaillés)  
  - [Exercice 4 : Pipeline de nettoyage](#exercice-4--pipeline-de-nettoyage)  
- [3. Module Pandas et Seaborn](#3-module-pandas-et-seaborn)  
  - [Exercice 5 : Manipulations de base avec pandas](#exercice-5--manipulations-de-base-avec-pandas)  
  - [Exercice 6 : Extraction de sous-ensembles](#exercice-6--extraction-de-sous-ensembles)  
- [3.1. Module seaborn](#31-module-seaborn)  
  - [Exercice 7 : Histogramme des médailles par pays](#exercice-7--histogramme-des-médailles-par-pays)  
  - [Exercice 8 : Médailles de la France aux JO d’été](#exercice-8--médailles-de-la-france-aux-jo-dété)  

---

## 1. Introduction

Dans ce TP, nous allons manipuler les données des athlètes ayant participé aux Jeux Olympiques, contenues dans le fichier `olympics.csv` : noms, sexes, nationalités, années et médailles obtenues L1_INFAV_TP5_Olympics-1.pdf](file-service://file-3hBTG55bBCAYZjm7BoawbC).

---

## 2. Module CSV

Nous commençons par nettoyer les anomalies du fichier CSV à l’aide du module `csv` de Python.

### Exercice 1 : Déduplication

**Objectif :**  
Écrire une fonction `deduplicate(f1, f2)` qui :  
1. Lit les lignes de `f1` (`olympics.csv`).  
2. Supprime les doublons.  
3. Écrit le résultat dédoublonné dans `f2`.

### Exercice 2 : Normalisation de la colonne « Sex »

**Objectif :**  
La colonne `Sex` contient des valeurs équivalentes mais écrites différemment (par ex. `M`, `Male`, `F`, `Female`).  
- Identifier ces variations.  
- Écrire une fonction `normalize(f1, f2)` qui normalise `Sex` en `M` ou `F`, puis écrit dans `f2`.

### Exercice 3 : Filtrage des médaillés

**Objectif :**  
Écrire une fonction `filter_medal(f1, f2)` qui :  
1. Lit `f1`.  
2. Ne garde que les lignes où l’athlète a remporté au moins une médaille.  
3. Écrit le résultat filtré dans `f2`.

### Exercice 4 : Pipeline de nettoyage

**Objectif :**  
Assembler les étapes précédentes dans `clean_data(f1, f2)` :  
1. Déduplication  
2. Normalisation de `Sex`  
3. Filtrage des non-médaillés  
4. Écrire le fichier nettoyé `olympics.cleaned.csv`.

---

## 3. Module Pandas et Seaborn

Nous utilisons `pandas` pour charger et manipuler `olympics.cleaned.csv`, puis `seaborn` pour visualiser.

### Exercice 5 : Manipulations de base avec pandas

1. Charger le CSV dans un DataFrame `df`.  
2. Afficher les 3 premières lignes (`df.head(3)`).  
3. Afficher les 3 dernières lignes (`df.tail(3)`).  
4. Afficher un échantillon aléatoire (`df.sample()`).  
5. Afficher la description statistique (`df.describe()`).

### Exercice 6 : Extraction de sous-ensembles

1. Afficher les 3 pays ayant obtenu le plus de médailles.  
2. Afficher les 3 athlètes féminines ayant obtenu le plus de médailles d’or.  
3. Afficher tous les athlètes français médaillés d’or après 1980.

---

## 3.1. Module seaborn

Après avoir exploré la [documentation seaborn](https://seaborn.pydata.org/), réaliser les graphiques suivants :

### Exercice 7 : Histogramme des médailles par pays

- Utiliser `seaborn.histplot` ou `seaborn.countplot` pour représenter le nombre total de médailles par pays.

### Exercice 8 : Médailles de la France aux JO d’été

1. Histogramme du nombre total de médailles par année pour la France aux JO d’été.  
2. Même graphique, mais en distinguant or, argent et bronze (couleurs superposées ou barres groupées).

---
