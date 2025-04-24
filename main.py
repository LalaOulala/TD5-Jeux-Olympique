import csv

def deduplicate(f1, f2):
    """
    Permet de nettoyer les lignes en double dans un fichier .csv de chemin f1
    et d'écrire sa version nettoyé dans un fichier de chemin f2

    Args:
        f1 (string): chemin vers un fichier .csv à traiter
        f2 (string): chemin vers un fichier .csv traité
    """
    data = []

    with open(f1) as f1_csv:
        reader = csv.reader(f1_csv, delimiter=",")
        for row in reader:
                if row[1:len(row)+1] not in data:
                     data.append(row)
    
    print(data)

    with open(f2,"w") as f2_csv:
         writer = csv.writer(f2_csv, delimiter=",")
         for row in data:
              writer.writerow(row)

    return 0
                
                
deduplicate("olympics_reduced.csv", "olympics_clean.csv")
