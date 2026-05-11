from acquisition.capteur import lecture_capteur
from processing.exposition import mesurer_exposition
from processing.stockage import sauvegarder_mesure

print("Démarrage du système TEMPO")

valeur = lecture_capteur()

if valeur > 3:
    statut = "Exposition élevée"
    print("⚠️ Niveau d'exposition élevé")
else:
    statut = "Niveau normal"
    print("✅ Niveau normal")

sauvegarder_mesure(valeur, statut)
mesurer_exposition(5)
