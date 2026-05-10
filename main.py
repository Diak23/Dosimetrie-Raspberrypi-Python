from acquisition.capteur import lecture_capteur
from processing.exposition import mesurer_exposition

print("Démarrage du système TEMPO")

valeur = lecture_capteur()

if valeur > 3:
    print("⚠️ Niveau d'exposition élevé")
else:
    print("✅ Niveau normal")

mesurer_exposition(5)
