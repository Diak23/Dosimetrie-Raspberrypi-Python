from acquisition.capteur import lecture_capteur
from processing.exposition import mesurer_exposition
from processing.stockage import sauvegarder_mesure
from interface.affichage import afficher_resume

print("Démarrage du système TEMPO")

valeur = lecture_capteur()

if valeur > 3:
    statut = "Exposition élevée"
else:
    statut = "Niveau normal"

afficher_resume(valeur, statut)
sauvegarder_mesure(valeur, statut)
mesurer_exposition(5)
