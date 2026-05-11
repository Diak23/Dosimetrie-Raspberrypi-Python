from acquisition.capteur import lecture_capteur
from processing.exposition import mesurer_exposition
from processing.stockage import sauvegarder_mesure
from interface.affichage import afficher_resume
from interface.alerte import declencher_alerte
from config.config import SEUIL_EXPOSITION, DUREE_MESURE

print("Démarrage du système TEMPO")

valeur = lecture_capteur()

if valeur > SEUIL_EXPOSITION:
    statut = "Exposition élevée"
else:
    statut = "Niveau normal"

afficher_resume(valeur, statut)
declencher_alerte(statut)
sauvegarder_mesure(valeur, statut)
mesurer_exposition(DUREE_MESURE)
