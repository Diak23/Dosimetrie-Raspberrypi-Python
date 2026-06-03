import csv
from datetime import datetime

def sauvegarder_mesure(valeur, statut):
    with open("data/mesures.csv", "a", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            round(valeur, 2),
            statut
        ])
