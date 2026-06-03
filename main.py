import time

from acquisition.capteur import lecture_capteur
from processing.stockage import sauvegarder_mesure
from interface.affichage import afficher_resume
from interface.alerte import declencher_alerte
from config.config import SEUIL_EXPOSITION

print("Démarrage du système TEMPO")

while True:

    valeur = lecture_capteur()

    if valeur > SEUIL_EXPOSITION:
        statut = "Exposition élevée"
    else:
        statut = "Niveau normal"

    afficher_resume(valeur, statut)

    declencher_alerte(statut)

    sauvegarder_mesure(valeur, statut)

    print("Nouvelle mesure dans 5 secondes...\n")

    time.sleep(5)
