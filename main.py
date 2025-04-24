import csv

def deduplicate(f1, f2):
    """
    ERXERCICE 1
    Permet de nettoyer les lignes en double dans un fichier .csv de chemin f1
    et d'écrire sa version nettoyé dans un fichier de chemin f2

    Args:
        f1 (string): chemin vers un fichier .csv à traiter
        f2 (string): chemin vers un fichier .csv traité
    """
    unique_rows = [] # toutes les lignes présente une seule fois

    with open(f1) as fichier_a_traiter:
        reader = csv.reader(fichier_a_traiter, delimiter=",")
        for row in reader:
            if row[1:] not in unique_rows: # on teste en enlevant le premier élément
                unique_rows.append(row[1:]) # on ajoute la ligne sans le premier élément qui n'a jamais été vu a unique_rows
        
    # on écrit les lignes de unique_rows dans le fichier f2
    nombre_ligne = 1
    with open(f2, "w") as fichier_a_completer:
        writer = csv.writer(fichier_a_completer, delimiter=",")
        for row in unique_rows:
            writer.writerow([nombre_ligne] + row)
            nombre_ligne+=1
                
                
def normalize(f1, f2):
    """
    EXERCICE 2
    Permet de normaliser l'écriture du descripteur sex sur chacune des lignes.
    Certaines lignes le renseigne par M ou F
    D'autres par Male ou Female
    On ne conservera que l'écriture -> M ou F

    Args:
        f1 (_type_): _description_
        f2 (_type_): _description_
    """
    normalize_rows = []

    with open(f1) as fichier_a_traiter:
        reader = csv.reader(fichier_a_traiter, delimiter=",")
        for row in reader:
            for i in range(len(row)):
                if row[i] == "Male":
                    row[i] = "M"
                elif row[i] == "Female":
                    row[i] = "F"
            normalize_rows.append(row)
    
    with open(f2, "w") as fichier_a_completer:
        writer = csv.writer(fichier_a_completer, delimiter=",")
        writer.writerows(normalize_rows)



deduplicate("olympics_reduced.csv", "olympics_clean.csv")
normalize("olympics_reduced.csv", "olympics_clean.csv")
