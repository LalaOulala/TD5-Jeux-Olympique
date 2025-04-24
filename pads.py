import pandas

df = pandas.read_csv("olympics_cleaned.csv")

# Affichage des trois premières lignes de la table
print(df.head(3))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
# Affichage des trois dernières lignes de la table
print(df.tail(3))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
# Affichage d'un échantillon aléatoire de trois valeurs
print(df.sample(n=3))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
# Affichage d'une description du .csv 
# (compte par colonne, moyenne, écart-type, minimum, 1er quartile, mediane, 3eme quartile, maximum)
print(df.describe())

def exercice6():
    """
    EXERCICE 6 :
    Nous allons maintenant extraire des sous-ensembles de la table de données.
    1. Afficher les 3 pays qui ont obtenu le plus de médailles.
    2. Afficher les 3 athlètes féminins qui ont obtenus le plus de médailles d’or.
    3. Afficher tous les athlètes français qui ont obtenu des médailles d’or après 1980.
    """
    # Question 1
    country_list = df["Team"]
    for country in country_list:
        