from acquisition.capteur import lecture_capteur

from processing.exposition import mesurer_exposition

print("Démarrage du système TEMPO")

lecture_capteur()
mesurer_exposition(5)
