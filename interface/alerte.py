def declencher_alerte(statut):
    if statut == "Exposition élevée":
        print("🚨 ALERTE : seuil d'exposition dépassé !")
    else:
        print("Aucune alerte.")
